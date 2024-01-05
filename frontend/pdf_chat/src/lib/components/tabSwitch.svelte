<script lang="ts">
  import anime from 'animejs';
  import { currentTab } from '$lib/store';

  const firstText = "Chat";
  const secondText = "Forum";

  $: currentTabValue = $currentTab;

  function toggleTab() {
      currentTab.update(value => value === 'chat' ? 'forum' : 'chat');
      animateTabSwitch();
  }

  function animateTabSwitch() {
      let targetValue = currentTabValue === 'chat' ? "93%" : "-=93%";

      anime({
          targets: "#current-tab",
          translateX: {
              value: targetValue,
              easing: 'easeInOutExpo',
              duration: 300
          },
      });
  }
</script>

<div class="mx-8 shadow rounded-full h-10 mt-4 flex p-1 relative items-center text-xs w-[10rem] md:w-full md:text-base">
    
    <div class="w-full flex justify-center">
        <button on:click="{toggleTab}">{firstText}</button>
    </div>
    <div class="w-full flex justify-center">
        <button on:click="{toggleTab}">{secondText}</button>
    </div>
    <span
    id="current-tab" 
    class="bg-indigo-600 shadow text-white capitalize flex items-center justify-center w-1/2 rounded-full h-8 top-[4px] absolute">
    {$currentTab}
    </span>

</div>
