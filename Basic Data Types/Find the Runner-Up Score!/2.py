if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newlist = sorted(list(set(arr)), reverse=True)
    print(newlist[1])
