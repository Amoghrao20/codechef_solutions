d1, v1, d2, v2, p = map(int, input().split())

if d1==d2 and d1==1:
    ans = 0
    count = 0
    while(ans<p):
        count+=1
        ans+=(v1+v2)
    print(count)
else:
    count=min(d1,d2)
    ans=0
    while(ans<p):
        if d1>d2:
            ans+=v2
            count+=1
            d2+=1
        elif d2>d1:
            ans+=v1
            count+=1
            d1+=1
        elif d1==d2:
            ans+=(v1+v2)
            count+=1
            d2+=1
            d1+=1
    print(count-1)


