# ⚾ KBO Baseball Data API & Python Package

> **프로야구 정보 제공을 위한 API 구축 및 Python 패키지 개발**  
> 대학교 졸업 팀 프로젝트 | 2023년 2학기 ~ 2024년 1학기

## 프로젝트 소개

KBO 프로야구 선수·팀 기록을 수집하고, 필요한 데이터를 보다 쉽게 조회할 수 있도록 **데이터 조회 API와 Python 패키지**를 개발한 졸업 팀 프로젝트입니다.

기존에는 야구 기록 데이터를 활용하기 위해 직접 웹사이트를 탐색하거나 크롤링해야 하는 불편함이 있었습니다. 이를 개선하기 위해 데이터를 수집·정리하여 MySQL에 저장하고, 사용자가 패키지를 설치해 원하는 기록을 조회할 수 있도록 개발했습니다.

## 주요 기능

| 기능 | 설명 |
| --- | --- |
| 선수 기록 조회 | 선수별 기록 데이터 조회 |
| 팀 기록 조회 | 팀 관련 기록 데이터 조회 |
| 팀 간 승패표 조회 | 팀별 상대 전적 데이터 조회 |
| 홈런 순위 조회 | 홈런 순위 정보 조회 |
| Python 패키지 | 데이터 조회 기능을 모듈로 제공 |
| 사용 가이드 | 설치·업데이트 및 모듈별 사용 방법 안내 |

## 시스템 구성

```text
KBO 기록 웹페이지
       │
       ▼
Python 크롤링 및 데이터 가공
       │
       ▼
   MySQL 데이터베이스
       │
       ▼
   데이터 조회 API
       │
       ▼
 Python 조회 모듈/패키지
       │
       ▼
 PyPI 배포 → 사용자 설치 및 조회
```

## 기술 스택

| 영역 | 기술 |
| --- | --- |
| 언어 | Python |
| 데이터 수집 | Selenium, BeautifulSoup |
| 데이터베이스 | MySQL |
| 패키지 배포 | PyPI |
| 사용 가이드 | Notion |
| 웹 개발 | Flask, HTML, CSS, JavaScript |

## 개발 과정

| 기간 | 진행 내용 |
| --- | --- |
| **2023년 2학기** | 데이터 수집 범위 및 크롤링 허용 범위 조사, 선수 데이터 수집, API 설계 및 요청·응답 테스트 |
| **2024년 1학기** | 팀·팀 간 승패표 데이터 확대, 조회 모듈 제작, 패키지 구성 및 배포, 가이드 작성 및 패키지 테스트 |

## 프로젝트 구조

```text
kbo-baseball/
├── crawler/
│   ├── hit_crawling.py
│   ├── pitcher_crawling.py
│   ├── defender_crawling.py
│   └── run_crawling.py
├── web/
│   ├── app.py
│   ├── graduation.html
│   ├── templates/
│   └── static/
└── README.md
```

- **`crawler/`**: KBO 선수 기록 수집 및 MySQL 데이터 저장
- **`web/`**: Flask 기반 웹 크롤링 및 관련 웹 화면

## 사용 가이드

Python 패키지 설치·업데이트 및 모듈별 사용 방법은 아래 가이드에서 확인할 수 있습니다.

**[📘 Baseball Package Guide Line (Notion)](https://www.notion.so/baseball-package-Guide-Line-da9ac49927904382938cb380b74ef670)**

## 원본 저장소

| 저장소 | 내용 |
| --- | --- |
| [`K-jinho/baseball-kbo`](https://github.com/K-jinho/baseball-kbo) | KBO 기록 크롤링 및 DB 저장 관련 코드 |
| [`K-jinho/python_webcrawling`](https://github.com/K-jinho/python_webcrawling) | Flask 웹 크롤링 코드 |

---

**Graduation Team Project · KBO Baseball Data API & Python Package**
