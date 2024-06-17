"""
遍历字典键值
"""
# 引用打印学号
import printInfo


if __name__ == '__main__':
    testDict = {"姓名": "张三", "专业": "财务管理", "籍贯": "福建", "理想": "服务人民"}
    print(f"字典：{testDict}")
    print("\n遍历键值：")
    for key, value in testDict.items():
        print(f"键={key},值={value}")
    print("\n遍历键：")
    for key in testDict.keys():
        print(f"键={key}")
    print("\n遍历值：")
    for value in testDict.values():
        print(f"值={value}")
    # 打印学号
    printInfo.printStudentId()
