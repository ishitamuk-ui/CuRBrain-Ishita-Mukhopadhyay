class Solution:
  def even(self):
    n=int(input("enter the number"))
    arr=[]
    l=0
    while(n>0):
      dig=n%10
      l+=1
      if(dig%2==0):
        arr.append(0)
      else:
        arr.append(dig)
      n=n//10
    for i in range(l-1,-1,-1):
      print(arr[i],end=" ")
sol=Solution()
sol.even()
