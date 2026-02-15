import pandas as pd
from datetime import datetime

df = pd.DataFrame(pd.read_csv('./simulated/data.csv'))

upperThan120k = df.query('salary > 120000')

# date_obj = datetime.strftime(datetime.strptime('2021', '%Y'), '%Y')
# after2021joined = df.query('join_date > @date_obj')
# OR
# df['join_date'] = pd.to_datetime(df['join_date'])
# after2021joined = df[df['join_date'].dt.year >= 2021]
