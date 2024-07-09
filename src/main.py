from dotenv import load_dotenv
from crewai import Crew
from tasks import Ai_Tasks
from agents import Ai_Agents


def main():
    load_dotenv()
    
    print("## Welcome to the Ai Landscape Crew")
    print('-------------------------------')

    tasks = Ai_Tasks()
    agents = Ai_Agents()
    
    research_agent = agents.research_agent()
    industry_analysis_agent = agents.industry_analysis_agent()
    innovation_strategy_agent = agents.innovation_strategy_agent()
    summary_and_briefing_agent = agents.summary_and_briefing_agent()
    
    # create tasks
    research_task = tasks.research_task(research_agent)
    industry_analysis_task = tasks.industry_analysis_task(industry_analysis_agent)
    innovation_strategy_task = tasks.innovation_strategy_task(innovation_strategy_agent)
    summary_and_briefing_task = tasks.summary_and_briefing_task(summary_and_briefing_agent)
    
    innovation_strategy_task.context = [research_task, industry_analysis_task]
    summary_and_briefing_task.context = [research_task, industry_analysis_task, innovation_strategy_task]
    
    crew = Crew(
        agents=[
            research_agent,
            industry_analysis_agent,
            innovation_strategy_agent,
            summary_and_briefing_agent
        ],
        tasks=[
            research_task,
            industry_analysis_task,
            innovation_strategy_task,
            summary_and_briefing_task
        ]
    )


    result = crew.kickoff()
    
    print("Here is the recent Ai landscape news:")
    print(result)

    
if __name__ == "__main__":
    main()