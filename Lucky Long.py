for i in range(int(input())):
    n=input()
    lis=[int(x) for x in n]
    count=0
    for i in lis:
        if(i==4 or i==7):
            continue
        else:
            count+=1
    print(count)

