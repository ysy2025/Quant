"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

不同单词可能对应一组char,因此需要hash 首先将每个字符串进行转换,得到对应 hash

然后针对
{
    'eat': {'e': 1, 'a': 1, 't': 1}, 'tea': {'t': 1, 'e': 1, 'a': 1}, 'tan': {'t': 1, 'a': 1, 'n': 1},
    'ate': {'a': 1, 't': 1, 'e': 1}, 'nat': {'n': 1, 'a': 1, 't': 1}, 'bat': {'b': 1, 'a': 1, 't': 1}
    }

需要根据hash进行排序;但是字典是不能hash和排序的

转换成list

然后排序

最后输出
"""

class Solution:
    def order(self, lst):
        # print("beginning lst is {0}, \n lst[0] is {1}, \n key is {2}, value is {3}".format(lst, lst[0], list(lst[0].keys())[0], lst[0]['eat']))
        if len(lst) <= 1:
            return lst

        flagKey = list(lst[0].keys())[0]
        flagValue = lst[0][flagKey]

        left = []
        right = []
        for each in lst:
            key = list(each.keys())[0]
            value = each[key]

            if value == flagValue:
                left.append(each)
            else:
                right.append(each)

        return left + self.order(right)

    def getStrMap(self, strs):
        res = {}
        for str in strs:
            res[str] = res.get(str, 0) + 1

        return res
    def groupAnagrams(self, strs):

        if len(strs) <= 1:
            print("at last is {0}".format(strs))
            return [strs]

        # 针对str得到hash
        strsMap = {}
        for str in strs:
            strsMap[str] = self.getStrMap(str)

        # 对hash转换成list
        strsMapList = []
        for k,v in strsMap.items():
            strsMapList.append({k:v})

        strsMapListSorted = self.order(strsMapList)

        # print("sorted list is {0}".format(strsMapListSorted))

        res = []

        if len(strsMapListSorted) == 0:
            res.append("")
        if len(strsMapListSorted) == 1:
            key = list(strsMapListSorted[0].keys())[0]
            res.append(key)
        else:
            temp = []
            length = len(strsMapListSorted)-1
            for i in range(length):
                key1 = list(strsMapListSorted[i].keys())[0]
                value1 = strsMapListSorted[i][key1]

                key2 = list(strsMapListSorted[i+1].keys())[0]
                value2 = strsMapListSorted[i+1][key2]

                print(key1, value1, key2, value2)
                if value1 == value2:
                    temp.append(key1)
                else:
                    temp.append(key1)
                    res.append(temp)
                    temp = []
            if temp != []:
                res.append(temp)
            # print("now res is {0}".format(res))
            # 最后一个怎么处理
            key1 = list(strsMapListSorted[length-1].keys())[0]
            value1 = strsMapListSorted[length-1][key1]

            key2 = list(strsMapListSorted[length].keys())[0]
            value2 = strsMapListSorted[length][key2]

            if value1 == value2:
                res[-1].append(key2)
            else:
                res.append([key2])

        # print("at last is {0}".format(res))
        return res


class Solution2:
    def groupAnagrams(self, strs):
        # 首先每个单词排序
        strsList = [''.join(sorted(list(each))) for each in strs]
        print("strsList is {0}".format(strsList))
        resDict = {}
        for i in range(len(strsList)):
            key = strsList[i]
            value = strs[i]
            resDict[key] = resDict.get(key, [])
            print(resDict[key])
            resDict[key].append(value)

        res = []

        for key, value in resDict.items():
            res.append(value)

        return res


    pass
if __name__ == '__main__':
    pass
    sol = Solution2()
    strs = ["yes", 'sey']
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = [""]

    print(sol.groupAnagrams(strs))

    # print(sol.getStrMap(strs))