from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'hardwareStore'

TABLES = {}
TABLES['suppliers'] = (
    "CREATE TABLE `suppliers` ("
    "  `account_num` int(11) NOT NULL AUTO_INCREMENT,"
    "  `address` date NOT NULL,"
    "  `name` varchar(14) NOT NULL,"
    "  `phone_num` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`account_num`)"
    ") ENGINE=InnoDB")
TABLES['department'] = (
    "CREATE TABLE `department` ("
    "  `account_num` int(11) NOT NULL AUTO_INCREMENT,"
    "  `address` date NOT NULL,"
    "  `name` varchar(14) NOT NULL,"
    "  `phone_num` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`account_num`)"
    ") ENGINE=InnoDB")
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `account_num` int(11) NOT NULL AUTO_INCREMENT,"
    "  `address` date NOT NULL,"
    "  `name` varchar(14) NOT NULL,"
    "  `phone_num` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`account_num`)"
    ") ENGINE=InnoDB")
TABLES['merchandise'] = (
    "CREATE TABLE `merchandise` ("
    "  `account_num` int(11) NOT NULL AUTO_INCREMENT,"
    "  `address` date NOT NULL,"
    "  `name` varchar(14) NOT NULL,"
    "  `phone_num` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`account_num`)"
    ") ENGINE=InnoDB")
TABLES['sales'] = (
    "CREATE TABLE `sales` ("
    "  `account_num` int(11) NOT NULL AUTO_INCREMENT,"
    "  `address` date NOT NULL,"
    "  `name` varchar(14) NOT NULL,"
    "  `phone_num` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`account_num`)"
    ") ENGINE=InnoDB")