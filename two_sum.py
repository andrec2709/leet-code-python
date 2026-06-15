"""
https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    """Solution implementation"""

    def two_sum(self, nums: List[int], target: int) -> List[int] | None:
        """Finds the indices of the first two integers that add up to target
        Args:
            nums: list of integers
            target: the target number the two found numbers need to add up to
        Returns:
            a list of two integers
        """

        # value => index in the array
        cache: dict[int, int] = {}

        for index, num in enumerate(nums):
            diff = target - num
            cached = cache.get(diff)

            if cached is not None:
                return [index, cached]

            cache[num] = index

        return None

def main():
    """Entry point"""
    solution = Solution()
    print(solution.two_sum([2, 2], 4))


if __name__ == "__main__":
    main()
