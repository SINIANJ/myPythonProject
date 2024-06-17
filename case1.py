"""
验证码
"""
# 引用打印学号
import printInfo

# 引用随机数模块
import random

if __name__ == '__main__':
    # 验证码字符串
    verificationCode = ""
    # 循环6次
    for i in range(6):
        # 随机生成的0-9的数字，转成字符串并拼接验证码
        verificationCode += str(random.randint(0, 9))
    # 打印验证码
    print("验证码：", verificationCode)
    # 输入验证码
    inputCode = input("请输入验证码：")
    # 判断验证码
    if verificationCode == inputCode:
        print("恭喜您，验证码正确！")
    else:
        print("验证码错误！")
    # 打印学号
    printInfo.printStudentId()
