# encoding=utf-8
import numpy as np
import pandas as pd


def main():
    # pandas数据结构
    s = pd.Series([i * 2 for i in range(1, 11)])
    print(s)

    dates = pd.date_range("20170301", periods=8)
    # print(dates)
    df = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list("ABCDE"))
    print(df)

#     基本操作
    print(df.head(3))
    print(df.tail(3))

    print(df.values)
    print(df.index)
    print(df.T)
    print(df.sort_index)

if __name__ == '__main__':
    main()
