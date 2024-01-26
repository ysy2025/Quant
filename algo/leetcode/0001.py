"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""
class Solution:
    def quickSort(self, nums):
        if len(nums) <= 1:
            return nums

        if len(nums) == 2:
            left = nums[0]
            right = nums[1]
            return [left, right] if left <= right else [right, left]
        else:
            mid = nums[0]
            left = [i for i in nums[1:] if i <= mid]
            right = [i for i in nums[1:] if i > mid]

            # print(left, right)
            # print(left + [mid] + right)
            return self.quickSort(left) + [mid] + self.quickSort(right)

    # 二分法查询
    def findORderedBySplit(self, nums, target):
        if len(nums) == 0:
            # raise Exception("sorry but no num in list")
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 1
            else:
                # raise Exception("sorry but we can not find target")
                return -1
        elif len(nums) == 2:
            if nums[0] == target:
                return 1
            elif nums[1] == target:
                return 1
            else:
                return -1
        else:
            if (target < nums[0]) or (target > nums[-1]):
                return -1
            else:
                length = len(nums)

                left = 0
                right = length - 1
                mid = length // 2

                while left + 1 < right:
                    # print("left is {0} and right is {1}".format(left, right))
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] < target:
                        left = mid
                        mid = (left + right) // 2
                    elif nums[mid] > target:
                        right = mid
                        mid = (left + right) // 2

                return 1 if (nums[left] == target or nums[right] == target) else -1

    # 首先快排,nlogn
    def twoSum(self, nums, target):
        print("|hello world and nums is {0}".format(nums))
        # 找到剩余值
        remains = [target - i for i in nums]
        print("remains is {0}".format(remains))
        # 初始化flag
        targetList = []

        # 遍历,叠加二分法查询,nlogn
        for i in range(len(remains)):
            temp = nums[:i] + nums[i+1:]
            orderedNums = self.quickSort(temp)
            print("i is {0} , and remain [i] is {1} and nums is {2} and temp is {3} and orderedNums is {4}".format(i, remains[i], i, nums, temp, orderedNums))
            if self.findORderedBySplit(orderedNums, remains[i]) == 1:
                print("nums is {0}, remain is {1}, index is {2}".format(nums, remains[i], nums.index(remains[i])))
                targetList.append(i)

        return targetList

if __name__ == '__main__':
    solution = Solution()

    nums = [3,3]
    target = 6
    res = solution.twoSum(nums, 6)
    print(res)

    # print(solution.findORderedBySplit([3, 12, 21, 45], 6))
if __name__ == '__main__':
    pass
    # nums = [2,7,11,15]
    # target = 9
    #
    # res = twoSum(nums, target)
    # print(res)

    # nums = [8,3,1,2,4,6,77]
    # print(quickSort(nums))
    # # quickSort(nums)
    #
    # sortedNums = quickSort(nums)
    #
    # print(findORderedBySplit(sortedNums, 5))