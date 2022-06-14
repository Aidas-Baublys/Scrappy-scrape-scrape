from helpers import format_and_clean_text, make_soup


news_soup = make_soup("https://www.delfi.lt")
headlines = news_soup.find_all("h3", class_="headline-title")

putin_links = []

for headline in headlines:
    if "Putin" in headline.text:
        putin_links.append(headline.a["href"])

for link in putin_links:
    putin_soup = make_soup(link)
    story_lead = putin_soup.find("div", class_="delfi-article-lead")
    text = format_and_clean_text(story_lead.text)
    # print(text)
    # print("-------")


porn_url = "https://www.pornhub.com"


def get_porn_headlines(url):
    soup = make_soup(url)
    return soup.find_all("span", class_="title")


def filter_porn_headlines(key_word, headline_str_arr):
    for head in headline_str_arr:
        if key_word in head.text:
            less_sloppy_head = format_and_clean_text(
                head.text
            ).strip()  # Pun very much intended.

            print(less_sloppy_head)


porn_headlines = get_porn_headlines(porn_url)

filter_porn_headlines("Mom", porn_headlines)

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

print("----")
filter_porn_headlines("Mom", porn_headlines)
