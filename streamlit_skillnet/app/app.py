
import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Import the dataset into a dataframe

@st.cache
def get_data():
    df = pd.read_csv(os.path.join('C:\Jalal\GitHub\demo_projects\streamlit_skillnet\data\demo_member_profiles.csv'))
    # df = pd.read_csv(('https://raw.githubusercontent.com/jalaljahir/demo_projects/main/streamlit_stock_NVDA/data/NVidia_stock_history.csv'))
    df = df[['Name', 'City', 'State', 'Company', 'Industry', 'Years of Experience', 'Skills']]

    cols = ['Name', 'City', 'State', 'Company', 'Industry', 'Years of Experience']
    # df.loc[df.duplicated(subset=cols), cols ] = ''
    # print (df)
    return df



# Delete rows where date is before 1/1/2019.
# df['Date'] = pd.to_datetime(df['Date'])
# df = df[~(df['Date'] < '2019-01-01')]
# df.head()

# # Reset the index to the Date column. 
# df['Date'] = pd.to_datetime(df['Date'],format='%Y/%m/%d')
# df.reset_index(drop=True,inplace=True)
# df.set_index('Date',inplace=True)

# # Specify the title and logo for the web page.
# st.set_page_config(page_title='Nvidia Stock Prices', 
# page_icon='https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png', layout="wide")

st.set_page_config(
     page_title="BD Skills Network",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

'''

### American Bangladesh Skills Network

'''


# # Add social media tags & links to the web page.
# """
# [![Star](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@xxx)
# [![Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/xxx)
# [![Follow](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/xxx)

# # Nvidia's Stock Performance

# """



# Add a sidebar to the web page. 
st.markdown('---')
# Sidebar Configuration
# st.sidebar.image('https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png', width=200)
st.sidebar.markdown('# Filter Selection')
# st.sidebar.markdown('Nvidia is a global leader in artificial intelligence hardware and software.')
# st.sidebar.markdown('Stock Data from 2019 thru 2021')
# st.sidebar.markdown('You can visualise Nvidia \'s Stock Prices Trends and Patterns over a given time span.') 




# Display the Data in the App.
# st.subheader('Looking at the Data')
# @st.cache
df = get_data()

ind = sorted(df['Industry'].unique())
ind_choice = st.sidebar.selectbox('Select your industry:', ind) #default = ind)

skills = sorted(df['Skills'].loc[df['Industry'].isin([ind_choice])].unique())

# skills = skills.sort()
print (skills)

# years = df['Years of Experience']
# city = df['City']
# state = df['State']

skills_choice = st.sidebar.selectbox(' ', skills)
# # years_choice = st.sidebar.selectbox('', years)
# # city_choice = st.sidebar.selectbox('', city)
# # state_choice = st.sidebar.selectbox('', state)

df = df[df['Industry'].isin([ind_choice])]
df = df[df['Skills'].isin([skills_choice])]
# # df = df[df['cost'] < price_choice]




st.dataframe(df, height=500, use_container_width = True)


st.sidebar.markdown('---')
st.sidebar.write('Developed by xxx xxx')
st.sidebar.write('Contact at xxx@xxx.xxx')
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