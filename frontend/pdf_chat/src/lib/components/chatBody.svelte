<script lang="ts">
    import TabSwitch from "./tabSwitch.svelte";
    import AiChat from "./AIChat/AIChat.svelte";
    let currentTab : string | null;
</script>

<!-- Content -->
<div class="w-screen h-screen pt-10 px-4 sm:px-6 md:px-8 lg:ps-72 flex flex-col items-center">
    <div class="w-1/3 mb-5">
        <TabSwitch currentTab={currentTab}/>
    </div>
    <div>
        {#if currentTab == "Chat" || currentTab == null}
            <AiChat/>
        {:else}
            <h2>Bye</h2>
        {/if}
    </div>

</div>
