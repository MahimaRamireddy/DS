#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_df = pd.read_csv("iris.csv")

# Separate features and labels
X = iris_df[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
y = iris_df['variety']

# Standardize the features
X_standardized = (X - X.mean()) / X.std()

# Calculate the Covariance Matrix
covariance_matrix = np.cov(X_standardized, rowvar=False)

# Eigen Decomposition to obtain eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

# Sort eigenvalues and corresponding eigenvectors in descending order
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Choose the number of principal components (2 in this case)
num_components = 2
selected_eigenvectors = eigenvectors[:, :num_components]

# Project the data onto the selected principal components
X_pca = X_standardized.dot(selected_eigenvectors)

# Visualize the data in the reduced-dimensional space
plt.figure(figsize=(10, 6))
for variety in iris_df['variety'].unique():
    # Scatter plot for each variety with different colors
    plt.scatter(X_pca[y == variety].iloc[:, 0], X_pca[y == variety].iloc[:, 1], label=variety)

# Add labels and title to the plot
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Iris Dataset')
plt.legend()  # Show legend indicating different varieties
plt.show()


# In[ ]:




