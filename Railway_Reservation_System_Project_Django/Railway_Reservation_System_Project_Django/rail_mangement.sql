DROP DATABASE IF EXISTS `RAIL_MANAGEMENT`;
CREATE DATABASE `RAIL_MANAGEMENT`;
USE `RAIL_MANAGEMENT`;


CREATE TABLE IF NOT EXISTS `PASSENGER`(
`P_ID` INT(8) UNIQUE NOT NULL PRIMARY KEY,
`P_NAME` VARCHAR(30) NOT NULL,
`GENDER` VARCHAR(10) NULL,
`PH_NUMBER` INT(10) UNIQUE NOT NULL,
`EMAIL_ID` VARCHAR(30) UNIQUE NOT NULL,
`SEAT_NO` INT UNIQUE NOT NULL,
`RES_STATUS` VARCHAR(20) NOT NULL
)ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `STATION`(
`STATION_ID` INT(4) UNIQUE NOT NULL PRIMARY KEY,
`STATION_NAME` VARCHAR(30) NOT NULL,
`STATION_GATES` INT NOT NULL,
`STATION_PLATFORMS` INT NOT NULL
)ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `TRAIN`(
`PNR_NO` VARCHAR(10) UNIQUE NOT NULL PRIMARY KEY,
`NAME_OF_TRAIN` VARCHAR(20) NOT NULL,
`STATION_ID` INT(4) UNIQUE NOT NULL,
FOREIGN KEY(`STATION_ID`)
REFERENCES STATION(`STATION_ID`)
		ON UPDATE CASCADE
            ON DELETE CASCADE
)ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `TICKETS`(
`TICKET_NO` INT UNIQUE NOT NULL PRIMARY KEY,
`SOURCE` VARCHAR(20) NOT NULL,
`DESTINATION` VARCHAR(20) NOT NULL,
`CLASS_ID` VARCHAR(10) NOT NULL,
`RECEIPT_NO` INT NOT NULL,
`JOURNEY_DATE` DATE NOT NULL,
`DEPARTMENT_TIME` TIME NOT NULL,
`ARRIVAL_TIME` TIME NOT NULL,
`SEAT_NO` INT UNIQUE NOT NULL,
`PNR_NO` VARCHAR(10) UNIQUE NOT NULL,
`P_ID` INT(8) NOT NULL,
`AVAILABILITY` INT NOT NULL,
FOREIGN KEY(`PNR_NO`) REFERENCES TRAIN(`PNR_NO`)
ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(`P_ID`) REFERENCES PASSENGER(`P_ID`)
		ON UPDATE CASCADE
            ON DELETE CASCADE
)ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE PASSENGER
ADD FOREIGN KEY(`SEAT_NO`)
REFERENCES TICKETS(`SEAT_NO`)
		ON UPDATE CASCADE
            ON DELETE cascade;

CREATE TABLE IF NOT EXISTS `CLASS`(
`CLASS_ID` VARCHAR(10) NOT NULL PRIMARY KEY,
`SEAT_NO` INT UNIQUE NOT NULL,
`PNR_NO` VARCHAR(10) UNIQUE NOT NULL)ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE TICKETS
ADD FOREIGN KEY(`CLASS_ID`) REFERENCES CLASS(`CLASS_ID`)
ON UPDATE CASCADE ON DELETE CASCADE;

CREATE TABLE IF NOT EXISTS `FARE`(
`RECEIPT_NO` INT UNIQUE NOT NULL PRIMARY KEY,
`PNR_NO` VARCHAR(10) UNIQUE NOT NULL,
`TICKET_NO` INT UNIQUE NOT NULL,
`CLASS_ID` VARCHAR(10) NOT NULL,
`FARE` INT NOT NULL,
FOREIGN KEY(`PNR_NO`) REFERENCES TRAIN(`PNR_NO`)
ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(`TICKET_NO`) REFERENCES TICKETS(`TICKET_NO`)
ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(`CLASS_ID`) REFERENCES CLASS(`CLASS_ID`)
ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE TICKETS
ADD FOREIGN KEY(`RECEIPT_NO`) REFERENCES FARE(`RECEIPT_NO`)
ON UPDATE CASCADE ON DELETE CASCADE;

CREATE TABLE IF NOT EXISTS `TIMES`(
`DEPARTMENT_TIME` TIME NOT NULL,
`ARRIVAL_TIME` TIME NOT NULL,
`JOURNEY_DATE` DATE NOT NULL,
`PNR_NO` VARCHAR(10) UNIQUE NOT NULL,
`STATION_ID` INT(4) UNIQUE NOT NULL,
`STATION_PLATFORMS` INT NOT NULL,
`AVAILABILITY` INT NOT NULL PRIMARY KEY,
FOREIGN KEY(`PNR_NO`) REFERENCES TRAIN(`PNR_NO`)
ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(`STATION_ID`) REFERENCES STATION(`STATION_ID`)
ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE TICKETS
ADD FOREIGN KEY(`AVAILABILITY`) REFERENCES TIMES(`AVAILABILITY`)
ON UPDATE CASCADE ON DELETE CASCADE;


