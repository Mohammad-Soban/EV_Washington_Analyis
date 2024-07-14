import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('./Data/DataSet_1_all_vehicles.csv')

# Group by 'State' and calculate sums
state_grouped = df.groupby('State').agg({'Electric Vehicle (EV) Total': 'sum', 'Non-Electric Vehicle Total': 'sum'}).reset_index()

print(state_grouped)

# Create bar chart using Plotly
fig = go.Figure(data=[
    go.Bar(name='Electric Vehicle (EV) Total', x=state_grouped['State'], y=state_grouped['Electric Vehicle (EV) Total']),
    go.Bar(name='Non-Electric Vehicle Total', x=state_grouped['State'], y=state_grouped['Non-Electric Vehicle Total'])
])

# Update layout and display the chart
fig.update_layout(title='Sums of Electric Vehicles (EV) and Non-Electric Vehicles by State',
                    xaxis_title='State', yaxis_title='Number of Vehicles')
fig.show()

# Filter DataFrame for Washington (WA) state
wa_df = df[df['State'] == 'WA']

# Calculate sums for Washington (WA)
wa_totals = wa_df[['Electric Vehicle (EV) Total', 'Non-Electric Vehicle Total']].sum()

# Create pie chart for Washington (WA) state
pie_fig = go.Figure(data=go.Pie(labels=['Electric Vehicle (EV) Total', 'Non-Electric Vehicle Total'],
                                values=wa_totals.values))
pie_fig.update_layout(title='Distribution of Vehicles in Washington (WA)',
                        showlegend=True)
pie_fig.show()