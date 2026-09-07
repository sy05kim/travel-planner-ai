import os
import json
import argparse
import requests  # API 호출을 위해 필요합니다
from datetime import datetime
from dotenv import load_dotenv

# 1. 환경 설정 및 API 키 로드
load_dotenv()
KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")

def get_kakao_places(query):
    """카카오 API를 통해 맛집 정보를 가져오는 함수"""
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {"query": query, "size": 5} # 5개만 가져오기
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json().get('documents', [])
        else:
            print(f"❌ API 호출 실패: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        return []

def main():
    # 2. 날짜 입력 받기
    parser = argparse.ArgumentParser(description="여행 계획 프로그램")
    parser.add_argument("-date", type=str, help="여행 날짜 (YYYY-MM-DD)", required=True)
    args = parser.parse_args()

    print(f"\n📅 여행 날짜: {args.date}")
    
    if not KAKAO_API_KEY:
        print("⚠️ API 키가 없습니다. .env 파일을 확인하세요!")
        return

    # 3. 진짜 데이터 가져오기 (카카오 API 호출)
    recommendation = "부산 해운대"
    search_query = f"{recommendation} 맛집"
    print(f"🔍 '{search_query}' 정보를 가져오는 중...")
    
    # API 호출 실행!
    places_data = get_kakao_places(search_query)
    
    # API 결과를 우리가 쓰기 편하게 정리
    places = []
    for p in places_data:
        places.append({
            "name": p['place_name'],
            "category": p['category_group_name'] if p['category_group_name'] else "기타",
            "address": p['address_name'],
            "url": p['place_url']
        })

    # 4. 화면 출력
    print(f"\n🤖 AI 추천 도시: {recommendation}")
    print(f"🍴 실제 검색된 맛집 리스트:")
    for i, p in enumerate(places, 1):
        print(f"{i}. {p['name']} ({p['address']})")

    # 5. 결과 저장
    if not os.path.exists("results"):
        os.makedirs("results")

    json_filename = f"results/{args.date}_data.json"
    md_filename = f"results/{args.date}_travel_plan.md"

    # JSON 저장
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump({"date": args.date, "recommendation": recommendation, "places": places}, f, ensure_ascii=False, indent=4)

    # Markdown 저장
    with open(md_filename, "w", encoding="utf-8") as f:
        f.write(f"# ✈️ {args.date} {recommendation} 여행 계획\n\n")
        f.write(f"### 🍴 추천 맛집 (카카오 맵 실시간 정보)\n")
        for p in places:
            f.write(f"- **[{p['name']}]({p['url']})**\n")
            f.write(f"  - 주소: {p['address']}\n")
            f.write(f"  - 카테고리: {p['category']}\n\n")

    print(f"\n✨ 실제 데이터로 파일이 업데이트 되었습니다!")
    print(f"📁 확인: {json_filename}, {md_filename}")

if __name__ == "__main__":
    main()