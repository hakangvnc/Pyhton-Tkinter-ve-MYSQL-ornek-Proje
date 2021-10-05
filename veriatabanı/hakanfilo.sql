-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 20 Haz 2020, 23:49:31
-- Sunucu sürümü: 10.4.11-MariaDB
-- PHP Sürümü: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `hakanfilo`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `arac_ucretleri`
--

CREATE TABLE `arac_ucretleri` (
  `tur_id` int(2) NOT NULL,
  `arac_tur` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `fiyatlar` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `arac_ucretleri`
--

INSERT INTO `arac_ucretleri` (`tur_id`, `arac_tur`, `fiyatlar`) VALUES
(1, 'OTOMOBİL', 200),
(2, 'MİNİBÜS', 300),
(3, 'OTOBÜS', 400),
(4, 'KAMYONET', 500),
(5, 'KAMYON', 600),
(6, 'TIR', 1000);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kiralama_kayitlari`
--

CREATE TABLE `kiralama_kayitlari` (
  `kayit_id` int(20) NOT NULL,
  `üye_tc` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `arac_plaka` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `arac_alim_tar` datetime NOT NULL DEFAULT current_timestamp(),
  `plan_teslim_tar` date NOT NULL,
  `teslim_alınan_tar` datetime NOT NULL,
  `arac_km` bigint(20) NOT NULL,
  `arac_izin_km` int(11) NOT NULL,
  `arac_teslim_km` int(11) NOT NULL,
  `arac_tutar` int(11) NOT NULL,
  `km_ceza_tutar` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kiralama_kayitlari`
--

INSERT INTO `kiralama_kayitlari` (`kayit_id`, `üye_tc`, `arac_plaka`, `arac_alim_tar`, `plan_teslim_tar`, `teslim_alınan_tar`, `arac_km`, `arac_izin_km`, `arac_teslim_km`, `arac_tutar`, `km_ceza_tutar`) VALUES
(15, '963852174', '55 HKN 65', '2020-05-28 18:45:57', '2020-08-07', '2020-06-01 18:05:15', 130000, 20000, 142000, 73900, 0),
(16, '741852963', '34 HKN 34', '2020-06-01 16:17:17', '2020-06-10', '2020-06-01 18:05:59', 1216, 1800, 3030, 1800, 14),
(17, '741852963', '55 HKN 65', '2020-06-03 00:34:20', '2020-06-20', '2020-06-03 18:14:18', 142000, 4000, 3000, 17300, 0),
(18, '963852741', '55 HKN 58', '2020-06-03 00:48:24', '2020-06-07', '2020-06-03 02:46:59', 1000, 2000, 3000, 4600, 0),
(19, '963852741', '55 HKN 65', '2020-06-03 18:25:11', '2020-06-06', '2020-06-03 18:27:20', 3000, 600, 2600, 3000, 0),
(20, '741852963', '55 HKN 64', '2020-06-03 18:26:00', '2020-06-06', '2020-06-03 19:26:15', 10000, 600, 3000, 3000, 0),
(21, '741852963', '55 HKN 65', '2020-06-03 19:28:07', '2020-06-09', '2020-06-03 19:29:32', 2600, 1200, 6000, 6000, 2200);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanıcı`
--

CREATE TABLE `kullanıcı` (
  `k_id` int(11) NOT NULL,
  `k_ad` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `k_sifre` varchar(10) COLLATE utf8_turkish_ci NOT NULL,
  `k_kayit_tar` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kullanıcı`
--

INSERT INTO `kullanıcı` (`k_id`, `k_ad`, `k_sifre`, `k_kayit_tar`) VALUES
(1, 'admin', 'admin', '2020-05-21 14:42:14'),
(2, 'admin', '12345', '2020-05-21 14:42:17');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `masraflar`
--

CREATE TABLE `masraflar` (
  `s_id` int(11) NOT NULL,
  `s_rapor` varchar(200) COLLATE utf8_turkish_ci NOT NULL,
  `s_tutar` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `masraflar`
--

INSERT INTO `masraflar` (`s_id`, `s_rapor`, `s_tutar`) VALUES
(1, 'Lastik değişimi', 800),
(2, 'Silecek tamiri', 80),
(3, 'Fren balata değişimi ön', 400),
(4, 'Fren balata değişimi arka', 400),
(5, 'Debriyaj balata değişimi', 600),
(6, 'Yağ değişimi', 340),
(7, 'Ufak elektiriksel sorunlar', 100),
(8, 'Pasta cila yapımı', 380),
(9, 'Far değişimi sol', 250),
(10, 'Far değişimi sağ', 250),
(11, 'Amortisör değişimi ön', 400),
(12, 'Amortisör değişişmi arka', 400),
(13, 'Rot kolu değişimi sağ', 140),
(14, 'Rot kolu değişimi sol', 140),
(15, 'Debriyaj balata değişimi', 380),
(16, 'Radyo anten değişimi', 160),
(17, 'GPS tamiri', 520),
(18, 'Bagaj kapağı kilit tamiri', 200),
(19, 'Kapı kol değişimleri', 340),
(20, 'Direksiyon kutusu tamiri', 800);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `musteriler`
--

CREATE TABLE `musteriler` (
  `üye_id` int(11) NOT NULL,
  `uye_tc` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `uye_ad` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `uye_soyad` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `uye_mail` varchar(50) COLLATE utf8_turkish_ci NOT NULL,
  `uye_tel` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `uye_dogum` date NOT NULL,
  `uye_kayit_tar` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `musteriler`
--

INSERT INTO `musteriler` (`üye_id`, `uye_tc`, `uye_ad`, `uye_soyad`, `uye_mail`, `uye_tel`, `uye_dogum`, `uye_kayit_tar`) VALUES
(2, '3581356365', 'HAKAN', 'GÜVENÇ', 'haskan.tr.1999@gmail.com', '536 852 7496', '1999-04-13', '2020-05-22 19:49:26'),
(3, '4528126176', 'ÖMER FARUK', 'ATLAS', 'ömerfaruk@hotmail.com', '538 856 95 95', '1989-06-05', '2020-05-22 19:59:00'),
(4, '95681556220', 'MURAT', 'KELEK', 'KELEK61@GMAİL.COM', '5378556361', '1978-03-06', '2020-05-26 18:01:11'),
(5, '65465465460', 'mahmut', 'kelek', 'kelek5563@email.com', '05369528475', '1986-04-06', '2020-05-26 18:05:33'),
(6, 'SASDAS', 'DASDA', 'SDAS', 'ASDASD', 'DASD', '2012-04-05', '2020-05-26 18:10:02'),
(7, '85274193632', 'tayfun', 'demircan', 'demircan@hotmail.com', '0532165485', '2018-05-06', '2020-05-26 18:17:03'),
(8, 'ASDA', 'DASDASD', 'ASD', 'SDASD', '514561654', '1958-05-04', '2020-05-26 18:19:57'),
(9, 'ASDAS', 'DASD', 'ASDA', 'ASDAS', 'SDASD', '1973-04-05', '2020-05-26 18:22:16'),
(10, '24896325', 'asdafs', 'asdafs', 'asdasdasd', '2586325369', '1996-06-05', '2020-05-26 18:24:32'),
(11, '1445215', 'ASD', 'ASD', 'ASDASFA', '8686', '1977-04-06', '2020-05-26 18:32:37'),
(12, '168451', 'asdaf', 'asdaf', 'asfafad', '36914', '2015-06-05', '2020-05-26 18:34:38'),
(13, '516816841', 'hakan', 'aukjbakbd', 'asdadwa', '5149262', '1960-06-06', '2020-05-26 18:37:46'),
(14, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:40:53'),
(15, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:40:57'),
(16, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:40:57'),
(17, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:40:57'),
(18, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:40:57'),
(19, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:40:58'),
(20, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:40:58'),
(21, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:41:00'),
(22, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:41:01'),
(23, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:41:02'),
(24, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:41:02'),
(25, '46815', 'asd', 'asd', 'ads', 'asd', '2015-07-04', '2020-05-26 18:41:02'),
(26, '1895265161', 'asd', 'asd', 'ads', 'asd', '0000-00-00', '2020-05-26 18:41:13'),
(27, '1895265161', 'asd', 'asd', 'ads', 'asd', '0000-00-00', '2020-05-26 18:41:13'),
(28, '1895265161', 'asd', 'asd', 'ads', 'asd', '0000-00-00', '2020-05-26 18:41:14'),
(29, '1895265161', 'asd', 'asd', 'ads', 'asd', '0000-00-00', '2020-05-26 18:41:14'),
(30, '1895265161', 'asd', 'asd', 'ads', 'asd', '0000-00-00', '2020-05-26 18:41:14'),
(31, '1895265161', 'asd', 'asd', 'ads', 'asd', '0000-00-00', '2020-05-26 18:41:14'),
(32, '1895265161', 'asd', 'asd', 'ads', 'asd', '0000-00-00', '2020-05-26 18:41:14'),
(33, '94896325530', 'LKJKB', 'ŞNKLJB', 'HBLIBKNLN', '1456320145', '1998-06-05', '2020-05-26 18:47:54'),
(34, '2486343846', 'ASDASD', 'ASDASF', 'AFGHAVCWDAVW', '8486348646', '1989-04-06', '2020-05-26 18:55:34'),
(36, '8416516841', 'ASDASF', 'ASDAF', 'asdawdwd', '56481351', '2013-07-06', '2020-05-26 19:00:24'),
(52, '984153', 'asda', 'asdasd', 'asdafw', '845152133', '2014-07-06', '2020-05-27 01:15:18'),
(54, '97562', 'ASD', 'ASD', 'ASDAWD', '6845321', '2013-08-07', '2020-05-27 01:20:59'),
(57, '96385274112', 'GÖKHAN', 'KALAMIZ', 'KALAMIZ@GMAİL.COM', '852741963', '2014-07-05', '2020-05-27 01:43:37'),
(58, '96385214712', 'KEMAL', 'KAMİL', 'KMAİL@kmaiil.com', '96325874133', '1971-03-03', '2020-05-27 14:41:14'),
(59, '74185296333', 'MELEK', 'KURT', 'mlk.kurt@gmail.com', '0563951753', '1999-08-05', '2020-05-27 14:45:46'),
(61, '741852963123', 'HAKAN', 'GÜVENÇ', 'asdawfawd', '0258963741', '2015-07-07', '2020-05-27 14:54:18'),
(62, '9638524177', '', '', '', '', '1982-06-06', '2020-05-27 14:59:37'),
(63, '74185296', 'asdfaw', 'dawfa', 'dasdawd', '786483', '1988-08-09', '2020-05-27 15:09:37'),
(65, '9637894561', 'ADWQDS', 'DAWDAWD', 'SFGAWDAD', '74185296A', '1967-06-05', '2020-05-27 15:21:24'),
(66, '12345678911', 'ADWQDS', 'DAWDAWD', 'SFGAWDAD', '74185296A', '0000-00-00', '2020-05-27 15:34:02'),
(67, '9876543210', 'RAMİZ', 'KARAESKİ', 'KARAESKİ@GMAİL.COM', '155', '1987-06-07', '2020-05-27 16:40:40'),
(68, '963852174', 'GÖKHAN', 'QUATR', 'QUATR@GMAİL.COM', '5969876352', '2013-08-12', '2020-05-28 18:45:57'),
(69, '741/852963', 'HAKAN', 'GÜVENÇ', 'güvenç@gmail.com', '05636263334', '1993-08-07', '2020-06-01 16:17:16'),
(70, '741852963', 'hakan', 'güvenç', 'wakjfkljbalbfaeafw', '0536932145', '1996-04-06', '2020-06-03 00:34:20'),
(71, '963852741', 'muratasfsea', 'aefaefef', 'awfawefafef', '974146464', '1991-05-06', '2020-06-03 00:48:24'),
(72, '963852741', 'murat', 'kamil', 'awkjflkeanfljeflkkjaef', '0537369533', '2014-06-07', '2020-06-03 18:25:11'),
(73, '741852963', 'osman', 'osmanoglu', 'dshbafkjnfkjaekfja', '0584959693', '1985-08-04', '2020-06-03 18:26:00'),
(74, '741852963', 'murat', 'kopuz', 'dkandçjvnasjnf', '01684632165', '1977-07-05', '2020-06-03 19:28:07');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `servis_kayitlari`
--

CREATE TABLE `servis_kayitlari` (
  `kayit_id` int(11) NOT NULL,
  `arac_plaka` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `hasar_id` int(11) NOT NULL,
  `arac_masraf` varchar(20) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `servis_kayitlari`
--

INSERT INTO `servis_kayitlari` (`kayit_id`, `arac_plaka`, `hasar_id`, `arac_masraf`) VALUES
(1, '55 HKN 64', 1, 'ÖDENDİ'),
(2, '55 HKN 65', 11, 'ÖDENDİ');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `tum_araclar`
--

CREATE TABLE `tum_araclar` (
  `arac_id` int(11) NOT NULL,
  `arac_plaka` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `arac_tur` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `arac_sase` varchar(40) COLLATE utf8_turkish_ci NOT NULL,
  `arac_marka` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `arac_model` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `arac_yakit` varchar(10) COLLATE utf8_turkish_ci NOT NULL,
  `arac_vites` varchar(10) COLLATE utf8_turkish_ci NOT NULL,
  `arac_uretim` date NOT NULL,
  `arac_km` varchar(14) COLLATE utf8_turkish_ci NOT NULL,
  `arac_durum` varchar(20) COLLATE utf8_turkish_ci NOT NULL,
  `arac_kayıt_tar` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `tum_araclar`
--

INSERT INTO `tum_araclar` (`arac_id`, `arac_plaka`, `arac_tur`, `arac_sase`, `arac_marka`, `arac_model`, `arac_yakit`, `arac_vites`, `arac_uretim`, `arac_km`, `arac_durum`, `arac_kayıt_tar`) VALUES
(1, '34 HKN 34', 'OTOMOBİL', '8D8AWD38435FB4', 'BMW', 'X5', 'MAZOT', 'MAMNUEL', '2007-09-06', '3030', 'HAZIR', '2020-05-21 14:35:39'),
(2, '01 HKN 01', 'OTOMOBİL', '843A51WD813A0', 'VOLKSWAGEN', 'PASSAT', 'MAZOT', 'OTOMATİK', '2020-04-04', '0', 'HAZIR', '2020-05-22 13:23:43'),
(3, '01 HKN 02', 'OTOMOBİL', '843A51WD813A1', 'VOLKSWAGEN', 'PASSAT', 'MAZOT', 'OTOMATİK', '2020-04-04', '0', 'HAZIR', '2020-05-22 13:24:06'),
(5, '01 HKN 03', 'OTOMOBİL', '843A51WD813A2', 'VOLKSWAGEN', 'PASSAT', 'MAZOT', 'OTOMATİK', '2020-04-04', '0', 'HAZIR', '2020-05-22 13:24:40'),
(6, '01 HKN 04', 'OTOMOBİL', '8A4SD684ASD464', 'VOLKSWAGEN', 'PASSAT', 'MAZOT', 'OTOMATİK', '2020-04-04', '0', 'HAZIR', '2020-05-22 13:26:50'),
(7, '01 HKN 05', 'OTOMOBİL', '8A4SD684ASD465', 'VOLKSWAGEN', 'PASSAT', 'MAZOT', 'OTOMATİK', '2020-04-04', '0', 'HAZIR', '2020-05-22 13:27:06'),
(8, '01 HKN 06', 'OTOMOBİL', '8A4SD684ASD466', 'VOLKSWAGEN', 'PASSAT', 'MAZOT', 'OTOMATİK', '2020-04-03', '0', 'HAZIR', '2020-05-22 13:27:23'),
(9, '01 HKN 07', 'OTOMOBİL', '8A4SD684ASD467', 'VOLKSWAGEN', 'PASSAT', 'MAZOT', 'OTOMATİK', '2020-06-04', '0', 'HAZIR', '2020-05-22 13:27:38'),
(10, '01 HKN 08', 'OTOMOBİL', '8A4SD684ASD469', 'VOLKSWAGEN', 'PASSAT', 'MAZOT', 'OTOMATİK', '2020-04-05', '0', 'HAZIR', '2020-05-22 13:28:01'),
(11, '01 HKN 09', 'OTOMOBİL', '8A4SD684ASD461', 'VOLKSWAGEN', 'PASSAT', 'MAZOT', 'OTOMATİK', '2020-04-04', '0', 'HAZIR', '2020-05-22 13:28:31'),
(12, '01 HKN 10', 'OTOMOBİL', '8A4SD684ASD410', 'VOLKSWAGEN', 'PASSAT', 'MAZOT', 'OTOMATİK', '2018-04-03', '0', 'HAZIR', '2020-05-22 13:30:47'),
(13, '01 HKN 11', 'MİNİBÜS', '8A4SD684ASD411', 'MERCEDES', 'SPRİNTER', 'MAZOT', 'OTOMATİK', '2020-05-09', '0', 'HAZIR', '2020-05-22 13:31:26'),
(14, '01 HKN 12', 'MİNİBÜS', '8A4SD684ASD412', 'MERCEDES', 'SPRİNTER', 'MAZOT', 'OTOMATİK', '2020-05-06', '0', 'HAZIR', '2020-05-22 13:31:47'),
(15, '01 HKN 13', 'MİNİBÜS', '8A4SD684ASD413', 'MERCEDES', 'SPRİNTER', 'MAZOT', 'OTOMATİK', '2020-08-08', '0', 'HAZIR', '2020-05-22 13:32:00'),
(17, '01 HKN 14', 'MİNİBÜS', '8A4SD684ASD414', 'MERCEDES', 'SPRİNTER', 'MAZOT', 'OTOMATİK', '2020-05-07', '0', 'HAZIR', '2020-05-22 13:32:21'),
(18, '01 HKN 15', 'MİNİBÜS', '8A4SD684ASD415', 'MERCEDES', 'SPRİNTER', 'MAZOT', 'OTOMATİK', '2020-04-07', '0', 'HAZIR', '2020-05-22 13:32:41'),
(19, '01 HKN 16', 'MİNİBÜS', '8A4SD684ASD417', 'MERCEDES', 'SPRİNTER', 'MAZOT', 'OTOMATİK', '2020-06-07', '2', 'HAZIR', '2020-05-22 13:33:33'),
(20, '01 HKN 17', 'MİNİBÜS', '8A4SD684ASD418', 'MERCEDES', 'SPRİNTER', 'MAZOT', 'OTOMATİK', '2020-04-06', '0', 'HAZIR', '2020-05-22 13:33:54'),
(21, '01 HKN 18', 'MİNİBÜS', '8A4SD684ASD419', 'MERCEDES', 'SPRİNTER', 'MAZOT', 'OTOMATİK', '2020-05-05', '0', 'HAZIR', '2020-05-22 13:34:59'),
(22, '01 HKN 19', 'MİNİBÜS', '8A4SD684ASD42', 'MERCEDES', 'SPRİNTER', 'MAZOT', 'OTOMATİK', '2020-03-04', '0', 'HAZIR', '2020-05-22 13:35:31'),
(23, '01 HKN 20', 'MİNİBUS', 'SF89ADA5DATB1', 'MERCEDES', 'SPRİNTER', 'MAZOT', 'OTOMATİK', '2020-05-06', '0', 'HAZIR', '2020-05-22 13:48:12'),
(24, '55 HKN 21', 'OTOBÜS', 'BGGTGHFHTRBRG1', 'MERCEDES', 'TRAVEGO', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(25, '55 HKN 22', 'OTOBÜS', 'BGGTGHFHTRBRG2', 'MERCEDES', 'TRAVEGO', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(26, '55 HKN 23', 'OTOBÜS', 'BGGTGHFHTRBRG3', 'MERCEDES', 'TRAVEGO', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(27, '55 HKN 24', 'OTOBÜS', 'BGGTGHFHTRBRG4', 'MERCEDES', 'TRAVEGO', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(28, '55 HKN 25', 'OTOBÜS', 'BGGTGHFHTRBRG5', 'MERCEDES', 'TRAVEGO', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(29, '55 HKN 26', 'OTOBÜS', 'BGGTGHFHTRBRG6', 'MERCEDES', 'TRAVEGO', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(30, '55 HKN 27', 'OTOBÜS', 'BGGTGHFHTRBR7', 'MERCEDES', 'TRAVEGO', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(31, '55 HKN 28', 'OTOBÜS', 'BGGTGHFHTRBRG8', 'MERCEDES', 'TRAVEGO', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(32, '55 HKN 29', 'OTOBÜS', 'BGGTGHFHTRBRG9', 'MERCEDES', 'TRAVEGO', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(33, '55 HKN 30', 'OTOBÜS', 'BGGTGHFHTRBR10', 'MERCEDES', 'TRAVEGO', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(34, '55 HKN 31', 'KAMYONET', 'ASFFASFRDFGG1', 'ISIZU', 'NPR', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(35, '55 HKN 32', 'KAMYONET', 'DFHDFGHDFGRG2', 'ISIZU', 'NPR', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(36, '55 HKN 33', 'KAMYONET', 'DFGDFGFDGFGG3', 'ISIZU', 'NPR', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(37, '55 HKN 34', 'KAMYONET', 'GHNGHNGHHMTG4', 'ISIZU', 'NPR', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(38, '55 HKN 35', 'KAMYONET', 'BH5H6HTYGGYG5', 'ISIZU', 'NPR', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(39, '55 HKN 36', 'KAMYONET', 'BH5H6HTYGGYG6', 'ISIZU', 'NPR', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(40, '55 HKN 37', 'KAMYONET', 'BH5H6HTYGGYG7', 'ISIZU', 'NPR', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(41, '55 HKN 38', 'KAMYONET', 'BH5H6HTYGGYG8', 'ISIZU', 'NPR', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(42, '55 HKN 39', 'KAMYONET', 'BH5H6HTYGGYG9', 'ISIZU', 'NPR', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(43, '55 HKN 40', 'KAMYONET', 'BH5H6HTYGGY20', 'ISIZU', 'NPR', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(44, '55 HKN 41', 'KAMYON', 'Y68SDFSFS6F8S1', 'VOLVO', 'FMX', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(45, '55 HKN 42', 'KAMYON', 'Y68SDFSFS6F8S2', 'VOLVO', 'FMX', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(46, '55 HKN 43', 'KAMYON', 'Y68SDFSFS6F8S3', 'VOLVO', 'FMX', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(47, '55 HKN 44', 'KAMYON', 'Y68SDFSFS6F8S4', 'VOLVO', 'FMX', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(48, '55 HKN 45', 'KAMYON', 'Y68SDFSFS6F8S5', 'VOLVO', 'FMX', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(49, '55 HKN 46', 'KAMYON', 'Y68SDFSFS6F8S6', 'VOLVO', 'FMX', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(50, '55 HKN 47', 'KAMYON', 'Y68SDFSFS6F8S7', 'VOLVO', 'FMX', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(51, '55 HKN 48', 'KAMYON', 'Y68SDFSFS6F8S8', 'VOLVO', 'FMX', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(52, '55 HKN 49', 'KAMYON', 'Y68SDFSFS6F8S9', 'VOLVO', 'FMX', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(53, '55 HKN 50', 'KAMYON', 'Y68SDFSFS6F810', 'VOLVO', 'FMX', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(54, '55 HKN 51', 'TIR', 'TAFASLŞJQWMKFB01', 'SCANİA', 'S730', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(55, '55 HKN 52', 'TIR', 'TAFASLŞJQWMKFB02', 'SCANİA', 'S730', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(56, '55 HKN 53', 'TIR', 'TAFASLŞJQWMKFB03', 'SCANİA', 'S730', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(57, '55 HKN 54', 'TIR', 'TAFASLŞJQWMKFB04', 'SCANİA', 'S730', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(58, '55 HKN 55', 'TIR', 'TAFASLŞJQWMKFB05', 'SCANİA', 'S730', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(59, '55 HKN 56', 'TIR', 'TAFASLŞJQWMKFB06', 'SCANİA', 'S730', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(60, '55 HKN 57', 'TIR', 'TAFASLŞJQWMKFB07', 'SCANİA', 'S730', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(61, '55 HKN 58', 'TIR', 'TAFASLŞJQWMKFB08', 'SCANİA', 'S730', 'MAZOT', 'OTOMATİK', '2020-01-01', '3000', 'HAZIR', '0000-00-00 00:00:00'),
(62, '55 HKN 59', 'TIR', 'TAFASLŞJQWMKFB09', 'SCANİA', 'S730', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(65, '55 HKN 60', 'TIR', 'TAFASLŞJQWMKFB10', 'SCANİA', 'S730', 'MAZOT', 'OTOMATİK', '2020-01-01', '0', 'HAZIR', '0000-00-00 00:00:00'),
(66, '55 HKN 61', 'TIR', '879a84wdad84w6d', 'MERCEDES', 'ACTROS', 'MAZOT', 'MAMNUEL', '2016-07-07', '170000', 'HAZIR', '2020-05-28 17:48:02'),
(67, '55 HKN 62', 'TIR', 'A8W4D6WA1D684', 'MERCEDES', 'AXOR 1840', 'MAZOT', 'MAMNUEL', '2015-08-28', '200000', 'HAZIR', '2020-05-28 17:55:24'),
(69, '55 HKN 63', 'TIR', '8WA4D68A4D684', 'MERCEDES', 'AXOR 1840', 'MAZOT', 'MAMNUEL', '2011-07-27', '120000', 'HAZIR', '2020-05-28 18:08:22'),
(70, '55 HKN 64', 'TIR', 'A1WD46AW84D6', 'MERCEDES', 'ACTROS', 'MAZOT', 'OTOMATİK', '2019-03-03', '3000', 'HAZIR', '2020-05-28 18:12:44'),
(72, '55 HKN 65', 'TIR', '1W6A8D46AW4', 'MERCEDES', 'ACTROS', 'MAZOT', 'MAMNUEL', '2014-08-06', '6000', 'HAZIR', '2020-05-28 18:41:36');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `arac_ucretleri`
--
ALTER TABLE `arac_ucretleri`
  ADD PRIMARY KEY (`tur_id`),
  ADD KEY `tur_id` (`tur_id`);

--
-- Tablo için indeksler `kiralama_kayitlari`
--
ALTER TABLE `kiralama_kayitlari`
  ADD PRIMARY KEY (`kayit_id`);

--
-- Tablo için indeksler `kullanıcı`
--
ALTER TABLE `kullanıcı`
  ADD PRIMARY KEY (`k_id`),
  ADD UNIQUE KEY `k_id` (`k_id`);

--
-- Tablo için indeksler `masraflar`
--
ALTER TABLE `masraflar`
  ADD PRIMARY KEY (`s_id`);

--
-- Tablo için indeksler `musteriler`
--
ALTER TABLE `musteriler`
  ADD PRIMARY KEY (`üye_id`),
  ADD UNIQUE KEY `üye_id` (`üye_id`,`uye_tc`);

--
-- Tablo için indeksler `servis_kayitlari`
--
ALTER TABLE `servis_kayitlari`
  ADD PRIMARY KEY (`kayit_id`);

--
-- Tablo için indeksler `tum_araclar`
--
ALTER TABLE `tum_araclar`
  ADD PRIMARY KEY (`arac_id`),
  ADD UNIQUE KEY `arac_id` (`arac_id`),
  ADD UNIQUE KEY `arac_plaka` (`arac_plaka`),
  ADD UNIQUE KEY `arac_sase` (`arac_sase`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `kiralama_kayitlari`
--
ALTER TABLE `kiralama_kayitlari`
  MODIFY `kayit_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Tablo için AUTO_INCREMENT değeri `kullanıcı`
--
ALTER TABLE `kullanıcı`
  MODIFY `k_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `masraflar`
--
ALTER TABLE `masraflar`
  MODIFY `s_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Tablo için AUTO_INCREMENT değeri `musteriler`
--
ALTER TABLE `musteriler`
  MODIFY `üye_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- Tablo için AUTO_INCREMENT değeri `servis_kayitlari`
--
ALTER TABLE `servis_kayitlari`
  MODIFY `kayit_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `tum_araclar`
--
ALTER TABLE `tum_araclar`
  MODIFY `arac_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
