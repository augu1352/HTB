import requests
import urllib.request
from html.parser import HTMLParser
import json


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag: ", tag)
        self.lasttag = tag

    def handle_endtag(self, tag):
        # print("Encountered an end tag: ", tag)
        pass


    def handle_data(self, data):
        if self.lasttag == "h3":
            code = data
        # print("Encountered some data: ", data)
            print(code)
        # json_data = json.loads(data)
        # print(data)

    # def handle_data(self, data):
    #     if "edge_followed_by" in data:
    #         # print("IMPORTANT DATA:", data[21:])
    #         json_data = json.loads(str(data[21:-1]))
    #         global followers
    #         followers = json_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_followed_by"]["count"]


def get_page():
    parser = MyHTMLParser()
    page = requests.get("http://docker.hackthebox.eu:30732")
    page2 = requests.get("http://docker.hackthebox.eu:30732")
    parser.feed(page.text)
    parser.feed(page2.text)
    # print(page.text)


get_page()
