-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: data
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contracts`
--

DROP TABLE IF EXISTS `contracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contracts` (
  `contract_no` int NOT NULL,
  `supplier_no` int DEFAULT NULL,
  `date_of_contract` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`contract_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contracts`
--

LOCK TABLES `contracts` WRITE;
/*!40000 ALTER TABLE `contracts` DISABLE KEYS */;
INSERT INTO `contracts` VALUES (201,111,'03/12/2018'),(202,105,'12/24/2020'),(203,109,'08/14/2018'),(204,115,'01/11/2019'),(205,111,'05/29/2017'),(206,115,'03/24/2019'),(207,108,'12/11/2020'),(208,107,'12/18/2018'),(209,101,'03/20/2019'),(210,101,'05/22/2018'),(211,109,'02/15/2018'),(212,115,'09/05/2017'),(213,113,'09/25/2019'),(214,114,'07/12/2020'),(215,110,'12/12/2020'),(216,116,'05/11/2020'),(217,120,'05/14/2020');
/*!40000 ALTER TABLE `contracts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `item_no` int NOT NULL,
  `item_desc` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (501,'Hammer'),(502,'Shovel'),(503,'Cement'),(504,'Sand'),(505,'Spade'),(506,'Nails'),(507,'Screw'),(508,'Saw'),(509,'Drill'),(510,'Gloves'),(511,'Chisel'),(512,'Hoe'),(513,'Ladder'),(514,'Scale'),(515,'Trowel'),(516,'Shoe'),(517,'Belt'),(518,'Tie');
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `madeof`
--

DROP TABLE IF EXISTS `madeof`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `madeof` (
  `order_no` int NOT NULL,
  `item_no` int NOT NULL,
  `order_quantity` int DEFAULT NULL,
  PRIMARY KEY (`order_no`,`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `madeof`
--

LOCK TABLES `madeof` WRITE;
/*!40000 ALTER TABLE `madeof` DISABLE KEYS */;
INSERT INTO `madeof` VALUES (401,501,15),(401,511,10),(402,501,15),(403,502,12),(404,502,11),(405,503,14),(405,504,22),(406,504,14),(407,511,5),(408,516,3),(420,517,45),(426,517,120);
/*!40000 ALTER TABLE `madeof` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_no` int NOT NULL,
  `date_req` varchar(10) DEFAULT NULL,
  `date_comp` varchar(10) DEFAULT NULL,
  `contract_no` int DEFAULT NULL,
  `project_no` int DEFAULT NULL,
  PRIMARY KEY (`order_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (401,'01/23/2019','12/12/2018',209,301),(402,'02/05/2019','02/05/2019',212,301),(403,'03/02/2018','05/24/2018',201,307),(404,'05/10/2020','05/10/2020',201,314),(405,'12/15/2016','11/15/2016',213,307),(406,'11/27/2020','12/25/2020',207,301),(407,'10/24/2018','12/01/2018',209,311),(408,'5/11/2020','5/12/2020',216,316),(420,'5/15/2020','5/14/2020',222,320),(426,'5/16/2020','5/15/2020',256,356);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `project_no` int NOT NULL,
  `project_data` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`project_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES (301,'Playground'),(302,'Mall'),(303,'Park'),(304,'School'),(305,'College'),(306,'Gym'),(307,'Gym'),(308,'Playground'),(309,'Park'),(310,'Parking'),(311,'Office'),(312,'Theater'),(313,'Office'),(314,'Mall'),(315,'House'),(316,'Mall');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `supplier_no` int NOT NULL,
  `supplier_name` varchar(20) DEFAULT NULL,
  `supplier_address` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`supplier_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (101,'Shubham','Hicksville'),(102,'Daksha','HIcksville'),(103,'Darshan','Plainview'),(104,'Askhit','East Medow'),(105,'Abhisekh','Arizona'),(106,'Momina','Bay Shore'),(107,'Sagar','Delhi'),(108,'Kartik','Hydrabad'),(109,'Aniket','Mumbai'),(110,'Akshay','Punjab'),(111,'Helena','Gujrat'),(112,'Norma','Gujrat'),(113,'Muskan','Old Westbury'),(114,'Happy','Manhattan'),(115,'Nyit','Old Westbury'),(116,'Lalith','New York City');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tosupply`
--

DROP TABLE IF EXISTS `tosupply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tosupply` (
  `contract_no` int NOT NULL,
  `item_no` int NOT NULL,
  `contract_amt` int DEFAULT NULL,
  `contract_price` int DEFAULT NULL,
  PRIMARY KEY (`contract_no`,`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tosupply`
--

LOCK TABLES `tosupply` WRITE;
/*!40000 ALTER TABLE `tosupply` DISABLE KEYS */;
INSERT INTO `tosupply` VALUES (201,502,52,152),(203,510,85,352),(204,507,156,600),(206,508,15,95),(207,504,10,50),(209,501,15,85),(209,503,50,200),(209,511,100,400),(210,509,54,150),(212,501,158,300),(212,510,234,543),(213,504,145,650),(216,516,3,150),(217,517,160,56);
/*!40000 ALTER TABLE `tosupply` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-17 19:22:36
