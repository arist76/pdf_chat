<script lang="ts">
    // import anime from 'animejs'

    const firstText = "Chat"
    const secondText = "Forum"

    // const chatTab = document.querySelector("#tab-switch-wrapper button:nth-child(1)")
    // const forumTab = document.querySelector("#tab-switch-wrapper button:nth-child(2)")
    // const toggle = document.querySelector("#tab-switch-wrapper button:nth-child(3)")
    
    // const toggleTab = () => {
    //     let current = toggle?.textContent

    //     if (current = firstText) {
    //         if (toggle) {
    //           toggle.textContent = secondText
    //         }
    //         anime({
    //             targets: toggle,
    //             translateX: "100%"
    //         })

    //     } else if (current === secondText) {
    //         if (toggle) {
    //           toggle.textContent = firstText
    //         }
    //         anime({
    //             targets: toggle,
    //             translateX: "100%"
    //         })
    //     } 

    // }
</script>

<div class="mx-8 shadow rounded-full h-10 mt-4 flex p-1 relative items-center" id="tab-switch-wrapper">
    <div class="w-full flex justify-center">
        <button>{firstText}</button>
    </div>
    <div class="w-full flex justify-center">
        <button>{secondText}</button>
    </div>
    <span 
    class="elSwitch bg-indigo-600 shadow text-white flex items-center justify-center w-1/2 rounded-full h-8 transition-all top-[4px] absolute left-1 ">
    {firstText}
    </span>
</div>