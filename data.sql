-- MariaDB dump 10.19  Distrib 10.10.2-MariaDB, for Android (aarch64)
--
-- Host: localhost    Database: Medical_Record
-- ------------------------------------------------------
-- Server version	10.10.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CaseFile`
--

DROP TABLE IF EXISTS `CaseFile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CaseFile` (
  `symptoms` varchar(128) NOT NULL,
  `diagnosis` varchar(128) NOT NULL,
  `prescription` varchar(128) NOT NULL,
  `testResult` varchar(128) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `staff_id` varchar(60) NOT NULL,
  `patient_id` varchar(60) NOT NULL,
  `healthcare_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `staff_id` (`staff_id`),
  KEY `patient_id` (`patient_id`),
  KEY `healthcare_id` (`healthcare_id`),
  CONSTRAINT `CaseFile_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `Doctor` (`id`),
  CONSTRAINT `CaseFile_ibfk_2` FOREIGN KEY (`patient_id`) REFERENCES `Patient` (`id`),
  CONSTRAINT `CaseFile_ibfk_3` FOREIGN KEY (`healthcare_id`) REFERENCES `HealthCareFacilities` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CaseFile`
--

LOCK TABLES `CaseFile` WRITE;
/*!40000 ALTER TABLE `CaseFile` DISABLE KEYS */;
INSERT INTO `CaseFile` VALUES
('\"Save,Nw\"','Diagnosis ','Prescribe ','Old test','57cb82c3-cef0-48b1-9f40-b855d957b813','2023-04-07 20:23:54','2023-04-07 20:23:54','2812ad2c-c3e7-438d-8d85-8d94fde374e1','e41f2b35-4b48-4c8b-bf7d-1df7b6d26e92','c295ae81-ca73-4af0-a293-2e17f318d5f7'),
('Pain; cough;','Headache ','Paracetamol ','Negative ','b3f7c761-2a18-45ed-aa79-3cfb552db3bb','2023-04-06 17:24:37','2023-04-06 17:24:37','2812ad2c-c3e7-438d-8d85-8d94fde374e1','e41f2b35-4b48-4c8b-bf7d-1df7b6d26e92','c295ae81-ca73-4af0-a293-2e17f318d5f7');
/*!40000 ALTER TABLE `CaseFile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Doctor`
--

DROP TABLE IF EXISTS `Doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Doctor` (
  `address` varchar(1024) DEFAULT NULL,
  `nxt_of_kin` varchar(256) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `nin` varchar(12) NOT NULL,
  `firstname` varchar(128) NOT NULL,
  `surname` varchar(128) NOT NULL,
  `middlename` varchar(128) DEFAULT NULL,
  `sex` varchar(15) NOT NULL,
  `dob` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `nin` (`nin`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Doctor`
--

LOCK TABLES `Doctor` WRITE;
/*!40000 ALTER TABLE `Doctor` DISABLE KEYS */;
INSERT INTO `Doctor` VALUES
(NULL,NULL,NULL,'2812ad2c-c3e7-438d-8d85-8d94fde374e1','2023-03-24 19:06:13','2023-03-24 19:08:39','873908487892','Inioluwa','Aderemi','Esther','Female','1997-08-30 00:00:00'),
(NULL,NULL,NULL,'6c1d7749-95d7-4ed0-8232-4ca118941b2d','2023-03-19 11:56:41','2023-03-19 11:57:56','12345654321','Rose','Aderemi','Yohanna','Female','1999-03-03 00:00:00'),
(NULL,NULL,NULL,'99f9fa08-5fba-4735-bf79-da3231a3637a','2023-04-02 20:59:39','2023-04-03 10:30:27','12345678987','Temitayo','Tolulope',NULL,'female','1989-03-10 00:00:00'),
(NULL,NULL,NULL,'fbbea63b-f3c5-4229-8be2-26de2edca124','2023-03-19 11:51:01','2023-03-19 11:52:05','12121212334','Rose','Aderemi','Yohanna','Female','1999-03-03 00:00:00');
/*!40000 ALTER TABLE `Doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HealthCareFacilities`
--

DROP TABLE IF EXISTS `HealthCareFacilities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HealthCareFacilities` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(60) NOT NULL,
  `maternity` varchar(60) DEFAULT NULL,
  `general` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `maternity` (`maternity`),
  KEY `general` (`general`),
  CONSTRAINT `HealthCareFacilities_ibfk_1` FOREIGN KEY (`maternity`) REFERENCES `Maternity` (`id`),
  CONSTRAINT `HealthCareFacilities_ibfk_2` FOREIGN KEY (`general`) REFERENCES `Hospital` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HealthCareFacilities`
--

LOCK TABLES `HealthCareFacilities` WRITE;
/*!40000 ALTER TABLE `HealthCareFacilities` DISABLE KEYS */;
INSERT INTO `HealthCareFacilities` VALUES
('487bdd9c-308a-4808-9f4d-f42208f399d5','2023-04-08 14:30:18','2023-04-08 14:30:18','Hospital','f5650445-ae97-4e26-a222-e1c3cc2f4d0f',NULL),
('6a2bab2c-35d3-4cbb-8ce2-edb2cafad650','2023-04-10 09:12:19','2023-04-10 09:12:19','Ore-Ofe Faith Home','76f9e883-c926-4035-bb6b-1cbc5279f444',NULL),
('c295ae81-ca73-4af0-a293-2e17f318d5f7','2023-04-06 17:21:10','2023-04-06 17:21:10','Hospital','f5650445-ae97-4e26-a222-e1c3cc2f4d0f',NULL);
/*!40000 ALTER TABLE `HealthCareFacilities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Hospital`
--

DROP TABLE IF EXISTS `Hospital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Hospital` (
  `address` varchar(1024) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(128) NOT NULL,
  `code` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Hospital`
--

LOCK TABLES `Hospital` WRITE;
/*!40000 ALTER TABLE `Hospital` DISABLE KEYS */;
/*!40000 ALTER TABLE `Hospital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Maternity`
--

DROP TABLE IF EXISTS `Maternity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Maternity` (
  `address` varchar(1024) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(128) NOT NULL,
  `code` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Maternity`
--

LOCK TABLES `Maternity` WRITE;
/*!40000 ALTER TABLE `Maternity` DISABLE KEYS */;
INSERT INTO `Maternity` VALUES
('Ile Ominira','76f9e883-c926-4035-bb6b-1cbc5279f444','2023-04-10 09:11:34','2023-04-10 09:12:19','Ore-Ofe Faith Home','MATOYSK293'),
('Ore Ofe Faith Home','f5650445-ae97-4e26-a222-e1c3cc2f4d0f','2023-04-06 17:20:42','2023-04-08 14:30:18','Hospital','MATOYSK123');
/*!40000 ALTER TABLE `Maternity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Patient`
--

DROP TABLE IF EXISTS `Patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Patient` (
  `occupation` varchar(60) DEFAULT NULL,
  `address` varchar(1024) DEFAULT NULL,
  `nxt_of_kin` varchar(256) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `nin` varchar(12) NOT NULL,
  `firstname` varchar(128) NOT NULL,
  `surname` varchar(128) NOT NULL,
  `middlename` varchar(128) DEFAULT NULL,
  `sex` varchar(15) NOT NULL,
  `dob` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `nin` (`nin`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Patient`
--

LOCK TABLES `Patient` WRITE;
/*!40000 ALTER TABLE `Patient` DISABLE KEYS */;
INSERT INTO `Patient` VALUES
(NULL,NULL,NULL,NULL,'b63e7956-8a93-4ec1-a4d9-4b2c792c124b','2023-03-25 11:11:11','2023-03-25 11:12:06','28928736278','Joseph','Aderemi','Iyanu','Male','1995-04-01 00:00:00'),
(NULL,NULL,NULL,NULL,'e41f2b35-4b48-4c8b-bf7d-1df7b6d26e92','2023-04-02 21:03:38','2023-04-03 10:30:27','09876543212','Tayo','Tayo','Tayo','female','1990-05-21 00:00:00');
/*!40000 ALTER TABLE `Patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientLogin`
--

DROP TABLE IF EXISTS `patientLogin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patientLogin` (
  `email` varchar(60) NOT NULL,
  `user_id` varchar(80) DEFAULT NULL,
  `hashed_password` varchar(250) NOT NULL,
  `nin` varchar(20) NOT NULL,
  `session_id` varchar(250) DEFAULT NULL,
  `reset_token` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `nin` (`nin`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `patientLogin_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Patient` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientLogin`
--

LOCK TABLES `patientLogin` WRITE;
/*!40000 ALTER TABLE `patientLogin` DISABLE KEYS */;
INSERT INTO `patientLogin` VALUES
('aderemi@joe.com','b63e7956-8a93-4ec1-a4d9-4b2c792c124b','myrose','28928736278','9418c1ac-7cc5-4ba6-bd2b-f15837f559b4',NULL);
/*!40000 ALTER TABLE `patientLogin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staffLogin`
--

DROP TABLE IF EXISTS `staffLogin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staffLogin` (
  `email` varchar(60) NOT NULL,
  `staff_id` varchar(80) DEFAULT NULL,
  `hashed_password` varchar(250) NOT NULL,
  `nin` varchar(20) NOT NULL,
  `auth_inst` varchar(200) NOT NULL,
  `session_id` varchar(250) DEFAULT NULL,
  `reset_token` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `nin` (`nin`),
  KEY `staff_id` (`staff_id`),
  CONSTRAINT `staffLogin_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `Doctor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staffLogin`
--

LOCK TABLES `staffLogin` WRITE;
/*!40000 ALTER TABLE `staffLogin` DISABLE KEYS */;
INSERT INTO `staffLogin` VALUES
('ini2win@gmail.com','2812ad2c-c3e7-438d-8d85-8d94fde374e1','edward','873908487892','[\"MATOYSK123\", \"MATOYSK293\"]','a2b4106d-de9d-4b76-ae67-d5021eb429ea',NULL),
('rose@aderemi.com','fbbea63b-f3c5-4229-8be2-26de2edca124','yohanna','12121212334','[\"MATOYSK123\", \"MATOYSK293\"]','b73e4b0e-6131-4ffb-97b7-996eea6e7523',NULL),
('rosey@aderemi.com','6c1d7749-95d7-4ed0-8232-4ca118941b2d','yohanna','12345654321','[\"MATOYSK123\", \"MATOYSK293\"]','830a3708-804a-4dc5-9d14-c5e93da54185',NULL);
/*!40000 ALTER TABLE `staffLogin` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-10 13:44:24
