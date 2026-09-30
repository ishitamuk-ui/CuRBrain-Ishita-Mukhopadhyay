class Solution():
  def sumprod(self):
    n=int(input("enter the number"))
    if(n==0):
       print("invalid")
       return
    sums=0
    prod=1
    while(n>0):
      dig=n%10
      sums+=dig
      prod*=dig
      n=n//10
    diff=prod-sums
    print(diff)

sol=Solution()
sol.sumprod()