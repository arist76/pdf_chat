<script>
	import TabSwitch from '$lib/components/tabSwitch.svelte';
	import ForumsList from '$lib/components/Forum/ForumsList.svelte';
	export let data;
</script>

<div class="flex">
	<div class="bg-gray-50 w-full dark:bg-slate-900">
		<!-- Content -->
		<div class="w-full h-auto pt-10 px-4 sm:px-6 md:px-8 lg:ps-72 flex flex-col items-center">
			<div class="mb-5 flex items-center justify-center w-full sm:w-1/3">
				<TabSwitch currentTab="forum" />
			</div>
			<div class="w-full lg:w-[80%]">
				<ForumsList data={data.forums} />
			</div>
		</div>
	</div>
</div>
