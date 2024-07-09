import os
from exa_py import Exa
from langchain.agents import tool
from typing import List

class ExaSearchToolset:
    @tool
    def search_ai_trends(query: str) -> List[dict]:
        """Search for the latest AI trends based on the query."""
        return ExaSearchToolset._exa().search(
            f"latest artificial intelligence trends {query}",
            use_autoprompt=True,
            num_results=5,
            start_published_date="2023-01-01"
        )

    @tool
    def search_ai_research(query: str) -> List[dict]:
        """Search for recent AI research papers based on the query."""
        return ExaSearchToolset._exa().search(
            f"artificial intelligence research paper {query}",
            use_autoprompt=True,
            num_results=5,
            content_type="research-article",
            start_published_date="2023-01-01"
        )

    @tool
    def search_ai_news(query: str) -> List[dict]:
        """Search for recent AI news articles based on the query."""
        return ExaSearchToolset._exa().search(
            f"artificial intelligence news {query}",
            use_autoprompt=True,
            num_results=5,
            content_type="news",
            start_published_date="2023-01-01"
        )

    @tool
    def find_similar(url: str) -> List[dict]:
        """Search for webpages similar to a given URL."""
        return ExaSearchToolset._exa().find_similar(url, num_results=5)

    @tool
    def get_contents(ids: str) -> str:
        """Get the contents of webpages."""
        ids = eval(ids)
        contents = ExaSearchToolset._exa().get_contents(ids)
        processed_contents = []
        for content in contents:
            processed_content = f"Title: {content.title}\nURL: {content.url}\nContent: {content.text[:1000]}..."
            processed_contents.append(processed_content)
        return "\n\n".join(processed_contents)

    @tool
    def search_ai_companies(query: str) -> List[dict]:
        """Search for information about AI companies based on the query."""
        return ExaSearchToolset._exa().search(
            f"artificial intelligence company {query}",
            use_autoprompt=True,
            num_results=5,
            start_published_date="2023-01-01"
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