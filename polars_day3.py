import polars as pl

# Create a LazyFrame query pipeline
lazy_query = (
    pl.scan_csv("data.csv")  # Does not load file immediately
    .filter(pl.col("age") > 25)  # Predicate Pushdown
    .select(["name", "age"])      # Projection Pushdown
)

# Inspect optimized query plan before execution
print("Optimized Logical Plan:")
print(lazy_query.explain())

# Execute query in Rust engine across CPU threads
# df = lazy_query.collect()