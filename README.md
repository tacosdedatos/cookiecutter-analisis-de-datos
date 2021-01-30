# Análisis de datos reproducibles

Una plantilla para proyectos de análisis de datos reproducibles inspirado [mkrapp/cookiecutter-reproducible-science](https://github.com/mkrapp/cookiecutter-reproducible-science) y [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science).

## Requisitos 
Instalar `cookiecutter`. En la línea de comandos: `pip install cookiecutter`    

## Uso
Para comenzar un nuevo proyecto:

`cookiecutter gh:tacosdedatos/cookiecutter-analisis-de-datos`

## La estructura del proyecto

```
.
├── AUTORES.md
├── LICENSE
├── README.md
├── datos
│   ├── brutos          <- Datos originales, ***inmutables***.
│   ├── externos        <- Datos de fuentes de terceros.
│   ├── interinos       <- Datos intermedios que han sido transformados.
│   └── procesados      <- Datos finales, listos para tus modelos/visualizaciones.
├── docs                <- Documentación. Por ejemplo, artículos científicos, periodísticos, etc. (ignorado por git)
├── notebooks           <- Jupyter/Rmarkdown notebooks
├── reportes            <- Para cualquier reporte/informe del proyecto y/o el manusctrito final.
│   └── figuras         <- Figuras para el manuscrito o informes.
└── src                 <- Código fuente para este proyecto.
    ├── datos           <- Scripts y programas para procesar datos.
    ├── externos        <- Cualquier código fuente externo, por ejemplo, extraer otros proyectos de git o bibliotecas externas
    ├── herramientas    <- Cualquier script de ayuda entra aquí.
    ├── modelos         <- Código fuente para tu propio modelo.
    └── visualizaciones <- Scripts para la visualización de sus resultados, por ejemplo, matplotlib, ggplot2, bokeh, altair.
```

## Licencia
Este proyecto está licenciado bajo los términos de la [Licencia MIT](/LICENSE)

## Información en el [wiki](https://github.com/tacos-de-datos/cookiecutter-analisis-de-datos/wiki)
