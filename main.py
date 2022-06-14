from bs4 import BeautifulSoup
import requests
from helpers import format_and_clean_text


html_parser = "lxml"

delfi_html = requests.get("https://www.delfi.lt").text
soup = BeautifulSoup(delfi_html, html_parser)
headlines = soup.find_all("h3", class_="headline-title")

putin_links = []

for headline in headlines:
    if "Putin" in headline.text:
        putin_links.append(headline.a["href"])


for link in putin_links:
    putin_link_html = requests.get(link).text
    soup = BeautifulSoup(putin_link_html, html_parser)
    story_lead = soup.find("div", class_="delfi-article-lead")

    text = format_and_clean_text(story_lead.text)

    # print(text)
    # print("-------")


porn_url = "https://www.pornhub.com"
pornhub_html = requests.get(porn_url).text
soup = BeautifulSoup(pornhub_html, html_parser)
porn_headlines = soup.find_all("span", class_="title")


def find_porn_headlines(key_word, headline_str_arr):
    for head in headline_str_arr:
        if key_word in head.text:
            less_sloppy_head = format_and_clean_text(
                head.text
            ).strip()  # Pun very much intended.

            print(less_sloppy_head)


find_porn_headlines("Mom", porn_headlines)


all_links = soup.find_all("a", href=True)


def find_next_page():
    for link in all_links:
        if "/video" in link["href"] and link.text.isdigit():
            query = link["href"]
            return f"{porn_url}{query}"


next_page_link = find_next_page()
next_page_html = requests.get(next_page_link).text
soup = BeautifulSoup(next_page_html, html_parser)
# print(soup)
