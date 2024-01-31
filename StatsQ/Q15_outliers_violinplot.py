import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset('tips')

print(data)
# Create a violin plot with outliers shown
sns.violinplot(x='day', y='total_bill', data=data, kde = True, showoutliers=True)
plt.show()