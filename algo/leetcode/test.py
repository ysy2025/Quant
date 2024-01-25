class Solution:
    def getMaxLength(self, strings):
        # Step 1: 定义需要维护的变量们 (对于滑动窗口类题目，这些变量通常是最小长度，最大长度，或者哈希表)
        maxLength = 0
        hashMap = {}

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(strings)):
            # Step 3: 更新需要维护的变量, 有的变量需要一个if语句来维护 (比如最大最小长度)
            # i.e. 把窗口末端元素加入哈希表，使其频率加1，并且更新最大长度
            hashMap[strings[end]] = hashMap.get(strings[end], 0) + 1
            print("now strings[end] is {0}, and hashMap is {1}".format(strings[end], hashMap))

            # 窗口长度等于哈希表的时候说明没有重复元素
            if len(hashMap) == end - start + 1:
                print("now now now  strings[end] is {0}, and hashMap is {1}".format(strings[end], hashMap))
                maxLength = max(maxLength, end - start + 1)
                print("这个时候，maxlength is {0}".format(maxLength))

            # Step 4:
            # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
            # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashMap)
            while end - start + 1 > len(hashMap):
                print("额哦不好意思有重复元素了 strings[end] is {0}, and hashMap is {1}".format(strings[end], hashMap))
                head = strings[start]
                hashMap[head] -= 1
                print("处理完毕，strings[end] is {0}, and hashMap is {1}".format(strings[end], hashMap))
                if hashMap[head] == 0:
                    del hashMap[head]
                start += 1

        return maxLength

if __name__ == '__main__':
    solution = Solution()

    a = "zzzz"
    solution.getMaxLength(a)