import re
import requests
from bs4 import BeautifulSoup

PERPAGE = 10
URL = f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EC%BD%94%EB%A1%9C%EB%82%98&sort=_score&perPage={PERPAGE}"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("nav",{"class":"pagination"})
    links = pagination.find_all('a')
    max_page = int(re.sub(r'[^0-9]', '', links[-1]['onclick']))
    return max_page

def extract_data(html):
    title = str(html.find("span",{"class":"title"}).get_text()).strip()
    info = str(html.find("dd",{"class":"ellipsis publicDataDesc"}).get_text()).strip()
    source = str(html.find("div",{"class":"info-data"}).find("span",{"class":"data"}).get_text()).strip()
    data = re.sub(r'[^0-9]', '', html.find("a",{"href":"#layer_filedata_preview"})["onclick"])
    return {
        'title':title,
        'source':source,
        'info':info,
        'details_link':f'https://www.data.go.kr/data/{data}/fileData.do'
    }
    

def extract_datas(last_page):
    datas = []
    for page in range(last_page):
        result = requests.get(f"{URL}&currentPage={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        result_list = soup.find("div",{"class":"result-list"})
        results = result_list.find_all("li")
        for result in results:
            datas.append(extract_data(result))
    return datas

def get_datas():
    last_page = get_last_page()
    datas = extract_datas(last_page)
    return datas