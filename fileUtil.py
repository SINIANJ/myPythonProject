import os

"""
  文件操作工具类  
"""


# 筛选获取文件信息
def getFiles(directory_path, fileType):
    result_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(fileType):
                filePath = os.path.join(root, file)
                obj = {
                    "root": root,
                    "file": file,
                    "filePath": filePath
                }
                result_files.append(obj)
        break
    return result_files


# 替换文件内容
def replaceFileContent(filepath, replace_dict):
    # 读取文件内容
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    # 替换符号
    for key, value in replace_dict.items():
        content = content.replace(key, value)
    # 将新内容写回文件
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
