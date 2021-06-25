from concurrent.futures.process import ProcessPoolExecutor
import itertools
import pandas as pd
import numpy as np
from tools.calc import *

if __name__ == '__main__':
    """
    真实的回测,有繁多的IO,有复杂的运算,因此想简单通过for循环串行计算,就很慢了
    一般用多任务并行的方式,来解决
    启动多个进程
    启动多个线程
    多进程+多线程
    """

    """
    全局解释锁;global interpreter  lock,只允许一个线程来控制Python解释器
    这就意味着在任何一个时间点只有一个线程处于执行状态
    GIL对执行单线程任务的程序员们来说并没什么显著影响,但是它成为了计算密集型(CPU-bound)和多线程任务的性能瓶颈
    GIL即使在拥有多个CPU核的多线程框架下都只允许一次运行一个线程
    参考:https://www.cnblogs.com/ajaxa/p/9111884.html
    
    多线程适合处理IO密集任务和并发执行的阻塞操作
    多进程适合处理并行的计算密集任务
    """

    # 使用多进程
    result = []
    keep_stock_list = np.arange(2, 30, 2).tolist()
    buy_change_list = (np.arange(-5, -16, -1) / 100).tolist()
    trade_days = 0
    # 回调数据,通过add_done_callback任务完成后调用
    def when_done(r):
        # when_done 在主进程中运行
        result.append(r.result())

    with ProcessPoolExecutor() as pool:
        for keep_stock_threshold, buy_change_threshold in itertools.product(keep_stock_list, buy_change_list):
            """
            submit 提交任务, calc 函数和参数通过submit提交到独立进程,提交的任务必须是简单函数,进程不支持类方法,闭包等
            函数参数和返回值必须兼容pickle序列化;进程间的通信需要传递可序列化对象
            """
            future_result = pool.submit(calc(keep_stock_threshold, buy_change_threshold, trade_days))

            # 进程完成任务后,calc运行结束,回调函数
            future_result.add_done_callback(when_done)
    print(future_result)