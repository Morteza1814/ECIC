import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter

# Prefetching methods and their respective speedups over the baseline
methods = ['PIF', 'RDIP', 'FNL-MMA (12KB)', 'FNL-MMA (96KB)', 'MANA (16KB)', 'MANA (122KB)']
speedup_1 = [28, 14.8, 24.5, 29.2, 25.6, 27.8]  # Replace with actual speedup values in percent for the first bar
speedup_2 = [27.7, 14, 23, 28.2, 24.9, 27.3]   # Replace with actual speedup values in percent for the second bar
# Colors for the bars
color_1 = 'blue'
color_2 = 'orange'

# Create a bar plot with two bars per prefetcher
fig, ax = plt.subplots()
bar_width = 0.35
index = range(len(methods))

bar1 = ax.bar(index, speedup_1, bar_width, color=color_1, label='32KB 8-way')
bar2 = ax.bar([p + bar_width for p in index], speedup_2, bar_width, color=color_2, label='32KB 2-way')

# Add labels and title
# ax.set_xlabel('Prefetching Methods')
ax.set_ylabel('Average Speedup (%)', labelpad=20, fontsize=20)
# ax.set_title('Average Speedup of Prefetching Methods over Baseline')
ax.set_xticks([p + bar_width / 2 for p in index])
ax.set_xticklabels(methods, rotation=45, ha='right', fontsize=12)  # Rotate x-axis labels for better visibility

# Display the values on top of the bars
# for rect in bar1 + bar2:
#     height = rect.get_height()
#     ax.annotate('{}'.format(height),
#                 xy=(rect.get_x() + rect.get_width() / 2, height),
#                 xytext=(0, 3),  # 3 points vertical offset
#                 textcoords="offset points",
#                 ha='center', va='bottom')

# Set y-axis ticks as percentages
ax.yaxis.set_major_locator(FixedLocator(ax.get_yticks()))
ax.yaxis.set_major_formatter(FixedFormatter(['{:.0f}%'.format(x) for x in ax.get_yticks()]))
ax.set_ylim(0, 40)

# Add gridlines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend
ax.legend(fontsize=12)

ax.tick_params(axis='y', labelsize=13)
# Adjust layout to provide more space
plt.tight_layout()

# Show the plot
plt.show()

plt.savefig('speedup.png')
