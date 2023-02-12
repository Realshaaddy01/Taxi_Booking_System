-- phpMyAdmin SQL Dump
-- version 5.3.0-dev+20230111.1d37607132
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 12, 2023 at 09:59 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bajeko_taxi_service`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `AID` int(100) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Phone` int(255) NOT NULL,
  `Password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`AID`, `Name`, `Address`, `Email`, `Phone`, `Password`) VALUES
(1, 'admin', 'addressAdmin', 'admin', 981, 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `CID` int(100) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `Age` varchar(3) NOT NULL,
  `Password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`CID`, `Name`, `Address`, `Email`, `Phone`, `Age`, `Password`) VALUES
(94, 'anjil', 'ktm', 'anjiL@gmail.com', '9817564', '25`', 'anjil123'),
(95, 'roshan sathi', 'banepa', 'roshan@gmail.com', '9823263456', '24', 'roshan123'),
(96, 'nzl_kharel', 'damak', 'nzl1@gmail.com', '98456456', '25', 'anjil123'),
(97, 'nzl', 'bhaktapur', 'nzl1@gmail.com', '981564564', '25', 'anjil123'),
(98, 'nzl_kharel', 'bhaktapur', 'nzl1@gmail.com', '98178594', '12', 'anjil123'),
(100, 'nzl', 'bhaktapur', 'nzlc1@gmail.com', '9817942834', '25', 'anjil123'),
(101, 'avi_sek', 'ktm,baneswor', 'avishek@gmail.com', '9817942834', '25', 'Anjil@1234'),
(102, 'anjil_kharel', 'bkt,baneshwor', 'anjil@gmail.com', '9817942834', '25', 'Nzl@123456'),
(103, 'john doe', 'usa,las vegas', 'john@gmail.com', '9845125432', '25', 'johN@123'),
(104, 'david ', 'uk,london', 'david@gmail.com', '9817564565', '24', 'David@123');

-- --------------------------------------------------------

--
-- Table structure for table `drivers`
--

CREATE TABLE `drivers` (
  `DID` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Phone` int(10) NOT NULL,
  `Liscense_num` int(16) NOT NULL,
  `Registration_num` int(4) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `driver_status` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `drivers`
--

INSERT INTO `drivers` (`DID`, `Name`, `Address`, `Email`, `Phone`, `Liscense_num`, `Registration_num`, `Password`, `driver_status`) VALUES
(40, 'nzl', 'damak', 'nzl@gmail.com', 2147483647, 123456, 0, 'nzl@123', 'inactive'),
(41, 'dhiwang', 'kadaghari', 'dhiwang@gmail.com', 2147483647, 2147483647, 0, 'dhiwang123', 'inactive'),
(42, 'nzl_kharel', 'lalitpur', 'nzld@gmail.com', 98179462, 253544, 0, 'anjild1', 'active'),
(43, '', '', '', 0, 0, 0, '', 'inactive'),
(44, 'nzl', 'dmaka', 'nzl123@gmail.com', 98426, 23154456, 100, 'nzl@12345', 'active'),
(45, 'angelina jolie', 'usa, las vegas', 'angelina@gmail.com', 2147483647, 545665, 100, 'Angelina@123', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `trips`
--

CREATE TABLE `trips` (
  `TID` int(11) NOT NULL,
  `Payment` varchar(255) NOT NULL,
  `Pickup` varchar(255) NOT NULL,
  `Dropoff` varchar(255) NOT NULL,
  `Time` varchar(255) NOT NULL,
  `Date` varchar(255) NOT NULL,
  `CID` int(100) DEFAULT NULL,
  `DID` int(11) DEFAULT NULL,
  `booking_status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `trips`
--

INSERT INTO `trips` (`TID`, `Payment`, `Pickup`, `Dropoff`, `Time`, `Date`, `CID`, `DID`, `booking_status`) VALUES
(32, '100', 'kupondole', 'baneshwor', '10:00', '21/12/2023', 94, 40, 'completed'),
(33, '1000', 'ktm', 'bkt', '2:00', '1/10/2023', 94, 41, 'booked'),
(34, '20', 'banepa', 'kupondole', '5:00', '20/1/22', 95, NULL, 'pending'),
(35, '1200', 'bkt', 'llt', '1:00', '1/10/2023', 94, 42, 'completed'),
(36, '500', 'KTM', 'KPL', '2:59 PM', '1/12/23', 94, 43, 'booked'),
(37, '500', 'ktm', 'bkt', '12:59 PM', '1/13/23', 102, 42, 'booked'),
(38, '500', 'ktm', 'bkt', '4:59 AM5:00', '1/2/23', 95, 40, 'completed'),
(39, '500', 'bedford', 'london', '1:59 PM', '2/8/23', 104, 40, 'booked'),
(40, '500', 'london', 'bedford', '3:59 PM', '2/16/23', 104, 45, 'completed');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`AID`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`CID`);

--
-- Indexes for table `drivers`
--
ALTER TABLE `drivers`
  ADD PRIMARY KEY (`DID`);

--
-- Indexes for table `trips`
--
ALTER TABLE `trips`
  ADD PRIMARY KEY (`TID`),
  ADD KEY `CID` (`CID`),
  ADD KEY `DID` (`DID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `AID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `CID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT for table `drivers`
--
ALTER TABLE `drivers`
  MODIFY `DID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `trips`
--
ALTER TABLE `trips`
  MODIFY `TID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `trips`
--
ALTER TABLE `trips`
  ADD CONSTRAINT `trips_ibfk_1` FOREIGN KEY (`CID`) REFERENCES `customers` (`CID`),
  ADD CONSTRAINT `trips_ibfk_2` FOREIGN KEY (`DID`) REFERENCES `drivers` (`DID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
