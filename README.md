# ✈️ AI 다중 API 여행 추천 프로그램 (Travel Planner AI)

사용자가 입력한 여행 일정에 맞춰 최적의 도시를 추천하고, **Kakao Local API**를 활용해 해당 지역의 실제 맛집 정보를 제공하는 CLI 기반 여행 플래너입니다.

## ✨ 주요 기능 (Functional Requirements)
- **사용자 맞춤 일정 입력**: `argparse`를 통해 CLI 환경에서 여행 시작일과 종료일을 입력받습니다.
- **다중 데이터 통합**: 
  - 추천 도시, 날씨, 이벤트 정보를 구조화된 데이터로 처리합니다.
  - **Kakao Local API** 연동을 통해 해당 도시의 실제 맛집(음식점) 데이터 5곳을 실시간으로 가져옵니다.
- **자동 결과 리포트 생성**:
  - 실행 시 `results/` 폴더를 자동으로 생성합니다.
  - 추천 결과는 `JSON` 형식과 가독성이 좋은 `Markdown` 형식 두 가지로 저장됩니다.
- **예외 처리 및 안정성**:
  - API 키 미설정, 검색 결과 부재, 네트워크 오류 등에 대한 에러 핸들링이 적용되어 있습니다.

## 🛠 기술 스택 및 제약 사항 (Constraints)
- **Language**: Python 3.14+ 호환 (최신 파이썬 버전의 `datetime` 라이브러리 변화 대응)
- **APIs**: Kakao Local API (REST API)
- **Environment**: `.env` 파일을 통한 API 키 보안 관리
- **Libraries**: `requests`, `python-dotenv`, `argparse`

## 🚀 시작하기

### 1. 환경 변수 설정
프로젝트 루트 폴더에 `.env` 파일을 생성하고 Kakao REST API 키를 입력합니다.
```env
KAKAO_API_KEY=your_kakao_api_key_here
