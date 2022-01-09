import re
import requests
from bs4 import BeautifulSoup

def get_last_page(url):
    result = requests.get(url)
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
    

def extract_datas(last_page, url):
    datas = []
    for page in range(last_page):
        result = requests.get(f"{url}&currentPage={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        result_list = soup.find("div",{"class":"result-list"})
        results = result_list.find_all("li")
        for result in results:
            datas.append(extract_data(result))
    return datas

def get_datas(word):
    try:
        url = f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword={word}&sort=_score&perPage=40"
        last_page = get_last_page(url)
        datas = extract_datas(last_page, url)
        return datas
    except:
        return 0