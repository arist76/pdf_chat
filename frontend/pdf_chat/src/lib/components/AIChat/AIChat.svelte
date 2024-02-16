<script lang="ts">
	import { getChat } from "$lib/api/getChat";
	import { postChat } from "$lib/api/postChat";
  import aiSparkle from "$lib/images/aiSparkle.png"
	import { createMutation, createQuery, useQueryClient } from "@tanstack/svelte-query";

  const queryClient = useQueryClient()
  const chats = createQuery({queryKey: ['chats'],queryFn: getChat,})
  const createChat = createMutation({mutationFn: postChat})
  let messageText = '';

    
  function sendMessage() {
    $createChat.mutate(messageText, {
    onSuccess: () => {
      messageText = '';
      queryClient.invalidateQueries({queryKey:['chats']})
    },
  });
  }
  function handleInput(event: Event & { currentTarget: HTMLTextAreaElement }) {
  if (event.target instanceof HTMLTextAreaElement) {
      messageText = event.target.value;
  }
}
</script>

<!-- Content -->
<div class="relative h-screen">
    <div class="py-10 lg:py-14">

      <ul class="mt-16 space-y-5">

      {#if $chats.isLoading}
        <p>Loading...</p>
      {:else if $chats.isError}
        <p>Error: {$chats.error.message}</p>
      {:else if $chats.isSuccess}

  
      {#each $chats.data as message}
          {#if message.type === 'Human'}
              <!-- User Chat Bubble -->
              <li class="max-w-4xl py-2 px-4 sm:px-6 lg:px-8 mx-auto flex gap-x-2 items-center sm:gap-x-4">
                <!-- User Avatar or Placeholder -->
                <div class="flex-shrink-0 w-[2.375rem] h-[2.375rem] rounded-full">
                  <img src="{aiSparkle}" alt="User Avatar" class="w-full h-full">
                </div>

                <div class="space-y-3">
                  <div class="space-y-1.5">
                    <p class="mb-1.5 text-sm text-gray-800 dark:text-white">
                      {message.text}
                    </p>
                  </div>
                </div>
              </li>
              <!-- End User Chat Bubble -->
        {:else if message.type === 'Ai'}
          <!-- AI Chat Bubble -->
          <li class="py-2 sm:py-4">
            <div class="max-w-4xl px-4 sm:px-6 lg:px-8 mx-auto">
              <div class="max-w-2xl flex gap-x-2 sm:gap-x-4">
                <!-- AI Avatar or Placeholder -->
                <span class="flex-shrink-0 inline-flex items-center justify-center h-[2.375rem] w-[2.375rem] rounded-full bg-gray-600">
                  <span class="text-sm font-medium text-white leading-none">AI</span>
                </span>

                <div class="grow mt-2 space-y-3">
                  <p class="text-gray-800 dark:text-gray-200">
                    {message.text}
                  </p>
                </div>
              </div>
            </div>
          </li>
          <!-- End AI Chat Bubble -->
        {/if}
    {/each}
    {/if}
  
      </ul>
    </div>
  
    <!-- Search -->
    <div class="sticky bottom-0 z-10 bg-white border-t border-gray-200 pt-2 pb-3 sm:pt-4 sm:pb-6 dark:bg-slate-900 dark:border-gray-700">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center mb-3">
          <button type="button" class="py-1.5 px-2 inline-flex items-center gap-x-2 text-xs font-medium rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-white dark:hover:bg-gray-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
            <svg class="w-3 h-3" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
              <path d="M5 3.5h6A1.5 1.5 0 0 1 12.5 5v6a1.5 1.5 0 0 1-1.5 1.5H5A1.5 1.5 0 0 1 3.5 11V5A1.5 1.5 0 0 1 5 3.5z"/>
            </svg>
            Stop generating
          </button>
        </div>
  
        <!-- Input -->
        <div class="relative">
          <textarea bind:value={messageText}
          on:input={handleInput} class="p-4 pb-12 block w-full border-gray-200 border rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600" placeholder="Ask me anything..."></textarea>
  
          <!-- Toolbar -->
          <div class="absolute bottom-px inset-x-px p-2 rounded-b-md bg-white dark:bg-slate-900">
            <div class="flex justify-between items-center">
              <!-- Button Group -->
              <div class="flex items-center">
              </div>
              <!-- End Button Group -->
  
              <!-- Button Group -->
              <div class="flex items-center gap-x-1">
  
                <!-- Send Button -->
                <button on:click={sendMessage} type="button" class="inline-flex flex-shrink-0 justify-center items-center h-8 w-8 rounded-lg text-white bg-blue-600 hover:bg-blue-500 focus:z-10 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
                  <svg class="flex-shrink-0 h-3.5 w-3.5" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083l6-15Zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471-.47 1.178Z"/>
                  </svg>
                </button>
                <!-- End Send Button -->
              </div>
              <!-- End Button Group -->
            </div>
          </div>
          <!-- End Toolbar -->
        </div>
        <!-- End Input -->
      </div>
    </div>
    <!-- End Search -->
  </div>
  <!-- End Content -->