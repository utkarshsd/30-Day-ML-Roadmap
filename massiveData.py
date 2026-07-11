import pandas as pd
import numpy as np

print("Generating 1 million rows of data... please wait...")

# Create 1 million random user IDs, roles, and experience levels
data = {
    'User_ID': np.arange(1000000, 2000000),
    'Role': np.random.choice(['Developer', 'Data Analyst', 'Designer'], size=1000000),
    'Experience_Yrs': np.random.randint(1, 15, size=1000000)
}

# Save it as a CSV file in your folder
df = pd.DataFrame(data)
df.to_csv('massive_dataset.csv', index=False)

print("Success! 'massive_dataset.csv' is ready in your folder.")

