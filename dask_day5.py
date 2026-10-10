import dask.array as da

# Create a giant 10,000x10,000 matrix split into 1,000x1,000 chunks
x = da.random.random((10000, 10000), chunks=(1000, 1000))

# Lazy computation: builds a Task Graph without executing math yet
result = x.sum(axis=0)

print("Number of tasks in DAG:", len(result.dask))

# Triggers compute across CPU cores via local scheduler
# final_val = result.compute()