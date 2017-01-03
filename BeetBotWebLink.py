def request_search(query):
    r = requests.get("https://www.youtube.com/results?search_query=" + str(query))
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    tmp = []
    for link in soup.find_all('a'):
        tmp.append(link.get('href'))
    tmp = tmp[42]
    print(query)
    tmp = 'https://www.youtube.com' + tmp
    print(tmp)
    return tmp
from bs4 import BeautifulSoup
import socket, requests
