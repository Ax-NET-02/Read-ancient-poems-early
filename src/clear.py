import pandas as pd

# 读取CSV文件
df = pd.read_csv('../database/poems.csv')

# 获取poembr列的内容
poembr_column = df['poembr']

# 使用正则表达式清除<p>和</p>标签
# poembr_column_cleaned_p = poembr_column.str.replace(r'<br\s*\/?>', '<br>', regex=True)

# # 清除多余空格
# poembr_column_cleaned = poembr_column.str.replace(r'\s+', ' ', regex=True)

# # 在句号后添加<br>标签
poembr_column_cleaned_br = poembr_column.str.replace(r'\.\s*(?!\s*$)', '.<br>', regex=True)

# poembr_column_cleaned_br = poembr_column.str.replace(r'<br\s*\/?>', '', regex=True)

# 去掉括号及其内容
# poembr_column_cleaned = poembr_column_cleaned_br.str.replace(r'\([^()]*\)', '', regex=True)

# 更新DataFrame中的poembr列
df['poembr'] = poembr_column_cleaned_br

# 重新保存DataFrame到poems.csv
df.to_csv('../database/poems.csv', index=False)

print("更新后的数据已保存到 poems.csv 文件。")
