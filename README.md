# FastAPI Blog Management System: v2.0

FastAPI 기반 블로그 관리 시스템입니다. MySQL 데이터베이스와 연동하여 블로그 글 작성, 수정, 삭제, 조회 기능을 제공합니다.

## 주요 기능

- 블로그 글 작성, 수정, 삭제, 조회 (CRUD)
- Jinja2 템플릿을 사용한 웹 인터페이스
- MySQL 데이터베이스 연동
- SQLAlchemy ORM을 통한 효율적인 데이터베이스 관리
- Connection Pool을 활용한 성능 최적화
- Pydantic을 사용한 데이터 유효성 검사

## 기술 스택

- **Backend**: FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy 2.0+
- **Template Engine**: Jinja2
- **Data Validation**: Pydantic
- **Environment**: Python 3.12+

## v2.0 주요 변경사항

- **서비스 레이어 분리**: 비즈니스 로직을 별도의 서비스 레이어로 분리하여 코드 구조 개선

- **모듈화 개선**: 각 기능별로 더 명확하게 분리된 모듈 구조

## 프로젝트 구조

```
/
├── main.py                 # FastAPI 애플리케이션 진입점
├── routes/
│   └── blog.py            # 블로그 관련 라우터
├── services/              # 비즈니스 로직 서비스 레이어 (NEW)
│   └── blog_svc.py        # 블로그 서비스 로직
├── schemas/
│   └── blog_schema.py     # Pydantic 모델 정의
├── db/
│   └── database.py        # 데이터베이스 연결 관리
├── templates/             # HTML 템플릿
│   ├── index.html         # 메인 페이지
│   ├── show_blog.html     # 블로그 상세 보기
│   ├── new_blog.html      # 새 블로그 작성
│   └── modify_blog.html   # 블로그 수정
├── utils/
│   └── utils.py           # 유틸리티 함수
├── initial_data.sql       # 데이터베이스 초기화 스크립트
├── pyproject.toml         # 프로젝트 설정 및 의존성 관리
└── .env                   # 환경 변수 (복사 필요)
```

## 설치 및 실행

### 1. 저장소 클론

```bash
git clone <repository-url>
cd dev
```

### 2. 환경 설정

```bash
# uv를 사용한 의존성 설치
uv sync

# 또는 pip 사용
pip install -r requirements.txt
```

### 3. 데이터베이스 설정

MySQL 데이터베이스를 설정하고 `initial_data.sql`을 실행하여 테이블과 초기 데이터를 생성합니다.

```sql
-- MySQL에서 실행
source initial_data.sql
```

### 4. 환경 변수 설정

`.env` 파일을 생성하고 데이터베이스 연결 정보를 설정합니다:

```env
DATABASE_CONN=mysql+mysqlconnector://username:password@localhost:3306/blog_db
```

### 5. 애플리케이션 실행

```bash
fastapi dev main.py
```

애플리케이션이 `http://localhost:8000`에서 실행됩니다.

## API 엔드포인트

| Method | Path | Description |
|--------|------|-------------|
| GET | `/blogs/` | 모든 블로그 글 목록 조회 |
| GET | `/blogs/show/{id}` | 특정 블로그 글 상세 조회 |
| GET | `/blogs/new` | 새 블로그 작성 폼 |
| POST | `/blogs/new` | 새 블로그 글 생성 |
| GET | `/blogs/modify/{id}` | 블로그 수정 폼 |
| POST | `/blogs/modify/{id}` | 블로그 글 수정 |
| POST | `/blogs/delete/{id}` | 블로그 글 삭제 |

## 데이터베이스 스키마

```sql
CREATE TABLE blog_db.blog (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    content VARCHAR(4000) NOT NULL,
    image_loc VARCHAR(300) NULL,
    modified_dt DATETIME NOT NULL
);
```

## 의존성

주요 의존성은 `pyproject.toml`에서 확인할 수 있습니다:

- `fastapi[standard]>=0.116.1`
- `sqlalchemy>=2.0.0`
- `python-dotenv`
- `mysql-connector-python>=9.4.0`

## 개발 노트

### v2.0 아키텍처 개선사항
- **서비스 레이어 도입**: 라우터에서 비즈니스 로직을 분리하여 더 깔끔한 아키텍처 구현
- **모듈화된 구조**: 각 계층(라우터, 서비스, 스키마, 데이터베이스)이 명확히 분리
- **향상된 오류 처리**: 서비스 레이어에서 체계적인 예외 처리

### 기존 기능들
- 연결 풀링을 통한 데이터베이스 성능 최적화
- 예외 처리를 통한 안정적인 오류 관리
- HTML 템플릿을 사용한 사용자 친화적 인터페이스
- Pydantic을 활용한 강력한 데이터 검증

## 라이선스

이 프로젝트는 학습 목적으로 작성되었습니다.