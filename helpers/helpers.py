import requests
from bs4 import BeautifulSoup
import yaml


def get_config_as_dict():
    config = {}
    with open("config.yaml") as file:
        config = yaml.safe_load(file)
        file.close()
    return config


def make_soup(url):
    raw_html = requests.get(url).text
    return BeautifulSoup(raw_html, "lxml")


def format_and_clean_text(text):
    return "".join(
        [
            char
            for char in text
            if (
                char.isalpha()
                or char == " "
                or char == "."
                or char == ":"
                or char == "-"
                or char == "?"
                or char == "\u2013"
            )
        ]
    )
