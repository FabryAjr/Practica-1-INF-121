class Fruta:
    def __init__(self, Nombre, Tipo, Vitaminas):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Vitaminas = Vitaminas
        self.NroVitaminas = len(Vitaminas)

    def getNombre(self):
        return self.Nombre

    def getTipo(self):
        return self.Tipo

    def getNroVitaminas(self):
        return self.NroVitaminas

    def getVitaminas(self):
        return self.Vitaminas

    def mostrarVitaminas(self):
        print(f"{self.Nombre} tiene las siguientes vitaminas: {', '.join(self.Vitaminas)}")

fruta1 = Fruta("Kiwi", "Subtropical", ["K", "C", "E"])
fruta2 = Fruta("Naranja", "Cítrica", ["C", "A"])
vitaminas_manzana = ["B1", "B2", "C"]
fruta3 = Fruta("Manzana", "Templada", vitaminas_manzana)

frutas = [fruta1, fruta2, fruta3]

fruta_mas_vit = max(frutas, key=lambda f: f.getNroVitaminas())
print(f"La fruta con más vitaminas es {fruta_mas_vit.getNombre()} con {fruta_mas_vit.getNroVitaminas()} vitaminas.")

fruta1.mostrarVitaminas()

citricas = [f for f in frutas if f.getTipo().lower() == "cítrica"]
for f in citricas:
    print(f"{f.getNombre()} tiene {f.getNroVitaminas()} vitaminas (cítrica).")

ordenadas = sorted(frutas, key=lambda f: f.getVitaminas()[0])
print("\nFrutas ordenadas por la primera vitamina:")
for f in ordenadas:
    print(f"{f.getNombre()} → {f.getVitaminas()}")
