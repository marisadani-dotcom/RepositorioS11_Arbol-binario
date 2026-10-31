# =====================================================================
# ACTIVIDAD INTEGRADORA - SEMANA 11: ÁRBOLES BINARIOS
# =====================================================================

class Nodo:
    """Clase que representa un nodo en un árbol binario."""
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    """Clase para gestionar la estructura y operaciones del árbol binario."""
    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        """Verifica si el árbol está vacío."""
        return self.raiz is None

    def mostrar_arbol(self, nodo=None, nivel=0, prefijo="Raíz: "):
        """
        Muestra la representación gráfica del árbol en consola de forma jerárquica.
        """
        if nodo is None:
            if nivel == 0:
                print("   (El árbol está vacío)")
            return

        print(" " * (nivel * 4) + prefijo + str(nodo.dato))
        
        if nodo.izquierdo or nodo.derecho:
            if nodo.izquierdo:
                self.mostrar_arbol(nodo.izquierdo, nivel + 1, "├─ [Izq]: ")
            else:
                print(" " * ((nivel + 1) * 4) + "├─ [Izq]: None")
                
            if nodo.derecho:
                self.mostrar_arbol(nodo.derecho, nivel + 1, "└─ [Der]: ")
            else:
                print(" " * ((nivel + 1) * 4) + "└─ [Der]: None")

    def obtener_hojas(self, nodo, hojas=None):
        """Identifica y retorna una lista con todos los nodos hoja (sin hijos)."""
        if hojas is None:
            hojas = []

        if nodo is not None:
    
            if nodo.izquierdo is None and nodo.derecho is None:
                hojas.append(nodo.dato)
            self.obtener_hojas(nodo.izquierdo, hojas)
            self.obtener_hojas(nodo.derecho, hojas)

        return hojas


# =====================================================================
# MENÚ INTERACTIVO Y DEMOSTRACIÓN
# =====================================================================

def ejecutar_demostracion():
    print("=" * 50)
    print("      SISTEMA DE GESTIÓN DE ÁRBOLES BINARIOS")
    print("=" * 50)

    arbol = ArbolBinario()
    arbol.raiz = Nodo("Ana")
    
    arbol.raiz.izquierdo = Nodo("Luis")
    arbol.raiz.derecho = Nodo("María")

    arbol.raiz.izquierdo.izquierdo = Nodo("Carlos")
    arbol.raiz.izquierdo.derecho = Nodo("Elena")
    arbol.raiz.derecho.derecho = Nodo("Sofia")

    print("\n---> Representación del Árbol Binario:")
    arbol.mostrar_arbol(arbol.raiz)

    hojas = arbol.obtener_hojas(arbol.raiz)
    print("\n---> Nodos Hoja encontrados:")
    print(f"   Hojas: {hojas}")
    print("=" * 50)

if __name__ == "__main__":
    ejecutar_demostracion()