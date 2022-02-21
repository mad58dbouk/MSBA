from email import header
from optparse import Values
import pandas as pd
import numpy as np


from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


import streamlit as st 
st.markdown("Mohamad Dbouk MSBA 325 streamlit Assignment")

st.markdown("""Note: please note that all these figures are for the sake of plotting figures and presenting several visualizations using plotly and streamlit.""" )

df = pd.read_csv('countries.csv')

df.drop(columns=['Agriculture','Industry','Service'], axis=1 ,inplace = True)
df.rename({'Literacy (%)':'Literacy','GDP ($ per capita)':'GDP','Infant mortality (per 1000 births)':'Infantmortality','Phones (per 1000)':'Phonesperthou'}, axis=1 ,inplace = True)


st.markdown(""" 1. Taking a look at the first 5 rows of the dataset.""")
st.write(df.head())


import plotly.express as px
import plotly.graph_objects as go
import plotly as ply


st.title("""Please mark the assignmnet after you're done using the slider below""")
st.subheader("slide here")
x = st.slider("A number between 0-100")
st.write("Grade:", x)

st.header("""A better overview of the essential columns of the data""")
import plotly.figure_factory as ff
fig = go.Figure(data=go.Table(header=dict(values=list(df[['Country', 'Region', 'Population', 'Infantmortality','GDP','Literacy','Birthrate','Deathrate']].columns),fill_color = 'gold',align ='center'),cells= dict(values=[df.Country, df.Region, df.Population, df.Infantmortality,df.GDP, df.Literacy,df.Birthrate,df.Deathrate],fill_color = 'ghostwhite', align = 'left')))
fig.update_layout(margin=dict(l=4,r=4,b=8,t=8))
st.write(fig)


rad = st.sidebar.radio("Navigation (please slide to the bottom of the page to view the selected figure)",["Barplot of most populated","Strip plot","Histogram", "second Barplot","sunburst figure", "treemap figure", "3D scatter plot"])

if rad == "Barplot of most populated":

    st.header(""" Bar plot showing the top 10 most populated countries in the world""")
    df_population= df[['Country','Population']]
    df_population_sorted = df_population.sort_values('Population', ascending = False)
    top_10_pop = df_population_sorted.head(10)
    dataline = [go.Bar(x=top_10_pop.Country, y= top_10_pop.Population)]
    st.plotly_chart(dataline)
    


if rad == "Strip plot":

    st.header("""Interactive Strip chart showing Infant mortality for every country that is displayed through hovering over, with colours determining the Region to which that country belong.  
    """)
    df_infmort = df[['Country','Region','Infantmortality']]
    fig2 = px.strip(df_infmort, x = 'Infantmortality', color = 'Region', hover_name = 'Country')
    fig2.update_layout(showlegend = True, width=750, height=750)
    st.plotly_chart(fig2)

if rad == "Histogram":

    st.header("""Histogram showing countries' Literacy and population measures """)
    fig3 = px.histogram(df, x ="Population" , y = 'Literacy' , color = "Region", hover_name ='Country', width = 700 )
    fig3.update_layout(showlegend=True)
    st.plotly_chart(fig3)


if rad == "second Barplot":

    st.header("""Interactive Bar plot showing population per Region with country showing through hovering""")
    fig4 = px.bar(df, x='Population', y= 'Region',color ='Region', hover_name= 'Country', height = 600)
    st.plotly_chart(fig4)

if rad == "sunburst figure":

    st.header("""Interactive Sunburst chart showing literacy rate(colour scale didn’t show) spread across Regions with pie size determined through population.
    """)
    fig5 = px.sunburst(df, values='Population', path=['Region', 'Country'] ,color ='Literacy', hover_name= 'Country', height = 500)
    fig5.update_layout(showlegend= True)
    st.plotly_chart(fig5)

if rad == "treemap figure":

    st.header("""Interactive Tree map show same values as Sunburst but with different design 
    """)
    fig6 = px.treemap(df, values='Population', path=['Region', 'Country'] ,color ='Literacy', hover_name= 'Country', height = 600)
    st.plotly_chart(fig6)


if rad == "3D scatter plot":

    st.header(""" 3D plot showing population, country and GDP""")


    x = df['Country']
    y= df['GDP']
    z= df['Population']

    trace = go.Scatter3d(x=x,y=y,z=z, mode ='markers',marker =dict(size=12,color=z,colorscale='Viridis',opacity=0.8))
    data = [trace]
    layout = go.Layout(margin = dict(l=0,r=0,b=0,t=0))
    fig7 = go.Figure(data=data, layout = layout)
    st.plotly_chart(fig7)


st.title("""you've reached the end""")
result = st.button("Click Here If You Like It")

st.write(result)
if result:
    st.write("Thank You :smile:")








