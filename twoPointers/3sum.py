# Two pointers implementation of 3sum - we need to find triplets in our array of nums that add up to 0
# First we sort our array, then we break it out into an enum
# Then for each number in the array a we iterate with two "pointers" like in the palindrome example till we find a sum to zero (or not)
# Since the array is sorted, if the sum total of a plus the two numbers pointed either side is greater than zero, we decrement the right side pointer
# likewise if its below zero we increment the left side pointer

def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if a > 0:
            break

        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res
