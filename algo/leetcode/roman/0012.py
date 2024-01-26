"""
数字转罗马数字

针对数值进行切分,按照分位处理
求 %5 结果 和分位数量

"""
import math


class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {1: ["I", "X", "C", "M"], 5: ["V", "L", "D"]}
        # index用来得到mapping位置的
        index = len(str(num)) - 1
        resString = ""

        # 遍历分位
        while index >= 0:
            # 初始化分位的string
            indexString = ""
            print("num is {0}, index is {1}".format(num, index))
            indexNum = int(num//math.pow(10, index))
            print("indexNum is {0}".format(indexNum))

            # 得到indexNum后进行处理,对5取余数,为4则特殊处理
            indexNumMulti = indexNum // 5
            indexNumRemain = indexNum % 5

            # 非4,9处理
            if indexNumRemain < 4:
                indexString = mapping[5][index] + mapping[1][index] * indexNumRemain if indexNumMulti else mapping[1][index] * indexNumRemain
            else:
                # 9
                indexString = mapping[1][index] + mapping[1][index+1] if indexNumMulti else mapping[1][index] + mapping[5][index]

            print("indexString is {0}".format(indexString))

            num = int(num%math.pow(10, index))
            index -= 1
            resString += indexString
            print("resString is {0}\n".format(resString))

        return resString

if __name__ == '__main__':
    sol = Solution()
    x = 3999
    sol.intToRoman(x)