
<script>
  import Sidebar from "$lib/components/sidebar.svelte";
  import TopBreadcrumb from "$lib/components/topBreadcrumb.svelte";
  import ChatBody from "$lib/components/chatBody.svelte";
  import { browser } from "$app/environment";
  import { page } from "$app/stores";


  // if (browser) {
  //   document.cookie += `grade=${$page.params.grade}; path=/;`
  //   document.cookie += `subject=${$page.params.subject}; path=/;`
  //   console.log(document.cookie)
  // }

</script>

<div class="flex">
  <div class="bg-gray-50 w-full dark:bg-slate-900">
    <TopBreadcrumb/>
    <Sidebar/>
    <ChatBody/>
  </div>
</div>