from time import sleep
from helpers import format_and_clean_text, make_soup
from datetime import datetime


porn_url = "https://www.pornhub.com"
start_page = 1


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


def make_50_shades_manuscript(headline_arr, chapter_num, chapter_name):
    with open(f"scraped_text/69_Shades.txt", "a", encoding="utf-8") as file:
        date_of_execution = datetime.now().strftime("%Y")

        if chapter_num == 1:
            file.write(f"\nWritten with passion in {date_of_execution}\n\n")
            file.write(
                f"Inspired by many amazing artist and creators from {porn_url}\n\n"
            )

        file.write(f"\n\nChapter {chapter_num}: {chapter_name}\n\n")

        for headline in headline_arr:
            file.write(f"{headline}\n")

        file.close()


def find_next_page_link(link_arr):
    current_page = start_page
    for link in link_arr:
        if "/video" in link["href"] and link.text.isdigit():
            page_num = int(link.text)
            if page_num > current_page:
                query = link["href"]
                return f"{porn_url}{query}"


def initial_greetings():
    print(
        "\nAwesome! You'll see that writing wont be as hard as you when we're done.\n"
    )
    sleep(3)
    print(
        "First, tell me how many chapters of epic fan fiction do you want me to write?\n"
    )
    sleep(1)
    print("Quick note: I will need a word or phrase from you for every chapter.")
    sleep(2)
    print(
        "So if you give 5, you will need to -- putin -- 5 words later for inspiration.\n\n"
    )
    sleep(3)
    print("Don't go crazy if you don't want to go all the way, honey.")
    print("This is not Ukraine.\n")
    sleep(2)
    input("Cool? Press any key to continue.\n")


def show_try_again_msg():
    sleep(1)
    print("Try again.\n")
    sleep(1)


def get_int_from_user():
    got_int = False
    while not got_int:
        user_given_page = input("Whole positive number, please: \n\n\n")
        try:
            page_num = int(user_given_page)
            got_int = True
        except ValueError:
            print(f"Whole positive numbers are 7, 13, 420, and not {user_given_page}.")
            show_try_again_msg()
        except Exception:
            print("I don't even know what you did, you naughty so and so...")
            show_try_again_msg()

    return page_num


def inspire_words():
    print("Superb. Now it's time for inspiration.\n")
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
            search = input("Ready? Your word: \n").capitalize()
        elif current_page == last_page:
            search = input("And the last one: \n")
        else:
            search = input("One more: \n")

        porn_headlines = get_porn_headlines(current_url)
        filtered_porn_headlines = filter_porn_headlines(search, porn_headlines)
        make_50_shades_manuscript(filtered_porn_headlines, current_page, search)

        porn_soup = make_soup(current_url)
        all_links = porn_soup.find_all("a", href=True)

        current_url = find_next_page_link(all_links)
        current_page += 1

    print("*** We have arrived! ***\n")
    sleep(3)
    print("You can now forget Putin with porn!\n")
    sleep(2)
    print("New hot novel is now in your computer!")
    print("Check out the latest chapter in 69_Shades.txt!\n")
