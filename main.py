from bs4 import BeautifulSoup
import requests

html_raw = requests.get("https://www.delfi.lt/").text

soup = BeautifulSoup(html_raw, "lxml")

headlines = soup.find_all("div", class_="headline")

leads = soup.find_all("p", class_="headline-lead")
