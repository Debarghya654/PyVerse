class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Count trailing zeroes in n! by counting factors of 5
        TC: O(log₅ n), SC: O(1)
        """
        zeros = 0
        power_of_5 = 5
        
        # Count factors of 5 in numbers 1 to n
        while n >= power_of_5:
            zeros += n // power_of_5  # Numbers divisible by current power of 5
            power_of_5 *= 5           # Move to next power of 5
            
        return zeros

# Alternative implementation with explicit powers:
class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Alternative approach using division by 5
        TC: O(log₅ n), SC: O(1)
        """
        zeros = 0
        
        # Keep dividing n by powers of 5
        while n >= 5:
            n //= 5
            zeros += n
            
        return zeros

# TC: O(log₅ n) - loop runs log₅ n times
# SC: O(1) - constant extra space
