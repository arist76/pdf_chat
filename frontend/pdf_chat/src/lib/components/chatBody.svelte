<script>
    import TabSwitch from "./tabSwitch.svelte";
</script>

<!-- Content -->
<div class="w-screen h-screen pt-10 px-4 sm:px-6 md:px-8 lg:ps-72 flex flex-col items-center">
    <div class="w-1/3 mb-5">
        <TabSwitch/>
    </div>
    <div>
        {#if false}
            <h1>Hello</h1>
        {:else}
            <h2>Bye</h2>
        {/if}
    </div>

</div>
