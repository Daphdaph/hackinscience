a = 0
for i in range(0, 1001):
    if i % 3 == 0:
        a = a+i
    else:
        if i % 5 == 0:
            a = a+i
print(a)
