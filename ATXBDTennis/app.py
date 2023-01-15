
import os
import streamlit as st
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import datetime
# from gsheetsdb import connect
import secret
from secret import *
# from PIL import Image




st.set_page_config(page_title="ATXBDTENNIS2022", layout="wide")

# '''

# # :tennis: :green[Austin Bangladeshi Tennis Tournament 2023] :tennis:

# '''

# st.title(":green[University of Tennessee Parking Lot Availability]")

# Remove the sandwich menu in the upper right corner
hide_streamlit_style = """
            <style>
            # MainMenu {visibility: hidden;}
            header, footer {visibility: hidden;}
            div.block-container {padding-top:1rem;padding-left:2rem;padding-right:2rem;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# st.markdown('<div style="text-align: center;">Hello World!</div>', unsafe_allow_html=True)
# st.markdown('<div style="text-align: left;">Hello World!</div>', unsafe_allow_html=True)
# st.markdown('<div style="text-align: right;">Hello World!</div>', unsafe_allow_html=True)
# st.markdown('<div style="text-align: justify;">Hello World!</div>', unsafe_allow_html=True)

st.title(":tennis: :green[Austin Bangladeshi Tennis Tournament 2022] :tennis:")


# Create a connection object.
# conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     rows = rows.fetchall()
#     return rows

# sheet_url = st.secrets["public_gsheets_url"]

# # print(sheet_url)
# rows = run_query(f'SELECT * FROM "{sheet_url}"')
# df = pd.DataFrame(rows)
# df = df.fillna("")



url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

df = pd.read_csv(url)
df = df.fillna("")



# df = df.style.highlight_null(null_color="orange")
# sheet_url2 = st.secrets["public_gsheets_url"]["test"]
# rows2 = run_query(f'SELECT * FROM "{sheet_url2}"')
# df2 = pd.DataFrame(rows2)
# df2 = df2.fillna("")

# st.table(df2)


# st.write(rows)
# pd.io.formats.style.styler.to_html(bold_headers=True)
# st.table(df)
# st.dataframe(df, height=550, use_container_width = True)

styles = [
    dict(selector="tr:hover",
                props=[("background", "#f4f4f4")]),
    dict(selector="th", props=[("color", "#fff"),
                               ("border", "1px solid #eee"),
                               ("padding", "5px 5px"),
                               ("border-collapse", "collapse"),
                               ("background", "#32755F"),
                               ("text-transform", "uppercase"),
                               ("font-size", "15px"),
                               ("text-align", "center"),
                               
                            #    ("width", "5000px")
                               ]),
    dict(selector="td", props=[("color", "#000a03"),
                               ("border", "1px solid #000a03"),
                               ("padding", "5px 5px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "15px"),
                               ("text-align", "center"),
                            #    ("word-break", "keep-all"),
                               ("width", "1000px")
                               ]),
    dict(selector="table", props=[
                                    ("font-family" , 'Arial'),
                                    ("margin" , "25px auto"),
                                    ("border-collapse" , "collapse"),
                                    ("border" , "1px solid #eee"),
                                    ("border-bottom" , "2px solid #00cccc"),
                                    ("column-width", "5500px")                                    
                                      ]),
    dict(selector="caption", props=[("caption-side", "bottom")])
]

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Welcome", "Rules", "Schedule", "Schedule by Team", "Group Score", "SF/F Schedule", "SF Score", "Finals Score"])

with tab1:
    st.header("Welcome")
    
    # image_file = Image.open('assets/tennis_poster22.jpg')
    image_file = ('assets/tennis_poster22.jpg')
    st.image(image_file)


with tab2:
    st.header("Tournament Rules")
    st.download_button(
    label="Download Rules",
    data='assets/Tennis-Rules-2022-Nov-15.pdf',
    file_name='ATX-Tennis-Rules-2022.pdf',
    # mime='text/csv',
)
    



with tab3:
    st.header("Schedule")
    st.markdown(df.style.set_table_styles(styles).hide_index().highlight_null(null_color='red').to_html(), unsafe_allow_html=True)


with tab4:
    st.header("Schedule by Team")
    url2 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME2}'

    df2 = pd.read_csv(url2)
    df2 = df2.fillna("")
    
    captain = sorted(df2["Captain"].unique())
    captain_choice = st.selectbox('Select Your Captain', captain)
    df2 = df2[df2['Captain'].isin([captain_choice])]
    st.markdown(df2.style.set_table_styles(styles).hide_index().highlight_null(null_color='red').to_html(), unsafe_allow_html=True)
    


with tab5:
    st.header("Group Point Table")
    url5 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME5}'

    df5 = pd.read_csv(url5)
    df5 = df5.fillna("")
    
    st.markdown(df5.style.set_table_styles(styles).hide_index().highlight_null(null_color='red').to_html(), unsafe_allow_html=True)
       
    
    st.header("Group Score - Head to Head")
    url4 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME4}'

    df4 = pd.read_csv(url4)
    df4 = df4.fillna("")
    
    st.markdown(df4.style.set_table_styles(styles).hide_index().highlight_null(null_color='red').to_html(), unsafe_allow_html=True)
    

with tab6:
    st.header("Semi-Final Schedule by Team")
    url3 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME3}'

    df3 = pd.read_csv(url3)
    df3 = df3.fillna("")
    # df3 = df3[df3['Match Type'] == "Semi Finals"]
    # df3 = df3[['Match type', 'Court', 'Time', 'Teams', 'Names', 'Captain', 'Opponent', 'Opponent Captain']]
    match = sorted(df3["Match Type"].unique())
    match_choice = st.selectbox('Select Your Match Type', match)
    captain = sorted(df3["Captain"].unique())
    captain_choice = st.selectbox('Select Your Captain', captain)
    df3 = df3[df3['Captain'].isin([captain_choice])]
    st.markdown(df3.style.set_table_styles(styles).hide_index().highlight_null(null_color='red').to_html(), unsafe_allow_html=True)







with tab7:
    st.header("Semi-Finals Point Table")
    url7 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME7}'

    df7 = pd.read_csv(url7)
    df7 = df7.fillna("")
    
    st.markdown(df7.style.set_table_styles(styles).hide_index().highlight_null(null_color='red').to_html(), unsafe_allow_html=True)
       
    
    st.header("Semi-Finals Head to Head")
    url6 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME6}'

    df6 = pd.read_csv(url6)
    df6 = df6.fillna("")
    
    
    df6 = df6[['Team 1', 'Team 1 Captain', 'Team 2', 'Team 2 Captain', 'Game Style', 'Team 1 Result', 'Team 2 Result', 'Team 1 Set Wins', 'Team 2 Set Wins', 'Team 1 Point', 'Team 2 Point']]
    
    
    st.markdown(df6.style.set_table_styles(styles).hide_index().highlight_null(null_color='red').to_html(), unsafe_allow_html=True)
     


with tab8:
    st.header("Finals Point Table")
    url9 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME9}'

    df9 = pd.read_csv(url9)
    df9 = df9.fillna("")
    
    st.markdown(df9.style.set_table_styles(styles).hide_index().highlight_null(null_color='red').to_html(), unsafe_allow_html=True)
       
    
    st.header("Finals Head to Head")
    url8 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME8}'

    df8 = pd.read_csv(url8)
    df8 = df8.fillna("")
    
    
    df8 = df8[['Team 1', 'Team 1 Captain', 'Team 2', 'Team 2 Captain', 'Game Style', 'Team 1 Result', 'Team 2 Result', 'Team 1 Set Wins', 'Team 2 Set Wins', 'Team 1 Point', 'Team 2 Point']]
    
    
    st.markdown(df8.style.set_table_styles(styles).hide_index().highlight_null(null_color='red').to_html(), unsafe_allow_html=True)
    




# skills = sorted(df['Skills'].unique())
# skills_choice = st.sidebar.selectbox('Select Skill ', skills)
# # # years_choice = st.sidebar.selectbox('', years)
# # # city_choice = st.sidebar.selectbox('', city)
# # # state_choice = st.sidebar.selectbox('', state)

# # df = df[df['Industry'].isin([ind_choice])]
# df = df[df['Skills'].isin([skills_choice])]
# # # df = df[df['cost'] < price_choice]




# st.dataframe(df, height=500, use_container_width = True)






# st.markdown(df.style.hide(axis="index").to_html(sparse_columns=False, bold_headers=True, bold_rows=True), unsafe_allow_html=True)

# st.markdown(df.style.hide(axis="index").set_properties(**{'background-color': 'black',                                                   
#                                     'color': 'lawngreen',                       
#                                     'border-color': 'red'}).to_html(sparse_columns=True, bold_headers=False, bold_rows=True), unsafe_allow_html=True)
# hide(axis="index").to_html(sparse_columns=False), unsafe_allow_html=True)



# Print results.
# for row in rows:
#     st.write(f"{row.name} has a :{row.pet}:")








# Import the dataset into a dataframe

# @st.cache
# def get_data():
#     df = pd.read_csv(os.path.join('C:\Jalal\GitHub\demo_projects\streamlit_skillnet\data\demo_member_profiles.csv'))
#     # df = pd.read_csv(('https://raw.githubusercontent.com/jalaljahir/demo_projects/main/streamlit_stock_NVDA/data/NVidia_stock_history.csv'))
#     df = df[['Name', 'City', 'State', 'Company', 'Industry', 'Years of Experience', 'Skills', 'LinkedIn Profile']]

#     cols = ['Name', 'City', 'State', 'Company', 'Industry', 'Years of Experience']
#     # df.loc[df.duplicated(subset=cols), cols ] = ''
#     # print (df)
#     return df



# # Delete rows where date is before 1/1/2019.
# # df['Date'] = pd.to_datetime(df['Date'])
# # df = df[~(df['Date'] < '2019-01-01')]
# # df.head()

# # # Reset the index to the Date column. 
# # df['Date'] = pd.to_datetime(df['Date'],format='%Y/%m/%d')
# # df.reset_index(drop=True,inplace=True)
# # df.set_index('Date',inplace=True)

# # # Specify the title and logo for the web page.
# # st.set_page_config(page_title='Nvidia Stock Prices', 
# # page_icon='https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png', layout="wide")

# st.set_page_config(
#      page_title="BD Skills Network",
#      page_icon="🧊",
#      layout="wide",
#      initial_sidebar_state="expanded",
#      menu_items={
#          'Get Help': 'https://www.extremelycoolapp.com/help',
#          'Report a bug': "https://www.extremelycoolapp.com/bug",
#          'About': "# This is a header. This is an *extremely* cool app!"
#      }
#  )

# '''

# ### American Bangladesh Skills Network

# '''


# # # Add social media tags & links to the web page.
# # """
# # [![Star](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@xxx)
# # [![Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/xxx)
# # [![Follow](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/xxx)

# # # Nvidia's Stock Performance

# # """



# # Add a sidebar to the web page. 
# st.markdown('---')
# # Sidebar Configuration
# # st.sidebar.image('https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png', width=200)
# st.sidebar.markdown('# Filter Selection')
# # st.sidebar.markdown('Nvidia is a global leader in artificial intelligence hardware and software.')
# # st.sidebar.markdown('Stock Data from 2019 thru 2021')
# # st.sidebar.markdown('You can visualise Nvidia \'s Stock Prices Trends and Patterns over a given time span.') 




# # Display the Data in the App.
# # st.subheader('Looking at the Data')
# # @st.cache
# df = get_data()

# # ind = sorted(df['Industry'].unique())
# # ind_choice = st.sidebar.selectbox('Select your industry:', ind) #default = ind)

# # skills = sorted(df['Skills'].loc[df['Industry'].isin([ind_choice])].unique())

# # skills = skills.sort()
# # print (skills)

# # years = df['Years of Experience']
# # city = df['City']
# # state = df['State']

# skills = sorted(df['Skills'].unique())
# skills_choice = st.sidebar.selectbox('Select Skill ', skills)
# # # years_choice = st.sidebar.selectbox('', years)
# # # city_choice = st.sidebar.selectbox('', city)
# # # state_choice = st.sidebar.selectbox('', state)

# # df = df[df['Industry'].isin([ind_choice])]
# df = df[df['Skills'].isin([skills_choice])]
# # # df = df[df['cost'] < price_choice]




# st.dataframe(df, height=500, use_container_width = True)


# st.sidebar.markdown('---')
# st.sidebar.write('Developed by xxx xxx')
# st.sidebar.write('Contact at xxx@xxx.xxx')
# st.dataframe(df.style.hide(axis="index"))
# st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
# # Display statistical information on the dataset.
# st.subheader('Statistical Info about the Data')
# st.write(df.describe())

# # Selection for a specific time frame.
# st.subheader('Select a Date Range')
# df_select = df 

# col1, col2 = st.columns(2)

# with col1:
#     st.write('Select a Start Date')
#     start_date = st.date_input('Start Date',min_value= datetime.date(2019,1,2),max_value=datetime.date(2021,11,12),value=datetime.date(2019,1,2))

# with col2:    
#     st.write('Select an End Date')
#     end_date = st.date_input('End Date',min_value=datetime.date(1999,1,22),max_value=datetime.date(2021,11,12),value=datetime.date(2021,11,12))

# if(start_date != None or end_date != None):
#     if(start_date < end_date):
#         df_select = df[start_date:end_date]
#     else:
#         st.warning("Invalid Date Range - Re-enter Dates")
        

# # Graphs and charts for selected date range.

# # Open & Close Prices.  
# st.subheader("Open & Close Prices for Nvidia Stock")
# st.markdown("\n\n")
# st.line_chart(df_select[['Open','Close']])

# # High and Low Values. 
# st.subheader("High and Low Prices for Nvidia Stock")
# st.markdown("\n\n")
# st.line_chart(df_select[['High', 'Low']])

# # Volume of Stock Traded.
# st.subheader("Volumn Traded for Nvidia Stock")
# st.markdown("\n\n")
# st.bar_chart(df_select['Volume'])

# # Moving average from 50 days to 250 days.
# st.subheader('Moving Averages of Open and Closing Stock Prices')
# movevavg_len = st.slider('Select the number of days for Moving Averages',min_value=0,max_value=250,value=50)
# moveavg_oc =  df_select[['Open','Close']].rolling(50).mean()
# st.line_chart(moveavg_oc)
