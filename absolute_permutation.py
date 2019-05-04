'''Q: We define P to be a permutation of the first n natural numbers in the range [1,n].
Let pos[i] denote the value at position i in permutation P using 1-based indexing.
P is considered to be an absolute permutation if |pos[i]-i|=k holds true for every i in [1,n].
Given n and k, print the lexicographically smallest absolute permutation P.
If no absolute permutation exists, print -1.
'''

t=int(input("Enter the number of test cases: \n"))
for _ in range(t):
    print("Enter 'n' and 'k': ")
    nk=input().split()
    n=int(nk[0])
    k=int(nk[1])

    li=[]
    for i in range(1,n+1):
        li.append(i)
    if k==0:
        li=li
    elif k>int(n/2):
        li=[-1]
    else:
        if n%2!=0:
            li=[-1]
        else:
            if n%(2*k)==0:
                j=0
                while j<=(n-2*k):
                    for i in range(k):
                        temp=li[j+i]
                        li[j+i]=li[j+i+k]
                        li[j+i+k]=temp
                    j+=2*k
            else:
                li=[-1]
    

    print(li)
        
