# web_scrapper
---

이 문서는 노마드 코더에서 제공하는 'Python으로 웹 스크래퍼 만들기' 강좌를 응용해 만든</br>
정부 공공데이터 포탈의 데이터를 추출하는 웹 스크래퍼 와</br>
python Flask를 이용해 추출된 데이터를 보여주는 웹페이지 코드입니다.</br></br>
https://www.data.go.kr/index.do</br>
https://nomadcoders.co/python-for-beginners

---
아래는 AWS(Amazon Web Services)와 연동시킨 웹 주소입니다.</br>

http://52.79.201.104:5000/</br></br>


~~※주의</br>
최초 데이터 검색(DB에 등록되지 않은 데이터)에는 시간이 오래 걸릴 수 있습니다.</br>
정식 DB를 사용한 것이 아닌 fake DB로 받은 데이터를 메모리에 올려 DB 역할을 수행하고 있기 때문에 검색 데이터가 많아지면 웹페이지 자체가 정상적으로 작동하지 않을 수 있습니다.</br>~~
메모리 과부하 방지를 위해 fake DB 삭제됨

---
도커 파일 추가<br>
80포트 사용<br><br><br>


docker build -t web-scrapper . #깃허브 파일 빌드<br>
또는<br>
docker pull mentaldisaster/web_scrapper #도커허브 이미지<br><br>

docker run -dp 5000:80 web-scrapper<br>
#nginx의 기본포트 80과 로컬호스트 5000포트 연결 도커 튜토리얼에서 80번 포트를 사용해 사용자의 5000포트 사용<br>
명령어를 이용해 localhost:5000로 접근 

---

노마드 코더 챌린지 통과<br>
자세한 챌린지 코드는 https://replit.com/@mental-disaster/Day-Thirteen-and-Fourteen#main.py에서 확인할 수 있습니다.<br><br>

<img src="https://user-images.githubusercontent.com/54014203/149989075-cb8e6c9b-45a4-4e40-959d-da7975ba4fd5.jpg"/>
