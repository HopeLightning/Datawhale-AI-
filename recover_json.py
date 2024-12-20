import json

# 读取包含转义Unicode编码内容的JSON文件（这里假设编码格式是'utf-8'，根据实际调整）
with open('new_file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 将处理后的数据重新写入新的JSON文件（这里可以选择覆盖原文件或者另存为新文件，注意编码格式指定）
with open('new_file.json', 'w', encoding='utf-8') as new_file:
    json.dump(data, new_file, indent=4, ensure_ascii=False)