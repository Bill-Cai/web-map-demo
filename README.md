# Web Map Demo (GeoServer+FastAPI+Leaflet)

说明：

- 内容：完成一个Web端的地图服务小案例。
- 目标：
  - 了解Web端应用的概念，理解前后端和网页服务；
  - 了解地图服务；
  - 简单学习前后端的技术框架。
- 技术路线：[GeoServer](https://geoserver.org/) + [FastAPI](https://fastapi.tiangolo.com/) + [Leaflet](https://leafletjs.com/)

代码库：[https://github.com/Bill-Cai/web-map-demo](https://github.com/Bill-Cai/web-map-demo)

目录：

- [Web Map Demo (GeoServer+FastAPI+Leaflet)](#web-map-demo-geoserverfastapileaflet)
  - [1 背景介绍](#1-背景介绍)
  - [2 相关技术](#2-相关技术)
    - [2.1 GeoServer](#21-geoserver)
    - [2.2 FastAPI](#22-fastapi)
    - [2.3 Leaflet](#23-leaflet)
  - [3 案例实现](#3-案例实现)

## 1 背景介绍

随着地理信息技术的快速发展，Web地图服务已经成为各种应用的核心组成部分。Web地图通过将地图数据与Web前端技术结合，向用户展示动态、交互式的地理信息。本项目将使用GeoServer、FastAPI和Leaflet技术构建一个Web地图服务，提供地理数据的可视化展示。通过这一过程，展示新手该如何搭建一个Web端地图应用，并对前后端技术的基本框架有一个初步的认识。

该案例的目标是让用户熟悉Web地图服务的基本工作原理，掌握如何通过**后端提供地图数据**，通过**前端地图框架展示数据**，并实现简单的交互功能。

## 2 相关技术

### 2.1 GeoServer

[GeoServer](https://geoserver.org/) 是一个开源的地图服务器软件，用于发布、共享、编辑和处理地理空间数据。GeoServer支持多种标准数据格式，如Shapefile、PostGIS数据库、GeoTIFF等，并通过标准的Web服务协议（如WMS、WFS、WCS）向客户端提供地图服务。在本案例中，GeoServer将用于发布地图数据并通过Web接口提供给前端进行显示。

### 2.2 FastAPI

[FastAPI](https://fastapi.tiangolo.com/) 是一个用于构建现代Web APIs的高性能框架，基于Python语言构建，能够快速开发高效且易于使用的API。在本案例中，FastAPI将作为后端服务框架，用于提供GeoServer的地图数据接口，并将其传递到前端进行展示。

### 2.3 Leaflet

[Leaflet](https://leafletjs.com/) 是一个轻量级、开源的JavaScript库，用于构建交互式地图应用。它支持从多个来源加载地图数据（包括GeoServer、OpenStreetMap、Google Maps等），并能够在地图上进行标记、绘制图形等操作。在本案例中，Leaflet将用于构建前端地图应用，向用户展示GeoServer提供的地图数据，并提供交互式的地理信息浏览体验。

## 3 案例实现
