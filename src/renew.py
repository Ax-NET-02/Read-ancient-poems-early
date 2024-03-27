import re
import requests
import csv

# 定义爬取目标网页的URL
url = 'https://so.gushiwen.cn/gushi/sanbai.aspx'

# 定义请求头，伪装成用户访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
}

# 发送带有伪装请求头的HTTP GET请求获取页面内容
response = requests.get(url, headers=headers)
html_content = response.text

# 使用正则表达式匹配所有的<span>标签
span_tags = re.findall(r'<span.*?>(.*?)</span>', html_content)

# 创建一个 CSV 文件并写入标题行
with open('../data/poems.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['title', 'author', 'poembr']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # 使用正则表达式匹配<span>标签内的<a>标签
    for span_content in span_tags:
        a_tags = re.findall(r'<a\s+.*?href=[\'"](.*?)[\'"].*?>(.*?)</a>', span_content)
        # 输出匹配到的<a>标签内容和链接a_content
        for link, text in a_tags:
            urla = 'https://so.gushiwen.cn{}'.format(link)
            responsea = requests.get(urla, headers=headers)
            a_content = responsea.text

            # 使用正则表达式匹配标题、作者、朝代和诗句内容
            title_match = re.search(r'<h1.*?>(.*?)</h1>', a_content, re.DOTALL)
            author_match = re.search(r'<p class="source">.*?<a[^>]*>(.*?)</a>(?:<img[^>]*>)?.*?<a[^>]*>(.*?)</a>', a_content, re.DOTALL)
            poem_match = re.search(r'<div class="contson" id="contson.*?">(.*?)</div>', a_content, re.DOTALL)

            if title_match and author_match and poem_match:
                # 获取标题、作者、朝代和诗句内容
                title = title_match.group(1).strip()
                author = author_match.group(1).strip() + author_match.group(2).strip()
                poem = poem_match.group(1).strip()

                # 移除诗句中的 <br> 标签
                poembr = re.sub(r'<p\s*\/?>|<br\s*\/?>', '\n', poem)

                authorimg = re.sub(r'<img\s[^>]*>', '', author)
                
                # 清除多余的空格
                authorimg = ' '.join(authorimg.split())
                
                # 清除多余的空格
                poembr = ' '.join(poembr.split())

                # 将数据写入 CSV 文件
                writer.writerow({'title': title, 'author': authorimg, 'poembr': poembr})
                
                print('成功写入：\n', '标题：\n', title, '\n 作者朝代：\n', authorimg, '\n 诗句：\n', poembr)

print("数据已成功导出到 poems.csv 文件中！")
