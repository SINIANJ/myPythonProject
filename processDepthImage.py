"""
    处理深度图片转为深度数据
"""
import os
import cv2
import numpy as np
import fileUtil


# 获取深度数据
def getDepthData(depth_image_data):
    depth_str = ""
    # 遍历深度图像中的每个像素
    for row in range(depth_image_data.shape[0]):
        line = ""
        for col in range(depth_image_data.shape[1]):
            # 获取像素的深度值
            depth_value = depth_image_data[row, col]
            if col != 0:
                line += " "
            line += str(depth_value)
        if row != 0:
            depth_str += "\n"
        depth_str += line
    return depth_str


if __name__ == '__main__':
    directory = "E:\\CProjectTest\\CableTest\\newTest\\4"
    fileType = ".png"
    files = fileUtil.getFiles(directory, fileType)
    for file in files:
        filePath = file.get("filePath")
        fileName = file.get("file")
        root = file.get("root")
        depth_data_path = os.path.join(root, fileName.replace(fileType, '.txt'))
        # 读取图片
        depth_image = cv2.imread(filePath, cv2.IMREAD_UNCHANGED)
        print("深度图像的数据类型:", depth_image.dtype)
        print("深度图像的尺寸:", depth_image.shape)
        height, width = depth_image.shape
        # 创建矩阵数据
        depth_array = np.zeros((height, width))
        # 获取深度数据
        depth_data = getDepthData(depth_image)
        with open(depth_data_path, 'w') as f:
            f.write(depth_data)



