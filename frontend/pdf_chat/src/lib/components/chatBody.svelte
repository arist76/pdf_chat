<script lang="ts">
    import TabSwitch from "./tabSwitch.svelte";
    import AiChat from "./AIChat/AIChat.svelte";
    import {currentTab} from '$lib/store'
	import Forum from "./Forum/Forum.svelte";

</script>

<!-- Content -->
<div class="w-full h-auto pt-10 px-4 sm:px-6 md:px-8 lg:ps-72 flex flex-col items-center">
    <div class="mb-5 flex items-center justify-center w-full sm:w-1/3">
        <TabSwitch/>
    </div>
    <div class="w-full">
        {#if $currentTab == "chat" || currentTab == null}
            <AiChat/>
        {:else}
            <Forum/>
        {/if}
    </div>

</div>
