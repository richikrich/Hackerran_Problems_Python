#import math

t=int(input("Enter the number of cases: \n"))
for _ in range(t):
    print("Enter the row and column nos. of your main matrix: ")
    [R,C]=list(map(int,input().rstrip().split()))
    print("Enter your main matrix: ")
    G=[]
    for _ in range(R):
        G_item=input().rstrip()
        G.append(G_item)
    print("Enter the row and column nos. of your test matrix: ")
    [r,c]=list(map(int,input().rstrip().split()))
    print("Enter your test matrix: ")
    P=[]
    for _ in range(r):
        P_item=input().rstrip()
        P.append(P_item)

    result='No'
    for i in range(len(G)-len(P)+1):
        
        if result=='No':
            if P[0] in G[i]:
                k=0
                while k<=C-c:
                    if G[i][k:k+c]==P[0]:
                        j=1
                        while j<len(P):
                            if G[i+j][k:k+c]==P[j]:
                                j+=1
                            else:
                                break
                        if j==len(P):
                            result='Yes'
                            break
                        else:
                            k+=1
                    else:
                        k+=1
        else:
            break
        #print(result)
    '''if i==len(G)-1:
        result="No"
    '''
    print(result)
    
           
       
