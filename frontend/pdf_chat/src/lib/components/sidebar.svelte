<script>
  import SidebarButton from "./sidebarUtils/sidebarButton.svelte";
  import ThemeToggle from "./themeToggle.svelte";
  const subjects = ["Math", "English", "Amharic", "Physics"]
</script>

<!-- Sidebar -->
<div id="application-sidebar-brand" class="hs-overlay hs-overlay-open:translate-x-0 -translate-x-full transition-all duration-300 transform hidden fixed top-0 start-0 bottom-0 z-[60] w-64 bg-blue-700 pt-7 pb-10 overflow-y-auto lg:block lg:translate-x-0 lg:end-auto lg:bottom-0 [&::-webkit-scrollbar]:w-2 [&::-webkit-scrollbar-thumb]:rounded-full [&::-webkit-scrollbar-track]:bg-gray-100 [&::-webkit-scrollbar-thumb]:bg-gray-300 dark:[&::-webkit-scrollbar-track]:bg-slate-700 dark:[&::-webkit-scrollbar-thumb]:bg-slate-500">

  <div class="px-6 flex justify-between items-center">
    <a class="flex-none text-xl font-semibold text-white" href="#" aria-label="Brand">Grade Up</a>
  </div>

  <nav class="hs-accordion-group p-6 w-full flex flex-col flex-wrap" data-hs-accordion-always-open>
    <ul class="space-y-1.5">

      {#each [9, 10 ,11, 12] as grade}
        <li class="hs-accordion" id="account-accordion">
          <SidebarButton name={`Grade ${grade}`}/>

          <div id="account-accordion-child" class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300 hidden">
            <ul class="pt-2 ps-2">
              {#each subjects as subject}
              <li>
                <a class="flex items-center gap-x-3.5 py-2 px-2.5 text-sm text-white hover:text-white rounded-lg hover:bg-blue-600" href="#">
                  {subject}
                </a>
              </li>
              {/each}
            </ul>
          </div>
        </li>
      {/each}  
    </ul>
  </nav>

	<!--Buttons-->
  <div class="fixed bottom-0 w-full h-auto p-4 flex items-center justify-center font-semibold text-blue-900 text-sm"> 
		<button on:click class="bg-white px-6 py-1 border rounded-sm"> Logout </button>
</div>
</div>

<!-- End Sidebar -->
