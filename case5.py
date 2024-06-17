"""
录入学生成绩
"""
# 引用打印学号
import printInfo


# 计算人数、总分、平均分
def calculate_score(studentInfoDict):
    # 学生人数
    studentCount = len(studentInfoDict)
    # 总分
    score = studentDict.values()
    totalScore = sum(score)
    # 平均分
    avgScore = totalScore / studentCount
    print(f"人数：{studentCount},总分：{totalScore},平均分：{avgScore}")


# 判断成绩水平
def check_score_grades(studentInfoDict):
    # 获取所有学生序号
    studentNumDict = studentInfoDict.keys()
    # 成绩水平
    grades = ""
    for num in studentNumDict:
        # （优秀为≥90，良好为80-89分，中等为70-79分，合格为60-69分）
        score = studentInfoDict[num]
        if 90 <= score:
            grades = "优秀"
        elif 80 <= score <= 89:
            grades = "良好"
        elif 70 <= score <= 79:
            grades = "中等"
        elif 60 <= score <= 69:
            grades = "合格"
        else:
            grades = "不合格"
        print(f"学生{num}语文成绩为{score}分，{grades}！")


if __name__ == '__main__':
    # 存放学生成绩的字典
    studentDict = {}
    # 学生序号
    studentNum = 1
    # while循环，
    while True:
        inputStr = input(f"请输入学生{studentNum}的语文成绩：")
        if "a" == inputStr:
            break
        else:
            studentScore = int(inputStr)
            studentDict[studentNum] = studentScore
            studentNum += 1
    # 计算人数、总分、平均分
    calculate_score(studentDict)
    # 判断成绩水平
    check_score_grades(studentDict)
    # 打印学号
    printInfo.printStudentId()
