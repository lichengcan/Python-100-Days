"""
生成器 - 使用yield关键字

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""

# yield 是一个在 Python 中用于定义生成器函数的关键字。
# 生成器函数是一种特殊类型的函数，它可以在需要时逐个生成值，而不是一次性生成所有值并将它们存储在内存中。
# 这使得生成器在处理大型数据集或需要逐个产生值的情况下非常有用，因为它们可以减小内存消耗。
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n += 1


for x in fib(20):
    print(x)
