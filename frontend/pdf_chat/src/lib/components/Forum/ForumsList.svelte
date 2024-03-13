<script lang="ts">
	import type { ForumDataTypes } from "../../../routes/(main)/types";

	export let data:ForumDataTypes[];
</script>

<section class="w-full h-auto mt-14 flex flex-col justify-center items-center gap-6 min-w-full">
	{#each data as item (item.id)}
		<!-- card -->
		<div class="flex flex-col gap-4 w-full text-xs p-4 border-y-[.5px] border-gray-300 sm:text-sm">
			<!-- status -->
			<div class="flex gap-2">
				<p>{item.grade} votes</p>
				<p>{item.grade} answers</p>
				<p>{item.id} views</p>
			</div>
			<!-- title and desc -->
			<div class="flex flex-col gap-2">
				<a href={`/forum/${item.grade}/${item.subject}/${item.title_slug}`} class="text-sm text-blue-900 font-semibold sm:text-lg">{item.title}</a>
				<p>{item.description}</p>
			</div>
			<!-- tags and date-->
			<div class="flex justify-between">
				<div class="flex gap-2">
					<!--{#each item.tags as tag (tag)}-->
					<!--<p class="h-auto p-1 border rounded-md bg-blue-200 text-xs">{tag}</p>-->
					<!--{/each}-->
				</div>
				<!--data-->
				<p>{item.subject}</p>
			</div>
		</div>
	{/each}
</section>
