import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('./Data/fts_cleaned.csv')

# Filter rows where the fuel type is either "Battery Electric" or "Plug-in Hybrid"
filtered_df = df[
    ((df['Fuel'] == 'Plug-in Hybrid') | (df['Fuel'] == 'Battery Electric')) & (df['Make'] != 'OTHER/UNK')
]

# Display the filtered DataFrame
print(filtered_df)

def maxCarsSoldCompanywise():
    modelGroup = filtered_df.groupby('Make')

    # Calculate total sales for each company
    company_sales = {}
    top_5_companies = []

    for make, group_df in modelGroup:
        company_sales[make] = group_df.shape[0]
        
        print(f"Total Cars sold by {make} company are : {group_df.shape[0]}")

def topFiveCarBrandsBySales():
    # Group by 'Make' and sum the 'Vehicles' column to get the total sales for each make
    sales_by_make = filtered_df["Make"].value_counts().reset_index()

    # Sort the DataFrame by 'Vehicles' in descending order and get the top 5 makes
    sales_by_make.columns = ["Make", "Count"]
    
    top_5_makes = sales_by_make.head()

    # Display the top 5 makes based on highest number of sales
    print("Top 5 car brands based on sales:")
    print(top_5_makes)

maxCarsSoldCompanywise()
topFiveCarBrandsBySales()