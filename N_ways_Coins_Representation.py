
def coinWays(n,coins) :

    dp=[0]*(n+1)

    dp[0]=1


    for i in range(1,n+1) :

        if i in coins :
            dp[i]=1

        for coin in coins :

            if i>coin :


                if dp[i-coin]!=0 and dp[coin]!=0:
                    dp[i]=max(dp[i-coin],dp[coin])




    return dp[n]

print coinWays(4,[1,2,3])
