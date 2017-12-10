# encoding=utf-8

import numpy as np
from numpy.linalg import *


def main():
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))

    np_lst = np.array(lst)
    print(type(np_lst))

    np_lst = np.array(lst, np.float)
    # numpy有自己支持的数据类型，ndarray只能放一种数据结构

    # shape属性表示数组行列信息
    print(np_lst.shape)

    # 数组维数
    print(np_lst.ndim)

    # 数组数据类型
    print(np_lst.dtype)

    # 数组数据类型字节数
    print(np_lst.itemsize)

    # 元素个数
    print(np_lst.size)

    #     numpy常用数组
    print(np.zeros([2, 4]))  # 0
    print(np.ones([3, 5]))  # 1
    print(np.random.rand(2, 4))  # 随机数
    print(np.random.rand())
    print(np.random.randint(1, 10, 3))  # 指定范围
    print(np.random.randn(2, 4))  # 符合正态分布的
    print(np.random.beta(1, 10, 100))  # 符合beta分布的
    print(np.random.choice([10, 20, 30, 2, 8]))  # 指定随机数

    #     numpy数组常用操作
    lst = np.arange(1, 11).reshape([2, -1])  # 产生等差数组 生成2行5列的数组

    print(np.exp(lst))
    print(np.exp2(lst))
    print(np.sqrt(lst))
    print(np.sin(lst))
    print(np.log(lst))

    lst = np.array([[[1, 2, 3, 4], [4, 5, 6, 7]], [[7, 8, 9, 10], [10, 11, 12, 13]]])
    print(lst.sum(axis=2))
    print(lst.max(axis=1))
    print(lst.min(axis=0))

    lst1 = np.array([10, 20, 30, 40])
    lst2 = np.array([4, 3, 2, 1])
    print("add")
    print(lst1 + lst2)

    print("sub")
    print(lst1 - lst2)

    print("mul")
    print(lst1 * lst2)

    print("div")
    print(lst1 / lst2)

    print("square")
    print(lst1 ** 2)

    #     向量点乘运算
    print(np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))

    # 数组追加
    print(np.concatenate((lst1, lst2), axis=0))
    print(np.vstack((lst1, lst2)))
    print(np.hstack((lst1, lst2)))
    print(np.split(lst1, 4))
    print(np.copy(lst1))

    #     numpy线性运算

    lst = np.eye(3)
    lst = np.array([[1, 2], [3, 4]])
    print(lst)
    print(inv(lst))  # 逆矩阵
    print(lst.transpose())  # 矩阵转置
    print(det(lst))  # 行列式
    print(det(lst))  # 特征值
    print(eig(lst))  # 特征向量

    y = np.array([[5], [7]])
    print(solve(lst, y))  # 解方程组 1*x + 2y = 5 3*x + 4y = 7


if __name__ == '__main__':
    main()
