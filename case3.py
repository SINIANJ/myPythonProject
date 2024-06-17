"""
计算圆锥体表面积和体积
"""
# 引用打印学号
import printInfo
# 引用数学类函数库
import math


# 计算表面积 高：height, 半径：radius
def calculate_surface_area(height, radius):
    """
        计算表面积公式：侧面积 + 底面积 = (π * r * l) + (π * r^2)
        l 为圆锥母线长度 计算公式为：√h^2 + r^2
        所以表面积 = (π * r * (h^2 + r^2)) + (π * r^2)
    """
    # 计算母线长度
    length = math.sqrt(height ** 2 + radius ** 2)
    # 计算表面积
    # math.pi就是π ，3.141592653
    s = (math.pi * radius * length) + (math.pi * (radius ** 2))
    return s


# 计算体积 高：height, 半径：radius
def calculate_volume(height, radius):
    """
        计算体积公式：(π * r^2) * h / 3
    """
    # math.pi就是π ，3.141592653
    v = math.pi * (radius ** 2) * height / 3
    return v


if __name__ == '__main__':
    # 输入圆锥体的高和半径
    h = float(input("请输入圆锥体的高："))
    r = float(input("请输入圆锥体的半径："))
    # 调用计算表面积的方法
    surfaceArea = calculate_surface_area(h, r)
    print(f"圆锥体的表面积为：{surfaceArea}")
    # 调用计算体积的方法
    volume = calculate_volume(h, r)
    print(f"圆锥体的体积为：{volume}")
    # 打印学号
    printInfo.printStudentId()