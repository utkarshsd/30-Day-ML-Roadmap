# ⚡ BLAZING FAST: C-Speed Vectorization
# Processes millions of rows instantly
import pandas as pd
import numpy as np

# 1. Create a dummy dataset so the code actually has data to process
data = {
    'Username': ['alex_ai', 'coder_99', 'ml_wizard', 'python_dev'],
    'Experience_Yrs': [6, 2, 8, 3]
}
df = pd.DataFrame(data)




df['Role_Tier'] = np.where(
    df['Experience_Yrs'] >= 5, 
    'Senior', 
    'Junior'
)
