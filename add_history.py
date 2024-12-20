import json

try:
    # 读取JSON文件内容，指定编码为'utf-8'
    with open('CPR_6_sys.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 遍历数据列表，为每条记录添加 "history": [] 字段
    for item in data:
        item["history"] = []

    # 将处理后的数据重新写入新的JSON文件（这里选择另存为新文件，注意编码格式指定）
    with open('new_file.json', 'w', encoding='utf-8') as new_file:
        json.dump(data, new_file, indent=4)
    print("数据处理并保存成功，已生成new_file.json文件。")
except FileNotFoundError:
    print("指定的JSON文件 'CPR_6_sys.json' 不存在，请检查文件路径和文件名是否正确。")
except json.JSONDecodeError:
    print("读取JSON文件时出现解析错误，请确保文件格式符合JSON规范。")
except Exception as e:
    print(f"出现其他未知错误: {str(e)}")