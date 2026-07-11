# ❌ Beginner Organizing Data

import pandas as pd
import numpy as np
import time

# Load the file into memory
df = pd.read_csv('massive_dataset.csv')

# Make copies so we can test both methods fairly
df_beginner = df.copy()
df_engineer = df.copy()

#============================================
print("Starting Beginner loop processing...")
start_time = time.time()

# Iterating row-by-row through 1 million rows
for index, row in df_beginner.iterrows():
    if row['Experience_Yrs'] >= 5:
        df_beginner.loc[index, 'Role_Tier'] = 'Senior'
    else:
        df_beginner.loc[index, 'Role_Tier'] = 'Junior'

end_time = time.time()
print(f"Beginner Loop Took: {end_time - start_time:.2f} seconds 🐌")

