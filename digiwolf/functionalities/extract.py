import requests
from bs4 import BeautifulSoup
import json


def extract_from_faro_de_ceuta(pages):
    data = {
        'comments': []
    }
    for i in range(1, int(pages) + 1):
        print(f"Pagina {i}")
        URL = f"https://elfarodeceuta.es/politica/?page={i}"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        result = soup.find_all("h3", class_="jeg_post_title")
        for tag in result:
            new_url = tag.find("a")["href"]
            page = requests.get(new_url)
            soup = BeautifulSoup(page.content, "html.parser")
            result = soup.find_all("li", class_="comment")
            for comment_tag in result:
                user_tag = comment_tag.find("cite", class_="“fn”")
                user = user_tag.find("a") if user_tag.find("a") else user_tag
                comment_model = {"username": user.text,
                                 "comment": comment_tag.find("div", class_="comment-content").text}
                data["comments"].append(comment_model)
    return json.dumps(data, indent=4)
