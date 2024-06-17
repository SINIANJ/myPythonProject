"""
输入工时计算工资
"""
# 引用打印学号
import printInfo


# 计算工资
def calculate_earnings(hoursNum):
    earnings = 0
    if 130 <= hoursNum <= 160:
        earnings = hoursNum * 80
    elif hoursNum > 160:
        earnings = 160 * 80 + (hoursNum - 160) * (80 * 1.3)
    elif hoursNum < 130:
        earnings = hoursNum * 80 * 0.8
    return earnings


if __name__ == '__main__':
    # 循环输入
    while True:
        inputStr = input("请输入工时计算工资(输入a结束)：")
        if "a" == inputStr:
            break
        hours = float(inputStr)
        money = calculate_earnings(hours)
        print(f"工资为：{money}元")
        print()
    # 打印学号
    printInfo.printStudentId()

