class solution:
  def abs(self):
    n=int(input("enter the no of elemenst"))
    arr=[]
    for i in range(n):
      ele=int(input("enter the elements"))
      arr.append(ele)
    min=arr[0]

    for i in arr:
      if(abs(i)<abs(min)):
        min=i

    print(min)

sol=solution()
sol.abs()