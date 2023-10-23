#!/usr/bin/python3
def magic_calculation(a, b):
a = 1
b = 3
result = 0

for i in range(1, 3):
    try:
        if i > a:
            raise Exception('Too far')
        result += (a ** b) / i
    except Exception:
        result += a + b

print(result)
