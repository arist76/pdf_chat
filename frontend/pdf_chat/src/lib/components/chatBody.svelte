<script lang="ts">
    import TabSwitch from "./tabSwitch.svelte";
    import AiChat from "./AIChat/AIChat.svelte";
</script>

<!-- Content -->
<div class="w-full h-auto pt-10 px-4 sm:px-6 md:px-8 lg:ps-72 flex flex-col items-center">
    <div class="mb-5 flex items-center justify-center w-full sm:w-1/3">
        <TabSwitch currentTab='chat'/>
    </div>
    <div class="w-full">
		<AiChat/>
    </div>
</div>
