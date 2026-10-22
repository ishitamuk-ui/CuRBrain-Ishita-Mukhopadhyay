class Solution:
    def mod_power(self, base: int, power: int, mod: int) -> int:
        # Start with result = 1 % MOD as required
        result = 1 % mod
        
        # Repeat the multiplication in a loop exactly power times
        for _ in range(power):
            result = (result * base) % mod
            
        return result

if __name__ == "__main__":
    sol = Solution()
    
    # Reading input from user
    base = int(input("Enter base: "))
    power = int(input("Enter power: "))
    mod = int(input("Enter MOD: "))
    
    ans = sol.mod_power(base, power, mod)
    print(f"Result: {ans}")