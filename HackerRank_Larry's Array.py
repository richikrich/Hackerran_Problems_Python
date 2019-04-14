'''
Q. Larry has been given a permutation of a sequence of natural numbers incrementing from 1 as an array. He must determine whether the array can be sorted using the following operation any number of times:
Choose any 3 consecutive indices and rotate their elements in such a way that ABC ->BCA ->CAB -> ABC.
For eg> If A={1,6,5,2,4,3}
[1,6,5,2,4,3]->[1,5,2,6,4,3]->[1,2,6,5,4,3]->[1,2,3,5,6,4]->[1,2,3,4,5,6]
'''
import math
#the following function counts the number of inversion count of a given array. It denotes how far the array is from being sorted
#inversion count is basically the number of inversions needed in the array,i.e., for i<j if A[i]>A[j], inversion number+=1
def count_inv(li):
    inv=0
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                inv+=1
    return inv
#for a given triplet to be sort-able, it is observed that it's inversion count must be an even number. Also the application of the given operation either brings about a reduction of 0 or 2 on the triplet and hence the entire array, i.e., it doesn't effect the even or odd nature of the inversion number
#a sorted array's inversion number is zero. Therefore, an array is sortable by the given operation only if it's inversion number is even(since every operation reduces the number by 2)
t=int(input("Enter the number of test cases: \n"))
for i in range(0,t):
    A = list(map(int, input("Enter the array inputs: \n").rstrip().split()))
    y=count_inv(A)
    if y%2==0:
        print("Yep it's happening")
    else:
        print("Nah, not gonna happen")
    
