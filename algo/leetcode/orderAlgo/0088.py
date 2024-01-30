"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

"""

class Solution:
    def sortList(self, listIn):
        # 长度不够
        if len(listIn) <= 1:
            return listIn
        # 只有两个元素
        elif len(listIn) == 2:
            return [listIn[1], listIn[0]] if listIn[0] > listIn[1] else listIn
        else:
            mid = listIn[0]
            left = [each for each in listIn[1:] if each <= mid]
            right = [each for each in listIn[1:] if each > mid]

            return self.sortList(left) + [mid] + self.sortList(right)



    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 特殊情况
        if m == 0:
            return nums2
        if n == 0:
            return nums1

        # 简单方法
        print(nums1[:m])
        res = nums1[:m] + nums2
        # 给res 排序
        res = self.sortList(res)

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    sol = Solution()

    a = [6,5,4,7,3,4,2,23]

    mid = a[0]
    left = [each for each in a if each <= mid]

    # print(sol.sortList(a))

    print(sol.merge(nums1, m, nums2, n))
