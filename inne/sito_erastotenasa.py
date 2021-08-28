n = int(input("Podaj liczbe koncowa"))
arr = [1] * n
for x in range(2, n):
    if arr[x] != 0:
        for y in range(2 * x, len(arr), x):
            arr[y] = 0

for x in range(2, len(arr)):
    if arr[x] != 0:
        print(x, end=" ")
