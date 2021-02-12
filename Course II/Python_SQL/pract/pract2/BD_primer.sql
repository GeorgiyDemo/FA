-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Хост: 127.0.0.1
-- Время создания: Апр 05 2013 г., 12:02
-- Версия сервера: 5.5.27
-- Версия PHP: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `julia_lisina`
--

-- --------------------------------------------------------

--
-- Структура таблицы `exam_marks`
--

CREATE TABLE IF NOT EXISTS `exam_marks` (
  `EXAM_ID` int(11) NOT NULL,
  `STUDENT_ID` int(11) NOT NULL,
  `SUBJ_ID` int(11) NOT NULL,
  `MARK` smallint(6) DEFAULT NULL,
  `EXAM_DATE` date NOT NULL,
  PRIMARY KEY (`EXAM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=cp1251;

--
-- Дамп данных таблицы `exam_marks`
--

INSERT INTO `exam_marks` (`EXAM_ID`, `STUDENT_ID`, `SUBJ_ID`, `MARK`, `EXAM_DATE`) VALUES
(34, 32, 10, 4, '2000-01-23'),
(43, 6, 22, 4, '2000-01-18'),
(75, 55, 10, 5, '2000-01-05'),
(145, 12, 10, 5, '2000-01-12'),
(238, 12, 22, 3, '1999-06-17'),
(639, 55, 22, NULL, '1999-06-22');

-- --------------------------------------------------------

--
-- Структура таблицы `lecturer`
--

CREATE TABLE IF NOT EXISTS `lecturer` (
  `LECTURER_ID` int(11) NOT NULL,
  `SURNAME` text NOT NULL,
  `NAME` text NOT NULL,
  `CITY` text NOT NULL,
  `UNIV_ID` int(11) NOT NULL,
  PRIMARY KEY (`LECTURER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=cp1251;

--
-- Дамп данных таблицы `lecturer`
--

INSERT INTO `lecturer` (`LECTURER_ID`, `SURNAME`, `NAME`, `CITY`, `UNIV_ID`) VALUES
(24, 'Колесников', 'Борис', 'Воронеж', 10),
(46, 'Никонов', 'Иван', 'Воронеж', 10),
(74, 'Лагутин', 'Павел', 'Москва', 22),
(108, 'Струков', 'Николай', 'Москва', 22),
(276, 'Николаев', 'Виктор', 'Воронеж', 10),
(328, 'Сорокин', 'Андрей', 'Орел', 10);

-- --------------------------------------------------------

--
-- Структура таблицы `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `STUDENT_ID` int(11) NOT NULL,
  `SURNAME` text NOT NULL,
  `NAME` text NOT NULL,
  `STIPEND` int(11) NOT NULL,
  `KURS` smallint(6) NOT NULL,
  `CITY` text,
  `BIRTHDAY` date DEFAULT NULL,
  `UNIV_ID` int(11) NOT NULL,
  PRIMARY KEY (`STUDENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=cp1251;

--
-- Дамп данных таблицы `student`
--

INSERT INTO `student` (`STUDENT_ID`, `SURNAME`, `NAME`, `STIPEND`, `KURS`, `CITY`, `BIRTHDAY`, `UNIV_ID`) VALUES
(1, 'Иванов', 'Иван', 150, 1, 'Орел', '1982-12-03', 10),
(3, 'Петров', 'Петр', 200, 3, 'Курск', '1980-12-01', 10),
(6, 'Сидоров', 'Вадим', 150, 4, 'Москва', '1979-06-07', 22),
(10, 'Кузнецов', 'Борис', 0, 2, 'Брянск', '1981-12-08', 10),
(12, 'Зайцева', 'Ольга', 250, 2, 'Липецк', '1981-05-01', 10),
(32, 'Котов', 'Павел', 150, 5, 'Белгород', NULL, 14),
(55, 'Белкин', 'Вадим', 250, 5, 'Воронеж', '1980-01-07', 10),
(265, 'Павлов', 'Андрей', 0, 3, 'Воронеж', '1979-11-05', 10),
(276, 'Петров', 'Антон', 200, 4, NULL, '1981-08-05', 22),
(654, 'Лукин', 'Артем', 200, 3, 'Воронеж', '1981-12-01', 10);

-- --------------------------------------------------------

--
-- Структура таблицы `subject`
--

CREATE TABLE IF NOT EXISTS `subject` (
  `SUBJ_ID` int(11) NOT NULL,
  `SUBJ_NAME` text NOT NULL,
  `HOUR` int(11) NOT NULL,
  `SEMESTER` smallint(6) NOT NULL,
  PRIMARY KEY (`SUBJ_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=cp1251;

--
-- Дамп данных таблицы `subject`
--

INSERT INTO `subject` (`SUBJ_ID`, `SUBJ_NAME`, `HOUR`, `SEMESTER`) VALUES
(10, 'Информатика', 56, 1),
(22, 'Физика', 34, 1),
(43, 'Математика', 56, 2),
(56, 'История', 34, 4),
(73, 'Физкультура', 34, 5),
(94, 'Английский', 56, 3);

-- --------------------------------------------------------

--
-- Структура таблицы `subj_lect`
--

CREATE TABLE IF NOT EXISTS `subj_lect` (
  `LECTURER_ID` int(11) NOT NULL,
  `SUBJ_ID` int(11) NOT NULL,
  PRIMARY KEY (`LECTURER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=cp1251;

--
-- Дамп данных таблицы `subj_lect`
--

INSERT INTO `subj_lect` (`LECTURER_ID`, `SUBJ_ID`) VALUES
(24, 24),
(46, 46),
(74, 74),
(108, 108),
(276, 276),
(328, 328);

-- --------------------------------------------------------

--
-- Структура таблицы `university`
--

CREATE TABLE IF NOT EXISTS `university` (
  `UNIV_ID` int(11) NOT NULL,
  `UNIV_NAME` text NOT NULL,
  `RATING` int(11) NOT NULL,
  `CITY` text NOT NULL,
  PRIMARY KEY (`UNIV_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=cp1251;

--
-- Дамп данных таблицы `university`
--

INSERT INTO `university` (`UNIV_ID`, `UNIV_NAME`, `RATING`, `CITY`) VALUES
(10, 'ВГУ', 296, 'Воронеж'),
(11, 'НГУ', 345, 'Новосибирск'),
(14, 'БГУ', 326, 'Белгород'),
(15, 'ТГУ', 368, 'Томск'),
(18, 'ВГМА', 327, 'Воронеж'),
(22, 'МГУ', 606, 'Москва'),
(32, 'РГУ', 416, 'Ростов');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
