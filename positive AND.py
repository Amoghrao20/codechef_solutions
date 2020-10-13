# cook your dish here
def ispower(n):
    return  (n&(n-1)==0)
for i in range(int(input())):
    n=int(input())
    if n==1:
        print("1")
        continue
    elif ispower(n):
        print("-1")
        continue
    elif n==3:
        print("2 3 1")
        continue
    elif n==5:
        print("2 3 1 5 4")
        continue
    else:
        print(" 2 3 1 5 4")
        i=6
        while(i<=n):
            if ispower(i):
                print(i+1,i)
                i+=2
            else:
                print(i)
                i+=1
