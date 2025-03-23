import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Menyiapkan data day_df
day_df = pd.read_csv("Data/day.csv")

# Menghapus kolom yang tidak diperlukan
drop_col = ['windspeed']
for col in drop_col:
    if col in day_df.columns:
        day_df.drop(labels=col, axis=1, inplace=True)

# Mengubah nama kolom untuk konsistensi
day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_cond',
    'cnt': 'count'
}, inplace=True)

# Mengubah angka menjadi kategori
day_df['month'] = day_df['month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})

# Visualisasi yang sesuai dengan notebook
st.title("Bike Sharing Dashboard")

st.subheader("Distribusi Penyewaan Sepeda per Bulan")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='month', y='count', data=day_df, estimator=sum, ax=ax)
plt.xlabel("Bulan")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.subheader("Distribusi Penyewaan Sepeda per Musim")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='season', y='count', data=day_df, estimator=sum, ax=ax)
plt.xlabel("Musim")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)
