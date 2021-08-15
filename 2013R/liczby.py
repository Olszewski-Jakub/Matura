def DowToDec(num, sys):
    sum = 0
    pot = 1
    for x in str(num)[::-1]:
        sum += int(x) * pot
        pot *= sys
    return sum


with open('dane.txt') as dane, open('odp.txt', "w") as odp:
    dane = dane.read().split()


    def a():
        count = 0
        for x in dane:
            if x[0] == x[-1]:
                count += 1
        odp.write(f"a {count}")


    def b():
        count = 0
        for x in dane:
            x = str(DowToDec(int(x), 8))
            if x[0] == x[-1]:
                count += 1
        odp.write(f"\nb {count}")


    def c():
        count = 0
        arr = []
        for x in dane:
            for y in range(0, len(x) - 1):
                if x[y] <= x[y + 1]:
                  count+=1
                else: break
            arr.append(int(x))
        odp.write(f"\nc {max(arr)}, {min(arr)}")
    a()
    b()
    c()
