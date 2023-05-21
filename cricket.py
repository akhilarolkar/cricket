# import the streamlit library
import streamlit as st
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

select_match = st.number_input("Select Match Number", min_value=1,max_value=37)
select_inning = st.number_input("Select Inning Number",min_value=1,max_value=2)
st.divider()

six='6'
four='4'
wicket='w'

tab1, tab2, tab3, tab4 = st.tabs(["Details", "Sixes", "Fours", "Wickets"])

with tab1:
    output = df.loc[(df['match_no'] == select_match) & (df['inningno'] == select_inning)]

    wickets = len(output[output['outcome'] == wicket])
    
    runs = output['outcome'].replace(['0', '1lb', '1', '4', 'w', '6', '1nb', '4lb', '2', '1b', '1wd','2nb','5nb','7nb','3','5wd','4b','2wd','5','3wd','2lb','3nb'], [0,1,1,4,0,6,1,4,2,1,1,2,5,7,3,5,4,2,5,3,2,3])
    df_runs=pd.DataFrame(runs)
    total_runs=df_runs['outcome'].sum()

    score = (f"Innings's Score: {total_runs}/{wickets}")
    score
   
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