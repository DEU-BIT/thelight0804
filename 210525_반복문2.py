#반복문 사용하여 * 찍기
for i in range(0, 5, 1):
    print("*")
    for n in range(0, i+1, 1):
        print("*", end="")