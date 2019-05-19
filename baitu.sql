-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-05-2019 a las 15:28:30
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
(58, 'C:\\fakepath\\run.py'),
(75, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fbici.jpg?alt=media&token=ce64630d-39a1-4f4c-abc0-ed8bafaa4fe8'),
(75, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fcoleccionismo.jpg?alt=media&token=1df961f6-58a9-4791-86a3-d598c2d29f21'),
(75, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectronica.jpg?alt=media&token=bab41776-95e2-4fec-975e-e9bb2c0b78ee'),
(75, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Ftelefonia.jpg?alt=media&token=a7ad8f55-5bcd-4fb0-a3f0-916579a1cb2b'),
(77, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fdeporte.jpg?alt=media&token=a9a32d0c-5c44-4577-844f-54d86e5ae760'),
(77, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectrodomestico.jpg?alt=media&token=44ba4851-5424-4514-951b-7e1771d82138'),
(77, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectronica.jpg?alt=media&token=37ffea33-8207-4c62-9a8e-4210a29dd941'),
(77, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Flibro.jpg?alt=media&token=ca0a0ea3-5316-44af-b397-97fd295845ae'),
(78, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Finmobiliaria.jpg?alt=media&token=ed31d84c-3a22-4c17-a03d-8b6c4dd64c89'),
(78, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fmoda.jpg?alt=media&token=2086e49d-ec43-4ccf-b257-bf696fe1c2be'),
(78, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fmoda.jpg?alt=media&token=a9d84c1b-1b62-4506-a2e4-33f63117f669'),
(78, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Ftodo.jpg?alt=media&token=b9f27186-16b4-4823-b503-ec76931d00e8'),
(83, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fconstruccion.jpg?alt=media&token=895adc0e-7463-44b7-91d0-99c73d412bb8'),
(83, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectronica.jpg?alt=media&token=da8478ad-0cd1-4f4b-8e14-4c3a0a700c2d'),
(83, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fempleo.jpg?alt=media&token=7f5afa54-b0eb-457b-ae93-549d457f87de'),
(83, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Flibro.jpg?alt=media&token=e50a77cc-3ee0-436f-89e4-c38ae8a06759'),
(85, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fbixorobar.jpg?alt=media&token=441ab194-063b-43e0-87de-8b93f2198137'),
(85, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectronica.jpg?alt=media&token=7f29a278-b4e7-45ee-8536-95c7a6ec6495'),
(85, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fempleo.jpg?alt=media&token=832df898-b0ad-4f5d-b817-1f92fad252d8'),
(85, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fmoda.jpg?alt=media&token=193ef988-deb9-489d-9572-a91c713103df'),
(86, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectrodomestico.jpg?alt=media&token=0eb57f6f-b3ad-44d9-a822-8337232fd56a'),
(86, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectronica.jpg?alt=media&token=96cf144c-f6f8-469d-88fa-daf5cbe561fd'),
(86, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fempleo.jpg?alt=media&token=3a36437c-2f80-4dd3-8fc4-bcccde6aad3d'),
(86, 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Ficono.png?alt=media&token=340459a1-a176-4a57-99fa-0d216738259f');

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
  `Vendedor` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `FotoPrincipal` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `publicacion`
--

INSERT INTO `publicacion` (`id`, `Nombre`, `Descripcion`, `Fecha`, `Categoria`, `nuevoUsuario`, `Vendedor`, `FotoPrincipal`) VALUES
(58, 'Ipad mini', 'Semi nuevo.', '11/3/2019', '...', 'Pepe', 'Alex', ''),
(75, 'Barbacoa', 'fff', '18/4/2019', 'Libros y Música', '', 'Alex', 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fcoleccionismo.jpg?alt=media&token=1df961f6-58a9-4791-86a3-d598c2d29f21'),
(77, 'Abrigo nuevo', 'dds', '18/4/2019', 'Construcción', '', 'Alex', 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectrodomestico.jpg?alt=media&token=44ba4851-5424-4514-951b-7e1771d82138'),
(78, 'Abrigo', 'gfddfs', '2019-5-19', 'Empleo', '', 'Alex', 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Fmoda.jpg?alt=media&token=2086e49d-ec43-4ccf-b257-bf696fe1c2be'),
(83, 'p3', 'eee', '2019-5-19', 'Empleo', '', 'Alex', 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Flibro.jpg?alt=media&token=e50a77cc-3ee0-436f-89e4-c38ae8a06759'),
(85, 'subasta3 (SUBASTA)', 'dds', '2019-5-19', 'Moda', '', 'Alex', 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectronica.jpg?alt=media&token=7f29a278-b4e7-45ee-8536-95c7a6ec6495'),
(86, 'subaste3', 'ddd', '2019-5-19', 'Niños', '', 'Alex', 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectrodomestico.jpg?alt=media&token=0eb57f6f-b3ad-44d9-a822-8337232fd56a');

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
  `precio_actual` double NOT NULL,
  `precio_salida` double NOT NULL,
  `hora_limite` text COLLATE utf8_unicode_ci NOT NULL,
  `fecha_limite` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `subasta`
--

INSERT INTO `subasta` (`publicacion`, `precio_actual`, `precio_salida`, `hora_limite`, `fecha_limite`) VALUES
(85, 24, 24, '12:00', '2019-05-24');

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
('Alex', 'Alex', 'Costa Moreno', 'hola', '', '', 0, 'a.guti1417@hotmail.com', 0),
('Josete', 'Josete', 'josetess', 'hola', '', 'https://firebasestorage.googleapis.com/v0/b/proyectosoftware-2397d.appspot.com/o/fotos%2Felectrodomestico.jpg?alt=media&token=478d5275-3532-4c59-9a2d-ebed86e962eb', 7878, 'javiurbe@gmail.com', 0),
('Juan', 'Juan', 'Bosco', 'hola', '', '', 86639883, 'a.guti3@hotmail.cox', 0),
('sergio', 'sergio', 'costa moreno', 'hola', '', '', 0, '', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `Publicacion` int(11) NOT NULL,
  `Precio` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`Publicacion`, `Precio`) VALUES
(58, 400),
(75, 15),
(77, 12),
(78, 24),
(83, 15),
(86, 24);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

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
