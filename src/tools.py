import os
import ast
import datetime as dt

from exa_py import Exa
from langchain.agents import tool
from typing import List, Union

today = dt.date.today()
week_ago = today - dt.timedelta(days=7)

class ExaSearchToolset:
    @tool
    def search_ai_trends(query: str) -> List[dict]:
        """Search for the latest AI trends based on the query."""
        return ExaSearchToolset._exa().search(
            f"latest artificial intelligence trends {query}",
            use_autoprompt=True,
            num_results=5,
            start_published_date= str(week_ago),
            end_published_date = str(today)
        )

    @tool
    def search_ai_research(query: str) -> List[dict]:
        """Search for recent AI research papers based on the query."""
        return ExaSearchToolset._exa().search(
            f"artificial intelligence research paper {query}",
            use_autoprompt=True,
            num_results=5,
            start_published_date= str(week_ago),
            end_published_date = str(today)
        )

    @tool
    def search_ai_news(query: str) -> List[dict]:
        """Search for recent AI news articles based on the query."""
        return ExaSearchToolset._exa().search(
            f"artificial intelligence news {query}",
            use_autoprompt=True,
            num_results=5,
            start_published_date= str(week_ago),
            end_published_date = str(today)
        )

    @tool
    def find_similar(url: str) -> List[dict]:
        """Search for webpages similar to a given URL."""
        return ExaSearchToolset._exa().find_similar(url, num_results=5)

    @tool
    # def get_contents(ids: str) -> str:
    #     """Get the contents of webpages."""
    #     ids = eval(ids)
    #     contents = ExaSearchToolset._exa().get_contents(ids)
    #     processed_contents = []
    #     for content in contents:
    #         processed_content = f"Title: {content.title}\nURL: {content.url}\nContent: {content.text[:1000]}..."
    #         processed_contents.append(processed_content)
    #     return "\n\n".join(processed_contents)
    def get_contents(ids: Union[str, List[str]]) -> str:
        """Get the contents of webpages.
        
        Args:
            ids (Union[str, List[str]]): A string representation of a list of ids, or a list of ids directly.
        
        Returns:
            str: Processed contents of the webpages.
        """
        if isinstance(ids, str):
            try:
                ids = ast.literal_eval(ids)
            except (ValueError, SyntaxError):
                # If it's not a valid Python literal, assume it's a single ID
                ids = [ids]
        
        if not isinstance(ids, list):
            raise ValueError("ids must be a list or a string representation of a list")
        
        exa = ExaSearchToolset._exa()
        processed_contents = []
        
        for id in ids:
            try:
                content = exa.get_contents(id)
                processed_content = f"Title: {content.title}\nURL: {content.url}\nContent: {content.text[:1000]}..."
                processed_contents.append(processed_content)
            except Exception as e:
                processed_contents.append(f"Error retrieving content for ID {id}: {str(e)}")
        
        return "\n\n".join(processed_contents)

    @tool
    def search_ai_companies(query: str) -> List[dict]:
        """Search for information about AI companies based on the query."""
        return ExaSearchToolset._exa().search(
            f"artificial intelligence company {query}",
            use_autoprompt=True,
            num_results=5,
            start_published_date= str(week_ago),
            end_published_date = str(today)
        )

    @staticmethod
    def tools():
        return [
            ExaSearchToolset.search_ai_trends,
            ExaSearchToolset.search_ai_research,
            ExaSearchToolset.search_ai_news,
            ExaSearchToolset.find_similar,
            ExaSearchToolset.get_contents,
            ExaSearchToolset.search_ai_companies
        ]

    @staticmethod
    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))