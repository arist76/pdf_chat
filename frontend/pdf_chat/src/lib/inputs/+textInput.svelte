<!-- Floating Input -->
<script lang="ts">
  export let type : string;
  export let placeholder : string;
  export let required : boolean;


  const strongPassword = {
    "target": "#hs-strong-password-with-indicator-and-hint-in-popover",
    "hints": "#hs-strong-password-popover",
    "stripClasses": "hs-strong-password:opacity-100 hs-strong-password-accepted:bg-teal-500 h-2 flex-auto rounded-full bg-blue-500 opacity-50 mx-1",
    "mode": "popover"
  }

</script>
<div class="relative flex-1">
  <input type="{type}" id="hs-floating-underline-input-text" class="peer py-4 px-0 block w-full bg-transparent border-t-transparent border-b-2 border-x-transparent border-b-slate-300 text-sm placeholder:text-transparent focus:border-t-transparent focus:border-x-transparent focus:border-b-blue-500 focus:ring-0 disabled:opacity-50 disabled:pointer-events-none dark:border-b-gray-700 dark:text-gray-400 dark:focus:ring-gray-600 dark:focus:border-b-gray-600
  focus:pt-6
  focus:pb-2
  [&:not(:placeholder-shown)]:pt-6
  [&:not(:placeholder-shown)]:pb-2
  autofill:pt-6
  autofill:pb-2
  outline-none"
  placeholder="********"
  {required}/>
  {#if type == "password"}
  
    <div id="hs-strong-password-popover" class="hidden absolute z-10 w-full bg-white shadow-md rounded-lg p-4 dark:bg-gray-800 dark:border dark:border-gray-700 dark:divide-gray-700">
      <div id="hs-strong-password-in-popover" data-hs-strong-password="{JSON.stringify(strongPassword)}" class="flex mt-2 -mx-1">
      </div>

      <h4 class="mt-3 text-sm font-semibold text-gray-800 dark:text-white">
        Your password must contain:
      </h4>

      <ul class="space-y-1 text-sm text-gray-500">
        <li data-hs-strong-password-hints-rule-text="min-length" class="hs-strong-password-active:text-teal-500 flex items-center gap-x-2">
          <span class="hidden" data-check>
            <svg class="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
          </span>
          <span data-uncheck>
            <svg class="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          </span>
          Minimum number of characters is 6.
        </li>
        <li data-hs-strong-password-hints-rule-text="lowercase" class="hs-strong-password-active:text-teal-500 flex items-center gap-x-2">
          <span class="hidden" data-check>
            <svg class="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
          </span>
          <span data-uncheck>
            <svg class="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          </span>
          Should contain lowercase.
        </li>
        <li data-hs-strong-password-hints-rule-text="uppercase" class="hs-strong-password-active:text-teal-500 flex items-center gap-x-2">
          <span class="hidden" data-check>
            <svg class="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
          </span>
          <span data-uncheck>
            <svg class="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          </span>
          Should contain uppercase.
        </li>
        <li data-hs-strong-password-hints-rule-text="numbers" class="hs-strong-password-active:text-teal-500 flex items-center gap-x-2">
          <span class="hidden" data-check>
            <svg class="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
          </span>
          <span data-uncheck>
            <svg class="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          </span>
          Should contain numbers.
        </li>
        <li data-hs-strong-password-hints-rule-text="special-characters" class="hs-strong-password-active:text-teal-500 flex items-center gap-x-2">
          <span class="hidden" data-check>
            <svg class="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
          </span>
          <span data-uncheck>
            <svg class="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          </span>
          Should contain special characters.
        </li>
      </ul>
    </div>
    
  {/if}

  <label for="hs-floating-underline-input-passowrd" class="absolute top-0 start-0 py-4 px-0 h-full text-sm truncate pointer-events-none transition ease-in-out duration-100 border border-transparent dark:text-white peer-disabled:opacity-50 peer-disabled:pointer-events-none
    peer-focus:text-xs
    peer-focus:-translate-y-5
    peer-focus:text-gray-500
    peer-[:not(:placeholder-shown)]:text-xs
    peer-[:not(:placeholder-shown)]:-translate-y-5
    peer-[:not(:placeholder-shown)]:text-gray-500">{placeholder}</label>
</div>
<!-- End Floating Input -->