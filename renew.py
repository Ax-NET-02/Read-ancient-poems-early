import re
import requests

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

# 使用正则表达式匹配<span>标签内的<a>标签
for span_content in span_tags:
    a_tags = re.findall(r'<a\s+.*?href=[\'"](.*?)[\'"].*?>(.*?)</a>', span_content)
    # 输出匹配到的<a>标签内容和链接
    for link, text in a_tags:
        urla = 'https://so.gushiwen.cn{}'.format(link)
        responsea = requests.get(urla, headers=headers)
        a_content = responsea.text
        
        
        # 使用正则表达式匹配第一个<a>标签中的作者内容
        author_match = re.search(r'<a\s+(?!.*?<img)(?=.*?<b).*?href=[\'"].*?[\'"].*?>.*?<b>(.*?)</b>.*?</a>', a_content)
        if author_match:
            author = author_match.group(1)
            print("作者：", author)
            
        # 使用正则表达式匹配<h1>标签内容
        h1_content = re.search(r'<h1.*?>(.*?)</h1>', a_content)
        if h1_content:
            print("标题:", h1_content.group(1))
            
            
        div_id = re.search(r'<div class="contson" id="contson(.*?)">', a_content)
        if div_id:
            id_content = div_id.group(1)
            
            # 使用匹配到的id属性值构建正则表达式来匹配<div>标签内容中的诗句
            poem = re.search(r'<div class="contson" id="contson{}">(.*?)</div>'.format(id_content), a_content, re.DOTALL)
            if poem:
                poem_text = poem.group(1)
                # 清理诗句中的<br>标签
                poem_text = re.sub(r'<br>', '\n', poem_text)
                print("诗句内容:")
                print(poem_text.strip())  # 去除首尾空白字符
