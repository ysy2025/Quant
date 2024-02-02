"""

给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

默认悲观,达不到最后;

如果中间有值可以超过length,递归

"""
class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return True

        # 贪心,得到每个数能跳到最远的索引 [2, 4, 3, 4, 8]
        greedy = [None] * len(nums)
        for i in range(len(nums)):
            greedy[i] = i + nums[i]
        print("after greedy is {0}".format(greedy))

        # 长度, 索引, 步数
        length = len(nums) - 1
        index = 0
        print("beginning ==> length is {0} index is {1} greedy[index] is {2}\n".format(length, index, greedy[index]))

        # 逆序,遍历,如果知道最后都不大于len,则达不到
        while index < length:
            if greedy[index] >= length:
                print("可以跳到尾巴了, 截取为 {0}".format(nums[:index+1]))
                return self.jump(nums[:index+1])
            index += 1
        # 到了最后一个才满足条件
        else:
            return False

        # while index:
        #     # print("now index is {0} and length is {1} greedy[index] is {2}".format(index, length, greedy[index]))
        #     if greedy[index] >= length:
        #         return self.jump(nums[:index+1])
        #     # [1,2,0,2] 这种,逆序,到了0,继续减
        #     else:
        #         index -= 1
        # # 默认悲观,达不到最后;到了最后一个才满足条件
        # return False



class Solution2:
    """
    尽可能到达最远位置（贪心）。
如果能到达某个位置，那一定能到达它前面的所有位置。
初始化最远位置为 0，然后遍历数组，如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置。最后比较最远位置和数组长度。
    """

    def canJump(self, nums):
        # if len(nums) <= 1:
        #     return True

        max_i = 0  # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
            if max_i >= i and i + jump > max_i:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + jump  # 更新最远能到达位置

            print("i is {0} max_i is {1}".format(i, max_i))

        return max_i >= len(nums)-1

if __name__ == '__main__':
    # nums = [3,0,8,2,0,0,1]
    # nums = [1,1]
    # nums = [1,1,1,0,0]
    # nums = [2,0,0]
    nums = [0]
    # sol = Solution()
    # print(sol.jump(nums))
    sol = Solution2()
    print(sol.canJump(nums))