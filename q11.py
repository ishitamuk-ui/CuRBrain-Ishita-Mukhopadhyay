class Solution:
  mod=10**9+7
  def modsum(self, arr: list[int], mod: int = mod) -> int:
        total = 0
        for num in arr:
            total = (total + num) % mod
        return total

user_input = input("Enter integers separated by spaces: ")
arra = list(map(int, user_input.strip().split()))

sol = Solution()
print(sol.modsum(arra))