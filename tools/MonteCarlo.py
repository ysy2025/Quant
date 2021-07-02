from abc import ABCMeta, abstractmethod
import six
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

    def do_seek_days(self):
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

#

    # 具体的追求方向
