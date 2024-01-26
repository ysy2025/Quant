"""
例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。

如何处理4和9的判断最关键;核心在于,1右边的字符串,要么index不对,要么key不对;
一个罗马字符,分解为 key,index 3个属性,然后去判断即可

"""
import math


class Solution:
    def romanToInt(self, s: str):
        mapping = {1: ["I", "X", "C", "M"], 5: ["V", "L", "D"]}
        length = len(s)

        key = []
        index = []
        value = []

        # 进行key和index的转换
        for i in range(length):
            string = s[i]
            mapKey = 1 if string in mapping[1] else 5
            key.append(mapKey)
            index.append(mapping[mapKey].index(string))
        print("key is {0}".format(key))
        print("index is {0}".format(index))
        print(list(s))
        print("\n")

        # 继续遍历一次,取值并判断;设置起点
        start = 0
        while start+1 <= (length - 1):
            print("=========> start is {4} key[start]{0}, key[start+1]{1}, index[start]{2}, index[start+1]{3}".format(key[start], key[start-1], index[start], index[start-1], start))
            # 是4或者9
            if (index[start] < index[start+1]) or (index[start] == index[start+1] and key[start] < key[start+1]):
                value.append(int(key[start+1] * math.pow(10, index[start+1]) - key[start] * math.pow(10, index[start])))
                print('now value is {0}'.format(value))
                start += 2
            else:
                value.append(int(key[start] * math.pow(10, index[start])))
                print("now value is {0}".format(value))
                start += 1
        print("now start is {0}".format(start))
        if start <= length - 1:
            value.append(int(key[start] * math.pow(10, index[start])))
        print(value)
        return sum(value)
if __name__ == '__main__':
    roman = "CCXCIII"
    sol = Solution()
    print(sol.romanToInt(roman))