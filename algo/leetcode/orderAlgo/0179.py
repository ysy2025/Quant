"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：

输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"

"""


def exchangOrder(a):
    length = len(a)
    index = 0
    print("beginning a is {0}".format(a))
    for i in range(length):
        for j in range(length-i-1):
            print("i is {0} and a[i] is {1} j is {2} and a[j] is {3}".format(i, a[i], j, a[j]))
            index += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

        print("now a is {0}".format(a))
        print(index)

def bubble_sort(demo:list):
    length = len(demo)
    for i in range(length):
        print("*"*30)
        for j  in range(length-i-1):
            if demo[j] > demo[j+1]:
                demo[j],demo[j+1] = demo[j+1], demo[j]
        print('{}次:'.format(i),demo)
    print("最终排序：",demo)


"""
本题目实际上是排序的变种
第一个字符比,大的在前;
第一个字符相同的,看第二个字符;(没有第二个的默认第二个是inf.max)


两个数字对应的字符串a和b，如果字典序a+b>b+a，此时a排在b的前面即可获得更大值
示例：a=3,b=32,两者拼接的值：332>323，所以3应排在32前面

作者：追风少年
链接：https://leetcode.cn/problems/largest-number/solutions/717342/python3-san-chong-fang-fa-qiu-zui-da-shu-cpi4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
class Solution:
    def compareString(self, listA, listB):
        # 双指针
        left = listA
        right = listB
        lenLeft = len(listA)
        lenRight = len(listB)
        while len(left) and len(right):
            # 大于
            if left[0] > right[0]:
                return 1
            # 小于
            if left[0] < right[0]:
                return 0
            else:
                # 切片,丢掉前面的字符
                left = left[1:]
                right = right[1:]
        # 针对剩余的进行比较
        if lenRight> lenLeft:
            print(listA, listB[lenLeft:])
            return self.compareString(listA, listB[lenLeft:])
        if lenLeft > lenRight:
            print(listA[lenRight:], listB)
            return self.compareString(listA[lenRight:], listB)
        # 等于也返回1
        return 1

    def exchangOrderConcat(self, a):
        length = len(a)
        print("beginning a is {0}".format(a))
        for i in range(length):
            for j in range(length-i-1):
                print("j is {0} and a[j] is {1} j+1 is {2} and a[j+1] is {3}".format(j, a[j], j+1, a[j+1]))
                # 按照字符来比;得到两个字符
                left = str(a[j])
                right = str(a[j+1])
                # 左边小于右边
                if not self.compareString(left, right):
                    a[j],a[j+1] = a[j+1], a[j]

        # 最后针对000000这种进行处理
        index = 0
        for i in range(len(a)):
            if a[i] == 0:
                index += 1
            else:
                break
        a = a[index:] if index < len(a) else [0]

        return ''.join([str(each) for each in a])



if __name__ == '__main__':
    # nums = [3,30,34,5,9]
    # nums = [10, 2]

    nums = [999999991,9]
    sol = Solution()
    print(sol.exchangOrderConcat(nums))

    a = '99999991'
    b = '9'
    # sol.compareString(a, b)