-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2018 at 08:53 AM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `testcasedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `testcases`
--

CREATE TABLE `testcases` (
  `ID` int(11) NOT NULL,
  `testCaseName` varchar(100) NOT NULL,
  `command` varchar(100) NOT NULL,
  `target` text NOT NULL,
  `value` varchar(100) NOT NULL,
  `dateCreated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `testcases`
--

INSERT INTO `testcases` (`ID`, `testCaseName`, `command`, `target`, `value`, `dateCreated`) VALUES
(1, 'xmlkatalon.xml', 'open', 'https://www.google.mu/search?q=gmail&rlz=1C1SQJL_en-gbMU799MU799&oq=gmail&aqs=chrome.0.0j69i61j69i60', '', '2018-06-06 09:34:38'),
(2, 'xmlkatalon.xml', 'click', 'link=Gmail - Google', '', '2018-06-06 09:34:38'),
(3, 'xmlkatalon.xml', 'click', '//div[@id=\'view_container\']/form/div[2]/div/div/div/ul/li[2]/div/div[2]/p', '', '2018-06-06 09:34:38'),
(4, 'xmlkatalon.xml', 'type', 'name=password', '1234', '2018-06-06 09:34:38'),
(5, 'xmlkatalon.xml', 'click', '//div[@id=\'passwordNext\']/div[2]', '', '2018-06-06 09:34:38'),
(6, 'xmlkatalon.xml', 'click', '//body[@id=\'yDmH0d\']/div', '', '2018-06-06 09:34:38'),
(7, 'xmlkatalon.xml', 'click', '//body[@id=\'yDmH0d\']/div', '', '2018-06-06 09:34:38'),
(8, 'facebooktests.xml', 'open', 'https://www.facebook.com/', '', '2018-06-07 09:37:34'),
(9, 'facebooktests.xml', 'type', 'id=email', 'salmanplaystation2@gmail.com', '2018-06-07 09:37:35'),
(10, 'facebooktests.xml', 'click', 'id=pass', '', '2018-06-07 09:37:35'),
(11, 'facebooktests.xml', 'type', 'id=pass', '12345678', '2018-06-07 09:37:35'),
(12, 'facebooktests.xml', 'click', 'id=u_0_3', '', '2018-06-07 09:37:35'),
(13, 'facebooktests.xml', 'assertElementPresent', '//div[@id=\'globalContainer\']/div[3]/div/div', '', '2018-06-07 09:37:35'),
(14, 'facebooktests.xml', 'assertElementPresent', 'link=Recover Your Account', '', '2018-06-07 09:37:35'),
(15, 'facebooktests.xml', 'assertElementPresent', 'id=email', '', '2018-06-07 09:37:35'),
(39, 'kaufmanverifier.xml', 'open', 'https://www.kaufmanbroad.fr/', '', '2018-06-07 16:33:21'),
(40, 'kaufmanverifier.xml', 'click', '//section[@id=\'hp-avant-premiere\']/div/div/div/div[3]/article/div[2]/div/a/p[2]', '', '2018-06-07 16:33:21'),
(41, 'kaufmanverifier.xml', 'click', '//div[@id=\'node-809982\']/div/div[7]/header/section/div[3]/div/a[2]/span/span[2]', '', '2018-06-07 16:33:21'),
(42, 'kaufmanverifier.xml', 'waitForVisible', '//form[@id=\'webform-formulaire-rendez-vous\']/div', '', '2018-06-07 16:33:21'),
(43, 'kaufmanverifier.xml', 'click', 'xpath=(//input[@name=\'nom\'])[14]', '', '2018-06-07 16:33:21'),
(44, 'kaufmanverifier.xml', 'type', 'xpath=(//input[@name=\'nom\'])[14]', '123', '2018-06-07 16:33:21'),
(45, 'kaufmanverifier.xml', 'click', 'xpath=(//input[@name=\'prenom\'])[14]', '', '2018-06-07 16:33:22'),
(46, 'kaufmanverifier.xml', 'type', 'xpath=(//input[@name=\'prenom\'])[14]', '123', '2018-06-07 16:33:22'),
(47, 'kaufmanverifier.xml', 'click', 'id=btn-formulaire-rendez-vous', '', '2018-06-07 16:33:22'),
(48, 'kaufmanverifier.xml', 'assertTextPresent', ' Sans acceptation de ces conditions dâ€™utilisation, Kaufman & Broad ne peut accÃ©der Ã  votre demande de rendez-vous', '', '2018-06-07 16:33:22');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `testcases`
--
ALTER TABLE `testcases`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `testcases`
--
ALTER TABLE `testcases`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
