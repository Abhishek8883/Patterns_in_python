# sol 1 
n = int(input("Enter the number"))

for i in range(1,n+1):
    for j in range(0,n+1-i):
        print(n , end = ' ')
    print()

# Sol 2
n = int(input('Enter the last number'))

for i in range(0,n):
    for j in range(0,n+1-i):
        print(j,end = ' ')
    print()

# sol 3
n = int(input('Enter the last number'))
count = 0
for i in range(0,n+1):
    if i==1:
        print(1)
    elif i%2 !=0:
        count +=1
        for j in range(0,count+1):
            print(i,end = ' ')
        print()


# sol4
n = int(input('Enter the biggest number\n'))

for i in range(1,n+1):
    print(i ,end = ' ')
    for j in range (1,i):
        print((j-i)*(-1) , end =' ')
    print()

# sol5
n = int(input('Enter the biggest number\n'))

lst =[0]
for i in range(1,n//2):
        s = i+int(lst[i-1])
        lst.append(s) 
        print(s,end = ' ')
        for j in range (1,i):
            print((j-s)*(-1), end =' ' )
        print()

# sol6
n = int(input('Enter the number of lines\n'))
for i in range(n):
    print(' '.join(map(str, str(11**i))))

# sol 7

n = int(input('Enter the number of lines\n'))

for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()

# sol8

n = int(input('Enter the number of lines\n'))

for i in range(1,n+1):
    print(i,end = ' ')
    for j in range(1,i):
        print(i+i*j,end=' ')
    print()

# sol9

n = int(input('Enter the number of lines\n'))

for i in range(0,n):
    for j in range(1,i+1):
        print('',end=' ')
    for k in range(0,n-i):
        print('*',end=' ')
    print()

# sol 10

n = int(input('Enter the number of lines\n'))

for i in range(0,n):
    for j in range(0,n):
        print(' ',end='')
    for k in range(0,i+1):
        print('*',end=' ')
    n-=1
    print()

# sol 11

n = int(input('Enter the number of lines\n'))

for i in range(0,n):
    for k in range(0,i+1):
        print('*',end=' ')
    print()
print()
for i in range(0,n):
    for k in range(0,n):
        print('*',end=' ')
    n-=1
    print()

# sol 12

n = int(input('Enter the number of lines\n'))

for i in range(0,n):
    for k in range(0,i+1):
        print('*',end=' ')
    print()
for i in range(1,n):
    for k in range(1,n):
        print('*',end=' ')
    n-=1
    print()

# sol 13

n = int(input('Enter the number of lines\n'))
s=n
for i in range(0,n):
    for j in range(0,n):
        print(' ',end=' ')
    n-=1
    for k in range(0,i+1):
        print('*',end=' ')
    print()
for i in range(1,s):
    for j in range(0,i+1):
        print(' ',end=' ')
    for k in range(1,s):
        print('*',end=' ')
    s-=1
    print()

# sol 14

n = int(input('Enter the number of lines\n'))

for i in range(0,n):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(0,n-i):
        print('*',end=' ')
    print()
for i in range(0,n):
    for j in range(0,n):
        print(' ',end='')
    for k in range(0,i):
        print('*',end=' ')
    n-=1
    print()

# sol 15
n = int(input('Enter the number of lines\n'))

for i in range(0,n):
    for j  in range(0,n):
        print('*',end ='')
    for k in range(0,i):
        print('_',end='')
    for l in range(0,i):
        print('_',end='')
    for m in range(0,n):
        print('*',end='')
    n-=1    
    print()





