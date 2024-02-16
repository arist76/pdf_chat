<script lang="ts">
  import { toast } from '@zerodevx/svelte-toast'
  import { goto } from '$app/navigation';
  import TextInput from "$lib/inputs/+textInput.svelte";
  import SelectInput from "$lib/inputs/+selectInput.svelte";
  import ThemeToggle from "$lib/components/themeToggle.svelte";
	import { register,login,validatePassword } from '$lib/components/auth/auth';

  let formData = {
    firstName: '',
    lastName: '',
    email: '',
    username: '',
    gender: '',
    grade: '',
    password: '',
    repeatPassword: '',
    termsAccepted: false,
  };


 
  const handleSubmit = async () => {

      // Perform form submission logic, such as validation and sending to an API
      if (formData.password !== formData.repeatPassword) {
        toast.push('Passwords do not match.')
        return;
      }
      if (!validatePassword(formData.password)) {
        toast.push('Password must be longer than 8 characters and include uppercase, lowercase, numbers, and special characters.');
        return;
      }
      
      // register user 
      const isRegisterd = await register(formData.username,formData.email,formData.password)

      if (isRegisterd) {
        // login user 
        const isLogin = await login(formData.username,formData.password)
        if(isLogin) {
          toast.push('registerd successfully.')
          goto('/')
        }
        else {
          toast.push('registerd successfully. please login')
          goto('/signin')
        }
      } else {
        toast.push('Something went wrong. please try again!')

      }
      
      
    };
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
            <form on:submit|preventDefault={handleSubmit}>

            <div class="lg:max-w-lg lg:mx-auto lg:me-0 ms-auto">
              <!-- Card -->
              <div class="p-4 sm:p-7 flex flex-col bg-white rounded-2xl shadow-lg dark:bg-slate-900">
                <div class="text-center">
                  <h1 class="block text-2xl font-bold text-gray-800 dark:text-white">Start your free trial</h1>
                  <p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
                    Already have an account?
                    <a class="text-blue-600 decoration-2 hover:underline font-medium dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="/signin">
                      Sign in here
                    </a>
                  </p>
                </div>
  
                <div class="mt-5">
              
  
  
                  <!-- Grid -->
                  <div class="grid grid-cols-2 gap-4">
                    <!-- Input Group -->
                    <div>
                      <!-- Floating Input -->
                      <TextInput type="text" placeholder="First name" bind:value={formData.firstName} required={true}/>
                                   <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->
  
                    <!-- Input Group -->
                    <div>
                      <!-- Floating Input -->
                      <TextInput type="text" placeholder="Last name" bind:value={formData.lastName} required={true}/>
                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->
  
                    <!-- Input Group -->
                    <div>
                      <!-- Floating Input -->
                      <TextInput type="email" placeholder="Email" bind:value={formData.email} required={true}/>
                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->
  
                    <!-- Input Group -->
                    <div>
                      <!-- Floating Input -->
                      <TextInput type="text" placeholder="Username" bind:value={formData.username} required={true}/>
                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->

                    <!-- Input Group -->
                    <div class="relative col-span-full grid grid-cols-2 gap-4">
                      <div>
                        <SelectInput label="Gender" options={["Male", "Female"]} bind:selectedValue={formData.gender}/>
                      </div>
                      <div>
                          <SelectInput label="Grade" options="{[...Array(12).keys()].map(n => `Grade ${n+1}`)}" bind:selectedValue={formData.grade}/>
                      </div>
                    </div>
  
                    <!-- Input Group -->
                    <div class="relative col-span-full">
                      <!-- Floating Input -->
                    <TextInput type="password" placeholder="Password" bind:value={formData.password} required={true}/>

                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->
  
                    <!-- Input Group -->
                    <div class="col-span-full">
                      <!-- Floating Input -->
                      <TextInput type="password" placeholder="Repeat password" bind:value={formData.repeatPassword} required={true}/>
                      <!-- End Floating Input -->
                    </div>
                    <!-- End Input Group -->
                  </div>
                  <!-- End Grid -->
  
                  <!-- Checkbox -->
                  <div class="mt-5 flex items-center">
                    <div class="flex">
                      <input id="termsAccepted" type="checkbox" class="shrink-0 mt-0.5 border-gray-200 rounded text-blue-600 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:checked:bg-blue-500 dark:checked:border-blue-500 dark:focus:ring-offset-gray-800" bind:checked={formData.termsAccepted}>
                    </div>
                    <div class="ms-3">
                       <label for="termsAccepted"class="text-sm dark:text-white">I accept the <a class="text-blue-600 decoration-2 hover:underline font-medium dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">Terms and Conditions</a></label>
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