import requests


def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


url = 'http://maoyan.com/board/4'
html = get_one_page(url)
print(html)
