#신규 사이트 프로비저닝
========================

## 필요 패키지
* nginx
* Python3
* Git
* pip
* supervisor
* virtualenvwrapper

ubuntu에서의 실행 방법 예:

    sudo apt install nginx git python3 python3-pip supervisor
    sudo pip3 install virtualenvwrapper 

## Nginx 가상 호스트 설정

* nginx.template.conf 참고
* SITENAME 부분을 다음과 같이 수정 staging.my-domain.com

## supervisor 설정

* gunicorn-supervisor.template.conf 참고
* SITENAME 부분을 다음과 같이 수정 staging.my-domain.com

## gunicorn 설정 

* superlists.conf.py 참고
* SITENAME 부분을 다음과 같이 수정 staging.my-domain.com

## 폴더 구조
사용자 계정의 홈 폴더가 /home/username 이라고 가정

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── supervisor.conf.py
