class Solution:
  def reverse(self):
    arr=[]
    arr1=[]
    n=int(input("enter the no of elements"))
    for i in range(n):
      item=int(input("enter the elemnets"))
      arr.append(item)
      arr1.append(0)
    start=int(input("enter start"))
    end=int(input("enter end"))
    arr1=arr[start:end+1]
    arr1=arr1[::-1]
    for i in range(n):
      if i >= start and i <= end:
        arr[i] = arr1[i - start]
    for i in arr:
      print(i)
sol=Solution()
sol.reverse()