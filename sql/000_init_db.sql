-- Adminer 4.8.1 MySQL 5.7.42 dump

SET NAMES utf8;

SET time_zone = '+00:00';

SET foreign_key_checks = 0;

SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

-- 2023-04-27 02:37:24

DROP TABLE IF EXISTS `User`;

CREATE TABLE
    `User` (
        `ID` int(11) NOT NULL AUTO_INCREMENT,
        `Name` text NOT NULL,
        `Username` text NOT NULL,
        `Email` text NOT NULL,
        `password` text NOT NULL,
        `Birth_date` date NOT NULL DEFAULT '2003-01-02',
        `Status` tinyint(4) NOT NULL DEFAULT '0',
        `Creation_date` date NOT NULL,
        `Last_update` timestamp NOT NULL,
        PRIMARY KEY (`ID`)
    ) ENGINE = InnoDB DEFAULT CHARSET = latin1;