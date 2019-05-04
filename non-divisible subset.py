#Q: Given a set of distinct integers, print the size of a maximal subset of where the sum of any numbers in is not evenly divisible by 'k'.

#A:

k=int(input('Enter the non-divisor: \n'))
arr=list(map(int,input('Enter the list: \n').strip().split()))

d=dict()
for i in range(k):
    d[i]=[]
for j in arr:
    d[j%k].append(j) #counting remainders

count=0 #counter of length of required set
if len(d[0])>0:
    count+=1 #since only one of the numbers, exactly divisible, can be kept in the set

li=[]
for i in range(1,int(k/2)+1): li.append([i,k-i]) #corresponding remainders can't be paired together

for [i,j] in li:
    if i!=j:
        if len(d[i])>=len(d[j]):
            count=count+len(d[i])
        else:
            count=count+len(d[j])
    else:
        count+=1 #for even 'k', only 1 no. with remainder 'k/2' can be counted

print('The largest required subset is: {}'.format(count))



    
 
