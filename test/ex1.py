for i in range(999, 100, -1):
    c = i % 10
    b = (i % 100) / 10
    a = (i / 100)
    if a*a*a + b*b*b + c*c*c == i:
        print i
