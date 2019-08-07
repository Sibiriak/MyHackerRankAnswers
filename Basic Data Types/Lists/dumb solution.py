if __name__ == '__main__':
    lst = []
    N = int(input())
    for _ in range(N):
        txt = input()
        if 'insert' in txt:
            position, element = txt.split(' ')[1:]
            lst.insert(int(position), int(element))            
        elif txt == 'print':
            print(lst)
        elif 'remove' in txt:
            item = int(txt.split(' ')[1])
            lst.remove(item)
        elif 'append' in txt:
            item = int(txt.split(' ')[1])
            lst.append(item)
        elif txt == 'sort':
            lst = sorted(lst)            
        elif txt == 'pop':
            item = lst.pop()            
        elif txt == 'reverse':
            lst = sorted(lst, reverse=True)
