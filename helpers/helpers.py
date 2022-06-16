from pathlib import Path
import requests
from bs4 import BeautifulSoup
import yaml


def get_config_as_dict():
    config = {}
    with open("config.yaml") as file:
        config = yaml.safe_load(file)
        file.close()
    return config


config = get_config_as_dict()
working_dir = Path(__file__).absolute().parent.parent

log_file_dir = config["log_config"]["dir"]
log_file_name = config["log_config"]["filename"]
logs_dir = f"{working_dir}/{log_file_dir}/{log_file_name}"

news_path = config["scrape_config"]["news"]["file_path"]
news_dir = f"{working_dir}/{news_path}"

porn_path = config["scrape_config"]["porn"]["file_path"]
porn_dir = f"{working_dir}/{porn_path}"


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
