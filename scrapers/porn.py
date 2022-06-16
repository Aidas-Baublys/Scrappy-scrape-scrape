from time import sleep
from datetime import datetime
from helpers.helpers import (
    format_and_clean_text,
    get_config_as_dict,
    make_soup,
    porn_dir,
)


config = get_config_as_dict()

porn_url = config["urls"]["porn_url"]
enc = config["encoding"]
start_page = config["scrape_config"]["porn"]["start_page"]
h_elam = config["scrape_config"]["porn"]["headline_el"]
h_class = config["scrape_config"]["porn"]["headline_class"]
l_query = config["scrape_config"]["porn"]["next_page_href_query"]
l_attr = config["scrape_config"]["porn"]["link_attr"]
attr = config["scrape_config"]["porn"]["href"]


def get_porn_headlines(url):
    soup = make_soup(url)
    return soup.find_all(h_elam, class_=h_class)


def filter_porn_headlines(key_word, headline_str_arr):
    less_sloppy_head = []
    for head in headline_str_arr:
        if key_word in head.text:
            clean_head = format_and_clean_text(
                head.text
            ).strip()  # Pun very much intended.

            less_sloppy_head.append(clean_head)

    return less_sloppy_head


def make_50_shades_manuscript(headline_arr, chapter_num, chapter_name):
    with open(porn_dir, "a", encoding=enc) as file:
        date_of_execution = datetime.now().strftime("%Y")

        if chapter_num == start_page:
            file.write(f"\nWritten with passion in {date_of_execution}\n\n")
            file.write(
                f"Inspired by many amazing artist and creators from {porn_url}\n"
            )

        file.write(f"\n\nChapter {chapter_num}: {chapter_name}\n\n")

        for headline in headline_arr:
            file.write(f"{headline}\n")

        file.close()


def find_next_page_link(link_arr):
    current_page = start_page
    for link in link_arr:
        if l_query in link[l_attr] and link.text.isdigit():
            page_num = int(link.text)
            if page_num > current_page:
                query = link[l_attr]
                return f"{porn_url}{query}"


def initial_greetings():
    print(
        "\nAwesome! You'll see that writing wont be as hard as you when we're done.\n"
    )
    sleep(4)
    print(
        "First, tell me how many chapters of epic fan fiction do you want me to write?\n"
    )
    sleep(2)
    print("Quick note: I will need a word or phrase from you for every chapter.")
    sleep(3)
    print(
        "So if you give 5, you will need to -- putin -- 5 words later for inspiration.\n"
    )
    sleep(4)
    print("If you give 500, well... Gonna write long time.\n")
    sleep(4)
    print("Don't go crazy if you don't want to go all the way, honey.")
    sleep(2)
    print("This is not Ukraine.\n")
    sleep(2)
    print("Also, some words are not in porn video titles.")
    sleep(2)
    print("I know, I'm surprised as well.")
    sleep(2)
    input("Cool? (Press any key to continue)\n")


def show_try_again_msg():
    sleep(1)
    print("Try again.\n")
    sleep(1)


def get_int_from_user():
    got_int = False
    while not got_int:
        user_given_page = input("Whole positive number, please: ")
        try:
            page_num = int(user_given_page)

            if page_num <= 0:
                print("\nPositive number, love. As in more than 0.")
                show_try_again_msg()
            else:
                got_int = True
        except ValueError:
            print(
                f"\nWhole positive numbers are 7, 13, 420, and not '{user_given_page}'."
            )
            show_try_again_msg()
        except Exception:
            print("\nI don't even know what you did, you naughty so and so...")
            show_try_again_msg()

    return page_num


def inspire_words():
    print("\nSuperb. Now it's time for inspiration.\n")
    sleep(2)
    print("Quick note: think of strong, emotional words...")
    sleep(2)
    print("Cock, cum, mom...\n")
    sleep(2)


def scrape_and_write():
    initial_greetings()
    last_page = get_int_from_user()
    current_page = start_page
    current_url = porn_url
    search = ""

    while current_page <= last_page:
        if current_page == 1:
            inspire_words()
            search = input("Ready? Your word: ")
        elif current_page == last_page:
            search = input("\nAnd the last one: ")
        else:
            search = input("\nOne more: ")

        print("Writing...")

        porn_headlines = get_porn_headlines(current_url)
        filtered_porn_headlines = filter_porn_headlines(search, porn_headlines)
        make_50_shades_manuscript(
            filtered_porn_headlines, current_page, search.capitalize()
        )

        porn_soup = make_soup(current_url)
        all_links = porn_soup.find_all("a", href=attr)

        current_url = find_next_page_link(all_links)
        current_page += 1

    print("\n*** We have arrived! ***\n")
    sleep(3)
    print("You can now forget Putin with porn!\n")
    sleep(2)
    print("New hot novel is now in your computer!")
    print("Check out the latest chapter in 69_Shades.txt!\n")
