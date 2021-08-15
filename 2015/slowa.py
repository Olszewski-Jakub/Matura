with open('nowe.txt') as nowe, open('slowa.txt') as slowa:
    nowe = nowe.read().split()
    slowa = slowa.read().split()


def a():
    arr = [0] * 12
    for x in slowa:
        a = len(x) - 1
        arr[a] = arr[a] + 1
    for x in range(0, 12):
        print(x + 1, " ", arr[x])
def b():
    for x in nowe:
        count1 = 0
        count2 = 0
        for y in slowa:
            if x == y:
                count1 += 1
            if x == y[::-1]:
                count2 += 1
        print(x,count1,count2)

b()
