import requests
import bs4
import datetime
from dateutil import parser

def get_page(website_url: str) -> (str):
    time = 5
    response = requests.get(website_url, timeout = time)
    return response.text

def parse_voyager_page(page: str) -> (str):
    soup = bs4.BeautifulSoup(page, "lxml")
    mission_details_info_block = soup.find("div", class_ = "MissionDetailStats")
    launch_date_block = mission_details_info_block.find("p", string = "Launch Date")
    date = launch_date_block.find_next_sibling("p").text
    return parser.parse(date).strftime("%Y%m%d")

def parse_rfc_page(page: str) -> (str):
    soup = bs4.BeautifulSoup(page, "lxml")
    page_block = soup.find("pre", class_ = "newpage")
    date_block = page_block.find("span", class_ = "grey")
    date_as_list = date_block.text.split(" ")
    concrete_date = date_as_list[-1] + " " + date_as_list[-2] + " " + date_as_list[-3]
    return parser.parse(concrete_date).strftime("%Y%m%d")

def parse_unicode_page(page: str) -> (str):
    brain_index = page.find("BRAIN") - 2
    unicode = ""
    while ((symbol := page[brain_index]) != "\n"):
        unicode = symbol + unicode
        brain_index -= 1
    return(unicode)

def parse_bitcoin_page(page: str) -> (str):
    result_time = ""
    index_of_comment = page.find("// Genesis Block:")
    index_of_time_genesis_block = page.find("block.nTime", index_of_comment)
    while (not page[index_of_time_genesis_block].isdigit()):
        index_of_time_genesis_block += 1
    else:
        while (page[index_of_time_genesis_block].isdigit()):
            result_time += page[index_of_time_genesis_block]
            index_of_time_genesis_block += 1
    datetime_object = datetime.datetime.fromtimestamp(float(result_time)).strftime("%Y%m%d")
    return datetime_object

def parse_icbn_page(page: str) -> (str):
    soup = bs4.BeautifulSoup(page, "lxml")
    book_title_block = soup.find("div", id = "booktitle")
    isbn_block = book_title_block.find("b", string = "ISBN-10:").find_parent()
    isbn_code = isbn_block.text.strip().split(" ")[1]
    return isbn_code