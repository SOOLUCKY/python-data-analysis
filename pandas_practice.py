# encoding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # pandas数据结构
    s = pd.Series([i * 2 for i in range(1, 11)])
    print(s)

    dates = pd.date_range("20170301", periods=8)
    # print(dates)
    df = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list("ABCDE"))
    print(df)

    #     向DataFrame传入字典数据
    df2 = pd.DataFrame({
        'A': 1,
        'B': pd.Timestamp('20130102'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'F': 'foo'
    })
    print(df2)
    print(df2.dtypes)

    # 基本操作
    print(df2.head(3))
    print(df2.tail(3))

    print(df2.values)
    print(df2.index)

    # 简单统计
    print(df2.describe())
    # 排序
    print(df2.sort_index(axis=1, ascending=False))
    print(df2.sort_values(by="B"))
    print(df2.T)


if __name__ == '__main__':
    main()
