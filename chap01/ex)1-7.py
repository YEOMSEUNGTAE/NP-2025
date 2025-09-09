def find_char_positions(s: str, ch: str) -> int:
    positions = [i for i, c in enumerate(s) if c == ch]
    if positions:
        print(",".join(map(str, positions)))  
    else:
        print("")  
    return len(positions)

# 테스트
print(find_char_positions("Hello", "l"))  # 콘솔: 2,3 출력 / 반환값: 2
