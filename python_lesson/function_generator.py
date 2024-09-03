def progression(limit=100):
    n = 2
    num = 1
    count = 1
    while count < limit:
        yield num
        num += n
        count += 1


for number in progression(10):
    print(number)

count_1 = 1
for number in progression(1000001):
    if count_1 == 1000000:
        print(number)
        break
    count_1 += 1

