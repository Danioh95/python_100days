import pandas as pd
import matplotlib.pyplot as plt

df_set = pd.read_csv("data/sets.csv")
df_color = pd.read_csv("data/colors.csv")
df_themes = pd.read_csv("data/themes.csv")

# print(df_color.nunique())
# print(df_color.groupby("is_trans").nunique())
# print(df_color.is_trans.value_counts())


# print(df_set.sort_values("year")["name"][df_set["year"]==1949].count())
try:
    print(df_set.head())

except:
    pass
print(df_set)
set_by_year = df_set.query('year < 2020').groupby("year").count()
plt.plot(set_by_year.index, set_by_year.set_num)
plt.show()