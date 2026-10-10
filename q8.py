class Solution:
  def factors(self):
    arr=[]
    n=int(input("enter the number"))
    k=int(input("enter the constraint"))
    for i in range(1,n+1):
      if(n%i==0):
        arr.append(i)
    if len(arr)<k:
      return -1
    else:
     return(arr[k-1])

sol=Solution()
print(sol.factors())
