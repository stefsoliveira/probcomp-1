n = int(input())
l = list(map(int,input().split()))
a = 0; cruzamentos = 0
while a < n-1:
        for i in range(1+a, n):
            if l[a] > l[i]:
                cruzamentos +=1
        a +=1

print(cruzamentos)