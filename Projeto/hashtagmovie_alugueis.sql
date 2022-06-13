-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: hashtagmovie
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
-- Table structure for table `alugueis`
--

DROP TABLE IF EXISTS `alugueis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alugueis` (
  `id_aluguel` int DEFAULT NULL,
  `id_cliente` int DEFAULT NULL,
  `id_filme` int DEFAULT NULL,
  `nota` text,
  `data_aluguel` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alugueis`
--

LOCK TABLES `alugueis` WRITE;
/*!40000 ALTER TABLE `alugueis` DISABLE KEYS */;
INSERT INTO `alugueis` VALUES (1,41,8,NULL,'2018/10/09'),(2,10,29,'10','2017/03/01'),(3,108,45,'4','2018/06/08'),(4,39,66,'8','2018/10/22'),(5,104,15,'7','2019/03/18'),(6,50,71,'7','2018/10/09'),(7,52,21,NULL,'2018/11/10'),(8,73,65,'10','2018/06/05'),(9,78,2,NULL,'2017/09/03'),(10,121,43,NULL,'2017/11/08'),(11,61,61,NULL,'2017/06/04'),(12,52,65,'10','2018/06/29'),(13,34,58,'7','2017/05/14'),(14,8,29,NULL,'2018/08/03'),(15,13,5,'10','2017/11/25'),(16,59,59,NULL,'2018/08/12'),(17,22,46,'10','2019/02/16'),(18,36,39,'10','2019/03/20'),(19,99,12,NULL,'2018/09/16'),(20,73,32,NULL,'2018/09/01'),(21,30,60,'10','2018/02/20'),(22,19,35,NULL,'2017/05/03'),(23,46,6,'9','2018/04/09'),(24,57,41,'7','2018/08/16'),(25,66,49,'7','2017/08/09'),(26,118,27,'8','2018/12/01'),(27,7,36,NULL,'2019/03/14'),(28,113,40,'7','2018/04/05'),(29,102,66,'7','2018/07/25'),(30,65,47,'10','2017/11/17'),(31,29,64,NULL,'2018/11/20'),(32,8,42,'10','2019/02/13'),(33,111,63,'8','2018/07/11'),(34,52,14,'6','2018/09/02'),(35,91,7,'8','2019/03/27'),(36,87,19,NULL,'2017/12/03'),(37,92,37,NULL,'2018/05/26'),(38,108,62,'10','2018/09/15'),(39,25,52,NULL,'2018/08/28'),(40,39,27,'8','2019/03/22'),(41,70,57,'9','2018/05/13'),(42,31,43,'6','2019/02/26'),(43,109,35,NULL,'2019/01/22'),(44,62,52,'6','2019/01/04'),(45,12,10,'6','2019/04/13'),(46,105,12,'10','2018/05/30'),(47,72,67,NULL,'2018/05/19'),(48,57,25,NULL,'2018/06/06'),(49,117,15,NULL,'2019/03/01'),(50,29,23,NULL,'2018/08/02'),(51,94,60,NULL,'2018/02/03'),(52,103,70,NULL,'2018/10/11'),(53,3,23,NULL,'2019/03/13'),(54,47,42,'8','2019/03/13'),(55,66,37,NULL,'2018/04/09'),(56,81,6,'10','2018/12/25'),(57,25,29,'6','2018/04/05'),(58,56,50,'6','2019/05/01'),(59,41,44,'4','2017/09/18'),(60,99,14,NULL,'2018/04/18'),(61,89,57,'8','2018/04/23'),(62,76,45,'7','2019/04/17'),(63,94,49,'10','2018/12/10'),(64,28,7,'7','2018/03/22'),(65,61,29,'9','2018/11/27'),(66,111,34,NULL,'2017/09/26'),(67,42,21,NULL,'2019/03/19'),(68,21,6,'9','2017/06/29'),(69,18,16,'6','2019/03/06'),(70,10,44,NULL,'2017/12/17'),(71,111,1,'5','2018/07/21'),(72,63,66,'5','2018/12/31'),(73,103,33,'9','2017/09/04'),(74,13,34,'7','2017/06/28'),(75,26,70,NULL,'2017/11/03'),(76,112,10,NULL,'2018/08/31'),(77,99,8,NULL,'2017/08/19'),(78,31,13,'10','2018/08/02'),(79,35,69,'9','2017/07/03'),(80,72,64,NULL,'2017/09/12'),(81,114,30,'10','2019/02/09'),(82,74,29,NULL,'2019/02/15'),(83,120,61,'6','2018/08/26'),(84,82,12,NULL,'2018/03/01'),(85,95,63,'10','2017/12/30'),(86,121,19,'9','2018/10/12'),(87,64,63,NULL,'2019/04/24'),(88,114,16,NULL,'2018/05/20'),(89,25,8,NULL,'2018/11/29'),(90,86,9,'10','2018/09/09'),(91,118,40,'5','2018/09/22'),(92,112,47,'9','2019/03/12'),(93,54,2,'8','2018/11/02'),(94,91,54,NULL,'2018/11/23'),(95,107,49,'9','2019/02/09'),(96,97,4,'7','2018/01/15'),(97,35,58,'9','2017/06/19'),(98,93,40,'7','2018/12/06'),(99,96,36,'7','2019/04/21'),(100,33,18,'6','2018/08/23'),(101,62,36,NULL,'2019/03/03'),(102,92,66,'6','2018/08/18'),(103,46,36,'7','2017/09/16'),(104,100,29,'6','2019/03/11'),(105,91,62,'9','2018/11/30'),(106,27,7,NULL,'2019/02/27'),(107,24,36,NULL,'2019/04/19'),(108,31,33,NULL,'2018/10/02'),(109,21,1,NULL,'2018/07/17'),(110,67,31,NULL,'2018/12/12'),(111,113,24,'6','2018/02/04'),(112,21,30,'5','2018/09/06'),(113,49,51,'9','2018/02/16'),(114,85,36,'8','2019/02/09'),(115,13,44,'7','2019/02/06'),(116,57,56,'9','2019/02/06'),(117,84,53,NULL,'2018/10/27'),(118,35,31,'5','2017/10/02'),(119,27,21,'7','2019/03/08'),(120,116,50,NULL,'2018/07/25'),(121,38,49,'8','2017/12/19'),(122,26,19,NULL,'2018/05/13'),(123,77,25,'7','2018/12/10'),(124,107,6,NULL,'2018/06/14'),(125,52,16,'9','2018/08/10'),(126,53,57,'9','2019/04/25'),(127,46,25,NULL,'2018/01/04'),(128,44,14,NULL,'2019/04/18'),(129,107,49,'9','2018/10/13'),(130,71,40,'10','2019/04/24'),(131,92,19,NULL,'2018/11/27'),(132,90,22,NULL,'2019/03/15'),(133,26,24,'10','2018/11/29'),(134,67,52,NULL,'2018/12/09'),(135,88,34,NULL,'2019/04/22'),(136,108,25,'8','2017/11/03'),(137,121,32,NULL,'2018/09/07'),(138,55,59,NULL,'2018/03/15'),(139,74,46,'7','2018/05/11'),(140,92,52,NULL,'2019/01/11'),(141,54,63,'9','2019/02/17'),(142,19,53,NULL,'2019/02/09'),(143,62,63,NULL,'2019/02/07'),(144,94,61,'10','2017/12/28'),(145,109,10,'6','2019/02/16'),(146,95,34,'10','2017/09/05'),(147,58,64,'5','2018/06/27'),(148,114,52,NULL,'2019/01/26'),(149,49,46,NULL,'2017/06/02'),(150,64,40,NULL,'2018/12/14'),(151,26,23,'8','2017/12/25'),(152,97,63,NULL,'2017/07/28'),(153,113,8,NULL,'2018/01/13'),(154,79,23,'8','2018/06/19'),(155,78,26,'7','2018/07/13'),(156,76,62,NULL,'2018/12/06'),(157,66,46,'9','2017/04/20'),(158,25,12,NULL,'2019/03/14'),(159,73,56,'7','2018/08/01'),(160,64,32,'9','2019/02/20'),(161,46,10,'8','2018/07/13'),(162,92,36,'8','2018/01/28'),(163,80,3,NULL,'2019/03/18'),(164,94,23,'8','2017/09/30'),(165,88,69,NULL,'2019/03/12'),(166,100,17,NULL,'2018/07/28'),(167,100,39,'10','2018/04/07'),(168,61,41,NULL,'2017/10/26'),(169,65,38,'10','2018/02/11'),(170,36,1,'10','2018/10/18'),(171,25,40,NULL,'2019/03/24'),(172,49,41,'8','2017/10/30'),(173,118,39,NULL,'2018/09/12'),(174,28,29,NULL,'2018/07/03'),(175,38,47,'9','2018/06/01'),(176,84,3,NULL,'2019/02/15'),(177,102,64,'10','2018/12/06'),(178,121,70,'9','2019/01/28'),(179,49,51,'6','2019/04/30'),(180,79,35,'7','2018/07/16'),(181,112,18,NULL,'2018/03/22'),(182,92,46,NULL,'2018/11/26'),(183,120,35,'8','2019/03/22'),(184,25,10,'6','2019/01/01'),(185,55,27,NULL,'2018/03/08'),(186,109,62,'7','2019/01/18'),(187,7,44,'8','2018/06/23'),(188,89,26,NULL,'2017/08/02'),(189,99,49,'10','2018/11/12'),(190,63,55,'5','2018/12/17'),(191,58,26,'10','2019/04/08'),(192,22,14,NULL,'2018/12/22'),(193,55,15,NULL,'2018/02/01'),(194,103,67,NULL,'2017/11/18'),(195,21,26,NULL,'2017/12/19'),(196,98,50,'9','2019/01/31'),(197,38,53,NULL,'2018/11/05'),(198,15,69,'9','2018/11/18'),(199,111,20,NULL,'2017/08/17'),(200,86,46,'3','2018/08/26'),(201,61,24,'8','2019/03/20'),(202,113,27,NULL,'2017/11/12'),(203,2,41,'6','2019/04/07'),(204,64,57,NULL,'2019/04/10'),(205,29,10,NULL,'2018/03/15'),(206,7,16,NULL,'2019/04/27'),(207,52,25,'5','2018/04/03'),(208,43,2,'7','2018/11/17'),(209,105,5,'9','2019/02/25'),(210,94,1,'7','2017/05/03'),(211,33,1,NULL,'2018/11/28'),(212,28,61,'8','2017/07/02'),(213,111,10,NULL,'2017/10/30'),(214,98,10,NULL,'2019/03/09'),(215,113,10,'6','2018/01/02'),(216,108,32,'7','2017/05/06'),(217,89,23,'7','2017/03/11'),(218,94,34,'6','2018/04/03'),(219,88,51,'8','2019/01/15'),(220,104,19,NULL,'2018/03/15'),(221,113,4,NULL,'2017/09/25'),(222,26,37,NULL,'2017/01/30'),(223,110,4,'7','2018/05/08'),(224,26,61,NULL,'2017/02/01'),(225,33,53,NULL,'2019/03/25'),(226,95,4,'9','2017/09/16'),(227,89,51,'10','2017/04/26'),(228,41,44,NULL,'2017/11/16'),(229,92,44,'7','2018/11/09'),(230,110,64,'8','2018/06/09'),(231,114,39,'6','2017/03/21'),(232,52,27,'8','2018/11/22'),(233,45,71,NULL,'2018/01/21'),(234,104,28,'4','2018/10/04'),(235,46,22,NULL,'2017/07/05'),(236,104,50,'7','2017/11/04'),(237,10,38,NULL,'2018/06/29'),(238,118,11,NULL,'2018/11/02'),(239,121,42,'10','2018/01/31'),(240,67,24,'8','2019/02/24'),(241,72,47,'7','2019/03/04'),(242,87,8,'8','2018/08/08'),(243,7,5,'10','2019/01/11'),(244,113,12,'7','2018/06/18'),(245,115,69,NULL,'2019/04/24'),(246,108,28,'9','2018/03/09'),(247,30,60,NULL,'2019/02/19'),(248,77,18,'10','2018/11/12'),(249,97,25,'10','2017/10/24'),(250,49,63,'9','2017/05/04'),(251,25,34,'10','2017/08/01'),(252,8,61,NULL,'2018/08/07'),(253,99,27,'9','2017/09/03'),(254,65,4,NULL,'2017/06/07'),(255,31,52,NULL,'2018/06/11'),(256,54,38,'6','2019/04/25'),(257,106,51,'8','2019/04/02'),(258,65,44,'8','2018/08/28'),(259,45,17,'8','2018/09/17'),(260,28,41,'7','2019/03/21'),(261,113,28,'8','2018/08/24'),(262,51,18,'10','2017/08/18'),(263,61,53,NULL,'2018/12/14'),(264,112,22,'10','2018/06/29'),(265,66,24,NULL,'2019/02/12'),(266,77,54,'6','2018/11/01'),(267,100,19,'7','2019/02/06'),(268,35,27,NULL,'2019/03/21'),(269,14,61,NULL,'2018/03/21'),(270,80,19,'8','2019/01/12'),(271,103,52,'7','2018/04/11'),(272,21,31,NULL,'2018/07/09'),(273,8,5,'10','2019/01/21'),(274,97,15,NULL,'2018/10/01'),(275,118,50,'10','2018/04/21'),(276,33,11,NULL,'2018/04/21'),(277,30,11,NULL,'2018/05/21'),(278,71,22,'9','2017/12/28'),(279,21,62,NULL,'2018/08/30'),(280,114,22,'9','2017/09/29'),(281,38,16,'9','2018/02/03'),(282,107,30,'7','2018/10/10'),(283,93,54,'9','2018/11/14'),(284,87,45,'8','2017/08/25'),(285,66,67,'6','2017/07/04'),(286,81,65,'7','2018/11/25'),(287,47,32,NULL,'2018/11/14'),(288,52,22,'7','2019/04/28'),(289,106,41,NULL,'2018/06/15'),(290,52,6,'9','2019/01/28'),(291,14,57,'8','2018/04/07'),(292,4,3,'8','2018/05/09'),(293,104,30,NULL,'2019/02/15'),(294,84,28,'10','2018/12/16'),(295,76,51,'8','2018/08/13'),(296,44,53,'8','2019/01/04'),(297,51,33,'7','2018/11/22'),(298,94,55,'10','2019/04/27'),(299,95,1,NULL,'2018/10/05'),(300,28,49,NULL,'2018/04/14'),(301,44,18,'10','2018/10/22'),(302,93,10,'9','2017/11/06'),(303,121,58,NULL,'2018/04/04'),(304,74,33,NULL,'2018/10/16'),(305,97,49,'10','2017/07/16'),(306,102,48,NULL,'2018/07/23'),(307,28,65,'9','2018/09/12'),(308,114,9,NULL,'2019/02/08'),(309,10,38,NULL,'2018/06/24'),(310,92,50,'7','2018/03/06'),(311,43,32,NULL,'2019/02/07'),(312,69,5,NULL,'2019/02/03'),(313,7,4,NULL,'2018/09/22'),(314,87,54,'10','2018/06/20'),(315,81,57,NULL,'2019/01/23'),(316,16,14,'9','2018/12/01'),(317,66,25,'6','2018/11/13'),(318,107,30,NULL,'2018/11/17'),(319,16,33,'9','2019/03/21'),(320,79,24,'10','2018/04/26'),(321,111,70,NULL,'2018/11/20'),(322,23,23,'9','2017/11/21'),(323,72,6,'7','2017/10/24'),(324,96,16,'9','2019/02/24'),(325,113,28,NULL,'2017/07/19'),(326,51,37,NULL,'2017/07/25'),(327,98,15,'6','2019/04/25'),(328,30,44,NULL,'2018/04/29'),(329,67,57,'9','2019/02/13'),(330,93,22,'8','2018/11/20'),(331,32,69,'7','2018/02/08'),(332,100,68,NULL,'2018/09/04'),(333,1,3,NULL,'2018/11/14'),(334,17,28,'10','2018/04/24'),(335,118,25,'8','2017/12/12'),(336,98,9,'8','2018/07/17'),(337,49,58,NULL,'2017/08/18'),(338,31,4,NULL,'2018/06/07'),(339,8,2,NULL,'2018/11/18'),(340,45,71,'9','2018/10/19'),(341,99,58,NULL,'2018/06/06'),(342,66,61,'9','2017/03/04'),(343,112,12,NULL,'2018/09/24'),(344,23,23,NULL,'2018/05/26'),(345,91,7,'7','2018/06/18'),(346,114,37,NULL,'2017/11/24'),(347,45,52,'5','2018/10/18'),(348,108,57,NULL,'2019/04/09'),(349,13,14,'5','2017/09/08'),(350,113,3,NULL,'2018/04/20'),(351,106,4,'8','2018/07/15'),(352,114,40,'10','2017/11/21'),(353,62,67,'10','2018/12/20'),(354,73,4,NULL,'2018/10/23'),(355,121,7,NULL,'2017/11/13'),(356,85,24,NULL,'2019/03/24'),(357,110,29,'8','2018/04/08'),(358,4,12,'7','2017/12/23'),(359,102,26,NULL,'2019/01/25'),(360,85,36,NULL,'2019/04/06'),(361,93,27,'9','2018/04/26'),(362,108,69,NULL,'2018/12/18'),(363,8,33,'7','2018/09/19'),(364,30,29,'7','2019/03/17'),(365,71,20,NULL,'2018/11/14'),(366,25,28,'7','2018/05/26'),(367,49,62,'7','2017/03/22'),(368,21,35,'9','2017/08/17'),(369,32,28,'7','2019/03/13'),(370,66,14,NULL,'2018/08/09'),(371,1,13,NULL,'2018/11/12'),(372,21,54,NULL,'2018/11/04'),(373,21,39,NULL,'2019/01/21'),(374,87,63,'10','2018/02/27'),(375,110,53,'6','2018/02/18'),(376,26,37,'9','2018/04/12'),(377,13,28,NULL,'2018/05/28'),(378,28,41,NULL,'2017/02/16'),(379,61,63,'10','2017/09/23'),(380,114,14,'6','2017/08/01'),(381,104,49,NULL,'2018/06/14'),(382,41,22,'9','2018/07/19'),(383,61,45,'9','2018/08/18'),(384,113,42,NULL,'2017/10/21'),(385,43,12,'6','2018/10/06'),(386,8,16,'10','2018/06/29'),(387,66,7,'10','2017/12/14'),(388,28,33,NULL,'2017/09/10'),(389,78,36,'7','2017/12/20'),(390,21,16,NULL,'2018/08/19'),(391,19,18,'9','2018/11/07'),(392,109,58,'9','2018/12/28'),(393,90,26,'8','2019/04/08'),(394,80,26,NULL,'2019/02/28'),(395,115,11,NULL,'2019/04/07'),(396,7,40,'10','2018/09/11'),(397,82,41,'9','2019/03/08'),(398,8,37,NULL,'2018/03/23'),(399,37,36,NULL,'2018/12/12'),(400,6,10,NULL,'2018/11/03'),(401,82,27,'7','2018/03/12'),(402,39,25,'8','2018/03/20'),(403,65,11,NULL,'2017/04/11'),(404,87,48,'10','2018/06/05'),(405,113,30,NULL,'2017/07/07'),(406,23,3,NULL,'2017/10/22'),(407,84,48,NULL,'2018/09/10'),(408,55,61,NULL,'2018/10/20'),(409,46,36,'5','2018/06/17'),(410,96,3,'10','2018/10/20'),(411,58,50,'10','2019/01/23'),(412,103,41,'10','2018/06/22'),(413,92,29,'10','2018/02/07'),(414,59,4,'10','2018/06/04'),(415,106,71,NULL,'2018/11/25'),(416,108,70,'10','2017/04/09'),(417,103,23,'10','2017/12/31'),(418,17,4,'9','2019/01/02'),(419,31,12,'9','2019/02/21'),(420,26,41,'8','2019/01/09'),(421,1,71,'10','2019/01/21'),(422,49,67,'7','2018/09/10'),(423,35,34,'6','2018/07/14'),(424,50,25,NULL,'2019/04/11'),(425,21,9,'7','2019/02/15'),(426,46,68,'5','2017/11/24'),(427,65,47,NULL,'2018/07/01'),(428,79,41,NULL,'2018/06/09'),(429,55,21,NULL,'2018/02/09'),(430,58,68,'7','2018/12/22'),(431,19,7,NULL,'2018/09/14'),(432,107,40,NULL,'2019/03/09'),(433,113,42,'10','2017/08/30'),(434,19,52,'9','2018/06/24'),(435,98,2,'7','2017/10/02'),(436,116,45,NULL,'2018/10/28'),(437,99,33,'10','2019/04/28'),(438,66,61,'9','2018/04/10'),(439,64,27,NULL,'2019/02/23'),(440,18,49,'10','2019/01/21'),(441,50,27,'9','2018/04/26'),(442,38,58,NULL,'2018/08/08'),(443,83,54,'7','2019/04/20'),(444,120,59,'3','2018/08/10'),(445,117,63,NULL,'2019/04/04'),(446,37,68,NULL,'2019/02/27'),(447,85,30,NULL,'2019/01/15'),(448,123,64,'10','2019/03/22'),(449,72,66,NULL,'2018/08/01'),(450,23,54,'7','2019/02/11'),(451,111,15,NULL,'2019/03/25'),(452,49,7,NULL,'2018/03/07'),(453,121,52,'7','2018/07/10'),(454,118,32,'6','2018/08/28'),(455,86,35,NULL,'2018/11/25'),(456,7,3,NULL,'2018/05/23'),(457,25,30,'7','2019/03/03'),(458,93,47,NULL,'2019/04/24'),(459,50,38,NULL,'2018/08/20'),(460,97,34,'9','2017/10/23'),(461,68,67,NULL,'2019/04/27'),(462,58,43,NULL,'2019/02/22'),(463,29,68,NULL,'2018/08/28'),(464,108,9,NULL,'2018/02/11'),(465,84,42,NULL,'2019/02/11'),(466,17,21,NULL,'2018/06/20'),(467,99,41,'8','2017/12/21'),(468,15,32,'7','2019/01/30'),(469,35,69,'8','2018/04/05'),(470,108,29,NULL,'2017/04/25'),(471,49,3,NULL,'2019/01/01'),(472,54,33,NULL,'2019/02/09'),(473,60,58,NULL,'2019/03/24'),(474,123,51,'10','2019/01/07'),(475,21,4,'6','2019/02/07'),(476,78,42,'10','2018/07/04'),(477,5,68,NULL,'2019/04/01'),(478,4,13,'7','2018/04/13'),(479,42,70,'5','2019/02/17'),(480,53,42,NULL,'2019/04/15'),(481,94,7,NULL,'2017/04/20'),(482,113,1,NULL,'2018/11/29'),(483,49,2,'7','2017/04/02'),(484,19,11,NULL,'2019/02/23'),(485,30,16,NULL,'2018/05/04'),(486,41,40,NULL,'2018/06/29'),(487,61,48,'10','2017/08/14'),(488,100,71,'6','2019/04/09'),(489,14,27,NULL,'2018/10/21'),(490,52,19,'9','2018/07/28'),(491,49,31,'8','2017/12/17'),(492,103,17,NULL,'2019/04/13'),(493,102,1,'7','2018/10/28'),(494,105,13,'7','2019/03/06'),(495,41,66,'8','2018/10/21'),(496,13,69,'6','2017/07/20'),(497,23,24,NULL,'2018/04/22'),(498,115,42,NULL,'2019/03/16'),(499,98,41,'7','2017/12/01'),(500,17,57,'10','2018/11/05'),(501,97,20,'7','2017/12/30'),(502,35,58,NULL,'2017/12/27'),(503,114,12,NULL,'2017/08/05'),(504,26,3,NULL,'2017/02/14'),(505,91,61,NULL,'2018/01/28'),(506,105,26,NULL,'2018/10/07'),(507,98,37,'7','2018/02/09'),(508,21,16,NULL,'2018/02/09'),(509,59,14,'6','2018/06/05'),(510,36,31,NULL,'2018/09/19'),(511,26,45,'7','2017/05/15'),(512,91,62,NULL,'2019/04/04'),(513,116,59,'9','2019/02/08'),(514,92,31,'6','2018/05/20'),(515,104,14,'7','2017/07/24'),(516,72,30,NULL,'2017/10/22'),(517,25,5,NULL,'2017/09/13'),(518,1,25,NULL,'2018/12/17'),(519,111,58,NULL,'2017/06/27'),(520,1,39,'6','2018/12/29'),(521,110,20,NULL,'2018/09/09'),(522,86,33,NULL,'2018/04/27'),(523,27,38,'10','2019/03/22'),(524,15,60,'7','2018/09/07'),(525,14,4,'7','2018/09/09'),(526,109,52,'7','2019/03/03'),(527,112,37,'7','2019/01/08'),(528,49,27,NULL,'2017/04/12'),(529,39,23,'6','2018/09/26'),(530,104,17,NULL,'2019/04/19'),(531,121,48,NULL,'2018/06/04'),(532,79,7,'8','2019/02/08'),(533,123,12,'8','2019/01/16'),(534,65,26,NULL,'2017/08/20'),(535,57,32,NULL,'2018/04/21'),(536,7,50,'8','2018/09/16'),(537,82,52,'9','2019/03/06'),(538,76,36,'9','2019/01/06'),(539,65,45,NULL,'2017/07/29'),(540,91,4,'8','2018/04/26'),(541,123,64,NULL,'2019/04/15'),(542,110,50,'7','2018/06/04'),(543,89,54,NULL,'2018/11/06'),(544,17,41,NULL,'2018/06/14'),(545,94,54,'10','2019/01/23'),(546,111,41,'8','2018/06/08'),(547,65,63,NULL,'2018/08/17'),(548,34,70,'7','2018/07/11'),(549,119,44,'10','2019/04/29'),(550,21,53,'8','2019/03/17'),(551,86,13,'8','2018/08/29'),(552,28,56,'1','2017/03/27'),(553,93,59,NULL,'2017/04/28'),(554,34,49,'8','2019/04/22'),(555,10,5,NULL,'2018/12/02'),(556,94,42,NULL,'2018/08/20'),(557,78,25,'8','2018/10/11'),(558,41,19,'3','2019/01/13'),(559,93,3,NULL,'2018/02/17'),(560,11,49,'6','2019/04/18'),(561,113,36,'5','2018/06/29'),(562,33,18,NULL,'2019/03/10'),(563,29,5,NULL,'2018/05/11'),(564,114,68,'7','2017/12/06'),(565,63,53,'10','2018/10/25'),(566,28,45,'7','2018/05/29'),(567,28,49,'8','2019/02/24'),(568,29,43,NULL,'2018/09/15'),(569,78,26,NULL,'2018/08/16'),(570,87,56,NULL,'2018/03/31'),(571,92,28,'9','2018/11/22'),(572,4,61,'6','2019/04/16'),(573,111,23,NULL,'2018/09/24'),(574,7,14,NULL,'2019/02/08'),(575,45,31,'10','2018/06/09'),(576,38,25,NULL,'2018/09/02'),(577,35,65,'9','2017/07/03'),(578,35,16,NULL,'2017/06/20');
/*!40000 ALTER TABLE `alugueis` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-01 10:45:56
