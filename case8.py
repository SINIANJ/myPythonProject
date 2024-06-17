"""
集合操作
"""
# 引用打印学号
import printInfo


if __name__ == '__main__':
    set1 = {2, 5, 9, 1, 3, 41, 29, 88, 4}
    set2 = {3, 6, 29, 8, 2, 5, 4}
    print(f"set1={set1}")
    print(f"set2={set2}\n")
    print("向set1中添加一个新的元素7")
    set1.add(7)
    print(f"set1={set1}\n")
    print("求set1和set2的并集")
    union = set1 | set2
    print(f"并集={union}\n")
    print("求set1和set2的交集")
    intersection = set1 & set2
    print(f"交集={intersection}\n")
    print("求set1和set2的差集")
    diffSet = set1 - set2
    print(f"差集={diffSet}\n")

    # 打印学号
    printInfo.printStudentId()
