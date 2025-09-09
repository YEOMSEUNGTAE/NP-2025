a = int(input('1번째 숫자를 입력하세요.'))
b = int(input('2번째 숫자를 입력하세요.'))

c = a+b 
e = a<<b
f = a*b

print(c)
print(e)
print(f)

if c>e and c>f:
    print(c) 
elif e>c and e>f:
    print(e)
else: print(f)


