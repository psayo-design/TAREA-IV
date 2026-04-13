import csv
import os

# ------------------------------
# Nodo del árbol
# ------------------------------
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

# ------------------------------
# Árbol Binario de Búsqueda (ABB)
# ------------------------------
class ABB:
    def insertar(self, raiz, valor):
        if not raiz:
            return Nodo(valor)
        if valor < raiz.valor:
            raiz.izq = self.insertar(raiz.izq, valor)
        else:
            raiz.der = self.insertar(raiz.der, valor)
        return raiz

    def buscar(self, raiz, valor):
        if not raiz or raiz.valor == valor:
            return raiz
        if valor < raiz.valor:
            return self.buscar(raiz.izq, valor)
        return self.buscar(raiz.der, valor)

    def eliminar(self, raiz, valor):
        if not raiz:
            return raiz
        if valor < raiz.valor:
            raiz.izq = self.eliminar(raiz.izq, valor)
        elif valor > raiz.valor:
            raiz.der = self.eliminar(raiz.der, valor)
        else:
            if not raiz.izq:
                return raiz.der
            elif not raiz.der:
                return raiz.izq
            temp = self.min_valor(raiz.der)
            raiz.valor = temp.valor
            raiz.der = self.eliminar(raiz.der, temp.valor)
        return raiz

    def min_valor(self, nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual

# ------------------------------
# Árbol AVL (hereda de ABB)
# ------------------------------
class AVL(ABB):
    def altura(self, nodo):
        return nodo.altura if nodo else 0

    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der) if nodo else 0

    def rotar_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        return x

    def rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        return y

    def insertar(self, raiz, valor):
        raiz = super().insertar(raiz, valor)
        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))
        balance = self.balance(raiz)

        # Rotaciones
        if balance > 1 and valor < raiz.izq.valor:
            return self.rotar_derecha(raiz)
        if balance < -1 and valor > raiz.der.valor:
            return self.rotar_izquierda(raiz)
        if balance > 1 and valor > raiz.izq.valor:
            raiz.izq = self.rotar_izquierda(raiz.izq)
            return self.rotar_derecha(raiz)
        if balance < -1 and valor < raiz.der.valor:
            raiz.der = self.rotar_derecha(raiz.der)
            return self.rotar_izquierda(raiz)

        return raiz

    def eliminar(self, raiz, valor):
        raiz = super().eliminar(raiz, valor)
        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))
        balance = self.balance(raiz)

        # Rebalanceo
        if balance > 1 and self.balance(raiz.izq) >= 0:
            return self.rotar_derecha(raiz)
        if balance > 1 and self.balance(raiz.izq) < 0:
            raiz.izq = self.rotar_izquierda(raiz.izq)
            return self.rotar_derecha(raiz)
        if balance < -1 and self.balance(raiz.der) <= 0:
            return self.rotar_izquierda(raiz)
        if balance < -1 and self.balance(raiz.der) > 0:
            raiz.der = self.rotar_derecha(raiz.der)
            return self.rotar_izquierda(raiz)

        return raiz

# ------------------------------
# Graphviz
# ------------------------------
def generar_graphviz(raiz, archivo="arbol.dot"):
    with open(archivo, "w") as f:
        f.write("digraph AVL {\n")

        def recorrer(nodo):
            if nodo:
                if nodo.izq:
                    f.write(f'    {nodo.valor} -> {nodo.izq.valor};\n')
                    recorrer(nodo.izq)
                if nodo.der:
                    f.write(f'    {nodo.valor} -> {nodo.der.valor};\n')
                    recorrer(nodo.der)
        recorrer(raiz)
        f.write("}\n")

    print(f"Archivo {archivo} generado.")
    print("Ejecuta: dot -Tpng arbol.dot -o arbol.png")

# ------------------------------
# Cargar CSV
# ------------------------------
def cargar_csv(ruta, arbol, raiz):
    try:
        with open(ruta, newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                for valor in fila:
                    raiz = arbol.insertar(raiz, int(valor))
        print("Datos cargados correctamente.")
    except Exception as e:
        print("Error:", e)
    return raiz

# ------------------------------
# Menú CLI
# ------------------------------
def menu():
    arbol = AVL()
    raiz = None

    while True:
        print("\n--- MENÚ AVL ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar CSV")
        print("5. Visualizar (Graphviz)")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = int(input("Ingrese número: "))
            raiz = arbol.insertar(raiz, valor)

        elif opcion == "2":
            valor = int(input("Buscar número: "))
            encontrado = arbol.buscar(raiz, valor)
            print("Encontrado" if encontrado else "No encontrado")

        elif opcion == "3":
            valor = int(input("Eliminar número: "))
            raiz = arbol.eliminar(raiz, valor)

        elif opcion == "4":
            ruta = input("Ruta del CSV: ")
            raiz = cargar_csv(ruta, arbol, raiz)

        elif opcion == "5":
            generar_graphviz(raiz)

        elif opcion == "6":
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
