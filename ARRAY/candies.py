class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        target = max(candies)
        for child in candies:
            if child + extraCandies >= target:
                result.append(True)
            else:
                result.append(False)
        return result