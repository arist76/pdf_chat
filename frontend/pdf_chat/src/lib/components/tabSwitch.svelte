<script lang="ts">
    import { page } from "$app/stores";
    
    export let currentTab:string;
    const firstText = "Chat";
    const secondText = "Forum";

    let grade : string | null = $page.params.grade 
    let subject : string | null = $page.params.subject 


</script>

<div class="mx-8 shadow rounded-full h-10 mt-4 flex p-1 relative items-center text-xs w-[10rem] md:w-full md:text-base">
    
    <div class="w-full flex justify-center">
        <a href="/chat/{grade}/{subject}">{firstText}</a>
    </div>
    <div class="w-full flex justify-center">
        <a href="/forum/{grade}/{subject}">{secondText}</a>
    </div>
    <span
    id="current-tab" 
    class="bg-indigo-600 shadow text-white capitalize flex items-center justify-center w-1/2 rounded-full h-8 top-[4px] absolute"
    style="transform: translateX({currentTab === 'forum' ? '90%' : '0'})"
    >
    {currentTab}
    </span>

</div>
