# PE-FIB-Transversal: NASA Exoplanet Archive Data

This repository contains data extracted from the official [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars), which consolidates various studies on each exoplanet. The extracted columns include:

1. **Planet Name (pl_name)**
2. **Host Name (hostname)**
3. **Planet Density (pl_dens)** - where available
4. **Planet Mass ("Earth Mass") (pl_bmasse)**
5. **Planet Radius ("Earth Radius") (pl_rade)**
6. **Equilibrium Temperature (pl_eqt)**
7. **Spectral Type (st_spectype)**
8. **Stellar Effective Temperature (st_teff)**
9. **Radial Velocity (ve(m/s))**


# Introducción General al Estudio

Con el propósito final de determinar qué clase de estrella presenta una mayor probabilidad de hospedar exoplanetas con características similares a la Tierra, emprenderemos un estudio estadístico basado en una muestra aleatoria (véase anexo) compuesta por 1031 planetas confirmados, cada uno de ellos con sus Índices de Similitud Terrestre (IST) debidamente calculados (véase anexo). Este análisis incluirá la aplicación de diversos modelos estadísticos con el fin de comparar las diferentes formas de calcular el IST y los cinco grupos generales de estrellas (A, F, G, K, M).

En una primera fase de nuestro estudio, estudiaremos y compararemos dos de las formas de calcular el Índice de Similitud Terrestre, el IST Interior y el IST Exterior. Los compararemos enfocándonos en la igualación del parámetro μ mediante muestras emparejadas (Y1, Y2), donde Di = μD + 𝜺𝜺i y D = Y1 – Y2, siendo esta última la variable de respuesta. La muestra emparejada estará compuesta por los IST Interior y IST Exterior de cada planeta, los cuales, en conjunto, constituirán nuestra muestra de análisis.

En la segunda fase, realizaremos dos modelos lineales de gran interés, uno de simple y otro de múltiple. El modelo lineal simple intentará predecir el IST Global del exoplaneta mediante la temperatura de su estrella anfitriona, veremos por ejemplo si una mayor temperatura reduce la posibilidad de que exista un planeta con una similitud con la Tierra, o todo lo contrario, la aumenta. Más adelante, realizaremos un modelo lineal múltiple que nos va a permitir calcular el IST Global del exoplaneta mediante su IST Interior y la temperatura de la estrella. Un modelo muy interesante ya que nos permitiría predecir el IST sin tener la temperatura superficial del exoplaneta, un dato que a veces es difícil de obtener.

Por último, cojeremos los dos grupos principales estelares (Grupos M, K) donde los analizaremos y determinaremos qué tipo de estrella tiene una mayor probabilidad de albergar planetas similares a la Tierra. Para realizar este estudio utilizaremos un modelo comparando el parámetro μ en los dos grupos independientes.

## Sample Data

Here are the first 10 entries of the dataset:

```plaintext
| pl_name       | hostname   | pl_rade | pl_bmasse | pl_dens | pl_eqt | st_spectype | st_teff | ve(m/s)    | ISTi           | ISTe           | IST global     |
|---------------|------------|---------|-----------|---------|--------|-------------|---------|------------|---------------|---------------|----------------|
| WASP-193 b    | WASP-193   | 16.41   | 44.17815  | 0.059   | 1254   | F           | 6078    | 18350.23598| 0.0686156919  | 0.05815374972 | 0.06316850302  |
| K2-141 c      | K2-141     | 7       | 8         | 0.081   | 695    | K           | 4570    | 11956.0619 | 0.1012485617  | 0.2224310563  | 0.1500693991   |
| WASP-17 b     | WASP-17    | 20.961  | 247.9074  | 0.082   | 1755   | F           | 6550    | 38461.91712| 0.07642018177 | 0.02211764498 | 0.041112461    |
| TOI-615 b     | TOI-615    | 18.977  | 138.25536 | 0.084   | 1666   | F           | 6850    | 30186.96084| 0.07951403407 | 0.02669463335 | 0.04607166141 |
| TOI-2641 b    | TOI-2641   | 18.103  | 122.68177 | 0.092   | 1387   | F           | 6100    | 29114.33818| 0.08448629932 | 0.04140903735 | 0.05914808809 |
| KELT-11 b     | KELT-11    | 15.132  | 54.34893  | 0.093   | 1712   | G           | 5375    | 21195.29738| 0.08916194844 | 0.02725710901 | 0.04929804203 |
| HAT-P-65 b    | HAT-P-65   | 21.185  | 167.49641 | 0.096   | 1930   | G           | 5835    | 31447.10703| 0.0827934965  | 0.01854854782 | 0.03918799726 |
| TrES-4 b      | TrES-4     | 18.046  | 247.9074  | 0.099   | 1778   | F           | 6200    | 41452.0917 | 0.0878829466  | 0.02100312824 | 0.04296297007 |
| WASP-94 A b   | WASP-94 A  | 17.71   | 158.915   | 0.118   | 1604   | F           | 6170    | 33501.58442| 0.09685335605 | 0.02843009722 | 0.05247428255 |
| WASP-79 b     | WASP-79    | 17.15   | 270.15415 | 0.13    | 1716   | F           | 6600    | 44388.03716| 0.1027742318  | 0.02243636411 | 0.04801958023 |
...
´´´






