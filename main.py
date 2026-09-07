import json
import os

DATA_FILE = "prompts.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return [
            {"title": "영어 번역기", "content": "번역해줘.", "category": "번역", "favorite": False},
            {"title": "파이썬 도우미", "content": "코드 고쳐줘.", "category": "코딩", "favorite": True},
            {"title": "요약 봇", "content": "요약해줘.", "category": "학습", "favorite": False}
        ]

def save_data(prompts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)

def add_prompt(prompts):
    print("\n--- 새 프롬프트 추가 ---")
    title = input("제목: ")
    content = input("내용: ")
    category = input("카테고리: ")
    prompts.append({"title": title, "content": content, "category": category, "favorite": False})
    save_data(prompts)
    print("✅ 추가되었습니다!")

def add_prompt(prompts):
    print("\n--- 새 프롬프트 추가 ---")
    
    # 1. 제목 입력 및 빈 값 검사
    title = input("제목을 입력하세요: ").strip()
    if not title:  # 입력값이 없으면
        print("❌ 오류: 제목을 입력해야 합니다. 추가를 취소합니다.")
        return  # 함수를 종료하고 메뉴로 돌아감

def add_prompt(prompts):
    title = input("새 프롬프트 제목: ")
    
    # [추가] 중복 제목 검사 로직
    for p in prompts:
        if p['title'] == title:
            print(f"❌ 에러: '{title}'은(는) 이미 존재하는 제목입니다. 중복 저장을 금지합니다.")
            return  # 함수 종료 (추가되지 않음)

    content = input("내용: ")
    # ... (기존 코드: 카테고리 입력 및 append 부분)

    # 2. 내용 입력 및 빈 값 검사
    content = input("내용을 입력하세요: ").strip()
    if not content:
        print("❌ 오류: 내용을 입력해야 합니다. 추가를 취소합니다.")
        return

    category = input("카테고리(기본: 미분류): ").strip() or "미분류"
    
    # ... (기존 저장 코드)

def show_prompts(prompts):
    print("\n--- 프롬프트 목록 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    
    for i, p in enumerate(prompts):
        # 즐겨찾기 여부에 따라 별표 표시
        fav = "⭐" if p.get('favorite') else "  "
        print(f"{i+1}. {fav} [{p['category']}] {p['title']}")
    print("--------------------")
    
def search_prompt(prompts):
    keyword = input("\n검색어(제목/내용/카테고리): ")
  results = [p for p in prompts if keyword in p['title'] or keyword in p['content'] or keyword in p['category']]
    print(f"\n--- '{keyword}' 검색 결과 ---")
    for p in results:
        fav = "⭐" if p.get("favorite") else "  "
        print(f"[{p.get('category', '미분류')}] {p['title']} {fav}\n   내용: {p['content']}")

def delete_prompt(prompts):
    show_prompts(prompts)
    try:
        idx = int(input("\n삭제할 번호: ")) - 1
        if 0 <= idx < len(prompts):
            removed = prompts.pop(idx)
            save_data(prompts)
            print(f"✅ '{removed['title']}' 삭제 완료!")
    except: print("❌ 잘못된 입력입니다.")

def toggle_favorite(prompts):
   show_prompts(prompts) 
   try:
        idx = int(input("\n즐겨찾기 토글 번호: ")) - 1
        if 0 <= idx < len(prompts):
            prompts[idx]["favorite"] = not prompts[idx].get("favorite", False)
            save_data(prompts)
            print("✅ 즐겨찾기 상태가 변경되었습니다.")
   except: print("❌ 잘못된 입력입니다.")

# --- 새로 추가된 6번 기능 ---
def show_by_category(prompts):
    """등록된 카테고리 목록을 보여주고 선택한 카테고리만 출력합니다."""
    categories = list(set(p.get('category', '미분류') for p in prompts))
    print("\n--- 현재 카테고리 목록 ---")
    for i, cat in enumerate(categories):
        print(f"{i+1}. {cat}")

def show_favorites(prompts):
    """즐겨찾기(⭐)된 프롬프트만 필터링하여 출력"""
    print("\n--- ⭐ 즐겨찾기 목록 ---")
    # favorite이 True인 항목만 골라냅니다.
    fav_list = [p for p in prompts if p.get('favorite') == True]
    
    if not fav_list:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(fav_list, 1):
        print(f"{i}. [⭐] {p['title']} ({p.get('category', '미분류')})")
        print(f"   내용: {p['content']}")

    try:
        choice = int(input("조회할 카테고리 번호: ")) - 1
        selected_cat = categories[choice]
        print(f"\n--- [{selected_cat}] 카테고리 목록 ---")
        for p in prompts:
            if p.get('category', '미분류') == selected_cat:
                fav = "⭐" if p.get("favorite") else "  "
                print(f"- {p['title']} {fav}")
    except:
        print("❌ 잘못된 선택입니다.")

def main():
    prompts = load_data()
    while True:
        # 7번 메뉴 텍스트 추가
        print("\n--- 프롬프트 관리 프로그램 ---")
        print("1. 추가 2. 목록 3. 검색 4. 삭제 5. 즐겨찾기 토글 6. 카테고리 조회 7. 즐겨찾기 모아보기 0. 종료")
        choice = input("선택: ")

        if choice == "1": add_prompt(prompts)
        elif choice == "2": show_prompts(prompts)
        elif choice == "3": search_prompt(prompts)
        elif choice == "4": delete_prompt(prompts)
        elif choice == "5": toggle_favorite(prompts)
        elif choice == "6": show_by_category(prompts)
        elif choice == "7": show_favorites(prompts)  # 이 줄을 추가!
        elif choice == "0":
            save_data(prompts)
            print("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()