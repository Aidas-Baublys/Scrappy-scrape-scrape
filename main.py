import logging
from time import sleep

from scrapers.porn import scrape_and_write
from scrapers.putin_news import keeping_up_with_putin


log_format = "[%(levelname)s]: %(asctime)s:\n%(message)s\n----"
logging.basicConfig(
    filename="logs/all_logs.log", level=logging.DEBUG, format=log_format
)


def start_and_greet():
    print("\n*** Hello and welcome! ***\n")
    sleep(2)
    print("I am Putin & Porn console app.")
    sleep(2)
    print("Trademark.\n")
    sleep(2)
    print(
        "I can get you latest news headlines and story leads about Putin from one Lithuanian news site."
    )
    sleep(4)
    print("Now available only in lithuanian!\n")
    sleep(3)
    print("And, with your help, I can write a passionate love novel...")
    sleep(2)
    print("... using only porn vidoe titles!")
    sleep(2)
    print("It will help your mind -- get off -- of Putin...\n")
    sleep(2)
    print(
        "Quick note: if in the end you get empty files or something takes too long..."
    )
    sleep(2)
    print("Not my problem. Either your internet or the sites are broken.\n")
    sleep(2)
    input("Ready? (Press any key to continue)\n")


start_and_greet()
keeping_up_with_putin()
sleep(2)
print("Ready for porn?")
sleep(1)
input("I mean, literature. (Press any key to continue)")
scrape_and_write()
sleep(2)
print("So long my friend!")
