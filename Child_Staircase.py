import sys


def childStepWays(stairs) :

    if stairs==0 : return 0

    dp=[0]*(stairs+1)
    dp[1]=1
    dp[2]=2

    i=3

    while i<=stairs :

        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

        i+=1

    return dp[stairs]

stairs=int(sys.stdin.readline().strip())

print childStepWays(stairs)        
