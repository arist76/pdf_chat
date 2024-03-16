<script lang="ts">
	import { page } from '$app/stores';
	import { downVoteForum, postForumAnswer, upVoteForum } from '$lib/api/postForum';
	import { scrollToBottom } from '$lib/utils';
	import { toast } from '@zerodevx/svelte-toast';
	import type { ForumDetailTypes } from '../../../routes/(main)/types';
	import ForumCard from './ForumCard.svelte';
	import { afterUpdate } from 'svelte';

	export let forumData: ForumDetailTypes[];
	let slug = $page.params.slug;
	let messageText: string | null = null;
	let sentMessages: ForumDetailTypes[] = [];

	function handleInput(event: Event & { currentTarget: HTMLTextAreaElement }) {
		if (event.target instanceof HTMLTextAreaElement) {
			messageText = event.target.value;
		}
	}
	const handleUpVote = () => {
		upVoteForum(slug);
	};
	const handleDownVote = () => {
		downVoteForum(slug);
	};

	const handlePostAnswer = async () => {
		if (messageText) {
			const newMessage = {
				id: sentMessages.length,
				text: messageText,
				date: Date(),
				upvotes: 0,
				downvotes: 0,
				room: 0,
				user: 0
			};
			sentMessages = [...sentMessages, newMessage];
			let temp = messageText;
			messageText = '';
			const res = await postForumAnswer({ slug: slug, text: temp });
			if (!res) {
				sentMessages.pop();
				messageText = temp;
				toast.push('Failed To Sent Try Again!');
			}
		}
	};

	// Watch for changes in the createChat mutation and scroll to the bottom if it changes
	afterUpdate(() => {
		if (sentMessages) scrollToBottom();
	});
</script>

<section class="w-full h-atuo flex flex-col justify-center items-center gap-6 min-w-full">
  <div class="w-full mb-14">
    <a class="bg-red mt-10 ml-10 " href="http://{$page.url.host}/forum/{$page.params.grade}/{$page.params.subject}/">
		<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="M12 2a10 10 0 1 0 10 10A10.011 10.011 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8.009 8.009 0 0 1-8 8z"/><path d="M13.293 7.293 8.586 12l4.707 4.707 1.414-1.414L11.414 12l3.293-3.293-1.414-1.414z"/></svg>
	</a>
	<h1 class="text-4xl font-bold ml-36 mt-10">
		{#if forumData}
			{forumData[0].room.title}
		{/if}
	</h1>
  </div>
  

	{#each forumData as data (data.id)}
		<!-- card container -->
		<ForumCard {data} handleUpVote={() => handleUpVote()} handleDownVote={() => handleDownVote()} />
	{/each}

	<!--data to be sent -->
	{#if sentMessages.length > 0}
		<!-- Corrected: Check if sentMessages array is not empty -->
		{#each sentMessages as data (data.id)}
			<!-- card container -->
			<ForumCard {data} handleUpVote={() => {}} handleDownVote={() => {}} />
		{/each}
	{/if}
	<!--space-->
	<div class="h-40 w-full"></div>

	<!-- Send Message -->
	<div
		class="fixed w-full bottom-0 pb-6 z-10 bg-white border-t border-gray-200 pt-2 sm:pt-4 sm:pb-6 dark:bg-slate-900 dark:border-gray-700"
	>
		<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
			<!-- Input -->
			<div class="relative">
				<textarea
					bind:value={messageText}
					on:input={handleInput}
					class="p-4 pb-12 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
					placeholder="write a message ..."
				></textarea>

				<!-- Toolbar -->
				<div class="absolute bottom-px inset-x-px p-2 rounded-b-md bg-white dark:bg-slate-900">
					<div class="flex justify-between items-center">
						<!-- Button Group -->
						<div class="flex items-center">
							<!-- Mic Button -->
							<button
								type="button"
								class="inline-flex flex-shrink-0 justify-center items-center h-8 w-8 rounded-lg text-gray-500 hover:text-blue-600 focus:z-10 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:hover:text-blue-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
							>
								<svg
									class="flex-shrink-0 h-4 w-4"
									xmlns="http://www.w3.org/2000/svg"
									width="24"
									height="24"
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
									><rect width="18" height="18" x="3" y="3" rx="2" /><line
										x1="9"
										x2="15"
										y1="15"
										y2="9"
									/></svg
								>
							</button>
							<!-- End Mic Button -->

							<!-- Attach Button -->
							<button
								type="button"
								class="inline-flex flex-shrink-0 justify-center items-center h-8 w-8 rounded-lg text-gray-500 hover:text-blue-600 focus:z-10 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:hover:text-blue-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
							>
								<svg
									class="flex-shrink-0 h-4 w-4"
									xmlns="http://www.w3.org/2000/svg"
									width="24"
									height="24"
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
									><path
										d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l8.57-8.57A4 4 0 1 1 18 8.84l-8.59 8.57a2 2 0 0 1-2.83-2.83l8.49-8.48"
									/></svg
								>
							</button>
							<!-- End Attach Button -->
						</div>
						<!-- End Button Group -->

						<!-- Button Group -->
						<div class="flex items-center gap-x-1">
							<!-- Mic Button -->
							<button
								type="button"
								class="inline-flex flex-shrink-0 justify-center items-center h-8 w-8 rounded-lg text-gray-500 hover:text-blue-600 focus:z-10 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:hover:text-blue-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
							>
								<svg
									class="flex-shrink-0 h-4 w-4"
									xmlns="http://www.w3.org/2000/svg"
									width="24"
									height="24"
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
									><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z" /><path
										d="M19 10v2a7 7 0 0 1-14 0v-2"
									/><line x1="12" x2="12" y1="19" y2="22" /></svg
								>
							</button>
							<!-- End Mic Button -->

							<!-- Send Button -->
							<button
								type="button"
								on:click={handlePostAnswer}
								class="inline-flex flex-shrink-0 justify-center items-center h-8 w-8 rounded-lg text-white bg-blue-600 hover:bg-blue-500 focus:z-10 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
							>
								<svg
									class="flex-shrink-0 h-3.5 w-3.5"
									xmlns="http://www.w3.org/2000/svg"
									width="16"
									height="16"
									fill="currentColor"
									viewBox="0 0 16 16"
								>
									<path
										d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083l6-15Zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471-.47 1.178Z"
									/>
								</svg>
							</button>
							<!-- End Send Button -->
						</div>
						<!-- End Button Group -->
					</div>
				</div>
				<!-- End Toolbar -->
			</div>
			<!-- End Input -->
		</div>
	</div>
</section>
