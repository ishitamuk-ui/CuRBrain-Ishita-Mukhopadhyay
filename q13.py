import ast

class Solution:
    def checkPrefixDivisible(self, arr: list[int], k: int) -> bool:
        # An empty array has no prefix values and returns False
        if not arr:
            return False
            
        # Use absolute value of k for consistent results across languages
        k = abs(k)
        
        running_sum = 0
        for num in arr:
            running_sum += num
            # Check if running prefix sum modulo k equals 0
            if running_sum % k == 0:
                return True
                
        return False


def parse_array_input(user_input: str) -> list[int]:
    """Parses list inputs, brackets, or space/comma separated numbers."""
    user_input = user_input.strip()
    if not user_input or user_input == "[]":
        return []
    try:
        parsed = ast.literal_eval(user_input)
        if isinstance(parsed, list):
            return parsed
    except Exception:
        pass
    cleaned = user_input.replace("[", "").replace("]", "").replace(",", " ")
    return [int(x) for x in cleaned.split()]


if __name__ == "__main__":
    sol = Solution()
    
    raw_arr = input("Enter array (e.g. [3, 1, 4, 2]): ")
    k_val = int(input("Enter k: "))
    
    arr = parse_array_input(raw_arr)
    result = sol.checkPrefixDivisible(arr, k_val)
    print(f"Result: {result}")