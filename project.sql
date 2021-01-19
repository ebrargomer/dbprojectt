-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 19 Oca 2021, 17:52:45
-- Sunucu sürümü: 5.7.31
-- PHP Sürümü: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `project`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `advertisement`
--

DROP TABLE IF EXISTS `advertisement`;
CREATE TABLE IF NOT EXISTS `advertisement` (
  `Adv_id` int(11) NOT NULL AUTO_INCREMENT,
  `User` int(11) NOT NULL,
  `Astro` int(11) NOT NULL,
  `Missing_Field` varchar(30) COLLATE utf16_turkish_ci DEFAULT NULL,
  `Game` int(11) NOT NULL,
  PRIMARY KEY (`Adv_id`),
  UNIQUE KEY `Adv_id` (`Adv_id`),
  KEY `advertisement_ibfk_1` (`Astro`),
  KEY `advertisement_ibfk_2` (`Game`),
  KEY `advertisement_ibfk_3` (`User`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf16 COLLATE=utf16_turkish_ci;

--
-- Tablo döküm verisi `advertisement`
--

INSERT INTO `advertisement` (`Adv_id`, `User`, `Astro`, `Missing_Field`, `Game`) VALUES
(1, 1, 1, 'Goalkeeper', 1),
(3, 5, 2, 'Striker', 2),
(4, 2, 7, 'Goalkeeper', 8),
(5, 7, 4, 'Defense', 4),
(6, 5, 3, 'Striker', 3),
(7, 3, 2, 'Defense', 5),
(8, 4, 5, 'Goalkeeper', 6),
(10, 6, 1, 'Defense', 10);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `advertisement_information`
--

DROP TABLE IF EXISTS `advertisement_information`;
CREATE TABLE IF NOT EXISTS `advertisement_information` (
  `Adv_info` int(11) NOT NULL,
  `Applicant_info` int(11) NOT NULL,
  PRIMARY KEY (`Adv_info`,`Applicant_info`),
  KEY `Applicant_info` (`Applicant_info`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_turkish_ci;

--
-- Tablo döküm verisi `advertisement_information`
--

INSERT INTO `advertisement_information` (`Adv_info`, `Applicant_info`) VALUES
(1, 1),
(1, 2),
(1, 4),
(3, 6),
(4, 7),
(5, 10);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `astropitch`
--

DROP TABLE IF EXISTS `astropitch`;
CREATE TABLE IF NOT EXISTS `astropitch` (
  `Astro_id` int(11) NOT NULL AUTO_INCREMENT,
  `Astro_name` varchar(60) COLLATE utf16_turkish_ci DEFAULT NULL,
  `Campaign` text COLLATE utf16_turkish_ci NOT NULL,
  `Price` float DEFAULT NULL,
  `Location` varchar(255) COLLATE utf16_turkish_ci NOT NULL,
  `Point` float NOT NULL,
  `Pssword` text COLLATE utf16_turkish_ci NOT NULL,
  PRIMARY KEY (`Astro_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf16 COLLATE=utf16_turkish_ci;

--
-- Tablo döküm verisi `astropitch`
--

INSERT INTO `astropitch` (`Astro_id`, `Astro_name`, `Campaign`, `Price`, `Location`, `Point`, `Pssword`) VALUES
(1, 'Karesi', 'Win the game, win the desert.', 12.75, 'Balıkesir', 3.7, '1234'),
(2, 'ITU', 'Drinks on us.', 14.5, 'İstanbul', 3.7, '1234'),
(3, 'Olimpik', 'No campaign', 8.25, 'Sivas', 4.1, '1234'),
(4, 'Kocatepe', 'No campaign', 14, 'İstanbul', 4.5, '1234'),
(5, 'Çimen', 'Gloves are on us.', 12.5, 'Balıkesir', 3.9, '1234'),
(6, 'RKAL', 'No campaign', 14.5, 'Balıkesir', 4.3, '1234'),
(7, 'Öncü', 'Discount for winner team.', 18, 'İstanbul', 2.6, '1234'),
(8, 'Vito', 'No campaign', 10, 'Kocaeli', 2.9, '1234'),
(9, 'Hugo', 'No campaign', 15, 'Sivas', 3.2, '1234'),
(10, 'Mars', 'No campaign', 14.5, 'İstanbul', 3.9, '1234');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `calendar`
--

DROP TABLE IF EXISTS `calendar`;
CREATE TABLE IF NOT EXISTS `calendar` (
  `Game_id` int(11) NOT NULL AUTO_INCREMENT,
  `Game_hour` time DEFAULT NULL,
  `Game_day` date DEFAULT NULL,
  `Astro_info` int(11) NOT NULL,
  PRIMARY KEY (`Game_id`),
  UNIQUE KEY `Game_hour` (`Game_hour`,`Game_day`),
  KEY `Astro_info` (`Astro_info`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf16 COLLATE=utf16_turkish_ci;

--
-- Tablo döküm verisi `calendar`
--

INSERT INTO `calendar` (`Game_id`, `Game_hour`, `Game_day`, `Astro_info`) VALUES
(1, '00:00:22', '2024-12-20', 1),
(2, '22:30:00', '2021-01-05', 2),
(3, '18:00:00', '2021-01-25', 3),
(4, '20:00:00', '2021-02-12', 4),
(5, '22:30:00', '2021-01-20', 2),
(6, '14:00:00', '2021-02-10', 5),
(7, '19:00:00', '2021-02-01', 6),
(8, '22:00:00', '2021-01-25', 7),
(9, '17:00:00', '2021-02-01', 2),
(10, '19:30:00', '2021-02-02', 1);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_name` varchar(60) COLLATE utf16_turkish_ci NOT NULL,
  `Age` int(11) NOT NULL,
  `Height` int(11) NOT NULL,
  `Weight` int(11) NOT NULL,
  `Location` varchar(255) COLLATE utf16_turkish_ci NOT NULL,
  `Phone_num` int(11) NOT NULL,
  `Pasw` text COLLATE utf16_turkish_ci NOT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf16 COLLATE=utf16_turkish_ci;

--
-- Tablo döküm verisi `user`
--

INSERT INTO `user` (`User_id`, `User_name`, `Age`, `Height`, `Weight`, `Location`, `Phone_num`, `Pasw`) VALUES
(1, 'Ebrar Ömer ', 15, 172, 60, 'Balıkesir', 12345, '1234'),
(2, 'Caner Erkin', 22, 180, 80, 'Balıkesir', 35436466, '1234'),
(3, 'Mehmet Topal', 30, 190, 85, 'İstanbul', 278325, '1234'),
(4, 'Arda Turan', 30, 175, 80, 'İstanbul', 5647897, '1234'),
(5, 'Phil Dunphy', 45, 190, 82, 'Adana', 325435, '1234'),
(6, 'Jay Prichett', 65, 193, 90, 'Sivas', 254235, '1234'),
(7, 'Burhan Altıntop', 35, 175, 65, 'İstanbul', 65435, '1234'),
(9, 'Gaffur Yılmaz', 40, 170, 60, 'İstanbul', 32523, '1234'),
(10, 'Osman Koçarslanlı', 35, 190, 75, 'İstanbul', 35232, '1234'),
(12, 'Mesut Özil', 30, 180, 75, 'İstanbul', 21412, '1234');

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `advertisement`
--
ALTER TABLE `advertisement`
  ADD CONSTRAINT `advertisement_ibfk_1` FOREIGN KEY (`Astro`) REFERENCES `astropitch` (`Astro_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `advertisement_ibfk_2` FOREIGN KEY (`Game`) REFERENCES `calendar` (`Game_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `advertisement_ibfk_3` FOREIGN KEY (`User`) REFERENCES `user` (`User_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `advertisement_information`
--
ALTER TABLE `advertisement_information`
  ADD CONSTRAINT `advertisement_information_ibfk_1` FOREIGN KEY (`Applicant_info`) REFERENCES `user` (`User_id`),
  ADD CONSTRAINT `advertisement_information_ibfk_2` FOREIGN KEY (`Adv_info`) REFERENCES `advertisement` (`Adv_id`);

--
-- Tablo kısıtlamaları `calendar`
--
ALTER TABLE `calendar`
  ADD CONSTRAINT `calendar_ibfk_1` FOREIGN KEY (`Astro_info`) REFERENCES `astropitch` (`Astro_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
