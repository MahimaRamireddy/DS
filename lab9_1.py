import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

#data cleaning

# Load the CSV file into a DataFrame
file_path = 'diabetes.csv'
df = pd.read_csv(file_path)

# Replace 0 values with the mean of the specific column
df.replace({'Glucose': {0: df['Glucose'].mean()}}, inplace=True)
df.replace({'BloodPressure': {0: df['BloodPressure'].mean()}}, inplace=True)
df.replace({'SkinThickness': {0: df['SkinThickness'].median()}}, inplace=True)
df.replace({'Insulin': {0: df['Insulin'].median()}}, inplace=True)
df.replace({'BMI': {0: df['BMI'].mean()}}, inplace=True)


# Remove duplicates
df.drop_duplicates(inplace=True)

# Save the cleaned data to a new CSV file
cleaned_file_path = 'cleaned_diabetes.csv'
df.to_csv(cleaned_file_path, index=False)

#print('Data cleaning completed. Cleaned data saved to', cleaned_file_path)

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


# Function to classify using Minimum Distance Classifier
def classify_minimum_distance(test_samples, train_samples, train_labels):
    predicted_labels = []
   
    for test_sample in test_samples:
        # Calculate Euclidean distances to all train samples
        distances = np.array([euclidean_distance(test_sample, train_sample) for train_sample in train_samples])
       
        # Find the index of the nearest neighbor
        nearest_neighbor_index = np.argmin(distances)
       
        # Predict the label of the nearest neighbor
        predicted_label = train_labels[nearest_neighbor_index]
        predicted_labels.append(predicted_label)
   
    return np.array(predicted_labels)

# Extract features and labels
features = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Age']].values
labels = df['Outcome'].values

# Split the data into train and test sets (80% and 20%)
train_size = int(0.8 * features.shape[0])
X_train = features[:train_size]
y_train = labels[:train_size]
X_test = features[train_size:]
y_test = labels[train_size:]

# Classify using Minimum Distance Classifier
predicted_test_labels = classify_minimum_distance(X_test, X_train, y_train)

# Calculate accuracy
accuracy = np.mean(predicted_test_labels == y_test)
print('Accuracy of Minimum Distance Classifier:', accuracy)
# Function to initialize centroids randomly
def initialize_centroids(X, n_clusters):
    n_samples, n_features = X.shape
    centroids = X[np.random.choice(n_samples, n_clusters, replace=False)]
    return centroids

# Function to assign points to the nearest centroid
def assign_points_to_centroids(X, centroids):
    n_samples = X.shape[0]
    distances = np.zeros((n_samples, len(centroids)))
   
    for i, centroid in enumerate(centroids):
        distances[:, i] = np.linalg.norm(X - centroid, axis=1)
   
    return np.argmin(distances, axis=1)

# Function to update centroids based on assigned points
def update_centroids(X, labels, n_clusters):
    centroids = np.zeros((n_clusters, X.shape[1]))
    for i in range(n_clusters):
        centroids[i] = np.mean(X[labels == i], axis=0)
    return centroids

# Function to perform K-means clustering
def kmeans(X, n_clusters, max_iters=100):
    centroids = initialize_centroids(X, n_clusters)
    for i in range(max_iters):
        old_centroids = centroids
        labels = assign_points_to_centroids(X, centroids)
        centroids = update_centroids(X, labels, n_clusters)
        if np.all(old_centroids == centroids):
            break
    return labels, centroids

# Function to calculate accuracy
def calculate_accuracy(test_labels, true_labels):
    cluster_to_true_label = {}

    for cluster in np.unique(test_labels):
        cluster_samples = true_labels[test_labels == cluster]
        true_label = np.argmax(np.bincount(cluster_samples))
        cluster_to_true_label[cluster] = true_label

    mapped_labels = np.array([cluster_to_true_label[cluster] for cluster in test_labels])
    accuracy = np.mean(mapped_labels == true_labels)
    return accuracy

# Load the diabetes dataset
file_path = 'cleaned_diabetes.csv'
df = pd.read_csv(file_path)

# Select features (exclude the outcome column)
features = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Age']].values

# Normalize the features (Min-Max scaling)
min_values = np.min(features, axis=0)
max_values = np.max(features, axis=0)
features_scaled = (features - min_values) / (max_values - min_values)

# Split the data into train and test sets (80% and 20%)
train_size = int(0.8 * features_scaled.shape[0])
X_train = features_scaled[:train_size]
X_test = features_scaled[train_size:]

# Perform K-means clustering
n_clusters = 2  # Number of clusters
train_labels, train_centroids = kmeans(X_train, n_clusters)

# Predict clusters for the test set
test_distances = np.linalg.norm(X_test[:, np.newaxis] - train_centroids, axis=2)
test_labels = np.argmin(test_distances, axis=1)

# Calculate accuracy
true_labels = df['Outcome'][train_size:].values
accuracy = calculate_accuracy(test_labels, true_labels)
print('Accuracy of K-means clustering:', accuracy)


# Visualize the clusters
plt.scatter(X_test[:, 1], X_test[:, 5], c=test_labels, cmap='viridis')
plt.scatter(train_centroids[:, 1], train_centroids[:, 5], marker='x', s=200, c='red', label='Cluster Centers')
plt.xlabel('Glucose (Min-Max Scaled)')
plt.ylabel('BMI (Min-Max Scaled)')
plt.title('KMeans Clustering')
plt.legend()
plt.show()