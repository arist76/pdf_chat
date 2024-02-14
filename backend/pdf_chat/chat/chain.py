from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.language_models.llms import LLM
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_qa_with_sources_chain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from pdf_chat import settings
import together




RESPONSE_TEMPLATE = """\
You are an expert tutor and problem-solver, tasked with answering any question \
about a given subject.

Generate a comprehensive and informative answer of 80 words or less for the \
given question based solely on the provided snippets of a text book related to the subject. You must \
only use information from the provided text book snippets. Use an unbiased and \
journalistic tone. Combine the text book together into a coherent answer. Do not \
repeat text. Cite text book snippets using [${{number}}] notation. Only cite the most \
relevant results that answer the question accurately. Place these citations at the end \
of the sentence or paragraph that reference them - do not put them all at the end. If \
different results refer to different entities within the same name, write separate \
answers for each entity.

You should use bullet points in your answer for readability. Put citations where they apply \
rather than putting them all at the end.

If there is nothing in the context relevant to the question at hand, just say "Hmm, \
I'm not sure." Don't try to make up an answer.

Anything between the following `context`  html blocks is retrieved from a text book pdf, ] \
not part of the conversation with the user. 

<context> 
    {context} 
<context/>

REMEMBER: If there is no relevant information within the context, just say "Hmm, I'm \
not sure." Don't try to make up an answer. Anything between the preceding 'context' \
html blocks is retrieved from a text book pdf, not part of the conversation with the \
user. \
"""

REPHRASE_TEMPLATE = """\
Given the following conversation and a follow up question, rephrase the follow up \
question to be a standalone question.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone Question:"""



class TogetherLLM(LLM):
    """A custom langchain LLM wrapper for togetherAI
    """

    model: str = "togethercomputer/LLaMA-2-7B-32K"
    together_api_key: str = "67a96691fabefa1320d838470ca884833d0d99131c6d59d741609361e2141ee2"

    temperature: float = 2
    max_tokens: int = 1024

    # temperature: float = 0.7
    # max_tokens: int = 512

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(
        self,
        prompt: str,
        **kwargs,
    ) -> str:
        """Call to Together endpoint."""
        together.api_key = self.together_api_key

        output = together.Complete.create(prompt,
                                        model=self.model,
                                        max_tokens=self.max_tokens,
                                        temperature=self.temperature,
                                        )
        print(output)
        text = output['output']['choices'][0]['text']


        return text


def get_chain(
        subject,
        grade,
        llm = TogetherLLM(),

):
    rephrase_prompt = PromptTemplate.from_template(REPHRASE_TEMPLATE)
    rephrase_chain = LLMChain(
        llm=llm,
        prompt=rephrase_prompt
    )

    qa_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate.from_template(RESPONSE_TEMPLATE),
    )
    response_prompt = PromptTemplate(
        template="Content: {page_content}\nSource: {source}",
        input_variables=["page_content", "source"],
    )

    final_qa_chain = StuffDocumentsChain(
        llm_chain=qa_chain,
        document_variable_name="context",
        document_prompt=response_prompt
    )

    vectordb = Chroma(
        persist_directory=settings.CHROMA_DB_DIR, 
        embedding_function = settings.CHAT_EMBEDDING_MODEL,
        collection_name = f"{subject}_{grade}"
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


    retrieval_qa = ConversationalRetrievalChain(
        question_generator=rephrase_chain,
        retriever=vectordb.as_retriever(),
        combine_docs_chain=final_qa_chain,
        memory=memory
    )

    return retrieval_qa