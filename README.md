#!/bin/bash
# 패키지 업데이트
sudo apt update && apt upgrade -y
sudo apt install python3-pip -y

# Django 프로젝트 클론
git clone https://github.com/devMuromi/ELB-example.git
cd ELB-example

# 의존성 설치
sudo pip install -r requirements.txt

# Django 서버 실행
python3 manage.py migrate
sudo gunicorn --bind 0:80 elb_example.wsgi