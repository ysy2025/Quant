import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
伯努利分布,离散分布
numpy.random.binomial(1,p)获取1的概率为p的前提下生成的随机便利
"""
if __name__ == '__main__':
    """
    如何在交易中获取优势地位?
    交易中,交易者永远是不利的,需要交手续费(抽水)
    实现函数casino,加入100个赌徒,if每个有100w,每个人都想在赌场玩1000w次;不同胜率,赔率和手续费下,casino函数如下
    """
    gamblers = 100
    def casino(win_rate, win_once = 1, loss_once = 1, commission = 1):
        """
        假设每个赌徒100w,每个赌徒想玩1000w次
        :param win_rate:胜率
        :param win_once: 每次赢多少钱
        :param loss_once: 每次输多少钱
        :param commission: 手续费,0.01,1%
        :return:
        """
        my_money = 1000000
        play_cnt = 10000000
        commission = commission
        for _ in np.arange(0, play_cnt):
            # 使用伯努利分布,根据win_rate来获取输赢
            w = np.random.binomial(1, win_rate)
            # 如果赢了
            if w:
                my_money += win_once
            # 如果输了
            else:
                my_money -= win_once
            # 钱输光了
            if my_money <= 0:
                break
        return my_money

    # 天堂赌场,胜率0.5,没有手续费,赔率1
    heaven_moneys = [casino(0.5, commission=0) for _ in np.arange(0, gamblers)]
    # 有老千,胜率0.4
    cheat_moneys = [casino(0.4, commission= 0) for _ in np.arange(0, gamblers)]
    # 没有老千,有手续费
    commission_money = [casino(0.5, commission=0.01) for _ in np.arange(0, gamblers)]

    _ = plt.hist(heaven_moneys, bins = 30)
    _.show()