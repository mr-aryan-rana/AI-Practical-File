from crewai import Agent, Task, Crew

# === AGENTS ===

research_agent = Agent(
    name="ResearchAgent",
    role="Information Researcher",
    goal="Find accurate and detailed information about the given topic.",
    backstory="An expert researcher capable of gathering reliable facts.",
)

writer_agent = Agent(
    name="WriterAgent",
    role="Content Writer",
    goal="Write a clear and concise summary based on the researcher's findings.",
    backstory="A professional writer skilled in summarizing technical details."
)

# === TASKS ===

research_task = Task(
    description="Research the topic: 'Artificial Intelligence applications in healthcare'.",
    agent=research_agent,
    expected_output="A list of detailed, factual research points."
)

writing_task = Task(
    description="Write a short, clear summary using the research output.",
    agent=writer_agent,
    expected_output="A well-structured paragraph summarizing the research."
)

# === CREW ===

crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, writing_task]
)

# === RUN ===

result = crew.run()
print(result)
