from crewai import Crew,Process
from agents import researcher,news_writer
from tasks import research_task,write_task


crew=Crew(
    agents=[researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential
)

## start the task execution process with enhanced feedback 
result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)