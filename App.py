# ✅ How AI Engineers Do

import pandas as pd
import numpy as np
import time

# Load the file into memory
df = pd.read_csv('massive_dataset.csv')

# Make copies so we can test both methods fairly
df_beginner = df.copy()
df_engineer = df.copy()

#============================================
print("\nStarting AI Engineer vectorized processing...")
start_time = time.time()

# 1 Single line of code handles all 1 million rows instantly
df_engineer['Role_Tier'] = np.where(df_engineer['Experience_Yrs'] >= 5, 'Senior', 'Junior')

end_time = time.time()
print(f"AI Engineer Vectorization Took: {end_time - start_time:.4f} seconds ⚡")

# 1. Generate 1 Million rows instantly in memory
print("⚡ LOADING 1,000,000 ROWS OF DATA...")
data = {
    'User_ID': np.arange(1000000, 2000000),
    'Role': np.random.choice(['Developer', 'Data Analyst'], size=1000000),
    'Experience_Yrs': np.random.randint(1, 15, size=1000000)
}
df = pd.DataFrame(data)

# 2. Print the Raw Table before processing
print("\n=== RAW INCOMING DATASET ===")
print(df)

print("\n" + "="*50)
print("⚡ APPLYING 1-LINE AI VECTORIZATION...")
print("="*50)

# 3. The 1-Line Vectorized Engine
df['Role_Tier'] = np.where(df['Experience_Yrs'] >= 5, 'Senior', 'Junior')

# 4. Print the Final Table showing the massive update
print("\n=== PROCESSED DATASET (VECTORIZED INSTANTLY) ===")
print(df)



