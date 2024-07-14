import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.lines import Line2D

# Data
models = ['Model Y', 'Model 3', 'Leaf', 'Model S', 'Bolt EV']
prices = [33890, 35990, 28140, 71090, 29280]
warranty = ['8yrs or 1lac miles', '8yrs or 1lac miles', '3yrs or 36000 miles', '8yrs or 1.5 lac miles', '8yrs or 1 lac miles']

# Convert warranty information to numerical values for plotting
warranty_numeric = []
for w in warranty:
    if '8yrs' in w:
        warranty_numeric.append(8)
    else:
        warranty_numeric.append(3)  # Assuming all other warranties are for 3 years

# Determine color for each bar based on warranty
colors = []
for w in warranty_numeric:
    if w <= 3:
        colors.append('#FFD580')
    elif w <= 6:
        colors.append('yellow')
    else:
        colors.append('#ADD8E6')

# Plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plotting the data
xpos = range(len(models))
ypos = prices
zpos = [0] * len(models)
dx = [1] * len(models)  # Width of bars along the x-axis
dy = [1000] * len(models)  # Width of bars along the y-axis
dz = warranty_numeric  # Height of bars along the z-axis

bars = ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors)

# Adding labels and title
ax.set_xlabel('Car Models', labelpad=22)
ax.set_ylabel('Price ($)', labelpad=10)
ax.set_zlabel('Battery Warranty (Years)', labelpad=10)
ax.set_title('3D Bar Plot: Car Prices and Battery Warranty')

# Setting ticks and tick labels
ax.set_xticks(xpos)
ax.set_xticklabels(models, rotation=45, ha='right')
ax.set_yticks(range(30000, 75000, 10000))

# Add color legend
legend_elements = [Line2D([0], [0], color='#FFD580', lw=4, label='1-3 years'),
                   Line2D([0], [0], color='yellow', lw=4, label='3-6 years'),
                   Line2D([0], [0], color='#ADD8E6', lw=4, label='6-9 years')]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1, 1))

# Show plot
plt.tight_layout()
# Save the image with transparent background
# Here we set the transparent background and the axis and the data should be white coloured
# The numbers displayed on the axes will be white and the numbers displayed over the bars will be white as well

fig.patch.set_alpha(0)
fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.zaxis.label.set_color('white')
ax.title.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='z', colors='white')

plt.savefig('Battery_warranty_1', transparent=True)
plt.show()