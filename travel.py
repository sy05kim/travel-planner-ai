import argparse
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

def get_kakao_places(city_name):
    api_key = os.getenv("KAKAO_API_KEY")
    print(f"로드된 키: {api_key}") # 이 줄을 추가해서 키가 잘 나오는지 확인!
    if not api_key: return ["API 키 미설정"]
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {api_key}"}
    params = {"query": f"{city_name} 맛집", "size": 5}
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return [f"{p['place_name']} ({p['category_name'].split(' > ')[-1]})" for p in data.get('documents', [])]
        return [f"에러: {response.status_code}"]
    except: return ["연동 실패"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    args = parser.parse_args()

    city = "부산"
    restaurants = get_kakao_places(city)
    
    result = {
        "recommended_city": city,
        "period": f"{args.start} ~ {args.end}",
        "restaurants": restaurants
    }

    print(f"\n📍 추천 도시: {city}")
    print(f"🍴 맛집: {', '.join(restaurants)}")

    os.makedirs("results", exist_ok=True)
    with open("results/recommendation.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    with open("results/recommendation.md", "w", encoding="utf-8") as f:
        f.write(f"# 여행 추천\n- 도시: {city}\n- 맛집: {', '.join(restaurants)}")

if __name__ == "__main__":
    main()