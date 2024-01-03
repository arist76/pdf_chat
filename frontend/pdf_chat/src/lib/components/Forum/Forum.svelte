<script>
    const forumData = [
      {
        name: "Jane Smith",
        message: "Aliquam erat volutpat. In hac habitasse platea dictumst. Optio itaque consectetur adipisicing elit. Optio itaque consectetur adipisicing elit. Optio itaque?",
        timestamp: "2 hours ago",
        likes: 5,
        dislikes: 1,
        imgUrl: "https://img.freepik.com/free-photo/portrait-confident-businesswoman-glasses_1262-20950.jpg"
      },
      {
        name: "Alex Johnson",
        message: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        timestamp: "1 day ago",
        likes: 3,
        dislikes: 0,
        imgUrl: "https://img.freepik.com/free-photo/portrait-white-man-isolated_53876-40306.jpg"
      },
      {
        name: "Samantha Lee",
        message: "Etiam porta sem malesuada magna mollis euismod.",
        timestamp: "1 week ago",
        likes: 8,
        dislikes: 2,
        imgUrl: "https://img.freepik.com/free-photo/portrait-young-woman-with-glasses_1139-844.jpg"
      }
    ];
  </script>

<section class="w-full h-auto mt-14 flex flex-col justify-center items-center gap-6 min-w-full">

    {#each forumData as data}
    <!-- card container -->
    <div class='bg-gray-100 w-full p-4 flex flex-col max-w-4xl md:px-8 md:py-1'>
        <!-- profile wrapper-->
        <div class="m-4 flex items-center">
            <div class="w-12 h-12 rounded-full flex justify-center items-center overflow-hidden">
                <img class="w-full h-full object-cover" src="{data.imgUrl}" alt="Handsome man with glasses" />
            </div>
            <div class="ml-4">
                <h1 class="font-bold text-xs my-1 sm:text-lg">{data.name}</h1>
                <p class="text-xs">{data.timestamp}</p>
            </div>
        </div>
        
        <!-- user message wrapper -->
        <p class="p-2 text-xs max-w-full sm:text-sm md:ml-2">{data.message}</p> 
        
        <!-- interactions wrapper -->
        <div class="text-xs flex items-center p-4 gap-4 sm:text-sm">
            <!-- like -->
            <div class="flex gap-1">
                <button class="w-4">
                    <svg class="feather feather-thumbs-up stroke-blue-700" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg>
                </button>
                <p><span class="text-blue-800">{data.likes}</span> likes</p>
            </div>
           
            <!-- dislike -->
            <div class="flex gap-1">
                <button class="w-4">
                    <svg class="feather feather-thumbs-down stroke-blue-700" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"></path></svg>
                </button>
                <p><span class="text-blue-800">{data.dislikes}</span> dislikes</p>
            </div>
        </div>
    </div>
    {/each}

</section>