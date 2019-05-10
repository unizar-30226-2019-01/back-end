-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-05-2019 a las 11:27:02
-- Versión del servidor: 10.1.36-MariaDB
-- Versión de PHP: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `baitu`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favoritos`
--

CREATE TABLE `favoritos` (
  `usuario` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `publicacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fotos`
--

CREATE TABLE `fotos` (
  `publicacion` int(11) NOT NULL,
  `foto` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `fotos`
--

INSERT INTO `fotos` (`publicacion`, `foto`) VALUES
(50, 'C:\\fakepath\\run.py'),
(51, 'C:\\fakepath\\baitu.sql'),
(53, 'C:\\fakepath\\LICENSE'),
(54, 'C:\\fakepath\\run.py');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ofertas`
--

CREATE TABLE `ofertas` (
  `usuario` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `venta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publicacion`
--

CREATE TABLE `publicacion` (
  `id` int(11) NOT NULL,
  `Nombre` text COLLATE utf8_unicode_ci NOT NULL,
  `Descripcion` text COLLATE utf8_unicode_ci NOT NULL,
  `Fecha` text COLLATE utf8_unicode_ci NOT NULL,
  `Categoria` text COLLATE utf8_unicode_ci NOT NULL,
  `nuevoUsuario` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Vendedor` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `publicacion`
--

INSERT INTO `publicacion` (`id`, `Nombre`, `Descripcion`, `Fecha`, `Categoria`, `nuevoUsuario`, `Vendedor`) VALUES
(7, 'ejemplo1', 'esto es el primer ejemplo', '10/04/2019', 'Hacker', '', 'sergio'),
(8, 'ejemplo1', 'esto es el primer ejemplo', '10/04/2019', 'Hacker', '', 'sergio'),
(33, 'ejemplo1', 'esto es el primer ejemplo', '10/04/2019', 'Hacker', '', 'sergio'),
(34, 'ejemplo1', 'esto es el primer ejemplo', '10/04/2019', 'Hacker', '', 'sergio'),
(35, 'ejemplo1', 'esto es el primer ejemplo', '10/04/2019', 'Hacker', '', 'sergio'),
(36, 'ejemplo1', 'esto es el primer ejemplo', '10/04/2019', 'Hacker', '', 'sergio'),
(38, 'ejemplo1', 'esto es el primer ejemplo', '10/04/2019', 'Hacker', '', 'sergio'),
(39, 'ejemplo1', 'esto es el primer ejemplo', '10/04/2019', 'Hacker', '', 'sergio'),
(40, 'ejemplo1', 'esto es el primer ejemplo', '10/04/2019', 'Hacker', '', 'sergio'),
(48, 'iPhone', 'dpm', '11223333', 'moviles', '', 'guti'),
(50, 'ukylkh', 'jjubj', '6/4/2019', '...', '', 'jj'),
(51, 'calculadorea', 'xd', '7/4/2019', '...', '', 'jj'),
(53, 'daniel', 'adklsjf', '7/4/2019', '...', '', 'jj'),
(54, 'mishuevos', 'son caros', '8/4/2019', '...', '', 'jj');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pujas`
--

CREATE TABLE `pujas` (
  `usuario` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `subasta` int(11) NOT NULL,
  `puja` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `subasta`
--

CREATE TABLE `subasta` (
  `publicacion` int(11) NOT NULL,
  `precio_actual` text COLLATE utf8_unicode_ci NOT NULL,
  `precio_salida` text COLLATE utf8_unicode_ci NOT NULL,
  `hora_limite` text COLLATE utf8_unicode_ci NOT NULL,
  `fecha_limite` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `subasta`
--

INSERT INTO `subasta` (`publicacion`, `precio_actual`, `precio_salida`, `hora_limite`, `fecha_limite`) VALUES
(7, '23', '10', '78787', '878778'),
(48, '100', '50', '12234', '12322');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `Login` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Nombre` text COLLATE utf8_unicode_ci NOT NULL,
  `Apellidos` text COLLATE utf8_unicode_ci NOT NULL,
  `Password` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Domicilio` text COLLATE utf8_unicode_ci NOT NULL,
  `Foto` text COLLATE utf8_unicode_ci NOT NULL,
  `Telefono` int(11) NOT NULL,
  `Email` text COLLATE utf8_unicode_ci NOT NULL,
  `Puntuacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`Login`, `Nombre`, `Apellidos`, `Password`, `Domicilio`, `Foto`, `Telefono`, `Email`, `Puntuacion`) VALUES
('guti', 'alex', 'gutierrez', 'hola', '', '', 123456789, 'gfadskmls@sgadf.com', 5),
('jj', 'Daniel', 'Cay', 'hola', '', '', 0, 'danielcay98@gmail.com', 0),
('sergio', 'sergio', 'costa moreno', 'hola', '', '', 0, '', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `Publicacion` int(11) NOT NULL,
  `Precio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`Publicacion`, `Precio`) VALUES
(40, 10),
(50, 999),
(51, 35),
(53, 500),
(54, 65);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD PRIMARY KEY (`usuario`,`publicacion`),
  ADD KEY `publicacion` (`publicacion`);

--
-- Indices de la tabla `fotos`
--
ALTER TABLE `fotos`
  ADD PRIMARY KEY (`publicacion`,`foto`);

--
-- Indices de la tabla `ofertas`
--
ALTER TABLE `ofertas`
  ADD PRIMARY KEY (`usuario`,`venta`),
  ADD KEY `venta` (`venta`);

--
-- Indices de la tabla `publicacion`
--
ALTER TABLE `publicacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Vendedor` (`Vendedor`);

--
-- Indices de la tabla `pujas`
--
ALTER TABLE `pujas`
  ADD PRIMARY KEY (`usuario`,`subasta`,`puja`),
  ADD KEY `subasta` (`subasta`);

--
-- Indices de la tabla `subasta`
--
ALTER TABLE `subasta`
  ADD PRIMARY KEY (`publicacion`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`Login`),
  ADD UNIQUE KEY `Email` (`Email`(120)) USING BTREE;

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`Publicacion`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `publicacion`
--
ALTER TABLE `publicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD CONSTRAINT `favoritos_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`Login`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `favoritos_ibfk_2` FOREIGN KEY (`publicacion`) REFERENCES `publicacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `fotos`
--
ALTER TABLE `fotos`
  ADD CONSTRAINT `fotos_ibfk_1` FOREIGN KEY (`publicacion`) REFERENCES `publicacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `ofertas`
--
ALTER TABLE `ofertas`
  ADD CONSTRAINT `ofertas_ibfk_2` FOREIGN KEY (`venta`) REFERENCES `venta` (`Publicacion`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ofertas_ibfk_3` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`Login`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `publicacion`
--
ALTER TABLE `publicacion`
  ADD CONSTRAINT `publicacion_ibfk_1` FOREIGN KEY (`Vendedor`) REFERENCES `usuario` (`Login`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `pujas`
--
ALTER TABLE `pujas`
  ADD CONSTRAINT `pujas_ibfk_2` FOREIGN KEY (`subasta`) REFERENCES `subasta` (`publicacion`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pujas_ibfk_3` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`Login`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `subasta`
--
ALTER TABLE `subasta`
  ADD CONSTRAINT `subasta_ibfk_1` FOREIGN KEY (`publicacion`) REFERENCES `publicacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `venta`
--
ALTER TABLE `venta`
  ADD CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`Publicacion`) REFERENCES `publicacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
