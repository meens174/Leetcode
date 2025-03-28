import pandas as pd

class Solution(object):
    def maxProfit(self, prices):
        diff_set={}
        df=pd.DataFrame(columns=['buy', 'sell', 'diffs'])
        lnp=len(prices)
        # print(lnp)
        for i in range(0,lnp ):
            
            for j in range(i+1, lnp):
                if prices[i]<prices[j]:
                    print(prices[j]-prices[i])
                    diff_set={'buy':i,'sell':j,'diffs': prices[j]-prices[i]}
                    df=df.append(diff_set, ignore_index=True)
                
        result=df.diffs.max()
        # print("Result=", df.head())
        return result    


        
def main():
    sol=Solution()
    res=sol.maxProfit([7,1,5,3,6,4])
    print(res)

if __name__ == '__main__':
    main()


          

     