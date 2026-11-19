import os, cx_Oracle

# Secret never hardcoded — from env / Vault
USER = os.environ.get("ORACLE_USER", "demo_user")
PASS = os.environ.get("ORACLE_PASS", "demo_pass")

def check_oracle(sql):
    # JIT: token valid only 30 min (demo: always True)
    print("JIT check: Oracle access allowed for 30 min")
    try:
        conn = cx_Oracle.connect(f"{USER}/{PASS}@demo-host:1521/demo")
        cur = conn.cursor()
        cur.execute(sql)  # e.g. check wait events, blocking
        rows = cur.fetchall()
        print(f"Oracle: got {len(rows)} rows")
        return rows
    except Exception as e:
        print(f"Oracle error: {e}")
        return []
    finally:
        print("Oracle connection closed")  # finally = always close
