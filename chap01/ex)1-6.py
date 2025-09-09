def sum_of_digits(x: int) -> int:
    x = abs(x)  
    total = 0
    while x > 0:
        total += x % 10
        x //= 10
    return total

# 테스트
print(sum_of_digits(274))   
print(sum_of_digits(-502)) 
