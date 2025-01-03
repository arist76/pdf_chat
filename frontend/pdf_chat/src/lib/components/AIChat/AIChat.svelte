<script lang="ts">
	import { afterUpdate} from 'svelte';
	import { getChat } from '$lib/api/getChat';
	import { postChat } from '$lib/api/postChat';
	import aiSparkle from '$lib/images/aiSparkle.png';
	import { createMutation, createQuery, useQueryClient } from '@tanstack/svelte-query';
	import { page } from '$app/stores';
	import { scrollToBottom } from '$lib/utils';

	const { params } = $page;
	const queryClient = useQueryClient();
	const chats = createQuery({
		queryKey: ['chats'],
		queryFn: () => getChat(params.grade, params.subject)
	});
	const createChat = createMutation({ mutationFn: postChat });
	let messageText: string | null = null;
	let newMessageRequest: string | null = null;

	function sendMessage() {
		if (newMessageRequest) {
			$createChat.mutate(
				{ text: newMessageRequest, grade: params.grade, subject: params.subject },
				{
					onSuccess: () => {
						queryClient.invalidateQueries({ queryKey: ['chats'] });
						newMessageRequest = null;
					}
				}
			);
		}
	}
	function handleInput(event: Event & { currentTarget: HTMLTextAreaElement }) {
		if (event.target instanceof HTMLTextAreaElement) {
			messageText = event.target.value;
		}
	}

	function handleMessageRequest() {
		// add message to message quee
		if (messageText) {
			newMessageRequest = messageText;
			// remove message from input filed and send message
			messageText = null;
			sendMessage();
		}
	}

	// Watch for changes in the createChat mutation and scroll to the bottom if it changes
	afterUpdate(() => {
		console.log('afterUpdate');
		if ($chats.data || $createChat.data ) scrollToBottom();
	});
</script>

<!-- Content -->
<div class="relative h-screen">
	<div class="py-10 lg:py-14">
		<ul id="chat" class="mt-16 space-y-5">
			{#if $chats.isLoading}
				<p class="text-center font-semibold">Loading...</p>
			{:else if $chats.isError}
				<p class="text-center font-semibold">{$chats.error.message}</p>
			{:else if $chats.isSuccess}
				{#each $chats.data as message}
					{#if message.type === 'Human'}
						<!-- User Chat Bubble -->
						<li
							class="max-w-4xl py-2 px-4 sm:px-6 lg:px-8 mx-auto flex gap-x-2 items-center sm:gap-x-4"
						>
							<!-- User Avatar or Placeholder -->
							<div class="flex-shrink-0 w-[2.375rem] h-[2.375rem] rounded-full">
								<img src={aiSparkle} alt="User Avatar" class="w-full h-full" />
							</div>

							<div class="space-y-3">
								<div class="space-y-1.5">
									<p class="mb-1.5 text-sm text-gray-800 dark:text-white">
										{message.text}
									</p>
								</div>
							</div>
						</li>
						<!-- End User Chat Bubble -->
					{:else if message.type === 'Ai'}
						<!-- AI Chat Bubble -->
						<li class="py-2 sm:py-4">
							<div class="max-w-4xl px-4 sm:px-6 lg:px-8 mx-auto">
								<div class="max-w-2xl flex gap-x-2 sm:gap-x-4">
									<!-- AI Avatar or Placeholder -->
									<span
										class="flex-shrink-0 inline-flex items-center justify-center h-[2.375rem] w-[2.375rem] rounded-full bg-gray-600"
									>
										<span class="text-sm font-medium text-white leading-none">AI</span>
									</span>

									<div class="grow mt-2 space-y-3">
										<p class="text-gray-800 dark:text-gray-200">
											{message.text}
										</p>
									</div>
								</div>
							</div>
						</li>
						<!-- End AI Chat Bubble -->
					{/if}
				{/each}
			{/if}

			{#if newMessageRequest}
				<!--user request message-->
				<li
					class="max-w-4xl py-2 px-4 sm:px-6 lg:px-8 mx-auto flex gap-x-2 items-center sm:gap-x-4"
				>
					<!-- User Avatar or Placeholder -->
					<div class="flex-shrink-0 w-[2.375rem] h-[2.375rem] rounded-full">
						<img src={aiSparkle} alt="User Avatar" class="w-full h-full" />
					</div>

					<div class="space-y-3">
						<div class="space-y-1.5">
							<p class="mb-1.5 text-sm text-gray-800 dark:text-white">
								{newMessageRequest}
							</p>
						</div>
					</div>
				</li>
			{/if}

			{#if $createChat.isPending || $createChat.isError}
				<!--Ai request is wating or failed -->
				<li class="py-2 sm:py-4">
					<div class="max-w-4xl px-4 sm:px-6 lg:px-8 mx-auto">
						<div class="max-w-2xl flex gap-x-2 sm:gap-x-4">
							<!-- AI Avatar or Placeholder -->
							<span
								class="flex-shrink-0 inline-flex items-center justify-center h-[2.375rem] w-[2.375rem] rounded-full bg-gray-600"
							>
								<span class="text-sm font-medium text-white leading-none">AI</span>
							</span>

							<div class="grow mt-2 space-y-3">
								{#if $createChat.isPending}
									<p class="text-gray-800 dark:text-gray-200">Generating...</p>
								{:else if $createChat.isError}
									<p class="text-gray-800 dark:text-gray-200">
										<button class="px-4 py-1 border rounded-md bg-blue-500" on:click={sendMessage}
											>Retry</button
										>
									</p>
								{/if}
							</div>
						</div>
					</div>
				</li>
				<!-- End AI Chat Bubble -->
			{/if}
		</ul>
	</div>

	<!-- Chat input -->
	<div
		class="sticky top-[70%] bottom-0 z-10 bg-white border-t border-gray-200 pt-2 pb-3 sm:pt-4 sm:pb-6 dark:bg-slate-900 dark:border-gray-700"
	>
		<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
			<!-- Input -->
			<div class="relative">
				<textarea
					bind:value={messageText}
					on:input={handleInput}
					class="p-4 pb-12 block w-full border-gray-200 border rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
					placeholder="Ask me anything..."
				></textarea>

				<!-- Toolbar -->
				<div class="absolute bottom-px inset-x-px p-2 rounded-b-md bg-white dark:bg-slate-900">
					<div class="flex justify-between items-center">
						<!-- Button Group -->
						<div class="flex items-center"></div>
						<!-- End Button Group -->

						<!-- Button Group -->
						<div class="flex items-center gap-x-1">
							<!-- Send Button -->
							<button
								on:click={handleMessageRequest}
								type="button"
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
	<!-- End Search -->
</div>
<!-- End Content -->
