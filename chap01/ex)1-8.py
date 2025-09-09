def sum_odds_between(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    if a % 2 == 0: 
        a += 1
    if b % 2 == 0:  
        b -= 1
    if a > b:
        return 0
    n_terms = ((b - a) // 2) + 1
    return n_terms * (a + b) // 2

# 테스트
print(sum_odds_between(5, 12))  
print(sum_odds_between(12, 5))  
