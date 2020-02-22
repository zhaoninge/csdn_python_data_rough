'''
通⽤函数就是能同时对元素内所有元素逐个进⾏运算的函数。
numpy专注于⼤量数据运算，python本身也能够对⼤量数据进⾏计算，但是速度相对缓慢，为了解决
这个问题，numpy对数据运算进⾏优化，使计算变得迅速简洁。
numpy进⾏快速数据运算的关键在于向量化。
numpy⽀持运算符操作，运算符看作是运算类函数的简写。
从运算符参与运算数据的⻆度分类，通⽤函数⾮为两类：
⼀元通⽤函数(unary ufunc): 对单个输⼊进⾏操作
⼆元通⽤函数(binary ufunc): 对两个输⼊进⾏操作
从功能上分类，通⽤函数分为算术计算函数，双曲三⻆函数，位运算类，⽐较运算符，弧度⻆度转换类
等。
更加复杂的通⽤函数放在scipy.special模块下，如果需要，可以查阅相关⽂档。
'''
