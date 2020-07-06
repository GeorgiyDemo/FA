-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Apr 25, 2020 at 05:44 PM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `OVS`
--

-- --------------------------------------------------------

--
-- Table structure for table `task5`
--

CREATE TABLE `task5` (
  `id` int(11) NOT NULL,
  `name` varchar(455) NOT NULL,
  `radiobutton` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `task5`
--

INSERT INTO `task5` (`id`, `name`, `radiobutton`) VALUES
(1, 'КОТ', '2'),
(2, 'KOT1', '1'),
(3, 'Check', '1'),
(4, '44444', '1'),
(5, 'rtytryrt', '2'),
(6, '4435345', '1'),
(7, 'dsfdsf', '1'),
(8, 'rrrr', '2'),
(9, 'LASK CHECK', '2');

-- --------------------------------------------------------

--
-- Table structure for table `task9_nomenclature`
--

CREATE TABLE `task9_nomenclature` (
  `id` int(11) NOT NULL,
  `warehouse_id` int(11) NOT NULL,
  `name` varchar(455) NOT NULL,
  `amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `task9_nomenclature`
--

INSERT INTO `task9_nomenclature` (`id`, `warehouse_id`, `name`, `amount`) VALUES
(1, 1, 'Калькулятор CITIZEN SDC 888TII, 12-разрядный, черный', 10),
(2, 3, 'Koshka', 1),
(3, 2, 'MOEW', 123);

-- --------------------------------------------------------

--
-- Table structure for table `task9_users`
--

CREATE TABLE `task9_users` (
  `id` int(11) NOT NULL,
  `name` varchar(455) NOT NULL,
  `password` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `task9_users`
--

INSERT INTO `task9_users` (`id`, `name`, `password`) VALUES
(1, 'Деменчук Г.М.', '81dc9bdb52d04dc20036dbd8313ed055'),
(2, 'Сидоров А.А.', '202cb962ac59075b964b07152d234b70'),
(3, 'Алисова К.И.', '202cb962ac59075b964b07152d234b70');

-- --------------------------------------------------------

--
-- Table structure for table `task9_warehouse`
--

CREATE TABLE `task9_warehouse` (
  `id` int(11) NOT NULL,
  `name` varchar(455) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `task9_warehouse`
--

INSERT INTO `task9_warehouse` (`id`, `name`) VALUES
(1, 'Холодильник в Бутово'),
(2, 'Основной'),
(3, 'Перевалочный пункт Очаково');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `login` varchar(455) NOT NULL,
  `password` varchar(455) NOT NULL,
  `name` varchar(455) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`id`, `login`, `password`, `name`) VALUES
(1, '32d2a7cd182f298607cb7362a6b96e89', 'c4ca4238a0b923820dcc509a6f75849b', '0JPQtdC+0YDQs9C40Lk=');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `task5`
--
ALTER TABLE `task5`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `task9_nomenclature`
--
ALTER TABLE `task9_nomenclature`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `task9_users`
--
ALTER TABLE `task9_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `task9_warehouse`
--
ALTER TABLE `task9_warehouse`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login_UNIQUE` (`login`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `task5`
--
ALTER TABLE `task5`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `task9_nomenclature`
--
ALTER TABLE `task9_nomenclature`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `task9_users`
--
ALTER TABLE `task9_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `task9_warehouse`
--
ALTER TABLE `task9_warehouse`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
