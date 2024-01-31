
class QuickSort:
    def partition(self, nums, left, right):

        mid = nums[left]

        while left < right:
            # 右边一直大
            while left < right and nums[right] > mid:
                print("right 需要 降低")
                right -= 1
            nums[left] = nums[right]
            print("右边起的循环结束 nums is {0}, left is {1}, right is {2}".format(nums, left, right))
            # 右边大的循环结束,换左边,一直小
            while left < right and nums[left] <= mid:
                print("left 需要 增加")
                left += 1
            nums[right] = nums[left]
            print("左边起的循环结束 nums is {0}, left is {1}, right is {2}\n".format(nums, left, right))

        # 所有循环结束,left会和right交汇
        nums[left] = mid

        return left


    def quickSort(self, nums, left, right):
        # 特殊情况
        if len(nums) <= 1:
            return nums

        if left >= right:
            return

        index = self.partition(nums, left, right)

        self.quickSort(nums, left, index-1)
        self.quickSort(nums, index+1, right)


if __name__ == '__main__':
    a = [8,7,6,5,6,87,9,2,5,67]
    qs = QuickSort()
    qs.quickSort(a, 0, 9)

    print(a)
