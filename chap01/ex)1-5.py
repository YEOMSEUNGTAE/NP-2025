def sum_range(n: int, m: int) -> int:
    if n > m:  
        n, m = m, n
    return (m - n + 1) * (n + m) // 2

# 테스트
print(sum_range(3, 7))   
print(sum_range(10, 1)) 
