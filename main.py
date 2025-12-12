import matplotlib.pyplot
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='diabetes', version=1, as_frame=True)
print(data.DESCR)

features = list(data.frame.columns)
selected_features = ['skin', 'insu', 'mass', 'pedi', 'age']
print("Selected features: ", selected_features)

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))
for ax, f in zip(axs, selected_features):
    ax.hist(data.frame[f], bins=5, color='pink', edgecolor='black')
    ax.set_xlabel(f)
  
reference_feature = selected_features[0]
comparison_feature = selected_features[4]

plt.figure(figsize=(5, 5))
plt.scatter(data.frame[reference_feature], data.frame[comparison_feature], alpha=0.6)
plt.xlabel(f'{reference_feature} (millimeter)')
plt.ylabel(f'{comparison_feature} (year)')
plt.title(f'Scatter Plot of {comparison_feature} vs. {reference_feature}')

plt.savefig('correlation_plot.png')

plt.show()
