alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while True:
    exc = input()
    res = ''
    if exc == 'R0C0':
        break
    else:
        c_index = exc.index('C')
        a,b = int(exc[1:c_index]), int(exc[c_index+1:])
        while b>0:
            r = b%26
            if r==0:
                res+='Z'
                b = b//26-1
            else:
                res+=alpha[r-1]
                b//=26
    print(''.join(reversed(res)), a, sep='')