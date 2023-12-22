<script lang="ts">
    export let options : string[];
    export let label : string;
</script>

<select class="py-3  block w-full text-slate-500 border-slate-300 border-b-2 text-sm focus:outline-none focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600">
    <option selected>{label}</option>
    {#each options as option}
        <option>{option}</option>
    {/each}
</select>