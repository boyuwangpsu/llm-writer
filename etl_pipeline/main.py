from typing import Any
import lib
from crawlers import GithubCrawler, MediumCrawler
from dispatcher import CrawlerDispatcher
from db.documents import UserDocument
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(service="llm-writer/crawler")

_dispatcher = CrawlerDispatcher()
_dispatcher.register("medium", MediumCrawler)
_dispatcher.register("github", GithubCrawler)


def handler(event, context: LambdaContext) -> dict[str, Any]:
    first_name, last_name = lib.user_to_names(event.get("user"))

    user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)

    link = event.get("link")
    crawler = _dispatcher.get_crawler(link)

    try:
        crawler.extract(link=link, user=user)

        return {"statusCode": 200, "body": "Link processed successfully"}
    except Exception as e:
        return {"statusCode": 500, "body": f"An error occurred: {str(e)}"}


if __name__ == "__main__":
    event = {
        "user": "Paul Iuztin",
        "link": "https://www.linkedin.com/in/vesaalexandru/",
    }
    handler(event, None)