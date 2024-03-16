<script lang="ts">
	import { formatDateString } from '$lib/utils';
	import type { ForumDetailTypes } from '../../../routes/(main)/types';

	export let data: ForumDetailTypes;
	export let handleUpVote;
	export let handleDownVote;
</script>

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
			<h1 class="font-bold text-xs my-1 sm:text-lg">{data.user.username}</h1>
			<p class="text-xs">{formatDateString(data.date)}</p>
		</div>
	</div>

	<!-- user message wrapper -->
	<p class="p-2 text-xs max-w-full sm:text-sm md:ml-2">{data.text}</p>

	<!-- interactions wrapper -->
	<div class="text-xs flex items-center p-4 gap-4 sm:text-sm">
		<!-- like -->
		<div class="flex gap-1">
			<button on:click={handleUpVote} class="w-4">
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
			<button on:click={handleDownVote} class="w-4">
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
