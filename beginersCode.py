# ❌ Beginner Code
# (Slow loop)
# ❌ SLOW: Row-by-row iteration
# Takes seconds to process big data
import pandas as pd
import numpy as np

# 1. Create a dummy dataset so the code actually has data to process
data = {
    'Username': ['alex_ai', 'coder_99', 'ml_wizard', 'python_dev'],
    'Experience_Yrs': [6, 2, 8, 3]
}
df = pd.DataFrame(data)




for index, row in df.iterrows():
    if row['Experience_Yrs'] >= 5:
        df.loc[index, 'Role_Tier'] = 'Senior'
    else:
        df.loc[index, 'Role_Tier'] = 'Junior'

        
