"""
解一元二次方程
"""
# 引用打印学号
import printInfo
# 引用数学类函数库
import math

if __name__ == '__main__':
    print("一元二次方程：ax^2+bx+c=0")
    # 输入的字符串转为数字
    a = int(input("请输入a:"))
    b = int(input("请输入b:"))
    c = int(input("请输入c:"))
    """
        判断是否有实数根: delta = b^2-4ac 
        delta > 0 有两个不相等的实根
        delta = 0 有两个相同的实根
        delta < 0 无实根
    """
    delta = (b ** 2) - (4 * a * c)
    if delta >= 0:
        # 求根公式：x = (-b ± √(b^-4ac)) / (2a)8
        # 调用数学函数库平方根的方法计算：√(b^-4ac))
        delta = math.sqrt(delta)
        # x1 = (-b + √(b ^ -4ac)) / (2a)
        x1 = (-b + delta) / (2 * a)
        # x2 = (-b - √(b^-4ac)) / (2a)
        x2 = (-b - delta) / (2 * a)
        print(f"该方程有实根：x1={x1}, x2={x2}")
    else:
        print("该方程无实根！")
    # 打印学号
    printInfo.printStudentId()

