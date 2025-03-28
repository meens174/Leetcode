# import pandas as pd

class Solution(object):
    def maxProfit(self, prices):
        union_set={'buy':[],'sell':[],'diffs':[]}
        diff_set={}
        # df=pd.DataFrame(columns=['buy', 'sell', 'diffs'])
        lnp=len(prices)
        
        for i in range(0,lnp ):
            
            for j in range(i+1, lnp):
                if prices[i]<prices[j]:
                    
                    diff_set={'buy':i,'sell':j,'diffs': prices[j]-prices[i]}
                    union_set['buy'].append(diff_set['buy'])
                    union_set['sell'].append(diff_set['sell'])
                    union_set['diffs'].append(diff_set['diffs'])
        # print(union_set)
                    # df=df.append(diff_set, ignore_index=True)
        if len(union_set['diffs']) == 0 :
            print("Empty Set")   
            result=0
        else:
            print(len(union_set))
            result=max(union_set['diffs'])
            return result    


        
def main():
    sol=Solution()
    res=sol.maxProfit([7,1,5,3,6,4])
    print(res)

if __name__ == '__main__':
    main()


          

     