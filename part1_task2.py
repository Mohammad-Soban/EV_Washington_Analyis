# import streamlit as st
import pandas as pd
import plotly.express as px

# # Load the dataset
# @st.cache_data
# def load_data():
#     # Assuming the Excel file is named 'car_data.xlsx' and is in the same directory
#     df = pd.read_excel('CAR_DATA.xlsx')
#     return df

# def main():
#     st.title('Car Features Comparison App')
    
#     # Load data
#     df = load_data()

#     # Sidebar selection
#     feature_to_compare = st.sidebar.selectbox('Select feature to compare:', df.columns[2:])  # Exclude Company and Model columns
#     num_models_to_display = st.sidebar.slider('Number of models to display:', min_value=1, max_value=len(df), value=10)

#     # Display bar graph
#     st.write(f"Comparison of {feature_to_compare} across different car models")
#     fig = px.scatter(df.head(num_models_to_display), x='Model ', y=feature_to_compare, color='Company', 
#                  title=f'{feature_to_compare} Comparison', size_max=20)  # Adjusted column name to 'Model '
#     fig.update_layout(xaxis_title='Model', yaxis_title=feature_to_compare)
#     st.plotly_chart(fig)

# if _name_ == '_main_':
#     main()

# I want to show the fig using the plotly graphs

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def load_data():
    # Load the dataset
    df = pd.read_excel('./Data/CAR_DATA.xlsx')
    return df

def plot_bar_chart(df, feature_to_compare, num_models_to_display=10):
    # Display bar chart
    fig = go.Figure(data=[
        go.Bar(name=feature_to_compare, x=df['Model '].head(num_models_to_display), y=df[feature_to_compare].head(num_models_to_display))
    ])
    fig.update_layout(title=f'{feature_to_compare} Comparison',
                      xaxis_title='Model', yaxis_title=feature_to_compare)

    return fig