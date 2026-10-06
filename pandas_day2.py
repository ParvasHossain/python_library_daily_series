import pandas as pd

df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': ['x', 'y', 'z']
})

# Accessing underlying block array structures
print("Internal Block Types:")
for block in df._mgr.blocks:
    print(f"Type: {block.dtype}, Columns: {block.shape}")

# Fast hash-table index lookup behind the scenes
print("\nRow lookup by index label:", df.loc[1, 'a'])