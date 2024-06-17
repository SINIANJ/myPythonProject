"""
列表操作
"""
# 引用打印学号
import printInfo


if __name__ == '__main__':
    grade = [68, 87, 83, 91, 93, 79, 68, 86, 66, 78, 55, 29, 48, 75, 99, 68]
    print(f"grade={grade}\n")
    grade.sort()
    print(f"升序排序grade={grade}\n")

    print(f"1、输出grade中的第2个元素 : grade[1] = {grade[1]}")
    print(f"2、输出grade中的第3~7个元素 : grade[2:6] = {grade[2:6]}")
    print(f"3、使用in查询grade中是否包含成绩87 : 87 in grade = {87 in grade}")
    print(f"4、调用index（）函数在grade中查找给定成绩为78的学生索引号 : grade.index(87) = {grade.index(87)}")
    print(f"5、使用count（）函数查询成绩68在grade中的出现次数 : grade.count(68) = {grade.count(68)}")
    print(f"6、使用len（）函数获取grade中的元素个数 : len(grade) = {len(grade)}")

    # 打印学号
    printInfo.printStudentId()
