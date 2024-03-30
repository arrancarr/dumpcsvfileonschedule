import os
import pytz
import pandas as pd
from datetime import datetime

# Create a random DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Timezone conversion to Singapore Time
singapore_zone = pytz.timezone('Asia/Singapore')
sg_time = datetime.now(singapore_zone).strftime("%Y-%m-%d_%H")

# Create the tiprank folder if it doesn't exist
if not os.path.exists('tiprank'):
    os.makedirs('tiprank')


# Create CSV filename with current date and time
csv_filename = f"tiprank/data_{sg_time}.csv"
  
# Dump dataframe to CSV
df.to_csv(csv_filename, index=False)

print(f"DataFrame dumped to {csv_filename}")