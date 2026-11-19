# predictive-sre-demo
# 3 Predictive SRE Portals — Demo (3 Files, 3 Logins)

This is a DEMO version. Real portals run offline inside the bank. No real data here.

## Why 3 files, not 1 file?
Because 3 databases have 3 different metrics, 3 different logins, 3 different failure modes.
One hybrid file would be wrong. Each portal is a separate program.

- `oracle_portal_demo.py` — Oracle only. Metrics: wait events, optimizer, RAC, ASM.
- `sqlserver_portal_demo.py` — SQL Server only. Metrics: blocking, deadlocks, Always On.
- `mongo_portal_demo.py` — MongoDB only. Metrics: replica set, oplog, slow ops.

## Common pattern in all 3 files (remember this, not 187 lines):
1. Secret from env / Vault — never hardcoded
2. JIT check — 30 min access, then auto-expire
3. Connect → Query → Fetch
4. try / except / finally — connection ALWAYS closed

## How to run
pip install cx_Oracle pyodbc pymongo
python oracle_portal_demo.py
python sqlserver_portal_demo.py
python mongo_portal_demo.py

Built with assistance of Claude AI for drafting. All design, logic, testing owned by me.
Runtime: Offline Random Forest, no LLM, no Cloud, no external AI.
