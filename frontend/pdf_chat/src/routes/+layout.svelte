<script lang="ts">
    import "../app.css";
    import { SvelteToast } from '@zerodevx/svelte-toast'
    import { afterNavigate } from "$app/navigation";
    import { browser } from '$app/environment'
    import { QueryClient, QueryClientProvider } from '@tanstack/svelte-query'

    const queryClient = new QueryClient({
        defaultOptions: {
        queries: {
            enabled: browser,
        },
        },
    })

    afterNavigate(() => {
        HSStaticMethods.autoInit();
    });
</script>

<SvelteToast />
<QueryClientProvider client={queryClient}>
    <slot />
</QueryClientProvider>


<style>
    :root {
    --toastBackground: #438eff;
    --toastColor: #ffffff;    
    --toastBarBackground: #265ffc; 
    }
</style>