<!-- Floating Input -->
<script lang="ts">
  export let type : string;
  export let placeholder : string;
  export let required : boolean;
  export let value: string;

  function handleInput(event: Event) {
  const input = event.target as HTMLInputElement;
  value = input.value;
}
  const strongPassword = {
    "target": "#hs-strong-password-with-indicator-and-hint-in-popover",
    "hints": "#hs-strong-password-popover",
    "stripClasses": "hs-strong-password:opacity-100 hs-strong-password-accepted:bg-teal-500 h-2 flex-auto rounded-full bg-blue-500 opacity-50 mx-1",
    "mode": "popover"
  }

</script>
<div class="relative flex-1">
  <input type="{type}" id="hs-floating-underline-input-text" class="peer py-4 px-0 block w-full bg-transparent border-t-transparent border-b-2  border-x-transparent border-b-slate-300 text-sm placeholder:text-transparent focus:border-t-transparent focus:border-x-transparent focus:border-b-blue-500 focus:ring-0 disabled:opacity-50 disabled:pointer-events-none dark:border-b-gray-700 dark:text-gray-400 dark:focus:ring-gray-600 dark:focus:border-b-gray-600
  focus:pt-6
  focus:pb-2
  [&:not(:placeholder-shown)]:pt-6
  [&:not(:placeholder-shown)]:pb-2
  autofill:pt-6
  autofill:pb-2
  outline-none"
  placeholder="********" 
  on:input={handleInput}
  {required}/>
    <label for="hs-floating-underline-input-passowrd" class="absolute top-0 start-0 py-4 px-0 h-full text-sm truncate pointer-events-none transition ease-in-out duration-100 border border-transparent dark:text-white peer-disabled:opacity-50 peer-disabled:pointer-events-none
      peer-focus:text-xs
      peer-focus:-translate-y-5
      peer-focus:text-gray-500
      peer-[:not(:placeholder-shown)]:text-xs
      peer-[:not(:placeholder-shown)]:-translate-y-5
      peer-[:not(:placeholder-shown)]:text-gray-500
      text-gray-500">{placeholder}</label>

</div>
<!-- End Floating Input -->