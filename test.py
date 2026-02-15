import pandas as pd
import numpy as np

data = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Hadi", "Nima", "Zahra"],
    "math": [18, 15, np.nan, 20, 17, 14, 19],
    "physics": [17, np.nan, 16, 19, 18, 13, 20],
    "chemistry": [19, 20, 1, 4, 9, np.nan, np.nan],
    "class": ["A", "A", "B", "B", "A", "B", "A"]
}
df = pd.DataFrame(data)

# شدت پراکندگی داده‌ها، با تأکید بیشتر روی فاصله‌های بزرگ -var
# می‌گه داده‌هات چقدر از میانگین پخش شدن -std

# df.rename(columns={'math':'riazi'}, inplace=True) -> بدون اینپلیس: نیاز به انتصاب به متغییر دارد و یک نسخه جدید درست میکند
# astype: تغییر نوع داده در یک ستون

# print(df.duplicated(subset=['class'], keep="first"))

# print(df.drop_duplicates(subset=['class'], keep="first"))

# print(df.loc[0, 'math'])
# print(df.iloc[0,1])
# print(df.loc[0:2]) # شامل اخری میشه
# print(df.iloc[0:2]) # شامل اخری نمیشه

# print(df.query("math > 18 and physics > 19"))
# print(df.query("math > 18 | physics > 11"))
# score = 10
# print(df.query("physics > @score")) # درصورت نیاز به استفاده از متغییر های لوکال بود از @ استفاده میکنیم
# print(df.loc[df.query("math > 18 and physics > 19").index, 'class'])

# print(df[df['name'].isin(['Hadi'])])
# print(df[~df['name'].isin(['Hadi'])]) # همه بجز هادی رو نشون بده
