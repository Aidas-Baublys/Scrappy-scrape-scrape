import logging
from helpers import format_and_clean_text, make_soup
from datetime import datetime as date_func


log_format = "[%(levelname)s]: %(asctime)s:\n%(message)s\n----"
logging.basicConfig(
    filename="logs/all_logs.log", level=logging.DEBUG, format=log_format
)


porn_url = "https://www.pornhub.com"

current_page = 1
search = input("Hello and welcome!")
last_page = 5


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


def make_50_shades_manuscript(headline_arr):
    with open(f"scraped_text/69_Shades.txt", "a") as file:
        datetime = date_func.now()
        date_of_execution = datetime.strftime("%Y")

        if current_page == 1:
            file.write(f"\nWritten with passion in {date_of_execution}\n\n")
            file.write(
                f"Inspired by many amazing artist and creators from {porn_url}\n\n"
            )

        file.write(f"\n\nChapter {current_page}: {search}\n\n")

        for headline in headline_arr:
            file.write(f"{headline}\n")

        file.close()


def find_next_page_link(link_arr):
    for link in link_arr:
        if "/video" in link["href"] and link.text.isdigit():
            page_num = int(link.text)
            if page_num > current_page:
                query = link["href"]
                return f"{porn_url}{query}"


current_url = porn_url

while current_page < last_page:
    porn_headlines = get_porn_headlines(current_url)
    filtered_porn_headlines = filter_porn_headlines(search, porn_headlines)
    make_50_shades_manuscript(filtered_porn_headlines)

    porn_soup = make_soup(current_url)
    all_links = porn_soup.find_all("a", href=True)

    current_url = find_next_page_link(all_links)
    current_page += 1


print("Forget Putin with porn!")
print("New hot novel is now in your computer!")
print("Check out the latest chapter in 69_Shades.txt!")
