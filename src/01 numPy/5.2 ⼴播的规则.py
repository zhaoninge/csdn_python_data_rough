'''
⼴播必须按照⼀定规则进⾏，不能瞎jb播，即便是按照规则，也不是⼀定能进⾏⼴播。
⼴播规则如下：
规则1： 如果两个数组维度不相同，则⼩维度数组形状在最左边补上1
规则2： 如果两数组的形状在任何⼀个维度上都不匹配，则数组的形状会沿着维度为1的维度扩展
以匹配零位⼀个数组
规则3： 如果两两个数组的形状在任何⼀个维度上都不匹配并且没有任何⼀个维度等于1， 则异
常。

个人体会：一句话总结，就是在缺少的第1个维度上刷一下
'''