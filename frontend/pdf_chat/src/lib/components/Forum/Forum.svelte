<script lang="ts">
	import { formatDateString } from '$lib/utils';
	import type { ForumDetailTypes } from '../../../routes/(main)/types';

	export let forumData: ForumDetailTypes[];
</script>

<section class="w-full h-atuo mt-14 flex flex-col justify-center items-center gap-6 min-w-full">
	{#each forumData as data (data.id)}
		<!-- card container -->
		<div class="bg-gray-100 w-full h-auto p-4 flex flex-col max-w-4xl md:px-8 md:py-1">
			<!-- profile wrapper-->
			<div class="m-4 flex items-center">
				<div class="w-12 h-12 rounded-full flex justify-center items-center overflow-hidden">
					<img
						class="w-full h-full object-cover"
						src={`https://xsgames.co/randomusers/assets/avatars/pixel/${data.id}.jpg`}
						alt="Handsome man with glasses"
					/>
				</div>
				<div class="ml-4">
					<h1 class="font-bold text-xs my-1 sm:text-lg">{data.user}</h1>
					<p class="text-xs">{formatDateString(data.date)}</p>
				</div>
			</div>

			<!-- user message wrapper -->
			<p class="p-2 text-xs max-w-full sm:text-sm md:ml-2">{data.text}</p>

			<!-- interactions wrapper -->
			<div class="text-xs flex items-center p-4 gap-4 sm:text-sm">
				<!-- like -->
				<div class="flex gap-1">
					<button class="w-4">
						<svg
							class="feather feather-thumbs-up stroke-blue-700 hover:stroke-black"
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
							><path
								d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"
							></path></svg
						>
					</button>
					<p><span class="text-blue-800">{data.upvotes}</span> likes</p>
				</div>

				<!-- dislike -->
				<div class="flex gap-1">
					<button class="w-4">
						<svg
							class="feather feather-thumbs-down stroke-blue-700 hover:stroke-black"
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
							><path
								d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"
							></path></svg
						>
					</button>
					<p><span class="text-blue-800">{data.downvotes}</span> dislikes</p>
				</div>
			</div>
		</div>
	{/each}

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
