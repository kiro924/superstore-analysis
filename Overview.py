
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide',
                  page_title='Sales Overview'
                   )

x=pd.read_csv('Super Store Analysis Modified')
df=pd.DataFrame(x)

st.markdown(
    f"<h3 style='color: purple; font-weight: bold; font-size: 40px; text-align: center;'>Store Sales Overview</h3>", 
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5, col6=st.columns(6)

col1.markdown(f"<h3 style='color: white;'>Total Sales {int(df['Sales'].sum()):,}</h3>", unsafe_allow_html=True)

col2.markdown(f"<h3 style='color: white;'>Total Customers {df['Customer Name'].nunique()}</h3>", unsafe_allow_html=True)

col3.markdown(f"<h3 style='color: white;'>New York City {252463:,}</h3>", unsafe_allow_html=True)

col4.markdown(f"<h3 style='color: white;'>November {350162:,}</h3>", unsafe_allow_html=True)

col5.markdown(f"<h3 style='color: white;'>2018<br>{722052:,}</h3>", unsafe_allow_html=True)

col6.markdown(f"<h3 style='color: white;'>Saturday {420905:,}</h3>", unsafe_allow_html=True)

col1, col2, col3=st.columns([4,4,4])

top_cities=df.groupby('City')['Sales'].sum().astype(int).sort_values(ascending=False).head(10).round()
fig1=go.Figure()
fig1.add_trace(go.Bar(x=top_cities.index,
                      y=top_cities.values,
                      marker=dict(color=px.colors.qualitative.Bold[1])
                     ))

fig1.update_layout(
title="Top 10 Cities by Sales",
xaxis_title="City",
yaxis_title="Sales")
col1.plotly_chart(fig1)

top_years=df.groupby('Year')['Sales'].sum().astype(int).sort_values(ascending=False).round()
fig2=go.Figure()
fig2.add_trace(go.Bar(x=top_years.index,
                      y=top_years.values,
                      marker=dict(color=px.colors.qualitative.Bold[1])
                     ))

fig2.update_layout(
title="Total Sales In Each Year",
xaxis_title="Years",
yaxis_title="Sales")
col2.plotly_chart(fig2)

top_days=df.groupby('Day')['Sales'].sum().astype(int).sort_values(ascending=False).round()
fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=top_days.index,  
    y=top_days.values,  
    mode='lines+markers',  
    line=dict(color=px.colors.qualitative.Bold[1])  
))

fig3.update_layout(
    title="Total Sales In Each Day",
    xaxis_title="Days",
    yaxis_title="Sales"
)

col3.plotly_chart(fig3)
