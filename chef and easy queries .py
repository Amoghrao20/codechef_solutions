# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    sum=0
    for i in  range(len(a)):
        sum+=a[i]
    b=sum//k
    print(b+1)


