#Q: A queen is standing on an n*n chessboard. The chessboard's rows are numbered from 1 to n, going from bottom to top; its columns are numbered from 1 to n, going from left to right. Each square on the board is denoted by a tuple, (r,c), describing the row, r, and column, c, where the square is located.
#   The queen is standing at position (r_q,c_q)  and, in a single move, she can attack any square in any of the eight directions (left, right, up, down, or the four diagonals).
#   There are k obstacles on the chessboard preventing the queen from attacking any square that has an obstacle blocking the the queen's path to it.
#   Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at (r_q,c_q).

#A:

n=int(input('The dimension of the matrix: \n'))
k=int(input('The number of obstacles: \n'))
r_qC_q=input('The position of the queen: \n').strip().split()
r_q=int(r_qC_q[0])
c_q=int(r_qC_q[1])
obstacles=[]
if k>0:
    print('Enter positions of obstacles: \n')
    for _ in range(k):
        obstacles.append(list(map(int,input().rstrip().split())))

up=((n+1)-r_q-1)
right=((n+1)-c_q-1)
down=((r_q)-1)
left=((c_q)-1)

[r,c]=[r_q,c_q]
while r<n+1 and c>0:
    r+=1
    c-=1
left_up=(r-r_q-1)
[r,c]=[r_q,c_q]
while r<n+1 and c<n+1:
    r+=1
    c+=1
right_up=(r-r_q-1)
[r,c]=[r_q,c_q]
while r>0 and c<n+1:
    r-=1
    c+=1
right_down=(c-c_q-1)
[r,c]=[r_q,c_q]
while r>0 and c>0:
    r-=1
    c-=1
left_down=(abs(r-r_q)-1)


for i,j in obstacles:
    i-=r_q
    j-=c_q
    if j==0:
        if i>0:
            if (i-1)<up:
                up=(i-1)
        else:
            if (abs(i)-1)<down:
                down=(abs(i)-1)
    elif i==0:
        if j>0:
            if (j-1)<right:
                right=(j-1)
        else:
            if (abs(j)-1)<left:
                left=(abs(j)-1)
                
    elif i==j:
        if i>0:
            if (i-1)<right_up:
                right_up=(i-1)
        elif i<0:
            if (abs(i)-1)<left_down:
                left_down=(abs(i)-1)
    elif i==(-j):
        if i>0:
            if (i-1)<left_up:
                left_up=(i-1)
        elif i<0:
            if (j-1)<right_down:
                right_down=(j-1)
print(up)
print(right)
print(down)
print(left)
print(left_up)
print(right_up)
print(right_down)
print(left_down)

    
'''
count_d=[min(n-r_q,c_q-1),min(n-r_q,n-c_q),min(r_q-1,n-c_q),min(r_q-1,c_q-1)]
count_s=[(n-r_q),(n-c_q),(r_q-1),(c_q-1)]

for x,y in obstacles:
    if abs(x-r_q)==abs(y-c_q):
        if (x-r_q)>0 and (y-c_q)<0:
            if (x-r_q)-1<count_d[0]:
                count_d[0]=(x-r_q)-1
        if (x-r_q)>0 and (y-c_q)>0:
            if (x-r_q)-1<count_d[1]:
                count_d[1]=(x-r_q)-1
        if (x-r_q)<0 and (y-c_q)>0:
            if (y-c_q)-1<count_d[2]:
                count_d[2]=(y-c_q)-1
        if (x-r_q)<0 and (y-c_q)<0:
            if abs(x-r_q)-1<count_d[3]:
                count_d[0]=abs(x-r_q)-1
    elif y==c_q:
        if x>r_q:
            if (x-r_q)-1<count_s[0]:
                count_s[0]=(x-r_q)-1
        else:
            if abs(x-r_q)-1<count_s[2]:
                count_s[2]=abs(x-r_q)-1
    elif x==r_q:
        if y>c_q:
            if (y-c_q)-1<count_s[1]:
                count_s[1]=(y-c_q)-1
        else:
            if abs(y-c_q)-1<count_s[1]:
                count_s[1]=abs(y-c_q)-1

print(count_d)
print(count_s)
print('The number of squares it can traverse is: \n {}'.format(sum(count_d)+sum(count_s)))
'''
