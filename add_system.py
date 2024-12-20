import json

# 定义要添加的system字段内容
system_content = "你作为 AI 急救培训师，根据历史对话洞察用户知识薄弱点，在回答时突出重点，对心脏急救知识进行系统梳理，补充相关细节，提供实用的操作建议，以亲切耐心的风格与用户互动，助力用户逐步成为心脏急救知识的行家，同时根据对话进展拓展相关知识领域"

# 读取JSON文件内容，指定编码为'utf-8'
with open('心脏复苏急救数据集-6-sys.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 遍历数据列表，为每条记录添加system字段
for item in data:
    item["system"] = system_content

# 将更新后的数据写回JSON文件（这里覆盖原文件了，你可以按需修改保存的文件名等）
with open('心脏复苏急救数据集-6-sys.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)