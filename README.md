![python](https://img.shields.io/badge/python-3.10.14-blue.svg?style=flat-square)
![miniforge](https://img.shields.io/badge/miniforge-24.5.0-blue.svg?style=flat-square)

# :sparkles: Jambaram-DataServer
> ARAM(칼바람) champion combination recommendation system TODO: [Demo](http://jambaram.xyz)

#### Architecture
![structure](https://github.com/user-attachments/assets/dc5b1772-db0d-4de9-92c7-ca450a97e594)


# API Docs
#### https://jambaram.xyz/api/model/docs#/

# :floppy_disk: Installation
가상환경 생성
```
$ conda create -n venv-name python=3.10
```

가상환경 실행
```
$ conda activate venv-name
```

Git Clone
```
$ git clone git@github.com:mondayy1/Jambaram-DataServer.git
```

패키지 설치
```
$ pip install -r requirements.txt
```

서버 실행
```
$ uvicorn main:app --reload
```

localhost:8000 접속!
