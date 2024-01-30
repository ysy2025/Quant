# 进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？

"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n - 1
        i, j = m - 1, n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

作者：ylb
链接：https://leetcode.cn/problems/merge-sorted-array/solutions/2385623/python3javacgotypescript-yi-ti-yi-jie-sh-8wja/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 特殊情况
        if m == 0:
            nums1 = nums2
        elif n == 0:
            nums1 = nums1
        # 初始化
        else:
            left = nums1[:m]
            right = nums2
            nums1 = [0 for each in nums1]

            print("left is {0} and right is {1}".format(left, right))

            # 双指针
            while m and n:
                # 左大于右
                if left[m - 1] >= right[n - 1]:
                    nums1[m +n - 1] = left[m - 1]
                    m -= 1
                    print("左大于右, nums1 是{0}".format(nums1))
                else:
                    nums1[m + n - 1] = right[n - 1]
                    n -= 1
                    print("左小于右, nums1 是{0}".format(nums1))

            # 最后剩下的
            temp = left[:m] + right[:n]
            lenRemain = m + n
            print("temp is {0}, lenRemain is {1}".format(temp, lenRemain))
            nums1 = temp + nums1[lenRemain:]
            print(nums1)


if __name__ == '__main__':
    nums1 = [2, 4, 0, 0, 0]
    m = 2
    nums2 = [1,2, 34]
    n = 3

    sol = Solution()

    a = [6, 5, 4, 7, 3, 4, 2, 23]

    mid = a[0]
    left = [each for each in a if each <= mid]

    # print(sol.sortList(a))

sol.merge(nums1, m, nums2, n)