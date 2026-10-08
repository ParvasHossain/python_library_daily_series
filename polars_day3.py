import polars as pl

# 1. Create a LazyFrame query pipeline pointing to your dataset
lazy_query = (
    pl.scan_csv("patient_churn_dataset.csv")  # Tracks data stream without immediate loading
    .filter(
        (pl.col("Age") > 30) &                # Capitalized 'Age' to match your schema
        (pl.col("Churn") == 1)                # Capitalized 'Churn' to match your schema
    )
    .select(["Patient_ID", "Age", "Churn"])   # Case-sensitive projection selection
)

# 2. Inspect the optimized query plan before execution
print("Optimized Logical Plan:")
print(lazy_query.explain())

# 3. Execute the query in the Rust engine across your CPU threads
df = lazy_query.collect()

# Preview the results
print("\nProcessed Data Preview:")
print(df.head())
