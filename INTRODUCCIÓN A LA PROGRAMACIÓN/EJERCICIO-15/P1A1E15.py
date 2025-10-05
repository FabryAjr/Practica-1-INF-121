class Carta:
    def __init__(self, Codigo, Descripcion, Remitente, Destinatario):
        self.Codigo = Codigo
        self.Descripcion = Descripcion
        self.Remitente = Remitente
        self.Destinatario = Destinatario

    def getCodigo(self):
        return self.Codigo

    def getDescripcion(self):
        return self.Descripcion

    def getRemitente(self):
        return self.Remitente

    def getDestinatario(self):
        return self.Destinatario

    def mostrar(self):
        print(f"Código: {self.Codigo} | Remitente: {self.Remitente} | Destinatario: {self.Destinatario}")
        print(f"Descripción: {self.Descripcion}\n")


class Buzon:
    def __init__(self, Nro):
        self.Nro = Nro
        self.Cartas = []
        self.NroC = 0

    def agregarCarta(self, carta):
        self.Cartas.append(carta)
        self.NroC += 1

    def eliminarCarta(self, codigo):
        self.Cartas = [c for c in self.Cartas if c.getCodigo() != codigo]
        self.NroC = len(self.Cartas)

    def contarCartasDestinatario(self, destinatario):
        return sum(1 for c in self.Cartas if c.getDestinatario() == destinatario)

    def buscarPalabra(self, palabra):
        resultado = []
        for c in self.Cartas:
            if palabra.lower() in c.getDescripcion().lower():
                resultado.append(c)
        return resultado

    def mostrarCartas(self):
        print(f"Buzón {self.Nro} ({self.NroC} cartas)")
        for c in self.Cartas:
            c.mostrar()


b1, b2, b3 = Buzon(1), Buzon(2), Buzon(3)

c1 = Carta("C123", "Querido amigo, espero que estés bien.", "Juan Alvarez", "Peter Chaves")
c2 = Carta("C456", "Ella no te ama, pero sigue adelante.", "Pepe Mujica", "Wilmer Pérez")
c3 = Carta("C789", "Te envío amor y fuerzas.", "Paty Vasques", "Pepe Mujica")

for b in [b1, b2, b3]:
    b.agregarCarta(c1)
    b.agregarCarta(c2)
    b.agregarCarta(c3)


destinatario = "Pepe Mujica"
print(f"\n{destinatario} recibió {b1.contarCartasDestinatario(destinatario)} cartas en el buzón 1.")

b1.eliminarCarta("C456")
print("\nDespués de eliminar la carta C456:")
b1.mostrarCartas()

remitente = "Pepe Mujica"
for carta in b1.Cartas:
    if carta.getRemitente() == remitente:
        print(f"\n{remitente} ha enviado una carta a {carta.getDestinatario()}.")

palabra = "amor"
coincidencias = b1.buscarPalabra(palabra)
print(f"\nCartas que contienen la palabra '{palabra}':")
for c in coincidencias:
    c.mostrar()

