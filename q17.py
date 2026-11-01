class Solution :
  def product(self):
    sales=[]
    n= int(input("enter the no of product ids"))
    for i in range(n):
      sales.append(int(input("enter")))
      freq={}
    for item in sales:
      freq[item]=freq.get(item,0)+1
    max=min(freq.keys(),key=lambda x:(-freq[x],x))
    return max

sol=Solution()
res=sol.product()
print(res)