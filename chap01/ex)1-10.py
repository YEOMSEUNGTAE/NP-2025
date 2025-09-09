def get_admission_year(student_id: str) -> int:
    year_str = student_id[:4]
    if not year_str.isdigit():
        raise ValueError("학번 앞 4자리가 숫자가 아닙니다.")
    return int(year_str)

# 테스트
print(get_admission_year("202110846"))  # 2021
