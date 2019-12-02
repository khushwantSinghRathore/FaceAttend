-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2019 at 07:12 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `collegeattend`
--

-- --------------------------------------------------------

--
-- Table structure for table `algorithms`
--

CREATE TABLE `algorithms` (
  `1` int(11) NOT NULL,
  `2` int(11) NOT NULL,
  `3` int(11) NOT NULL,
  `4` int(11) NOT NULL,
  `5` int(11) NOT NULL,
  `6` int(11) NOT NULL,
  `7` int(11) NOT NULL,
  `8` int(11) NOT NULL,
  `9` int(11) NOT NULL,
  `10` int(11) NOT NULL,
  `classdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `algorithms`
--

INSERT INTO `algorithms` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`) VALUES
(1, 1, 0, 1, 1, 0, 0, 0, 0, 0, '2019-12-01');

-- --------------------------------------------------------

--
-- Table structure for table `classdate`
--

CREATE TABLE `classdate` (
  `subjectcode` varchar(10) NOT NULL,
  `Date` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `collgdatatable`
--

CREATE TABLE `collgdatatable` (
  `semestername` varchar(10) NOT NULL,
  `subject1` varchar(50) NOT NULL,
  `subject2` varchar(50) NOT NULL,
  `subject3` varchar(50) NOT NULL,
  `subject4` varchar(50) NOT NULL,
  `subject5` varchar(50) NOT NULL,
  `subject6` varchar(50) NOT NULL,
  `subject7` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `collgdatatable`
--

INSERT INTO `collgdatatable` (`semestername`, `subject1`, `subject2`, `subject3`, `subject4`, `subject5`, `subject6`, `subject7`) VALUES
('MCA1', 'InformationTechnology', 'ComputerOrganization', 'IntroductionToProgramming', 'BusinessFunctions', 'DiscreteMathematics', 'DigitalandMicroprocessorLab', 'ComputerProgrammingLab'),
('MCA2', 'DataStructure', 'ComputerArchitecture', 'ObjectOrientedProgrammingUsingC++', 'StructuredSystemAnalysisandDesign', 'NumericalComputationalMethods', 'DataStructureLab', 'ObjectOrientatedProgrammingLab'),
('MCA3', 'DatabaseSystems', 'OperatingSystem', 'Algorithms', 'ObjectOrientedProgrammingusingJava', 'ComputerNetworks', 'JavaLab', 'OperatingSystemLab'),
('MCA4', 'CompilerDesign', 'ComputerGraphics', 'ManagementandInformationSystems', 'NetworkManagementandInformationSecurity', 'ClientServerComputing', 'GraphicsLab', 'ClientServerComputingLab'),
('MCA5', 'SoftwareEngineering', 'ModelingandSimulation', 'ArtificialIntelligence', 'AdvancedJavaProgramming', 'EmbeddedSystemDesign', 'MinorProject', 'AdvancedJavaProgrammingLab'),
('MCA6', 'ProjectWork', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `computernetworks`
--

CREATE TABLE `computernetworks` (
  `1` int(11) NOT NULL,
  `2` int(11) NOT NULL,
  `3` int(11) NOT NULL,
  `4` int(11) NOT NULL,
  `5` int(11) NOT NULL,
  `6` int(11) NOT NULL,
  `7` int(11) NOT NULL,
  `8` int(11) NOT NULL,
  `9` int(11) NOT NULL,
  `10` int(11) NOT NULL,
  `classdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `computernetworks`
--

INSERT INTO `computernetworks` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`) VALUES
(0, 1, 1, 1, 1, 0, 0, 0, 0, 0, '2019-12-01');

-- --------------------------------------------------------

--
-- Table structure for table `databasesystems`
--

CREATE TABLE `databasesystems` (
  `1` int(11) NOT NULL,
  `2` int(11) NOT NULL,
  `3` int(11) NOT NULL,
  `4` int(11) NOT NULL,
  `5` int(11) NOT NULL,
  `6` int(11) NOT NULL,
  `7` int(11) NOT NULL,
  `8` int(11) NOT NULL,
  `9` int(11) NOT NULL,
  `10` int(11) NOT NULL,
  `classdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `databasesystems`
--

INSERT INTO `databasesystems` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`) VALUES
(1, 1, 1, 1, 1, 0, 0, 0, 0, 0, '2019-11-28'),
(0, 1, 1, 1, 0, 0, 0, 0, 0, 0, '2019-12-01'),
(1, 1, 1, 1, 1, 0, 0, 0, 0, 0, '2019-12-02');

-- --------------------------------------------------------

--
-- Table structure for table `javalab`
--

CREATE TABLE `javalab` (
  `1` int(11) NOT NULL,
  `2` int(11) NOT NULL,
  `3` int(11) NOT NULL,
  `4` int(11) NOT NULL,
  `5` int(11) NOT NULL,
  `6` int(11) NOT NULL,
  `7` int(11) NOT NULL,
  `8` int(11) NOT NULL,
  `9` int(11) NOT NULL,
  `10` int(11) NOT NULL,
  `classdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `javalab`
--

INSERT INTO `javalab` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`) VALUES
(1, 1, 1, 1, 1, 0, 0, 0, 0, 0, '2019-12-01');

-- --------------------------------------------------------

--
-- Table structure for table `objectorientedprogrammingusingc++`
--

CREATE TABLE `objectorientedprogrammingusingc++` (
  `1` int(11) NOT NULL,
  `2` int(11) NOT NULL,
  `3` int(11) NOT NULL,
  `4` int(11) NOT NULL,
  `5` int(11) NOT NULL,
  `6` int(11) NOT NULL,
  `7` int(11) NOT NULL,
  `8` int(11) NOT NULL,
  `9` int(11) NOT NULL,
  `10` int(11) NOT NULL,
  `classdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `objectorientedprogrammingusingc++`
--

INSERT INTO `objectorientedprogrammingusingc++` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`) VALUES
(1, 1, 1, 1, 1, 0, 0, 0, 0, 0, '2019-11-16'),
(1, 1, 0, 0, 1, 0, 0, 0, 0, 0, '2019-11-17'),
(1, 1, 0, 0, 1, 0, 0, 0, 0, 0, '2019-11-18'),
(1, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2019-11-28');

-- --------------------------------------------------------

--
-- Table structure for table `objectorientedprogrammingusingjava`
--

CREATE TABLE `objectorientedprogrammingusingjava` (
  `1` int(11) NOT NULL,
  `2` int(11) NOT NULL,
  `3` int(11) NOT NULL,
  `4` int(11) NOT NULL,
  `5` int(11) NOT NULL,
  `6` int(11) NOT NULL,
  `7` int(11) NOT NULL,
  `8` int(11) NOT NULL,
  `9` int(11) NOT NULL,
  `10` int(11) NOT NULL,
  `classdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `objectorientedprogrammingusingjava`
--

INSERT INTO `objectorientedprogrammingusingjava` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`) VALUES
(1, 1, 0, 1, 0, 0, 0, 0, 0, 0, '2019-12-01');

-- --------------------------------------------------------

--
-- Table structure for table `operatingsystem`
--

CREATE TABLE `operatingsystem` (
  `1` int(11) NOT NULL,
  `2` int(11) NOT NULL,
  `3` int(11) NOT NULL,
  `4` int(11) NOT NULL,
  `5` int(11) NOT NULL,
  `6` int(11) NOT NULL,
  `7` int(11) NOT NULL,
  `8` int(11) NOT NULL,
  `9` int(11) NOT NULL,
  `10` int(11) NOT NULL,
  `classdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `operatingsystem`
--

INSERT INTO `operatingsystem` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`) VALUES
(1, 1, 1, 1, 1, 0, 0, 0, 0, 0, '2019-12-01');

-- --------------------------------------------------------

--
-- Table structure for table `operatingsystemlab`
--

CREATE TABLE `operatingsystemlab` (
  `1` int(11) NOT NULL,
  `2` int(11) NOT NULL,
  `3` int(11) NOT NULL,
  `4` int(11) NOT NULL,
  `5` int(11) NOT NULL,
  `6` int(11) NOT NULL,
  `7` int(11) NOT NULL,
  `8` int(11) NOT NULL,
  `9` int(11) NOT NULL,
  `10` int(11) NOT NULL,
  `classdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `operatingsystemlab`
--

INSERT INTO `operatingsystemlab` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`) VALUES
(1, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2019-12-01');

-- --------------------------------------------------------

--
-- Table structure for table `python`
--

CREATE TABLE `python` (
  `1` int(11) NOT NULL,
  `2` int(11) NOT NULL,
  `3` int(11) NOT NULL,
  `4` int(11) NOT NULL,
  `5` int(11) NOT NULL,
  `6` int(11) NOT NULL,
  `7` int(11) NOT NULL,
  `8` int(11) NOT NULL,
  `9` int(11) NOT NULL,
  `10` int(11) NOT NULL,
  `classdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `python`
--

INSERT INTO `python` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`) VALUES
(0, 1, 1, 1, 1, 0, 0, 0, 0, 0, '2019-11-28');

-- --------------------------------------------------------

--
-- Table structure for table `studentdetails`
--

CREATE TABLE `studentdetails` (
  `rollnum` varchar(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `fathername` varchar(30) NOT NULL,
  `enrollement` varchar(30) NOT NULL,
  `pic` varchar(255) DEFAULT NULL,
  `semester` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studentdetails`
--

INSERT INTO `studentdetails` (`rollnum`, `name`, `fathername`, `enrollement`, `pic`, `semester`) VALUES
('1', 'raj', 'aaj', '1225', 'rollpic1.png', 'MCA3'),
('2', 'kavita', 'kita', '1521', 'rollpic2.png', 'MCA3'),
('3', 'sita ', 'gita', '5848', 'rollpic3.png', 'MCA3'),
('4', 'rita ', 'pap', '95959', 'rollpic4.png', 'MCA3'),
('5', 'ram', 'dashraat', '55454', 'rollpic5.png', 'MCA3');

-- --------------------------------------------------------

--
-- Table structure for table `subjectteacher`
--

CREATE TABLE `subjectteacher` (
  `teacherid` varchar(30) NOT NULL,
  `subject1` varchar(50) DEFAULT NULL,
  `subject2` varchar(50) DEFAULT NULL,
  `subject3` varchar(50) DEFAULT NULL,
  `subject4` varchar(50) DEFAULT NULL,
  `subject5` varchar(50) DEFAULT NULL,
  `subject6` varchar(50) DEFAULT NULL,
  `subject7` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subjectteacher`
--

INSERT INTO `subjectteacher` (`teacherid`, `subject1`, `subject2`, `subject3`, `subject4`, `subject5`, `subject6`, `subject7`) VALUES
('khush123', 'OperatingSystem', 'Algorithms', 'ObjectOrientedProgrammingusingJava', 'ComputerNetworks', 'JavaLab', 'OperatingSystemLab', 'DatabaseSystems'),
('mcaraj', 'JavaLab', 'OperatingSystemLab', 'ComputerNetworks', 'CompilerDesign', 'ComputerGraphics', 'BusinessFunctions', 'DigitalandMicroprocessorLab');

-- --------------------------------------------------------

--
-- Table structure for table `userdatabase`
--

CREATE TABLE `userdatabase` (
  `userid` varchar(15) NOT NULL,
  `pass` varchar(255) NOT NULL,
  `teachername` varchar(25) NOT NULL,
  `contact` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userdatabase`
--

INSERT INTO `userdatabase` (`userid`, `pass`, `teachername`, `contact`) VALUES
('khush123', '8cb2237d0679ca88db6464eac60da96345513964', 'khushwant singh rathore', '2147483647'),
('mcaraj', '8cb2237d0679ca88db6464eac60da96345513964', 'raj', '8003430781');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `algorithms`
--
ALTER TABLE `algorithms`
  ADD PRIMARY KEY (`classdate`);

--
-- Indexes for table `collgdatatable`
--
ALTER TABLE `collgdatatable`
  ADD PRIMARY KEY (`semestername`) USING BTREE;

--
-- Indexes for table `computernetworks`
--
ALTER TABLE `computernetworks`
  ADD PRIMARY KEY (`classdate`);

--
-- Indexes for table `databasesystems`
--
ALTER TABLE `databasesystems`
  ADD PRIMARY KEY (`classdate`);

--
-- Indexes for table `javalab`
--
ALTER TABLE `javalab`
  ADD PRIMARY KEY (`classdate`);

--
-- Indexes for table `objectorientedprogrammingusingc++`
--
ALTER TABLE `objectorientedprogrammingusingc++`
  ADD PRIMARY KEY (`classdate`);

--
-- Indexes for table `objectorientedprogrammingusingjava`
--
ALTER TABLE `objectorientedprogrammingusingjava`
  ADD PRIMARY KEY (`classdate`);

--
-- Indexes for table `operatingsystem`
--
ALTER TABLE `operatingsystem`
  ADD PRIMARY KEY (`classdate`);

--
-- Indexes for table `operatingsystemlab`
--
ALTER TABLE `operatingsystemlab`
  ADD PRIMARY KEY (`classdate`);

--
-- Indexes for table `subjectteacher`
--
ALTER TABLE `subjectteacher`
  ADD PRIMARY KEY (`teacherid`);

--
-- Indexes for table `userdatabase`
--
ALTER TABLE `userdatabase`
  ADD PRIMARY KEY (`userid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
