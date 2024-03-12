
<script>
  import Sidebar from "$lib/components/sidebar.svelte";
  import TopBreadcrumb from "$lib/components/topBreadcrumb.svelte";
  import ChatBody from "$lib/components/chatBody.svelte";
</script>

<div class="flex">
  <div class="bg-gray-50 w-full dark:bg-slate-900">
    <Sidebar/>
    <ChatBody/>
  </div>
</div>