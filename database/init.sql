
CREATE DATABASE IF NOT EXISTS `tickets`;
USE `tickets`;

CREATE TABLE `User`
(
 `UserID`    int(11) NOT NULL AUTO_INCREMENT ,
 `Name`      varchar(40) NOT NULL ,
PRIMARY KEY (`UserID`)
);

CREATE TABLE `Show`
(
 `ID`               int(11) NOT NULL AUTO_INCREMENT ,
 `Name`             varchar(45) NOT NULL ,
 `No_of_Tickets`    int(11) NOT NULL ,
 `Price_per_Ticket` int(11) NOT NULL ,
 `Date`             varchar(45) NOT NULL ,
 `Hour`             varchar(45) NOT NULL ,
PRIMARY KEY (`ID`)
);

CREATE TABLE `Room`
(
 `ID`          int(11) NOT NULL AUTO_INCREMENT ,
 `Name`        varbinary(45) NOT NULL ,
 `No_of_Seats` int(11) NOT NULL ,
PRIMARY KEY (`ID`)
);

CREATE TABLE `Show_To_Room`
(
 `ID`              int(11) NOT NULL ,
 `ShowID`          int(11) NOT NULL ,
 `RoomID`          int(11) NOT NULL ,
 `Available_Seats` int(11) NOT NULL ,
PRIMARY KEY (`ID`),
KEY `fkIdx_235` (`ShowID`),
CONSTRAINT `FK_235` FOREIGN KEY `fkIdx_235` (`ShowID`) REFERENCES `Show` (`ID`),
KEY `fkIdx_238` (`RoomID`),
CONSTRAINT `FK_238` FOREIGN KEY `fkIdx_238` (`RoomID`) REFERENCES `Room` (`ID`)
);

CREATE TABLE `Ticket`
(
 `ID`           int(11) NOT NULL AUTO_INCREMENT ,
 `UserID`       int(11) NOT NULL ,
 `Show_To_Room` int(11) NOT NULL ,
PRIMARY KEY (`ID`),
KEY `fkIdx_247` (`UserID`),
CONSTRAINT `FK_247` FOREIGN KEY `fkIdx_247` (`UserID`) REFERENCES `User` (`UserID`),
KEY `fkIdx_250` (`Show_To_Room`),
CONSTRAINT `FK_250` FOREIGN KEY `fkIdx_250` (`Show_To_Room`) REFERENCES `Show_To_Room` (`ID`)
);