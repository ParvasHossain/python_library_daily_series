import duckdb
import pandas as pd

# Sample Pandas DataFrame
df = pd.DataFrame({"category": ["A", "B", "A", "C"], "sales": [100, 200, 150, 300]})

# Query Pandas DataFrame directly using embedded DuckDB engine without copying data
result = duckdb.query("""
    SELECT category, SUM(sales) as total_sales
    FROM df
    GROUP BY category
    ORDER BY total_sales DESC
""").df()

print(result)