# Enter your code here. Read input from STDIN. Print output to STDOUT
num=int(input())

for i in range(num):
    stroddeven=""
    strodd2=""
    STDIN=input()
    for j in range(len(STDIN)):
        if j%2==0:
            stroddeven+=STDIN[j]
        else:
            strodd2+=STDIN[j]
    print(stroddeven,strodd2)  
