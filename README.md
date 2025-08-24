# FastAPI Blog Management System: v2.2.0

FastAPI 기반 블로그 관리 시스템입니다. MySQL 데이터베이스와 연동하여 블로그 글 작성, 수정, 삭제, 조회 기능을 제공하며, 파일 업로드와 반응형 웹 인터페이스를 지원합니다.

## 🚀 주요 기능

### 📝 블로그 관리
- **CRUD 기능**: 블로그 글 작성, 수정, 삭제, 조회
- **이미지 업로드**: 블로그 포스트에 이미지 첨부 기능
- **파일 관리**: 안전한 파일 업로드 및 저장 시스템
- **텍스트 미리보기**: 긴 내용 자동 요약 표시

### 🎨 사용자 인터페이스
- **반응형 디자인**: Bootstrap 5 기반 모바일 친화적 UI
- **템플릿 시스템**: Jinja2를 활용한 동적 웹 페이지
- **레이아웃 컴포넌트**: 재사용 가능한 네비게이션, 푸터
- **이미지 표시**: 업로드된 이미지 자동 표시 및 기본 이미지 지원

### 🏗️ 아키텍처
- **서비스 레이어**: 비즈니스 로직과 API 분리
- **데이터베이스 커넥션 풀**: 효율적인 MySQL 연결 관리
- **정적 파일 서빙**: CSS, JS, 이미지 파일 제공
- **에러 핸들링**: 사용자 친화적 오류 처리

## 🛠️ 기술 스택

| 카테고리 | 기술 | 버전 | 용도 |
|---------|------|------|------|
| **Backend** | FastAPI | >=0.116.1 | 웹 프레임워크 |
| **Database** | MySQL | - | 데이터 저장 |
| **ORM** | SQLAlchemy | >=2.0.0 | 데이터베이스 ORM |
| **Template** | Jinja2 | - | HTML 템플릿 엔진 |
| **Frontend** | Bootstrap | 5.x | CSS 프레임워크 |
| **File Upload** | python-multipart | >=0.0.20 | 파일 업로드 처리 |
| **Validation** | Pydantic | - | 데이터 유효성 검사 |
| **Environment** | Python | >=3.12 | 런타임 환경 |
| **Package Manager** | uv | - | 빠른 Python 패키지 관리 |

## 📋 상세 기능 목록

### 블로그 포스트 관리
- ✅ 블로그 글 목록 보기 (페이지네이션 지원)
- ✅ 블로그 글 상세 보기
- ✅ 새 블로그 글 작성
- ✅ 기존 블로그 글 수정
- ✅ 블로그 글 삭제
- ✅ 이미지 파일 업로드 및 첨부
- ✅ 긴 텍스트 자동 요약 표시

### 파일 및 미디어 관리
- ✅ 이미지 파일 업로드 (.jpg, .jpeg, .png, .gif)
- ✅ 파일 크기 및 형식 검증
- ✅ 고유 파일명 생성 (타임스탬프 기반)
- ✅ 업로드 디렉토리 자동 생성
- ✅ 정적 파일 서빙 (/static 경로)
- ✅ 기본 이미지 제공

### 사용자 인터페이스
- ✅ 반응형 웹 디자인 (모바일, 태블릿, 데스크톱)
- ✅ Bootstrap 5 컴포넌트 활용
- ✅ 네비게이션 바 및 푸터
- ✅ 폼 유효성 검사 및 에러 메시지
- ✅ 이미지 미리보기 기능

## 📝 버전별 변경사항

### v2.2.0 (2025-08-25) - 비동기 처리 아키텍처 도입
- ⚡ **비동기 데이터베이스 연결**: SQLAlchemy AsyncEngine으로 성능 최적화
- 🔄 **Async/Await 패턴**: 모든 엔드포인트 및 서비스 레이어 비동기 처리
- 🚀 **FastAPI 라이프사이클**: 애플리케이션 시작/종료 이벤트 관리 구현
- 📈 **성능 향상**: 동시 요청 처리 능력 및 응답 속도 개선
- 🔧 **리소스 관리**: Graceful shutdown 및 연결 풀 최적화
- 📦 **의존성 추가**: `pymysql`, `aiomysql`, `greenlet`, `aiofiles`

### v2.1.0 (2025-08-25) - 정적 파일 및 UI 개선
- ✨ **정적 파일 서빙**: CSS, JS, 이미지 파일을 위한 `/static` 엔드포인트 추가
- 🏗️ **템플릿 레이아웃 시스템**: 재사용 가능한 레이아웃 컴포넌트 도입
  - `main_layout.html`: Bootstrap 통합 기본 레이아웃
  - `navbar.html`: 반응형 네비게이션 바
  - `footer.html`: 일관된 푸터 컴포넌트
- 📤 **파일 업로드 기능**: `python-multipart` 의존성 추가로 이미지 업로드 지원
- 🎨 **UI/UX 개선**: Bootstrap 5를 활용한 현대적이고 반응형 디자인
- 📁 **디렉토리 구조 개선**: `static/`, `templates/layout/` 디렉토리 추가
- 🖼️ **이미지 관리**: 업로드된 이미지 표시 및 기본 이미지 제공

### v2.0.0 (2024) - 서비스 레이어 아키텍처
- 🏗️ **서비스 레이어 분리**: 비즈니스 로직을 별도의 서비스 레이어로 분리
- 📦 **모듈화 개선**: 각 기능별로 더 명확하게 분리된 모듈 구조
- 🔧 **코드 품질 향상**: 관심사 분리로 테스트 용이성 및 유지보수성 개선

## 📁 프로젝트 구조

```
fastapi-blog-tutorial/
├── 📄 main.py                     # FastAPI 애플리케이션 진입점
├── 📁 static/                     # 정적 파일 디렉토리 (v2.1.0+)
│   ├── 📁 uploads/               # 사용자 업로드 파일 저장소
│   │   └── 📁 {author}/         # 작성자별 파일 분류
│   ├── 📁 default/              # 기본 이미지 및 에셋
│   │   └── 🖼️ blog_default.png  # 기본 블로그 이미지
│   └── 🖼️ db_fundamental.png    # 프로젝트 관련 이미지
├── 📁 routes/                    # API 라우터
│   └── 📄 blog.py               # 블로그 관련 엔드포인트
├── 📁 services/                  # 비즈니스 로직 서비스 레이어 (v2.0+)
│   └── 📄 blog_svc.py           # 블로그 서비스 로직
├── 📁 schemas/                   # 데이터 모델 정의
│   └── 📄 blog_schema.py        # Pydantic 스키마
├── 📁 db/                       # 데이터베이스 관련
│   └── 📄 database.py           # DB 연결 및 세션 관리
├── 📁 templates/                # HTML 템플릿
│   ├── 📁 layout/              # 레이아웃 컴포넌트 (v2.1.0+)
│   │   ├── 📄 main_layout.html  # 기본 레이아웃 (Bootstrap 통합)
│   │   ├── 📄 navbar.html       # 네비게이션 바
│   │   └── 📄 footer.html       # 푸터
│   ├── 📄 index.html           # 메인 페이지 (블로그 목록)
│   ├── 📄 show_blog.html       # 블로그 상세 보기
│   ├── 📄 new_blog.html        # 새 블로그 작성 폼
│   └── 📄 modify_blog.html     # 블로그 수정 폼
├── 📁 utils/                    # 유틸리티 함수
│   └── 📄 utils.py             # 공통 헬퍼 함수
├── 📄 initial_data.sql          # 데이터베이스 초기화 스크립트
├── 📄 pyproject.toml           # 프로젝트 설정 및 의존성
├── 📄 uv.lock                  # 의존성 잠금 파일
├── 📄 .env                     # 환경 변수 (수동 생성 필요)
└── 📄 README.md               # 프로젝트 문서
```

### 주요 디렉토리 설명

| 디렉토리 | 설명 | 주요 파일 |
|----------|------|-----------|
| `static/` | 정적 파일 제공 | CSS, JS, 이미지 파일 |
| `templates/layout/` | 재사용 가능한 UI 컴포넌트 | 네비바, 푸터, 기본 레이아웃 |
| `services/` | 비즈니스 로직 분리 | 데이터 처리, 유효성 검사 |
| `routes/` | API 엔드포인트 정의 | HTTP 요청/응답 처리 |
| `schemas/` | 데이터 구조 정의 | Pydantic 모델 |

## 🚀 설치 및 실행

### 사전 요구사항
- Python 3.12 이상
- MySQL 8.0 이상
- uv (빠른 Python 패키지 매니저) 또는 pip

### 1. 저장소 클론
```bash
git clone https://github.com/juun0-h/fastapi_blog_tutorial.git
cd fastapi_blog_tutorial
```

### 2. Python 환경 설정
```bash
# uv 사용 (권장)
uv sync

# 또는 가상환경 생성 후 pip 사용
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
```

### 3. 데이터베이스 설정
MySQL에서 데이터베이스를 생성하고 초기 데이터를 설정합니다:

```sql
-- MySQL 접속 후 실행
CREATE DATABASE blog_db;
USE blog_db;
SOURCE initial_data.sql;
```

### 4. 환경 변수 설정
프로젝트 루트에 `.env` 파일을 생성하고 다음 내용을 추가합니다:

```env
# .env 파일
DATABASE_CONN=mysql+mysqlconnector://your_username:your_password@localhost:3306/blog_db

# 예시
DATABASE_CONN=mysql+mysqlconnector://root:password123@localhost:3306/blog_db
```

### 5. 애플리케이션 실행
```bash
# 개발 모드 실행 (자동 리로드)
uv run uvicorn main:app --reload --port=8000

# 또는 FastAPI CLI 사용
uv run fastapi dev main.py

# 프로덕션 모드
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

### 6. 브라우저에서 확인
- 애플리케이션: http://localhost:8000/blogs/
- API 문서: http://localhost:8000/docs
- ReDoc 문서: http://localhost:8000/redoc

## 📚 API 엔드포인트

### 블로그 관리 API

| Method | Path | Description | Request Body | Response |
|--------|------|-------------|--------------|----------|
| `GET` | `/blogs/` | 모든 블로그 글 목록 조회 | - | HTML 페이지 |
| `GET` | `/blogs/show/{id}` | 특정 블로그 글 상세 조회 | - | HTML 페이지 |
| `GET` | `/blogs/new` | 새 블로그 작성 폼 | - | HTML 페이지 |
| `POST` | `/blogs/new` | 새 블로그 글 생성 | `title`, `author`, `content`, `image` | Redirect |
| `GET` | `/blogs/modify/{id}` | 블로그 수정 폼 | - | HTML 페이지 |
| `POST` | `/blogs/modify/{id}` | 블로그 글 수정 | `title`, `author`, `content`, `image` | Redirect |
| `POST` | `/blogs/delete/{id}` | 블로그 글 삭제 | - | Redirect |

### 정적 파일 API
| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/static/uploads/{author}/{filename}` | 업로드된 이미지 파일 |
| `GET` | `/static/default/{filename}` | 기본 이미지 파일 |

## 🗄️ 데이터베이스 스키마

### blog 테이블
```sql
CREATE TABLE blog_db.blog (
    id INTEGER AUTO_INCREMENT PRIMARY KEY COMMENT '블로그 글 고유 ID',
    title VARCHAR(200) NOT NULL COMMENT '블로그 글 제목',
    author VARCHAR(100) NOT NULL COMMENT '작성자 이름',
    content VARCHAR(4000) NOT NULL COMMENT '블로그 내용',
    image_loc VARCHAR(300) NULL COMMENT '첨부 이미지 경로',
    modified_dt DATETIME NOT NULL COMMENT '최종 수정 일시'
);
```

### 샘플 데이터
```sql
INSERT INTO blog (title, author, content, image_loc, modified_dt) VALUES 
('FastAPI 시작하기', '김개발', 'FastAPI는 Python 웹 프레임워크입니다...', 
 '/static/default/blog_default.png', NOW()),
('SQLAlchemy 활용법', '이데이터', 'SQLAlchemy를 사용하여 데이터베이스를...', 
 NULL, NOW());
```

## 📦 의존성 관리

### 핵심 의존성
주요 의존성은 `pyproject.toml`에서 관리됩니다:

```toml
[project]
dependencies = [
    "fastapi[standard]>=0.116.1",  # 웹 프레임워크 및 표준 확장
    "sqlalchemy>=2.0.0",           # ORM 및 데이터베이스 추상화
    "python-dotenv",                # 환경 변수 관리
    "mysql-connector-python>=9.4.0", # MySQL 드라이버
    "python-multipart>=0.0.20",    # 파일 업로드 지원
]
```

### 개발 도구 (선택사항)
```bash
# 코드 포맷팅
uv add --dev black isort

# 린팅
uv add --dev flake8 mypy

# 테스팅
uv add --dev pytest pytest-asyncio httpx
```

## 🔧 개발 노트

### 아키텍처 설계 원칙
1. **관심사 분리**: 라우터, 서비스, 데이터베이스 레이어 분리
2. **의존성 주입**: FastAPI의 Depends를 활용한 깔끔한 의존성 관리
3. **에러 핸들링**: 사용자 친화적 오류 메시지 및 적절한 HTTP 상태 코드
4. **코드 재사용**: 템플릿 상속 및 공통 유틸리티 함수 활용

### 파일 업로드 설계
- **보안**: 파일 확장자 검증 및 안전한 파일명 생성
- **조직화**: 작성자별 디렉토리 분리로 파일 관리 용이성
- **성능**: 정적 파일 서빙으로 효율적인 이미지 제공

### 데이터베이스 연결 관리
```python
# 컨텍스트 매니저를 사용한 안전한 연결 관리
@contextmanager
def context_get_conn():
    conn = None
    try:
        conn = engine.connect()
        yield conn
    finally:
        if conn:
            conn.close()
```

### 템플릿 상속 구조
```html
<!-- main_layout.html: 기본 레이아웃 -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
    <!-- Bootstrap CDN -->
</head>
<body>
    {% include 'layout/navbar.html' %}
    <main>{% block content %}{% endblock %}</main>
    {% include 'layout/footer.html' %}
</body>
</html>
```

## 🚀 향후 개발 계획

### v2.2.0 (예정)
- 🔐 **사용자 인증**: 회원가입, 로그인, JWT 토큰 기반 인증
- 🏷️ **태그 시스템**: 블로그 글 분류 및 검색 기능
- 💬 **댓글 시스템**: 블로그 글에 댓글 작성 기능

### v2.3.0 (예정)
- 📊 **대시보드**: 관리자용 통계 대시보드
- 🔍 **검색 기능**: 제목, 내용, 작성자별 검색
- 📱 **PWA 지원**: 모바일 앱처럼 사용할 수 있는 기능

### v3.0.0 (장기 계획)
- 🔄 **API 분리**: Frontend와 Backend 완전 분리
- ⚡ **성능 최적화**: 캐싱, 페이지네이션 개선
- 🧪 **테스트 커버리지**: 단위 테스트 및 통합 테스트 추가

## 🤝 기여 방법

### 브랜치 전략
이 프로젝트는 **GitHub Flow 기반 단순화 전략**을 사용합니다:

#### 브랜치 구조
- **`main`**: 항상 배포 가능한 안정적인 코드
- **`feature/*`**: 새로운 기능 개발 (`feature/기능명`)
- **`hotfix/*`**: 긴급 버그 수정 (`hotfix/버그명`)

#### 개발 워크플로우
```bash
# 새 기능 개발
git checkout main
git pull origin main
git checkout -b feature/새기능명

# 개발 및 커밋
git add .
git commit -m "feat: 새로운 기능 추가"
git push origin feature/새기능명

# main으로 머지 후 브랜치 삭제
git checkout main
git merge feature/새기능명
git branch -d feature/새기능명
git push origin --delete feature/새기능명
```

#### 버전 관리
- **메이저 릴리즈**: `v3.0.0` (Breaking Changes)
- **마이너 릴리즈**: `v2.2.0` (새로운 기능)
- **패치 릴리즈**: `v2.1.1` (버그 수정)

### 커밋 메시지 규칙
이 프로젝트는 [Conventional Commits](https://www.conventionalcommits.org/) 규칙을 따릅니다:

```
<type>: <description in Korean>

예시:
feat: 블로그 검색 기능 추가
fix: 이미지 업로드 오류 수정
docs: README 문서 업데이트
style: 코드 포맷팅 적용
refactor: 서비스 레이어 구조 개선
test: 블로그 서비스 단위 테스트 추가
chore: 의존성 버전 업데이트
```

### 개발 워크플로우
1. 최신 main 브랜치에서 기능 브랜치 생성
2. 기능 개발 및 단위별 커밋
3. 정기적으로 원격 저장소에 푸시 (백업)
4. 기능 완성 후 main으로 머지
5. 기능 브랜치 삭제 및 정리
6. 필요시 릴리즈 태그 생성

### 브랜치 명명 규칙
- **기능 개발**: `feature/user-auth`, `feature/blog-search`
- **버그 수정**: `hotfix/image-upload-bug`, `hotfix/security-fix`
- **문서 업데이트**: `docs/readme-update`, `docs/api-documentation`

### 코드 스타일
- **Python**: PEP 8 준수
- **HTML/CSS**: 들여쓰기 2칸
- **JavaScript**: ES6+ 문법 사용

## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 📞 문의 및 지원

- **GitHub Issues**: 버그 리포트 및 기능 요청
- **Discussions**: 질문 및 아이디어 공유
- **작성자**: juun0-h
- **프로젝트 저장소**: https://github.com/juun0-h/fastapi_blog_tutorial

---

⭐ 이 프로젝트가 도움이 되었다면 스타를 눌러주세요!

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