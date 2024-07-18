# Flask Server for SafeDeals

The Flask server is used for finding the optimal number of clusters that must be generated to accommodate new stores within any city. To compute the optimal value of k, for the k-Means clustering algorithm, the elbow method is utilized. The elbow method plots the WCSS (within-cluster sum of squares) against the number of clusters k, to find the elbow point (point where the rate of change in WCSS is maximum).

However, the value of k could be equal to or greater than the optimal value computed using the Elbow method. The primary reason behind creating more clusters than the optimal value is to maintain the location privacy within each cluster. Geo-indistinguishability implies that the privacy level decreases with increasing cluster size. Hence, k is chosen such that the average distance of points of interest from the cluster centroid is within 2km.
