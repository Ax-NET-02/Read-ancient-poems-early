-- 删除已有的数据库
DROP SCHEMA IF EXISTS verse;

-- 创建新的数据库
CREATE SCHEMA verse;

-- 使用新的数据库
USE verse;

-- 古诗词表
CREATE TABLE IF NOT EXISTS poems (
    poem_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    poem_text TEXT NOT NULL
);


-- 保存表
CREATE TABLE IF NOT EXISTS saves (
    save_id INT PRIMARY KEY AUTO_INCREMENT,
    poem_id INT NOT NULL,
    save_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
