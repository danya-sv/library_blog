import requests
from bs4 import BeautifulSoup as BS4

URL = "https://knigogid.ru/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

def get_html(url, params = ""):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_data(html):
    bs = BS4(html, features="html.parser")
    items = bs.find_all("div", class_="b-item")  # Поиск всех элементов книги
    book_list = []
    for item in items:
        # Безопасное извлечение данных
        title_tag = item.find("a", class_="b-item-name")
        author_tag = item.find("a", class_="b-item-author")
        genre_tag = item.find("div", class_="b-item-tag")
        grade_tag = item.find("div", class_="b-item-rate")
        
        title = title_tag.get_text(strip=True) if title_tag else "Не найдено"
        author = author_tag.get_text(strip=True) if author_tag else "Не найдено"
        genre = genre_tag.get_text(strip=True) if genre_tag else "Не найдено"
        grade = grade_tag.get_text(strip=True) if grade_tag else "Не найдено"

        book_list.append(
            {
                "title": title,
                "author": author,
                "genre": genre,
                "grade": grade
            }
        )
    return book_list


def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        book_list2 = []
        for page in range(1, 2): 
            response = get_html("https://knigogid.ru/books", params={"page": page})
            book_list2.extend(get_data(response.text))
        return book_list2  
    else:
        raise Exception("error")

# print(parssing())