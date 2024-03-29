## 早读诗词朗诵

### 开发动机：

看班上讲台上的领读者 一个一个的点诗词太麻烦了，决定用我所学的知识将这些诗词整合成一个网页



### 开发思路：

1.用Flask做后端
2.爬虫爬取古诗词网站诗词

3.爬取网站内容储存为CSV格式，并转存数据库，也可以直接使用CSV格式的数据



### 使用方法：

#### 1.安装环境

把项目git下来之后 在根目录打开 "CMD" 命令提示符 运行下面的指令 安装环境

```python
pip install -r requirements.txt
```

#### 2.创建数据库

(1).你可以用Docker拉一个数据库 也可以自己安装一个数据库

(2).连接数据库 可以是第三方软件连接如(Navicat Premium) 也可以是在命令提示符中连接数据库

```python
# 在命令提示符中输入下面指令 连接数据库 回车输入密码
mysql -u root -p
```

(3).创建数据库

```sql
-- 删除已有的数据库
DROP SCHEMA IF EXISTS verse;

-- 创建新的数据库
CREATE SCHEMA verse;

-- 使用新的数据库
USE verse;

CREATE TABLE IF NOT EXISTS poems (
    poem_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    poem_text TEXT NOT NULL
);
```

#### 3.将数据写入数据库

(1).修改connect.py 内容

只需要修改 "dbpw" 数据库连接密码和 "db" 数据库名字

```python
host = 'localhost'
user = 'root'
dbpw = '你自己的数据库密码'
db = 'verse'	# 数据库名字
port=3306
```



#### 4.打开database目录，如果前面配置正确的话 这一步不会报错

在终端中运行写入数据的代码 (运行成功之后不会提示任何信息 如果提示信息则写入失败)

```python
python write.py
```

#### 5.运行主程序（原神启动！）

```python
python app.py
```

