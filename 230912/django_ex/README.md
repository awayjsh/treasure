```shell
# 가상환경 설정
python -m venv venv
# python -m {venv 모듈명} {폴더명}
# ---
# -m : 모듈을 실행하겠음
# venv : 'venv' 모듈이름 -> virtual environment
# venv : venv 모듈을 통해서 생성해줄 가상환경을 담은 폴더명
# git bash에 우클릭 -> 복붙

# 가상환경 활성화
source venv/Scripts/activate
# source {적용하고자하는 소스코드 경로}
# ---
# (venv) <- 현재 적용중인 가상환경 폴더명
# pip list <- 현재 설치 중인 패키지/모듈들 목록 확인

# django (최신 버전) 설치
pip install Django
# pip list <- 현 가상환경에 설치된 내역 확인
# pip freeze <- pip list와 유사함
pip freeze > requirements.txt
# freeze : 현재 설치된 의존성(필요한 라이브러리)의 목록을 간결하게 표시
# > : to, 어떠한 경로의 파일에 저장할지
# requirements.txt : 일반적으로 의존성을 freeze하는 파일명
# pip install -r requirements.txt

# 가-프-앱-등-런

# django 프로젝트 생성
django-admin startproject firstpjt .
# django-admin start~
# django-admin --version
# django-admin <- Django 설치했을 때 딸려서 현 가상환경에 설치된 프로그램
# . 은 현재 경로를 의미합니다
# -> {현재폴더}/firstpjt + manage.py

# django 서버 실행
python manage.py runserver # 명령어를 입력하는 현 터미널에 manage.py가 있어야함 (pjt를 제대로 생성 안했거나, 경로가 다르면 실행 X)
# http://127.0.0.1:8000/