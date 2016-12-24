import sys

def robot_movement(grid) :

    dp=[]

    for i in range(0,len(grid[0])+1) :
        dp.append([0]*len(grid))

    m=len(grid[0])-1
    n=len(grid)-1

    i=m
    j=n


    while i>=0 :

        j=len(grid)-1
        while j>=0  :

            if grid[i][j]==1 :
                j-=1
                continue

            if i==m and j==n :
                dp[i][j]=1

            elif i==m :
                dp[i][j]=dp[i][j+1]

            elif j==n :
                dp[i][j]=dp[i+1][j]

            else :
                dp[i][j]=dp[i][j+1]+dp[i+1][j]

            j-=1

        i-=1


    return dp[0][0]


grid=[[0,0,0],
  [0,1,0],
  [0,0,0]]

print robot_movement(grid)
