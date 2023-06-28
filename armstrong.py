for x in range(1,1000):
    s = 0
    t = x
    while t != 0:
        rem = t % 10
        s += rem**3
        t = t // 10
    if s == x:
        print(x,end=' ')