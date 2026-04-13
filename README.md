# Proyecto Árbol AVL en Python

---

## Integrantes

| Nombre                                | Carnet 
| ------------------------------------  | ------ 
|    Daniel Alexander Ovalle Estrada    |  9091-24-19051
|    Pablo Andrés Say Oliva             |  9490-24-18876

---

## Descripción del Proyecto

Este proyecto consiste en la implementación de un programa interactivo en Python que permite la creación, manipulación y visualización de un Árbol AVL, extendiendo las funcionalidades de un Árbol Binario de Búsqueda (ABB).

El sistema funciona mediante una interfaz de línea de comandos (CLI), donde el usuario puede realizar diferentes operaciones sobre el árbol de forma dinámica.

---

## Objetivos

* Implementar un Árbol AVL utilizando herencia a partir de un ABB.
* Garantizar el balance automático del árbol mediante rotaciones.
* Permitir la interacción del usuario a través de un menú en consola.
* Cargar datos desde archivos CSV.
* Generar una representación visual del árbol utilizando Graphviz.

---

## Funcionalidades

El programa permite realizar las siguientes operaciones:

* Insertar elementos en el árbol AVL.
* Buscar un elemento dentro del árbol.
* Eliminar elementos asegurando el reequilibrio.
* Cargar datos desde archivos CSV.
* Generar una visualización del árbol en formato gráfico (Graphviz).

---

## Requisitos

* Python 3.x
* Graphviz instalado en el sistema

---

## Cómo ejecutar el programa

1. Clonar el repositorio:

```
git clone <URL_DEL_REPOSITORIO>
```

2. Acceder a la carpeta del proyecto:

```
cd nombre_del_proyecto
```

3. Ejecutar el programa:

```
python avl.py
```

---

## Uso del programa

Al ejecutar el programa, se mostrará un menú interactivo con las siguientes opciones:

1. Insertar un número
2. Buscar un número
3. Eliminar un número
4. Cargar datos desde archivo CSV
5. Visualizar árbol (Graphviz)
6. Salir

El usuario debe seleccionar la opción deseada e ingresar los datos correspondientes.

---

## Archivos CSV de ejemplo

El proyecto incluye tres archivos CSV para pruebas:

* archivo1.csv → Datos ordenados (prueba de rotaciones)
* archivo2.csv → Datos desordenados
* archivo3.csv → Datos equilibrados

---

## Visualización con Graphviz

Para generar la imagen del árbol:

1. Ejecutar la opción de visualización en el programa.
2. Luego ejecutar en la terminal:

```
dot -Tpng arbol.dot -o arbol.png
```

Esto generará una imagen del árbol AVL.

---

## Estructura del Código

El programa está organizado de la siguiente manera:

* Clase `Nodo`: Representa cada nodo del árbol.
* Clase `ABB`: Implementa el Árbol Binario de Búsqueda.
* Clase `AVL`: Extiende ABB e implementa el balanceo.
* Funciones auxiliares:

  * Carga de CSV
  * Generación de archivo Graphviz
* Menú interactivo (CLI)

---

## Observaciones

* Se utilizó herencia para extender el ABB a AVL.
* El código es modular y documentado para facilitar su comprensión.
* Se incluyen ejemplos de datos para pruebas.
* La visualización del árbol permite analizar su estructura y balance.
