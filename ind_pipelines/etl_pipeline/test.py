from selenium import webdriver
from crawlers import GithubCrawler, MediumCrawler, BaseAbstractCrawler, LinkedInCrawler


event = {
        "user": "Paul Iuztin",
        "link": "https://medium.com/decodingml/an-end-to-end-framework-for-production-ready-llm-systems-by-building-your-llm-twin-2cc6bb01141f",
    }

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=webdriver.ChromeService("/usr/local/bin/chromedriver"), options=options)
driver.get("https://medium.com/decodingml/an-end-to-end-framework-for-production-ready-llm-systems-by-building-your-llm-twin-2cc6bb01141f")
driver.quit()

crawler = BaseAbstractCrawler()
