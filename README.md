## 가상환경 만들기

$ python3 -m venv venv 


## 가상환경 들어가기  

$ source venv/bin/activate


## 나오기

$ deactivate


## 라이브러리 설치

pip install -r requirements.txt


## 라이브러리 설치하고 나서 requirements.txt 로 fix 하기

예를 들어 pytorch 설치하는 경우:

$ pip install torch

$ pip freeze > requirements.txt

Freeze 하고 나면 다른 사람이 requirements.txt 를 설치하여 같은 환경으로 만들 수 있다.