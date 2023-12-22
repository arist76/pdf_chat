<script lang="ts">
  import TextInput from "$lib/inputs/+textInput.svelte";
  import SelectInput from "$lib/inputs/+selectInput.svelte";
  import ThemeToggle from "$lib/components/themeToggle.svelte";


</script>

<!-- Hero -->

<div class="relative bg-gradient-to-bl from-blue-100 via-transparent dark:from-slate-900 dark:bg-slate-950">
  <div class="absolute top-10 left-10 w-auto h-auto">
    <ThemeToggle/>
  </div>
    <div class="max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
      <!-- Grid -->
      <div class="grid items-center md:grid-cols-2 gap-8 lg:gap-12">
        <div>
          <!-- small gradient text -->
          <p class="inline-block text-sm font-medium bg-clip-text bg-gradient-to-l from-blue-600 to-violet-500 text-transparent dark:from-blue-400 dark:to-violet-400">
            GradeUP: dive in to a new world
          </p>
  
          <!-- Title -->
          <div class="mt-4 md:mb-12 max-w-2xl">
            <h1 class="mb-4 font-semibold text-gray-800 text-4xl lg:text-5xl dark:text-gray-200">
              Use AI to power your studies.
            </h1>
            <p class="text-gray-600 dark:text-gray-400">
              Our goal is to create a ground breaking platform that students can use to easily integrate to their study methods. We use the power of AI and some other tools to create a dynamic way for students to interact with their books.
            </p>
          </div>
          <!-- End Title -->
        </div>
        <!-- End Col -->
  
        <div>
          <!-- Form -->
          <form>
            <div class="lg:max-w-lg lg:mx-auto lg:me-0 ms-auto">
              <!-- Card -->
              <div class="p-4 sm:p-7 flex flex-col bg-white rounded-2xl shadow-lg dark:bg-slate-900">
                <div class="text-center">
                  <h1 class="block text-2xl font-bold text-gray-800 dark:text-white">Start your free trial</h1>
                  <p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
                    Already have an account?
                    <a class="text-blue-600 decoration-2 hover:underline font-medium dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">
                      Sign in here
                    </a>
                  </p>
                </div>
  
                <div class="mt-5">
                  <button type="button" class="w-full py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-white dark:hover:bg-gray-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
                    <svg class="w-4 h-auto" width="46" height="47" viewBox="0 0 46 47" fill="none">
                      <path d="M46 24.0287C46 22.09 45.8533 20.68 45.5013 19.2112H23.4694V27.9356H36.4069C36.1429 30.1094 34.7347 33.37 31.5957 35.5731L31.5663 35.8669L38.5191 41.2719L38.9885 41.3306C43.4477 37.2181 46 31.1669 46 24.0287Z" fill="#4285F4"></path>
                      <path d="M23.4694 47C29.8061 47 35.1161 44.9144 39.0179 41.3012L31.625 35.5437C29.6301 36.9244 26.9898 37.8937 23.4987 37.8937C17.2793 37.8937 12.0281 33.7812 10.1505 28.1412L9.88649 28.1706L2.61097 33.7812L2.52296 34.0456C6.36608 41.7125 14.287 47 23.4694 47Z" fill="#34A853"></path>
                      <path d="M10.1212 28.1413C9.62245 26.6725 9.32908 25.1156 9.32908 23.5C9.32908 21.8844 9.62245 20.3275 10.0918 18.8588V18.5356L2.75765 12.8369L2.52296 12.9544C0.909439 16.1269 0 19.7106 0 23.5C0 27.2894 0.909439 30.8731 2.49362 34.0456L10.1212 28.1413Z" fill="#FBBC05"></path>
                      <path d="M23.4694 9.07688C27.8699 9.07688 30.8622 10.9863 32.5344 12.5725L39.1645 6.11C35.0867 2.32063 29.8061 0 23.4694 0C14.287 0 6.36607 5.2875 2.49362 12.9544L10.0918 18.8588C11.9987 13.1894 17.25 9.07688 23.4694 9.07688Z" fill="#EB4335"></path>
                    </svg>
                    Sign up with Google
                  </button>
  
                  <div class="py-3 flex items-center text-xs text-gray-400 uppercase before:flex-[1_1_0%] before:border-t before:border-gray-200 before:me-6 after:flex-[1_1_0%] after:border-t after:border-gray-200 after:ms-6 dark:text-gray-500 dark:before:border-gray-700 dark:after:border-gray-700">Or</div>
  
                  <!-- Grid -->
                  <div class="grid grid-cols-2 gap-4">
                    <!-- Input Group -->
                    <div>
                      <!-- Floating Input -->
                      <TextInput type="text" placeholder="First name" required={true}/>
                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->
  
                    <!-- Input Group -->
                    <div>
                      <!-- Floating Input -->
                      <TextInput type="text" placeholder="Last name" required={true}/>
                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->
  
                    <!-- Input Group -->
                    <div>
                      <!-- Floating Input -->
                      <TextInput type="email" placeholder="Email" required={true}/>
                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->
  
                    <!-- Input Group -->
                    <div>
                      <!-- Floating Input -->
                      <TextInput type="text" placeholder="Username" required={true}/>
                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->

                    <!-- Input Group -->
                    <div class="relative col-span-full grid grid-cols-2 gap-4">
                      <div>
                        <SelectInput label="Gender" options={["Male", "Female"]}/>
                      </div>
                      <div>
                        <SelectInput label="Grade" options="{[...Array(12).keys()].map(n => `Grade ${n+1}`)}"/>
                      </div>
                    </div>
  
                    <!-- Input Group -->
                    <div class="relative col-span-full">
                      <!-- Floating Input -->
                    <TextInput  type="password" placeholder="Password" required={true}/>

                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->
  
                    <!-- Input Group -->
                    <div class="col-span-full">
                      <!-- Floating Input -->
                      <TextInput  type="password" placeholder="Repeat password" required={true}/>
                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->
                  </div>
                  <!-- End Grid -->
  
                  <!-- Checkbox -->
                  <div class="mt-5 flex items-center">
                    <div class="flex">
                      <input id="remember-me" name="remember-me" type="checkbox" class="shrink-0 mt-0.5 border-gray-200 rounded text-blue-600 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:checked:bg-blue-500 dark:checked:border-blue-500 dark:focus:ring-offset-gray-800">
                    </div>
                    <div class="ms-3">
                      <label for="remember-me" class="text-sm dark:text-white">I accept the <a class="text-blue-600 decoration-2 hover:underline font-medium dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">Terms and Conditions</a></label>
                    </div>
                  </div>
                  <!-- End Checkbox -->
  
                  <div class="mt-5">
                    <button type="submit" class="w-full py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">Get started</button>
                  </div>
                </div>
              </div>
              <!-- End Card -->
            </div>
          </form>
          <!-- End Form -->
        </div>
        <!-- End Col -->
      </div>
      <!-- End Grid -->
    </div>
    <!-- End Clients Section -->
  </div>
  <!-- End Hero -->