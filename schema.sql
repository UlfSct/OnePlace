DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS userData;
DROP TABLE IF EXISTS dailyTasks;

CREATE TABLE users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255),
    password VARCHAR(500)
);

CREATE TABLE userData (
    userID INTEGER PRIMARY KEY,
    money INTEGER DEFAULT 0,
    exp INTEGER DEFAULT 0,
    Plant1 INTEGER DEFAULT 0,
    Plant2 INTEGER DEFAULT 0,
    Plant3 INTEGER DEFAULT 0,
    Plant4 INTEGER DEFAULT 0
);

CREATE TABLE dailyTasks (
    taskID INTEGER PRIMARY KEY AUTOINCREMENT,
    task VARCHAR(512),
    money INTEGER DEFAULT 0,
    exp INTEGER DEFAULT 0
);

CREATE TABLE markers (
    markerID INTEGER PRIMARY KEY AUTOINCREMENT,
    lat REAL,
    lon REAL,
    type VARCHAR(128),
    icon VARCHAR(256),
    desc VARCHAR(512)
);

INSERT INTO dailyTasks (task, money, exp) VALUES
    ("Сходи погуляй", 10, 20),
    ("Помой посуду", 50, 30),
    ("Займись делом", 30, 50),
    ("Апни 1000 пп в осу", 100, 500),
    ("Закрой практику", 1, 200);

INSERT INTO markers (lat, lon, type, icon, desc) VALUES
    (55.87606106886836, 37.5243455, "Стекло/Пластик", "glass:plastic", "Контейнеры для вторсырья ГУП 'Экотехпром'"),
    (55.77567706896828, 37.64321949999997, "Пластик/Металл/Батарейки", "plastic:metal:battery", "Точка приема батареек, фандомат для приема пластиковых бутылок в магазине ВкусВилл"),
    (55.73120156900297,37.4607535, "Стекло/Пластик", "glass:plastic", "Контейнеры для вторсырья ГУП 'Экотехпром'");
