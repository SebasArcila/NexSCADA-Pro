import psycopg2
from psycopg2.extras import RealDictCursor

DB_PARAMS = {
    'database': 'bd-scymd',
    'user': 'scada_admin',
    'password': 'Rlb*1985',
    'host': '181.143.156.230',
    'port': 5432,
    'connect_timeout': 5
}

def find_cloro():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # Buscamos en VAR20 = 3 o 4 (típicos para químicos/cloro)
    for t in ['variable2', 'variable2_1']:
        for v20 in [1, 2, 3, 4]:
            try:
                cur.execute(f"SELECT * FROM {t} WHERE iddispositivo = 95 AND var20 = {v20} ORDER BY fecha DESC LIMIT 1")
                res = cur.fetchone()
                if res:
                    print(f"[{t}] VAR20={v20} -> {res}")
            except:
                conn.rollback()

    cur.close()
    conn.close()

if __name__ == "__main__":
    find_cloro()
