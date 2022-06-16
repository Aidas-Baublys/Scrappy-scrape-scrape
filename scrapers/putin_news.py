from helpers.helpers import format_and_clean_text, get_config_as_dict, make_soup
from datetime import datetime as date_func


config = get_config_as_dict()

news_url = config["urls"]["news_url"]
enc = config["encoding"]
h_elem = config["scrape_config"]["news"]["headline_el"]
h_class = config["scrape_config"]["news"]["headline_class"]
query = config["scrape_config"]["news"]["search_word"]
l_attr = config["scrape_config"]["news"]["link_attr"]
s_elem = config["scrape_config"]["news"]["story_lead_el"]
s_class = config["scrape_config"]["news"]["story_lead_class"]

news_soup = make_soup(news_url)
headlines = news_soup.find_all(h_elem, class_=h_class)

putin_headlines = []
putin_links = []
putin_story_leads = []


def fill_headlines_and_links():
    for headline in headlines:
        if query in headline.text:
            clean_putin_headline = format_and_clean_text(headline.text)
            putin_headlines.append(clean_putin_headline)
            putin_links.append(headline.a[l_attr])


def fill_story_leads():
    for link in putin_links:
        putin_soup = make_soup(link)
        story_lead = putin_soup.find(s_elem, class_=s_class)
        text = format_and_clean_text(story_lead.text)
        putin_story_leads.append(text)


def write_putin_news():
    with open("scraped_text/putin_news.txt", "a", encoding=enc) as file:
        datetime = date_func.now()
        date_of_execution = datetime.strftime("%Y-%m-%d")
        time_of_execution = datetime.strftime("%H:%M:%S")

        file.write(
            f"\nScraped on {date_of_execution} at {time_of_execution} from {news_url}\n\n\n"
        )

        for i, headline in enumerate(putin_headlines):
            file.write(f"HEADLINE {i + 1}: {headline}\n")
            file.write(f"STORY LEAD: {putin_story_leads[i]}\n")
            file.write("-------\n")

        file.close()

        print("Putin is now in your computer!")
        print("Check out putin_news.txt and burn after reading!\n")


def keeping_up_with_putin():
    fill_headlines_and_links()
    fill_story_leads()
    write_putin_news()
