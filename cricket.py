# import the streamlit library
import streamlit as st
import tabula
import numpy as np
import pandas as pd
import warnings
import time
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("IPL23 Match Summary")
st.divider()

df = pd.read_csv('each_ball_records.csv')
pd.set_option("display.max_rows", None)
df=df.drop('comment',axis=1)

select_match = st.number_input("Select Match Number", 1)
select_inning = st.number_input("Select Inning Number",min_value=1,max_value=2)
st.divider()

six='6'
four='4'
wicket='w'

tab1, tab2, tab3, tab4 = st.tabs(["Details", "Sixes", "Fours", "Wickets"])

with tab1:
    st.text("Ball by Ball details for selected Match and Innings")
    output = df.loc[(df['match_no'] == select_match) & (df['inningno'] == select_inning)]
    st.dataframe(output)
    st.divider()

with tab2:
    st.text("No. of Sixes by the Batter")
    sixes=output[output['outcome']==six]
    df_sixes=pd.DataFrame(sixes).drop(['match_no','ballnumber','inningno','over','bowler'],axis=1)
    s=df_sixes.groupby(['batter']).count()
    st.bar_chart(s,use_container_width=True)
    st.divider()

with tab3:
    st.text("No. of Fours by the Batter")
    fours=output[output['outcome']==four]
    df_fours=pd.DataFrame(fours).drop(['match_no','ballnumber','inningno','over','bowler'],axis=1)
    f=df_fours.groupby(['batter']).count()
    st.bar_chart(f,use_container_width=True)
    st.divider()

with tab4:
    st.text("No. of Wickets by the Bowler")
    wickets=output[output['outcome']==wicket]
    df_wickets=pd.DataFrame(wickets).drop(['match_no','ballnumber','inningno','over','batter'],axis=1)
    w=df_wickets.groupby(['bowler']).count()
    st.bar_chart(w,use_container_width=True)
    st.divider()

#pies=output.groupby(['outcome']).sum()
#pie_fig = pies.iplot(kind="pie", labels="outcome", values="inningno",
#                         title="Wine Samples Distribution Per WineType",
#                         asFigure=True,
#                        hole=0.4)
#
#pie_fig
