# I want the backround of the image to be transparent. How can I do that?
# To do so, you can use the following code snippet:

import numpy as np
import matplotlib.pyplot as plt

# Data
models = ['Model Y', 'Model 3', 'Leaf', 'Model S', 'Bolt EV']
prices = [33890, 35990, 28140, 71090, 29280]
resale_values = [26896, 35076, 23025, 58168, 24252]

# Set the width of the bars
bar_width = 0.35

# Set the x locations for the groups
x = np.arange(len(models))

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting prices
ax.bar(x - bar_width/2, prices, bar_width, color='skyblue', label='Price')

# Plotting resale values
ax.bar(x + bar_width/2, resale_values, bar_width, color='orange', label='Resale Value')

# Adding labels and title
ax.set_xlabel('Car Model')
ax.set_ylabel('Price/Resale Value ($)')
ax.set_title('Car Prices vs. Resale Values')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()

# Adding values on top of each bar
for i in range(len(models)):
    ax.text(x[i] - bar_width/2, prices[i] + 200, f'${prices[i]}', ha='center')
    ax.text(x[i] + bar_width/2, resale_values[i] + 200, f'${resale_values[i]}', ha='center')

# Remove the frame around the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()

# Here we set the transparent background and the axis and the data should be white coloured
# The numbers displayed on the axes will be white and the numbers displayed over the bars will be white as well
fig.patch.set_alpha(0)
fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.title.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')


# Save the image with transparent background
plt.savefig('car_prices_vs_resale_values2.png', transparent=True)
plt.show()