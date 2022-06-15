import logging

from scrapers.porn import scrape_and_write


log_format = "[%(levelname)s]: %(asctime)s:\n%(message)s\n----"
logging.basicConfig(
    filename="logs/all_logs.log", level=logging.DEBUG, format=log_format
)

print("Hello and welcome!")
print("I am Putin & Porn console app.")
print(
    "I can get you latest news headlines and story leads about Putin from one Lithuanian news site"
)
print("Now available only in lithuanian.")
print("And, with your help, I can write passionate love novel.")
print("It will help your mind -- get off -- of Putin..")

# scrape_and_write()
