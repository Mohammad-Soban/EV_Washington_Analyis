import streamlit as st
from part1_task2 import load_data, plot_bar_chart
from part2_task1 import get_vehicle_counts
from part2_task2 import get_car_data
from part2_task2 import CarsCountyWise
from part2_task3 import categoriesCountBrandWise
from PIL import Image
from extra import maxCarsSoldModelwise


# I have a Battery_warranty.py file in the same directory as main.py which I want to import the figure which is created in Battery_warranty.py but I 

st.title('Electric Vehicle Sales Data Analysis')


# Create a dropdown menu with two options and a default value
option = st.selectbox('Select an option', ['Select','BEV Vechicles', 'PHEV Vehicles'], index=0)

# Check if an option is selected
if option=='Select':
    st.write("Nothing selected")
    # Print the selected option
else:
    bev_count, phev_count = get_vehicle_counts()
    if option == 'BEV Vechicles':
        st.write('BEV')
        st.write(f'Total BEV vehicles: {bev_count}')
    if option =='PHEV Vehicles':
        st.write('PHEV')
        st.write(f'Total PHEV vehicles: {phev_count}')

st.title('Cars and Count')



# Get the list from part2_task2.py
car_list = get_car_data()

# Display the list in the frontend using Streamlit
st.write('List of total cars per company:')
# st.write(car_list)

a = []
b = []
for car in car_list:
    a.append(car[0])
    b.append(car[1])



# Create a dropdown menu with car company names from list 'a'
option = st.selectbox('Select a car company', ['Select'] + a, index=0)

# Check if an option is selected
if option != 'Select':
    # Find the index of the selected car company in list 'a'
    selected_index = a.index(option)
    
    # Use the index to get the corresponding number from list 'b'
    selected_count = b[selected_index]
    
    # Display the selected car company and its corresponding number
    st.write(f'Total cars for {option}: {selected_count}')

st.title('Cars County-Wise Visualization')

# Call the function from part2_task2.py to get the figure object
fig = CarsCountyWise()

# Display the Plotly figure using Streamlit
st.plotly_chart(fig)

st.title('Electric Vehicle Category Sales by Brand')

# Call the function from part2_task3.py to get the pivot_df DataFrame
pivot_df = categoriesCountBrandWise()

# Display the DataFrame using Streamlit
st.write('Pivoted DataFrame:')
st.write(pivot_df)

st.title('Top 5 Models by Cars Sold')

# Call the function from extra.py to get the figure object and data strings
fig, data_strings = maxCarsSoldModelwise()

# Display the figure using Streamlit
st.plotly_chart(fig)

# Display the data strings using Streamlit
st.write('Top 5 Models by Cars Sold:')
for data_string in data_strings:
    st.write(data_string)

# I have a map.html file in the same directory as main.py which I want to display when the user clicks a button on a new tab

st.title('Feature Comparison of the Top 5 Car Models')
top5_df = load_data()

# Sidebar selection
# Exclude Company and Model columns and 
feature_to_compare = st.sidebar.selectbox('Select feature to compare:', top5_df.columns[3:-2])

# The below line of code creates a slider in the sidebar to select the number of models to display and value = 10 shows 10 models by default
num_models_to_display = st.sidebar.slider('Number of models to display:', min_value=1, max_value=len(top5_df), value=5)

st.write(f"Comparison of {feature_to_compare} across different car models")
fig = plot_bar_chart(top5_df, feature_to_compare, num_models_to_display)
st.plotly_chart(fig)

# Now I want to display the 3D bar plot created in Battery_warranty.py
st.title('Resale Value Comparison of Top 5 Car Models')
image = Image.open('./Imgs/car_prices_vs_resale_values2.png')
st.image(image, caption='Car Prices vs. Resale Values', use_column_width=True)
# By default, the 3D bar plot is displayed

st.title("3D Bar Plot: Car Prices and Battery Warranty")
img2 = Image.open('./Imgs/Battery_warranty_1.png')
st.image(img2, caption='3D Bar Plot: Car Prices and Battery Warranty', use_column_width=True)


if st.button('Show map'):
    html_file = open('./Imgs/map.html', 'r', encoding='utf-8')
    source_code = html_file.read()
    st.markdown(source_code, unsafe_allow_html=True)
    st.markdown('<a href="data:file/html;base64,'+source_code+'">Click here to download the map</a>', unsafe_allow_html=True)

