for i in range(int(input())):
    n,k,x,y=map(int,input().split())
    a=[]
    for i in range(n):
        b=((x+k*i)%n)
        a.append(b)
    if y in a:
        print("YES")
    else:
        print("NO")
