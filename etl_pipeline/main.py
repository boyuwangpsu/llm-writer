from typing import Any
import lib
from crawlers import GithubCrawler, MediumCrawler
from dispatcher import CrawlerDispatcher

_dispatcher = CrawlerDispatcher()
_dispatcher.register("medium", MediumCrawler)
_dispatcher.register("github", GithubCrawler)


def handler(event) -> dict[str, Any]:

    link = event.get("link")
    crawler = _dispatcher.get_crawler(link)

    try:
        crawler.extract(link=link)

        return {"statusCode": 200, "body": "Link processed successfully"}
    except Exception as e:
        return {"statusCode": 500, "body": f"An error occurred: {str(e)}"}


if __name__ == "__main__":
    event = {
        "user": "Paul Iuztin",
        "link": "https://www.linkedin.com/in/vesaalexandru/",
    }
    handler(event)