def testowanie(a):
    if len(a) < 16:
        return "Nie prawidłowy numer karty"
    elif len(a) > 16:
        return "Nie prawidłowy numer karty"
    else:
        koniec = a[-1]
        a.pop(-1)
        b = a.reverse()
        for x in b, 2:
            b[x] = b[x] * 2
        return b

a = [5,3,6,2,5,7,1,5,9,4,8,2,4,0,1,8]
print(testowanie(a))