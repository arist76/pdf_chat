<script lang="ts">
    import anime from 'animejs'
    import { browser } from "$app/environment";
    import { slide } from 'svelte/transition';

    export let currentTab : string | null = browser ? localStorage.getItem("currentTab") : null
    
    const firstText = "Chat"
    const secondText = "Forum"
    
    
    const toggleTab = () => {
        let currentTabSpan = document.querySelector("#current-tab")
        let currentTabSpanWidth = currentTabSpan?.computedStyleMap().get("width")
        
        if (currentTabSpan != null && currentTab == null) {
            currentTab = currentTabSpan.textContent 
        }
        
        if (currentTabSpan != null && currentTab == firstText) {
            currentTab = secondText
            // currentTabSpan.textContent = secondText
            // slide(currentTabSpan, {})
            anime({
                targets : currentTabSpan,
                translateX: {
                    value: "93%",
                    easing: 'easeInOutExpo',
                    duration: 500
                },
                textContent: {
                    value: secondText,
                    delay: 400
                }
            })

        } else if (currentTabSpan != null && currentTab == secondText) {
            currentTab = firstText
            // currentTabSpan.textContent = firstText
            // slide(currentTabSpan, {axis : "x"})
            anime({
                targets: currentTabSpan,
                translateX: {
                    value: "-=93%",
                    easing: 'easeInOutExpo',
                    duration: 500
                },
                textContent: {
                    value: firstText,
                    enddelay: 400
                }
            })

        }


    }
</script>

<div class="mx-8 shadow rounded-full h-10 mt-4 flex p-1 relative items-center">
    <div class="w-full flex justify-center">
        <button on:click="{toggleTab}">{firstText}</button>
    </div>
    <div class="w-full flex justify-center">
        <button on:click="{toggleTab}">{secondText}</button>
    </div>
    <span
    id="current-tab" 
    class="bg-indigo-600 shadow text-white flex items-center justify-center w-1/2 rounded-full h-8 top-[4px] absolute">
    {firstText}
    </span>

</div>