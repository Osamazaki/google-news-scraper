from requests_html import HTMLSession
import pandas as pd
headers = {  # not needed for requests_html cuz it already is like a human surfing web
        "User=Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
session = HTMLSession()
url = "https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en"
response = session.get(url)
response.html.render(sleep=1, scrolldown=0)  # to scroll down with or without render, render is used in case of
# JS code including encapsulating the html, and not pure html
articles = response.find("article")  # find element(s)) by css selector


def general_query():
    news_articles = []
    for article in articles:
        try:  # cause not all articles has h3, only the main ones, and that's really what we want
            article_dict = {
                "link": article.find("h3", first=True).absolute_links,   # finds first element only, equals find one in beautfifuloup
                "article_name": article.find("h3", first=True).text
                            }
            news_articles.append(article_dict)
        except:
            pass
    return news_articles


def specific_query(word):
    news_articles = []
    for article in articles:
        if word in article.find("h3", first=True).text:
            try:  # cause not all articles has h3, only the main ones, and that's really what we want
                article_dict = {
                    "link": article.find("h3", first=True).absolute_links,   # finds first element only, equals find one in beautfifuloup
                    "article_name": article.find("h3", first=True).text
                                }
                news_articles.append(article_dict)
            except:
                pass
        return news_articles

# news_list = general_query()


news_list = specific_query("tesla")
df = pd.DataFrame(news_list)
df.to_csv("news", index=False)

