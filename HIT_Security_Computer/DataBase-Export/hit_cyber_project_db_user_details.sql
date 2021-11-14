-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: hit_cyber_project_db
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_details` (
  `Username` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ID` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `Email` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Age` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `Current_Password` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Old_Password_1` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Old_Password_2` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Old_Password_3` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Old_Password_4` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Old_Password_5` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Old_Password_6` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Old_Password_7` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Old_Password_8` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Old_Password_9` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Old_Password_10` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `User_Lock_Until` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Attempt_Login_Failed_Count` varchar(45) COLLATE utf8mb4_general_ci DEFAULT '0',
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_details`
--

LOCK TABLES `user_details` WRITE;
/*!40000 ALTER TABLE `user_details` DISABLE KEYS */;
INSERT INTO `user_details` VALUES ('test','1','test@gmail.com','1','573fcdab9a796a6cc6d4dca109a605c1b8215d9a3583c8960ec38af07814f45d09eaaf8460de74dcb2e3eaf0110154a15527a65395448d856d95da01c96a5483380f992670dc4d868da01f035c9e23bcef837ed41590f558cdfe7ee0a0085011',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0');
/*!40000 ALTER TABLE `user_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-14 23:05:33
