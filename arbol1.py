class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

# Ejemplo de creación e interconexión básica
raiz = Nodo("A")
raiz.izquierdo = Nodo("B")
raiz.derecho = Nodo("C")