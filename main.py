import logging
from helpers import format_and_clean_text, make_soup
from datetime import datetime


log_format = "[%(levelname)s]: %(asctime)s:\n%(message)s\n----"
logging.basicConfig(filename="logs/putin.log", level=logging.DEBUG, format=log_format)


porn_url = "https://www.pornhub.com"


def get_porn_headlines(url):
    soup = make_soup(url)
    return soup.find_all("span", class_="title")


def filter_porn_headlines(key_word, headline_str_arr):
    less_sloppy_head = []
    for head in headline_str_arr:
        if key_word in head.text:
            clean_head = format_and_clean_text(
                head.text
            ).strip()  # Pun very much intended.

            less_sloppy_head.append(clean_head)

    return less_sloppy_head


porn_headlines = get_porn_headlines(porn_url)

filtered_porn_headlines = filter_porn_headlines("Mom", porn_headlines)


porn_soup = make_soup(porn_url)
all_links = porn_soup.find_all("a", href=True)

current_page = 1


def find_next_page_link():
    for link in all_links:
        if "/video" in link["href"] and link.text.isdigit():
            query = link["href"]
            return f"{porn_url}{query}"


next_page_link = find_next_page_link()

porn_headlines = get_porn_headlines(next_page_link)


# with open("scraped_text/putin_news.txt", "a", encoding="utf-8") as file:
#     datetime = datetime.now()
#     date_of_execution = datetime.strftime("%Y-%m-%d")
#     time_of_execution = datetime.strftime("%H:%M:%S")

#     file.write(
#         f"\nScraped on {date_of_execution} at {time_of_execution} from {porn_url}\n\n\n"
#     )

#     for i, headline in enumerate(putin_headlines):
#         file.write(f"HEADLINE {i + 1}: {headline} \n")
#         file.write(f"STORY LEAD: {putin_story_leads[i]} \n")
#         file.write("------- \n")

#     file.close()

#     print("Putin is now in your computer!")
#     print("Check out putin_news.txt and burn after reading!")
