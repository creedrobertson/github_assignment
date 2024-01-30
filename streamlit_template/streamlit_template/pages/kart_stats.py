import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

#Display first dataframe
df_kart = pd.read_csv('data/kart_stats.csv')
#st.dataframe(df_kart)

df_kart = df_kart[['Body','Weight', 'Acceleration', 'Mini-Turbo', 'On-Road traction', 'Off-Road Traction']]

st.dataframe(df_kart.style
             .highlight_max(color='lightgreen', axis=0,subset=['Body','Weight', 'Acceleration', 'Mini-Turbo', 'On-Road traction', 'Off-Road Traction'])
             .highlight_min(color='red', axis=0,subset=['Body','Weight', 'Acceleration', 'Mini-Turbo', 'On-Road traction', 'Off-Road Traction'])
)


# 2 Different Charts
st.header("2 charts for you to consider:")


#st.scatter_chart(df_kart, x='Weight', y=['Acceleration', 'Mini-Turbo', 'On-Road traction', 'Off-Road Traction'])
st.scatter_chart(df_kart, x='On-Road traction', y='Off-Road Traction')


st.bar_chart(df_kart, x='Body', y=['Acceleration', 'Mini-Turbo', 'On-Road traction', 'Off-Road Traction'])


#Dynamic bar chart for individual Kart
st.header("See kart stats:")
chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
st.bar_chart(df_unp_kart, x='category', y='strength')