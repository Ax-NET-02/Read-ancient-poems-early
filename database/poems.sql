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
