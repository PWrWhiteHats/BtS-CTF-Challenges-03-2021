CREATE DATABASE IF NOT EXISTS test_db CHARACTER SET utf8 COLLATE utf8_general_ci;
SET GLOBAL query_cache_size = 1000000;
GRANT SELECT ON test_db.* TO 'devuser'@'%' IDENTIFIED BY 'devpass';

USE test_db

CREATE TABLE `leaderboard` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `surname` varchar(45) DEFAULT NULL,
  `club_name` varchar(45) DEFAULT NULL,
  `r1` int DEFAULT NULL,
  `r2` int DEFAULT NULL,
  `visible` int DEFAULT NULL,
  `player_description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
);

INSERT INTO `leaderboard` VALUES (1,'Jakub','Wysocki','Katowice golf club',25,20,0,'Enter your description here'),(2,'Ryszard Michalski','n/a','Wroclaw',15,25,0,'Enter your description here'),(3,'Lucjan','Maciejewski','Zakopane golf club',25,20,1,'Enter your description here'),(5,'Klaudia','Kucharska','Wroclaw golf club',15,15,0,'Enter your description here'),(7,'Sebastian','Kowalczyk','Bydgoszcz golf club',35,15,0,'Enter your description here'),(10,'Andrew','Green','LA Golf club',20,35,1,'Enter your description here'),(13,'Katarzyna','Czarnecka','Wesola golf club',35,30,1,'Enter your description here'),(15,'Martin','Vohralik','Nesovice',20,35,0,'Enter your description here'),(37,'Veronika','Ročková','Velešín',25,35,0,'Enter your description here'),(39,'Olga','Treur','Oeversee golf club',12,39,0,'Enter your description here'),(41,'Craig','Bouterse','Klingelbach golf club',18,29,0,'Enter your description here'),(45,'Piotr','Kowalczyk','Koszalin golf club',15,31,0,'FLAGTOBEREPLACED321'),(46,'Jaroslav','Kolar','Janovice golf club',17,32,0,'Enter your description here...'),(52,'Michael','Drda','Byst golf club',15,38,0,'Enter your description here...'),(56,'Dominik','Wisniewski','Poznan golf club',15,27,1,'Enter your description here'),(58,'Michael','Drda','Budejovice golf club',25,38,0,'Enter your description here...'),(59,'Petr','Leitner','Lnare golf club',27,28,0,'Enter your description here...'),(61,'Jozef','Nowak','Poznan golf club',19,29,1,'Enter your description here'),(62,'Miroslav','Vavra','Roudnice golf club',17,28,0,'Enter your description here...'),(63,'Otakar','Braun','Neveklov golf club',27,25,1,'Enter your description here...'),(64,'Petr','Volf','Tynec golf club',23,22,0,'Enter your description here...'),(65,'Dawid','Jablonski','Zawiercie golf club',30,22,0,'Enter your description here...'),(71,'Wincenty','Sobczak','Rybnik golf club',25,22,0,'Enter your description here...'),(73,'Szymon','Dabrowski','Warszawa golf club',35,22,0,'Enter your description here...'),(76,'Zbigniew','Wysocki','Gdansk golf club',15,20,1,'Enter your description here');

