from abc import ABCMeta, abstractmethod
import six
import numpy as np
import pandas as pd

"""
6是一个Python 2和3兼容库它提供实用功能 为了消除python版本之间的差异 编写在两个python版本上都兼容的python代码
"""
k_initial_living_days = 27375


class Person(object):
    def __init__(self):
        self.living = k_initial_living_days
        self.happiness = 0
        self.wealth = 0
        self.fame = 0
        self.living_days = 0
        """
        lving = 寿命
        happiness = 幸福
        wealth = 财富
        fame = 权力
        living_days = 生命的第几天
        """
    def living_one_day(self, seek):
        """
        每天追寻的东西,seek,决定你得到什么
        :param seek:
        :return:
        """

        # 调用每个BasekSeekDay,都会实现do_seek_day,得到今天的收获
        consume_living, happiness, wealth, fame = seek.do_seek_day()
        # 每天减去生命消耗,有的seek前面还会增加生命
        self.living -= consume_living
        # 幸福累计etc

        self.happiness += happiness
        self.wealth += wealth
        self.fame += fame

        self.living_days += 1

class BaseSeekDay(six.with_metaclass(ABCMeta, object)):
    def __init__(self):
        #每个追求每天消耗的生命的常数
        self.consume_living_base = 0
        # 每个追求每天消耗的快乐的常数
        self.happiness_base = 0
        # 每个追求每天消耗的财富的常数
        self.wealth_base = 0
        # 每个追求每天消耗的权力的常数
        self.fame_base = 0
        # #每个追求每天消耗的生命的可变因素序列
        self.consume_living_factor = [0]
        # #每个追求每天消耗的幸福的可变因素序列
        self.happiness_factor = [0]
        # #每个追求每天消耗的财富的可变因素序列
        self.wealth_factor = [0]
        # #每个追求每天消耗的权力的可变因素序列
        self.fame_factor = [0]
        # 这一生,追求了多少天了?
        self.do_seek_day_cnt = 0
        self._init_self()

    @abstractmethod
    def _init_self(self, *args, **kwargs):
        # 抽象方法,子类必须实现
        pass
    @abstractmethod
    def _gen_living_days(self, *args, **kwargs):
        pass

    def do_seek_day(self):
        """
        每天的追求
        :return:
        """
        # 生命的消耗 = consume_living_base * consume_living_factor;这里获取消耗的生命力 consume_living
        # 超过living_factor,取最后一个
        if self.do_seek_day_cnt >= len(self.consume_living_factor):
            # consume_living,追求所消耗的生命
            consume_living = self.consume_living_factor[-1] * self.consume_living_base
        else:
            # 每个类,自定义这个追求的消耗生命常数,比如追求健康,那么living_factor的序列的值为负值->正值
            # 每个子类的livingfactor不同,导致每个追求对生命的消耗随着追求的次数变化不一
            consume_living = self.consume_living_factor[self.do_seek_day_cnt] * self.consume_living_base

        # 幸福指数= happiness_base * happiness_factor;同样存在幸福因子,如果超过序列,就取最后一个
        # happiness_factor,由n->0,所以追求次数越多,幸福感越低
        if self.do_seek_day_cnt >= len(self.happiness_factor):
            self.happiness_factor[-1] = 0
            happiness = self.happiness_factor[-1] * self.happiness_base
        else:
            # 每个类自定义追求的幸福指数常数和happiness_factor
            happiness = self.happiness_factor[self.do_seek_day_cnt] * self.happiness_base

        # 财富积累 wealth = wealth_base * wealth_factor
        if self.do_seek_day_cnt >= len(self.wealth_factor):
            # 获取的财富
            wealth = self.wealth_factor[-1] * self.wealth_base
        else:
            # 每个类,自定义这个追求的财富积累常数常数
            # 每个子类的 factor 不同,导致每个追求对财富的积累随着追求的次数变化不一
            wealth = self.wealth_factor[self.do_seek_day_cnt] * self.wealth_base
        
        # 权力积累 fame = fame_base * fame_factor
        if self.do_seek_day_cnt >= len(self.fame_factor):
            # 获取的权力
            fame = self.fame_factor[-1] * self.fame_base
        else:
            # 每个类,自定义这个追求的权力积累常数常数
            # 每个子类的 factor 不同,导致每个追求对权力的积累随着追求的次数变化不一
            fame = self.fame_factor[self.do_seek_day_cnt] * self.fame_base

        # 追求了多少天
        self.do_seek_day_cnt += 1
        # 返回追求的结果,生命,幸福,财富,权力
        return consume_living, happiness, wealth, fame

#常规操作
def regular_mm(group):
    # 最小-最大规范化
    return (group-group.min())/(group.max() - group.min())

# 具体的追求方向
class HealthSeekDay(BaseSeekDay):
    """
    追求健康长寿每一天
    形象:健身,旅游,娱乐,做感兴趣的事情
    抽象:追求健康长寿
    """
    def _init_self(self):
        #每天消耗生命常数=1
        self.consume_living_base = 1
        # 每天幸福指数常数 = 1
        self.happiness_base = 1
        # 设定可变因素序列
        self._gen_living_days()
    def _gen_living_days(self):
        """
        只生成12000个序列,因为下面的happiness_factor序列由1-0
        即,随着做一件事的次数越来越多,幸福感越来越低,知道完全体会不到幸福
        :return:
        """
        # 基础函数用sqrt
        days = np.arange(1, 12000)
        living_days = np.sqrt(days)
        """
        对什么消耗可变因素由-1->1,也就是这个追求一开始的时候对生命的消耗为负增长,延长寿命;
        随着追求次数增加,对生命消耗转正,毕竟再延年益寿也会gg
        """
        # *2-1的目的:regular_mm在0-1之间,HealthSeekDay要结果在-1到1之间
        self.consume_living_factor = regular_mm(living_days) *2 -1
        # 结果在1-0之间,[::-1],将0-1转换到1-0
        self.happiness_factor = regular_mm(days)[::-1]


class StockSeekDay(BaseSeekDay):
    """
    追求财富的一天
    """
    def _init_self(self):
        # 每天对生命的消耗为2
        self.consume_living_base = 2
        # 每天幸福指数常数= 1/2
        self.happiness_base = 0.5
        # 每天财富积累 = 10
        self.wealth_base = 10
        # 可变因素
        self._gen_living_days()
    def _gen_living_days(self):
        days = np.arange(1, 10000)
        #针对生命消耗的基础函数是sqrt
        living_days = np.sqrt(days)
        #不需要像HealthSeekDays从负数开始,直接从0-1
        self.consume_living_factor = regular_mm(living_days)
        # 幸福感,变化速度比sqrt快,用np.power4
        happiness_days = np.power(days, 4)
        # 幸福指数可变因素快速锐减
        self.happiness_factor = regular_mm(happiness_days)[::-1]
        # wealth_factor = living_factor;living_factor=0-1,因此wealth_factor=0-1,积累到后面越有效率,速度越快
        self.wealth_factor = self.consume_living_factor

class FameSeekDay(BaseSeekDay):
    """
    追求权力的一天
    """
    def _init_self(self):
        # 每天消耗3天生命
        self.consume_living_factor = 3
        # 幸福常数= 0.6
        self.happiness_factor = 0.6
        # 权力积累常数=10
        self.fame_base = 10
        #设定可变因素序列
        self._gen_living_days()
    def _gen_living_days(self):
        # 只产生12000个序列
        days = np.arange(1,12000)
        #针对生命消耗 living_factor的基础函数还是sqrt
        living_days = np.sqrt(days)
        # 直接regular_mm
        self.consume_living_factor = regular_mm(living_days)
        # 幸福感可变序列,np.power()
        # 变化速度比StockSeekDay慢,比HealthSeekDay快
        happiness_days = np.power(days, 2)
        # 幸福指数可变银子递减
        self.happiness_factor = regular_mm(happiness_days)
        # fame_factor = living_factor
        fame_factor = self.consume_living_factor

def my_life(weights):
    """
    追求健康长寿快乐的权重:weights[0]
    追求财富金钱的权重:weights[1]
    追求权力的权重:weights[2]
    :param weights:追求的生活的权重
    :return:
    """

    #追求健康长寿
    seek_health = HealthSeekDay()
    #追求财富金钱
    seek_stock = StockSeekDay()
    #追求权力之路
    seek_fame = FameSeekDay()

    # 放在一个list下面,对应下面np.random.choice()函数中的index[0,1,2]
    seek_list = [seek_health, seek_stock, seek_fame]

    # 初始化 me
    me = Person()

    # 加权随机抽取
    seek_choice = np.random.choice([0,1,2], 80000, p = weights)

    #活着
    while me.living > 0:
        # 追求从加权随机抽取序列已经初始化好了;每一天追求的已经由加权随机抽取确定了
        seek_ind = seek_choice[me.living_days]
        seek = seek_list[seek_ind]
        me.living_one_day(seek)

    return round(me.living_days/365, 2), round(me.happiness, 2), me.wealth, me.fame

if __name__ == '__main__':
    living_days, happiness, wealth, fame = my_life([0.3,0.4,0.3])
    print(living_days, happiness, wealth, fame)

    # # 初始化一个人
    # me = Person()
    # # 追求健康长寿
    # seek_health = HealthSeekDay()
    # # 只要还活着,就追求健康
    # while me.living > 0:
    #     me.living_one_day(seek_health)
    #     print("追求健康,能活多久,幸福多少,财富多少,权力多少")
    #     print(round(me.living_days/365, 2), round(me.happiness, 2), me.wealth, me.fame)

    # zhangsan = Person()
    # seek_wealth = StockSeekDay()
    #
    # while zhangsan.living > 0:
    #     zhangsan.living_one_day(seek_wealth)
    #     print("追求健康,能活多久,幸福多少,财富多少,权力多少")
    #     print(round(zhangsan.living_days/365, 2), round(zhangsan.happiness, 2), zhangsan.wealth, zhangsan.fame)

    # lisi = Person()
    # seek_fame = FameSeekDay()
    #
    # while lisi.living > 0:
    #     lisi.living_one_day(seek_fame)
    #     print("追求健康,能活多久,幸福多少,财富多少,权力多少")
    #     print(round(lisi.living_days/365, 2), round(lisi.happiness, 2), lisi.wealth, lisi.fame)

