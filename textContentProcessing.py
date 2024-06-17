"""
文本内容处理
"""
import os
import cv2
import numpy as np
import fileUtil


def removeContentLine(root, file):
    filepath = os.path.join(root, file)
    with open(filepath, 'r') as file:
        lines = file.readlines()
    # 删除指定行
    for index, value in enumerate(lines):
        fileName = str(len(lines)-index) + ".txt"
        with open(os.path.join(os.path.join(root, "lines"), fileName), 'w') as file:
            depth_arr = value.split(' ')
            final_value = ""
            for depth_index, depth_value in enumerate(depth_arr):
                final_value = depth_value + " " + final_value
            file.writelines(final_value)


def traverse_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        # files = sorted(files, key=lambda x: int(x.split('.')[0]))
        for file in files:
            if file.endswith(".txt"):
                filePath = os.path.join(root, file)
                print(filePath)
                # 替换文件内容
                fileUtil.replaceFileContent(filePath, {",": "", ";": "", "[": "", "]": ""})
                # 按行截取文件内容
                removeContentLine(root, file)
                # break

                # new_name = str(int(file.split(".")[0])-4)
                # new_name = new_name+".txt"
                # os.rename(filePath, os.path.join(root, new_name))
        break


def generateImages(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                data_file = os.path.join(root, file)
                # 读取深度数据
                depth_data = np.loadtxt(data_file)
                image_height = len(depth_data)
                image_width = len(depth_data[0])
                # 将一维数组转换为合适的图像形状
                depth_image = depth_data.reshape((image_height, image_width)).astype(np.uint8)
                depth_image = cv2.normalize(depth_image, depth_image, 0, 255, cv2.NORM_MINMAX)
                # 显示图像
                cv2.imshow('Depth Image', depth_image)
                cv2.waitKey(0)

                # 如果需要，保存图像
                fileName = str(file).replace(".txt", ".jpg")
                cv2.imwrite(os.path.join(directory_path, fileName), depth_image)

                # 关闭所有窗口
                cv2.destroyAllWindows()
        break


def intercept_depth_data(directory_path, save_row_interval, save_col_interval):
    newFileName = "newContent.txt"
    files = fileUtil.getFiles(directory_path, ".txt")
    for file in files:
        filePath = file.get("filePath")
        root = file.get("root")
        fileName = file.get("file")
        if fileName == newFileName:
            continue
        save_row_min = save_row_interval[0]  # 要保留的最小行号
        save_row_max = save_row_interval[1]  # 要保留的最大行号
        save_col_min = save_col_interval[0]  # 要保留的最小列号
        save_col_max = save_col_interval[1]  # 要保留的最大列号
        resultContent = ""
        with open(filePath, 'r') as fileContent:
            lines = fileContent.readlines()
        # 删除指定行
        for index, value in enumerate(lines):
            if save_row_min <= index <= save_row_max:
                depth_arr = value.split(' ')
                final_value = ""
                firstCol = True
                for depth_index, depth_value in enumerate(depth_arr):
                    if save_col_min <= depth_index <= save_col_max:
                        if firstCol:
                            firstCol = False
                        else:
                            depth_value = " " + depth_value
                        final_value += depth_value
                resultContent += final_value + "\n"
        while resultContent.endswith('\n'):  # 循环直到字符串不以换行符结尾
            resultContent = resultContent[:-1]  # 删除最后一个字符
        with open(os.path.join(root, newFileName), 'w') as newFile:
            newFile.write(resultContent)


if __name__ == '__main__':
    directory = "E:\\CProjectTest\\CableTest\\newTest"
    flag = 2
    row_interval = [300, 800]
    col_interval = [450, 900]
    directory = os.path.join(directory, str(flag))
    if flag == 1:
        # 深度数据转换为图片
        generateImages(directory)
    elif flag == 2:
        # 数据转换
        traverse_directory(directory)
    elif flag == 3:
        # 截取深度数据
        intercept_depth_data(directory, row_interval, col_interval)

