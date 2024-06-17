"""
验证股票号
"""
# 引用打印学号
import printInfo


# 校验股票抽签号
def verify_stock_code(code):
    result = False
    # 判断是否12位长度以及88开头
    if len(code) == 12 and code[0:2]:
        result = True
    return result


if __name__ == '__main__':
    # 输入股票抽签号
    ticketCode = input("请输入股票抽签号：")
    # 校验股票抽签号
    verifyRsult = verify_stock_code(ticketCode)
    if verifyRsult:
        print("恭喜您，股票号已中奖！")
    else:
        print("很遗憾，您的股票号未中奖！")
    # 打印学号
    printInfo.printStudentId()