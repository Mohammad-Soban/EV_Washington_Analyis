# import pandas as pd

# print("\nThis module tells Electric Range Model wise\n")

# df = pd.read_csv('DataSet_2_vehicle_model.csv')

# def electricRangeModelwise():
#     group_of_model = df.groupby('Model')
#     for i,j in group_of_model:
#         # print(i)
#         # print(j[['Make', 'Model', 'Electric Range']])
#         print(f"\nTotal Cars of Model {i} is : {j.shape[0]}\n")
    

# electricRangeModelwise()


import pandas as pd
import plotly.graph_objects as go


print("\nThis module tells Electric Range Model wise\n")

df = pd.read_csv('./Data/DataSet_2_vehicle_model.csv')

def electricRangeModelwise():
    group_of_model = df.groupby('Model').size().reset_index(name='Count')
    print(group_of_model.to_string(index='Count'))
    
    total_count = group_of_model['Count'].sum()
    print(f"Total Cars are : {total_count}")
    
    

# def modelYearwiseModel():
#     modelYear = df.groupby(['Model Year', 'Make']).unique()
#     for i, j in modelYear:
#         print(j[['Make', 'Model', 'Model Year']])
#     # print(modelYear)




def modelYearwiseModel():
    distinct_combinations = []
    model_years = df['Model Year'].unique()
    makes = df['Make'].unique()

    # print(makes)

    for year in model_years:
        for make in makes:
            filtered_df = df[(df['Model Year'] == year) & (df['Make'] == make)]
            if not filtered_df.empty:
                distinct_combinations.append(filtered_df[['Make', 'Model', 'Model Year']].iloc[0])

    distinct_combinations = pd.DataFrame(distinct_combinations)
    print(distinct_combinations)




def maxCarsSoldCompanywise():
    modelGroup = df.groupby('Make')

    # Calculate total sales for each company
    company_sales = {}
    top_5_companies = []

    for make, group_df in modelGroup:
        company_sales[make] = group_df.shape[0]
        
        print(f"Total Cars sold by {make} company are : {group_df.shape[0]}")

    print()
    
    # Sort companies based on sales in descending order
    sorted_companies = sorted(company_sales.items(), key=lambda x: x[1], reverse=True)

    # Get top 5 companies based on sales and add them to the list
    for make, sales in sorted_companies[:5]:
        top_5_companies.append(make)

    # return top_5_companies

# top_5_list = maxCarsSoldCompanywise()

    for make in top_5_companies:
        print(f"Company: {make}")
        company_df = df[df['Make'] == make]
        model_group = company_df.groupby('Model')
        
        labels = []
        values = []
        for model, group_df in model_group:
            total_cars_sold = group_df.shape[0]
            print(f"Model: {model} - Cars Sold: {total_cars_sold}")
            
            labels.append(model)
            values.append(total_cars_sold)
        
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_layout(title=f"Cars Sold by Model for {make}")
        fig.show()






def maxCarsSoldModelwise():
    df = pd.read_csv('./Data/DataSet_2_vehicle_model.csv')

    model_group = df.groupby(['Make', 'Model'])

    # Calculate total sales for each model
    model_sales = {}
    for (make, model), group_df in model_group:
        total_sales = group_df.shape[0]
        model_sales[(make, model)] = total_sales

    # Sort models based on sales in descending order
    sorted_models = sorted(model_sales.items(), key=lambda x: x[1], reverse=True)

    # Get top 5 models based on sales
    top_5_models = sorted_models[:5]

    # Extract data for plotting pie chart
    labels = [f"{make} - {model}" for (make, model), _ in top_5_models]
    values = [sales for _, sales in top_5_models]

    # Create pie chart using Plotly
    fig = go.Figure(data=go.Pie(labels=labels, values=values))
    fig.update_layout(title='Top 5 Models by Cars Sold (Pie Chart)')

    # Prepare data strings
    data_strings = [f"Company: {make} - Model: {model} - Cars Sold: {sales}" for (make, model), sales in top_5_models]

    return fig, data_strings














# electricRangeModelwise()
# modelYearwiseModel()

# maxCarsSoldCompanywise()
maxCarsSoldModelwise()

