import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd
iris = load_iris()
X = iris.data
y = iris.target

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_

pca = PCA(n_components=2)
reduced_X = pca.fit_transform(X)

df = pd.DataFrame(reduced_X, columns=["PC1", "PC2"])
df["Cluster"] = labels

plt.figure(figsize=(8, 6))
plt.scatter(df["PC1"], df["PC2"], c=df["Cluster"], cmap="viridis", s=50)
plt.suptitle("Name : Krishna | Roll No. : 1323215", fontsize=10)
plt.title("K-Means Clusters on Iris Dataset (PCA Reduced)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

print(df.head())
