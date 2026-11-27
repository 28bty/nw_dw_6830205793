import sys
import duckdb

con = duckdb.connect("northwind.duckdb")
rows = con.execute(sys.argv[1]).fetchall()
for row in rows:
    print(f"{row[0]:22}{row[1]:<12}{row[2]}")
          
