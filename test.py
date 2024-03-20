import re

# 假设这是包含 HTML 内容的字符串
html_content = """
<div id="zhengwen4c5705b99143">
<h1 style="font-size:20px; line-height:22px; height:22px; margin-bottom:10px;">关雎</h1>
<p class="source"><a href="/shiwens/default.aspx?astr=%e8%af%97%e7%bb%8f%c2%b7%e5%9b%bd%e9%a3%8e%c2%b7%e5%91%a8%e5%8d%97">
诗经·国风·周南</a><a href="https://so.gushiwen.cn/shiwens/default.aspx?cstr=%e5%85%88%e7%a7%a6">〔先秦〕</a></p>
<div class="contson" id="contson4c5705b99143">
关关雎鸠，在河之洲。窈窕淑女，君子好逑。<br>参差荇菜，左右流之。窈窕淑女，寤寐求之。<br>求之不得，寤寐思服。悠哉悠哉，辗转反侧。<br>参差荇菜，左右采之。窈窕淑女，琴瑟友之。<br>参差荇菜，左右芼之。窈窕淑女，钟鼓乐之。
</div>
</div>
"""

# 使用正则表达式匹配标题、作者、朝代和诗句内容
title_match = re.search(r'<h1.*?>(.*?)</h1>', html_content, re.DOTALL)
author_match = re.search(r'<p class="source">.*?<a[^>]*>(.*?)</a>.*?<a[^>]*>(.*?)</a>', html_content, re.DOTALL)
poem_match = re.search(r'<div class="contson" id="contson.*?">(.*?)</div>', html_content, re.DOTALL)

if title_match and author_match and poem_match:
    # 获取标题、作者、朝代和诗句内容
    title = title_match.group(1).strip()
    author = author_match.group(1).strip() + author_match.group(2).strip()
    poem = poem_match.group(1).strip()
    
    # 移除诗句中的 <br> 标签
    poem = re.sub(r'<br>', '\n', poem)
    # 移除诗句中的 <img> 标签
    poem = re.sub(r'<img.*?>', '', poem)
    
    print("标题:", title)
    print("作者和朝代:", author)
    print("诗句内容:")
    print(poem)
