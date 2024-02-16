<script>
    let dummyData = [
      {
        votes: 2,
        answers: 0,
        views: 11,
        title: "Links in my forum discussion reply not working",
        description:
          "Am a beginner in website PHP, html and CSS. I installed this PHP Script and it's working good, but the problem is anytime my users want to add links to discussion reply it will show the URL as text not ...",
        tags: ["Math", "PHP", "HTML"],
        date: "Feb 12 at 19:51",
      },
      {
        votes: 5,
        answers: 2,
        views: 23,
        title: "Responsive design not working on mobile devices",
        description:
          "I am trying to make my website responsive, but it's not working on mobile devices. I have added media queries and set the viewport, but still facing issues. Can someone help me troubleshoot this?",
        tags: ["Web Design", "CSS", "Responsive"],
        date: "Feb 15 at 08:30",
      },
      {
        votes: 8,
        answers: 3,
        views: 45,
        title: "Error in my Python script - 'SyntaxError: invalid syntax'",
        description:
          "I'm getting a 'SyntaxError: invalid syntax' in my Python script, but I can't seem to find the issue. I've checked the code multiple times. Can someone please take a look and help me identify the problem?",
        tags: ["Python", "Programming", "Syntax Error"],
        date: "Feb 16 at 12:15",
      },
      {
        votes: 3,
        answers: 1,
        views: 18,
        title: "Need advice on choosing a front-end framework",
        description:
          "I'm planning to start a new project and I'm confused about which front-end framework to use. I'm considering React, Vue, and Angular. Any recommendations or experiences to share?",
        tags: ["Front-end", "React", "Vue", "Angular"],
        date: "Feb 18 at 14:42",
      },
    ];
  </script>
  
  <section class="w-full h-auto mt-14 flex flex-col justify-center items-center gap-6 min-w-full">
    {#each dummyData as card (card)}
      <!-- card -->
      <div class="flex flex-col gap-4 text-xs p-4 border-y-[.5px] border-gray-300 sm:text-sm">
        <!-- status -->
        <div class="flex gap-2 ">
          <p>{card.votes} votes</p>
          <p>{card.answers} answers</p>
          <p>{card.views} views</p>
        </div>
        <!-- title and desc -->
        <div class="flex flex-col gap-2">
          <a href="/forum/1" class="text-sm text-blue-900 font-semibold sm:text-lg ">{card.title}</a>
          <p>{card.description}</p>
        </div>
        <!-- tags and date-->
        <div class="flex justify-between">
          <div class="flex gap-2">
            {#each card.tags as tag (tag)}
              <p class="h-auto p-1 border rounded-md bg-blue-200 text-xs ">{tag}</p>
            {/each}
          </div>
          <p>{card.date}</p>
        </div>
      </div>
    {/each}
  </section>
  