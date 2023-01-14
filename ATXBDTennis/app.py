
import os
import streamlit as st
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import datetime
from gsheetsdb import connect


st.set_page_config(page_title="ATXBDTENNIS2023", layout="wide")

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

st.title(":tennis: :green[Austin Bangladeshi Tennis Tournament 2023] :tennis:")


# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
df = pd.DataFrame(rows)
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
    dict(selector="td", props=[("color", "#999"),
                               ("border", "1px solid #eee"),
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

st.markdown(df.style.set_table_styles(styles).hide_index().highlight_null(null_color='red').to_html(), unsafe_allow_html=True)


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