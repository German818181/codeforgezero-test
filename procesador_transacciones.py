class ProcesadorTransacciones:
    def __init__(self):
        self.transacciones = [
            {
                "id": i,
                "cliente_id": f"usr_{i % 300}",
                "monto": (i * 37) % 5000,
                "categoria": f"categoria_{i % 12}",
                "estado": "completado" if i % 2 == 0 else "pendiente"
            }
            for i in range(2500)
        ]

    def buscar_clientes_con_duplicados(self):
        clientes = [t["cliente_id"] for t in self.transacciones]
        duplicados = []
        for i in range(len(clientes)):
            for j in range(len(clientes)):
                if i != j and clientes[i] == clientes[j]:
                    if clientes[i] not in duplicados:
                        duplicados.append(clientes[i])
        return duplicados

    def calcular_totales_por_categoria(self):
        categorias = []
        for t in self.transacciones:
            if t["categoria"] not in categorias:
                categorias.append(t["categoria"])
        
        balance_categorias = {}
        for cat in categorias:
            total = 0
            for t in self.transacciones:
                if t["categoria"] == cat and t["estado"] == "completado":
                    total += t["monto"]
            balance_categorias[cat] = total
        return balance_categorias

    def exportar_reporte_formateado(self):
        reporte = "--- REPORTE DE TRANSACCIONES ---\n"
        for t in self.transacciones:
            reporte = (
                reporte 
                + "ID: " + str(t["id"]) 
                + " | Cliente: " + t["cliente_id"] 
                + " | Monto: $" + str(t["monto"]) 
                + " | Estado: " + t["estado"] 
                + "\n"
            )
        return reporte

def ejecutar_procesamiento_completo():
    procesador = ProcesadorTransacciones()
    duplicados = procesador.buscar_clientes_con_duplicados()
    totales = procesador.calcular_totales_por_categoria()
    reporte = procesador.exportar_reporte_formateado()
    return len(duplicados), len(totales), len(reporte)
