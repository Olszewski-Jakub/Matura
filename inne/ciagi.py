from random import randint

n = int(input("Podaj dlugosc listy"))
arr = [randint(0, 10) for x in range(n)]
print(arr)
count = 1
temp = []
for x in range(1, len(arr)):
    if arr[x - 1] < arr[x]:
        count += 1
    else:
        temp.append(count)
        count = 1

temp.append(count)
print(max(temp))
