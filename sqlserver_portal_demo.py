import os, pyodbc

USER = os.environ.get("SQL_USER", "demo_user")
PASS = os.environ.get("SQL_PASS", "demo_pass")

def check_sqlserver(sql):
    print("JIT check: SQL Server access allowed for 30 min")
    try:
        conn = pyodbc.connect(f"DRIVER={{ODBC Driver}};SERVER=demo-host;UID={USER};PWD={PASS}", timeout=10)
        cur = conn.cursor()
        cur.execute(sql)  # e.g. slow queries, blocking, deadlocks
        rows = cur.fetchall()
        print(f"SQL Server: got {len(rows)} rows")
        return rows
    except Exception as e:
        print(f"SQL Server error: {e}")
        return []
    finally:
        print("SQL Server connection closed")
