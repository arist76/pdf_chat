<script lang="ts">
    import "../app.css";
    import { SvelteToast } from '@zerodevx/svelte-toast'
    import { afterNavigate } from "$app/navigation";

    afterNavigate(() => {
        HSStaticMethods.autoInit();
    });
</script>

<SvelteToast />
<slot />


<style>
    :root {
    --toastBackground: #438eff;
    --toastColor: #ffffff;    
    --toastBarBackground: #265ffc; 
    }
</style>