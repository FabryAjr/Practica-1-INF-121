class Matriz:
    def __init__(self, matriz=None):
        
        self.matriz = [[0.0]*10 for _ in range(10)]
        
        if matriz is None:
            
            for i in range(10):
                self.matriz[i][i] = 1.0
        else:
            for i in range(10):
                for j in range(10):
                    self.matriz[i][j] = matriz[i][j]

    def sumar(self, otro):
        resultado = Matriz()
        for i in range(10):
            for j in range(10):
                resultado.matriz[i][j] = self.matriz[i][j] + otro.matriz[i][j]
        return resultado

    def restar(self, otro):
        resultado = Matriz()
        for i in range(10):
            for j in range(10):
                resultado.matriz[i][j] = self.matriz[i][j] - otro.matriz[i][j]
        return resultado

    def igual(self, otro):
        for i in range(10):
            for j in range(10):
                if self.matriz[i][j] != otro.matriz[i][j]:
                    return False
        return True

    def mostrar(self):
        for fila in self.matriz:
            print("\t".join(map(str, fila)))
        print()


if __name__ == "__main__":
    m2 = [[0.0]*10 for _ in range(10)]
    m2[0][0] = 5
    m2[1][1] = 2  

    A = Matriz()      
    B = Matriz(m2)    

    print("Matriz A (Identidad):")
    A.mostrar()

    print("Matriz B:")
    B.mostrar()

    C = A.sumar(B)
    print("A + B:")
    C.mostrar()

    D = A.restar(B)
    print("A - B:")
    D.mostrar()

    print("A es igual a B?", "Sí" if A.igual(B) else "No")
