from typing import List, Dict
Contact = Dict[str, str]

def input_contacts() -> List[Contact]:
    contacts = []
    while True:
        name = input("이름 입력(종료: 0): ").strip()
        if name == "0":
            break
        age = input("나이 입력(종료: 0): ").strip()
        if age == "0":
            break
        phone = input("전화번호 입력: ").strip()
        contacts.append({"name": name, "age": age, "phone": phone})
        print("저장 완료!\n")
    return contacts

def print_contacts(contacts: List[Contact]) -> None:
    if not contacts:
        print("저장된 연락처가 없습니다.")
        return
    print("=== 연락처 목록 ===")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. 이름: {c['name']}, 나이: {c['age']}, 전화: {c['phone']}")

