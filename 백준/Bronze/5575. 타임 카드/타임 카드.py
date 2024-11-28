for i in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    t1 = s1 + m1*60 + h1*60*60
    t2 = s2 + m2*60 + h2*60*60
    time = t2-t1

    hour = time//60//60%24
    minute = time//60%60
    seconds = time%60
    print(hour, minute, seconds)