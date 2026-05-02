import psycopg2
import sys

# Configuración de Base de Datos
DB_PARAMS = {
    'database': 'bd-scymd',
    'user': 'scada_admin',
    'password': 'Rlb*1985',
    'host': '181.143.156.230',
    'port': 5432,
    'connect_timeout': 5
}

def test_final():
    print(f"--- Prueba Final de Variables Planta (ID 95) ---")
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        
        # Mapeo unificado a 'variable2' que es la que responde con datos
        vars_to_test = [
            ("pH Entrada",         "variable2", "var1", 1),
            ("Turbiedad Entrada",  "variable2", "var1", 2),
            ("pH Salida",          "variable2", "var2", 1),
            ("Turbiedad Salida",   "variable2", "var9", 2),
        ]

        for name, table, col, v20 in vars_to_test:
            query = f"SELECT {col}, fecha FROM {table} WHERE iddispositivo = 95 AND var20 = {v20} ORDER BY fecha DESC LIMIT 1"
            cur.execute(query)
            res = cur.fetchone()
            if res:
                print(f"[OK] {name}: {res[0]} (Fecha: {res[1]})")
            else:
                print(f"[!] {name}: Sin datos en {table} para VAR20={v20}")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_final()
