n = int(input())
l = []
for _ in range(n):
    raw = input().split()
    cmd = raw[0]
    args = raw[1:]
    if cmd!='print':
        eval('l.%s(%s)' %(cmd, ','.join(args)))
    else:
        print(l)
