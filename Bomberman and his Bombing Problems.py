'''
Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.
Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds.
Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells.
This means that if a bomb detonates in cell (i,j), any valid cells (i+-1,j) and (i,j+-1) are cleared. If there is a bomb in a neighboring cell,
the neighboring bomb is destroyed without detonating, so there's no chain reaction.
Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:
1.Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
2.After one second, Bomberman does nothing.
3.After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
4.After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
5.Bomberman then repeats steps 3 and 4 indefinitely.
Note that during every second Bomberman plants bombs, the bombs are planted simultaneously (i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.
Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine the state of the grid after N seconds.
'''
def blast(grid,zeros):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='O':
                if len(grid)==1:
                    zeros[i][j]='.'
                    if j!=0: zeros[i][j-1]='.'
                    if j!=len(grid[i])-1: zeros[i][j+1]='.'
                else:
                    if i==0:
                        zeros[i][j]='.'
                        zeros[i+1][j]='.'
                        if j!=0: zeros[i][j-1]='.'
                        if j!=len(grid[i])-1: zeros[i][j+1]='.'
                    elif i==len(grid)-1:
                        zeros[i][j]='.'
                        zeros[i-1][j]='.'
                        if j!=0: zeros[i][j-1]='.'
                        if j!=len(grid[i])-1: zeros[i][j+1]='.'
                #zeros[i-1]=''.join(zeros[i-1])
                #zeros[i]=''.join(zeros[i])
                    else:
                        zeros[i][j]='.'
                        zeros[i+1][j]='.'
                        zeros[i-1][j]='.'
                        if j!=0: zeros[i][j-1]='.'
                        if j!=len(grid[i])-1: zeros[i][j+1]='.'
                #zeros[i-1]=''.join(zeros[i-1])
    return zeros

print("Input:\n 1. No. of rows \n 2. No. of rows \n 3. Time in secs ")
rcn=input().rstrip().split()
r=int(rcn[0])
c=int(rcn[1])
n=int(rcn[2])

grid=[]
#print(zeros)
print("Input grid: ")
for _ in range(r):
    g=list(input().rstrip())
    grid.append(g)

if n<2:
    result=grid
elif n%2==0:
    result=[['O'for i in range(c)]for j in range(r)]
elif n==(((int((n-3)/4))*4)+3):
    zeros=[['O'for i in range(c)]for j in range(r)]
    result=blast(grid,zeros)
else:
    for i in range(2):
        zeros=[['O'for i in range(c)]for j in range(r)]
        grid=blast(grid,zeros)
    result=grid
for i in range(len(result)):
    result[i]=''.join(result[i])

print('\n'.join(result))
'''
print(grid)
print(zeros)
'''

    
    
