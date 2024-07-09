from textwrap import dedent
from crewai import Task
from datetime import date

today = date.today()


class Ai_Tasks():

    def research_task(self, agent):
        return Task(
        description=dedent(f"""\
            Identify the next big trend in artificial intelligence (AI) based on current developments and future projections.
            Consider advancements in machine learning, natural language processing, computer vision, and other relevant AI subfields.
            Analyze recent research papers, industry reports, and expert opinions published within the last 6 months.
            Focus on emerging technologies and methodologies that have the potential to significantly impact the AI landscape in the next 1-3 years.
            Current date: {today}
            """),
        expected_output=dedent(f"""\
            A detailed report summarizing:
            1. Current state of AI as of {today}
            2. Analysis of 3-5 emerging trends in AI
            3. Prediction of the most likely "next big trend" with supporting evidence
            4. Potential impact of this trend on various industries and society
            5. Timeline for expected mainstream adoption
            6. Key players and companies driving this trend
            7. Potential challenges or ethical considerations
            8. References to relevant research papers, reports, or expert opinions
            """),
        agent=agent,
        async_execution=True
        )
    
    def industry_analysis_task(self, agent):
        return Task(
                description=dedent(f"""\
                    Conduct a comprehensive analysis of the artificial intelligence (AI) industry as of {today}.
                    Focus on the following key areas:
                    1. Current market trends: Identify and analyze the top 3-5 trends shaping the AI industry.
                    2. Market size and growth: Provide current market size estimates and growth projections for the next 5 years.
                    3. Key players: Identify major companies, startups, and research institutions driving innovation.
                    4. Technological advancements: Highlight recent breakthroughs in AI subfields (e.g., machine learning, NLP, computer vision).
                    5. Industry challenges: Analyze technical, ethical, and regulatory challenges facing the AI industry.
                    6. Opportunities: Identify emerging opportunities for AI applications across various sectors.
                    7. Investment landscape: Summarize recent funding trends, major investments, and M&A activities.
                    8. Geographical analysis: Compare AI development and adoption across different regions globally.
                    
                    Base your analysis on reputable market reports, academic publications, industry news, and expert opinions from the past 12 months.
                    """),
                expected_output=dedent(f"""\
                    A comprehensive AI industry analysis report including:
                    1. Executive summary of key findings
                    2. Detailed analysis of each focus area mentioned in the task description
                    3. SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis of the AI industry
                    4. Future outlook: Short-term (1-2 years) and long-term (3-5 years) predictions for the industry
                    5. Recommendations for stakeholders (e.g., investors, policymakers, businesses)
                    6. Visual aids: Charts, graphs, or infographics to illustrate key points
                    7. List of sources and references used in the analysis
                    
                    The report should be insightful, data-driven, and provide actionable intelligence for decision-makers in the AI space.
                    """),
                async_execution=True,
                agent=agent
            )
    
    def innovation_strategy_task(self, agent):
        return Task(
                description=dedent(f"""\
                    Develop a comprehensive innovation strategy framework for an AI-focused technology company.
                    The framework should include:
                    1. Key innovation areas: Identify 3-5 critical areas for innovation based on current AI trends and market demands.
                    2. Strategic talking points: Develop concise, impactful statements that articulate the company's innovation vision and approach.
                    3. Discussion angles: Create thought-provoking perspectives on AI innovation to stimulate strategic conversations.
                    4. Probing questions: Formulate insightful questions to uncover opportunities, challenges, and unexplored areas in AI innovation.
                    5. Stakeholder considerations: Address how the innovation strategy impacts different stakeholders (e.g., employees, customers, investors, partners).
                    6. Resource allocation: Suggest how to balance resources between incremental improvements and disruptive innovations.
                    7. Innovation metrics: Propose key performance indicators (KPIs) to measure the success of innovation initiatives.
                    8. Competitive analysis: Include points on how this strategy positions the company against competitors.

                    Base your strategy on current AI industry trends, successful innovation models, and forward-thinking approaches in technology leadership.
                    """),
                expected_output=dedent("""\
                    A detailed innovation strategy report including:
                    1. Executive summary of the innovation framework
                    2. List of key innovation areas with brief justifications
                    3. 10-15 strategic talking points for leadership communication
                    4. 5-7 unique discussion angles to drive strategic conversations
                    5. 20-25 probing questions categorized by innovation area
                    6. Stakeholder impact analysis and engagement strategies
                    7. Proposed resource allocation model for innovation initiatives
                    8. Set of innovation KPIs and measurement methodologies
                    9. Competitive positioning analysis in the context of the innovation strategy
                    10. Implementation roadmap with short-term and long-term objectives
                    11. Potential risks and mitigation strategies for the proposed innovation approach

                    The report should be actionable, forward-thinking, and aligned with cutting-edge AI developments and business strategy best practices.
                    """),
                agent=agent
            )
    
    def summary_and_briefing_task(self, agent):
        return Task(
            description=dedent(f"""\
                Compile all research findings, industry analysis, and strategic insights into a comprehensive, 
                well-structured standard report. The report should synthesize information from previous tasks 
                and present a coherent overview of the AI industry, trends, and strategic recommendations.
                
                Ensure the report is clear, concise, and provides actionable insights for decision-makers.
                
                Current date: {today}
                """),
            expected_output=dedent(f"""\
                A comprehensive standard report with the following structure:

                1. Executive Summary (1 page)
                - Key findings and recommendations

                2. Table of Contents

                3. Introduction (1-2 pages)
                - Purpose of the report
                - Methodology
                - Current AI landscape overview

                4. AI Industry Analysis (3-4 pages)
                - Market size and growth projections
                - Key players and competitive landscape
                - Regional analysis

                5. Current AI Trends (3-4 pages)
                - Top 5 current trends with brief explanations
                - Potential impact on various industries

                6. Emerging Technologies (2-3 pages)
                - Breakthrough AI technologies
                - Potential applications and impact

                7. Challenges and Opportunities (2-3 pages)
                - Technical challenges
                - Ethical and regulatory considerations
                - Emerging opportunities in AI

                8. Strategic Recommendations (2-3 pages)
                - Short-term actions (next 12 months)
                - Long-term strategies (2-5 years)
                - Innovation focus areas

                9. Future Outlook (1-2 pages)
                - Predictions for AI development in the next 3-5 years
                - Potential disruptive scenarios

                10. Appendices
                    - Glossary of key AI terms
                    - List of key AI companies to watch
                    - Recent AI News Headlines with URL links (last 30 days)
                    - Selected AI research articles with brief summaries and URL links (last 6 months)

                11. References

                The report should be 20-25 pages in total (excluding appendices and references), 
                use clear and professional language, and include relevant charts, graphs, or 
                infographics to illustrate key points. Ensure all information is up-to-date as of {today}.
                """),
            agent=agent
        )