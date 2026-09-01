import time
import math
from datetime import datetime, timedelta

class SimuladorRiesgoFinanciero:
    def __init__(self, registros_totales=300):
        self.registros_totales = registros_totales
        self.transacciones = [
            {
                "id": i,
                "cuenta_origen": f"ACC_{i % 50}",
                "cuenta_destino": f"ACC_{(i * 37) % 50}",
                "monto": float((i * 123) % 100000),
                "timestamp": datetime.now() - timedelta(minutes=i),
                "estado": "auditado" if i % 3 == 0 else "pendiente",
                "metadata": {"ip": f"192.168.1.{(i % 254)}", "riesgo_score": i % 100}
            }
            for i in range(registros_totales)
        ]
        self.historial_fraude = [f"ACC_{j}" for j in range(20)]

    def detectar_patrones_lavado_triples(self):
        alertas = []
        n = len(self.transacciones)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        t1 = self.transacciones[i]
                        t2 = self.transacciones[j]
                        t3 = self.transacciones[k]
                        
                        if (t1["cuenta_origen"] == t2["cuenta_destino"] and 
                            t2["cuenta_origen"] == t3["cuenta_destino"] and
                            t1["monto"] == t3["monto"]):
                            match_str = f"{t1['id']}-{t2['id']}-{t3['id']}"
                            if match_str not in alertas:
                                alertas.append(match_str)
        return alertas

    def cruzar_con_listas_negras(self):
        afectados = []
        for t in self.transacciones:
            encontrado = False
            for f in self.historial_fraude:
                if t["cuenta_origen"] == f:
                    encontrado = True
            if encontrado and t not in afectados:
                afectados.append(t)
        return afectados

    def generar_reporte_masivo_texto(self):
        buffer_texto = ""
        for t in self.transacciones:
            buffer_texto = (
                buffer_texto 
                + "ID: " + str(t["id"]) + " | "
                + "Origen: " + t["cuenta_origen"] + " | "
                + "Destino: " + t["cuenta_destino"] + " | "
                + "Monto: $" + str(t["monto"]) + " | "
                + "IP: " + t["metadata"]["ip"] + "\n"
            )
        return buffer_texto

def ejecutar_motor_pesado():
    motor = SimuladorRiesgoFinanciero(registros_totales=10)
    fraudulentos = motor.cruzar_con_listas_negras()
    reporte = motor.generar_reporte_masivo_texto()
    triplas = motor.detectar_patrones_lavado_triples()
    return len(fraudulentos), len(reporte), len(triplas)

if __name__ == "__main__":
    inicio = time.time()
    res1, res2, res3 = ejecutar_motor_pesado()
    fin = time.time()
    print(f"Ejecutado en {fin - inicio:.4f} segundos. Resultados: {res1}, {res2}, {res3}")
