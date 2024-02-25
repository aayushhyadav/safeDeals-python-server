from sklearn.cluster import KMeans
import math

'''
# finds optimal value of k using elbow method
'''
def compute_wcss(scaled_data, data_points):
  wcss = []

  if(data_points > 10):
    upper_limit = 11
  else:
    upper_limit = data_points + 1

  for i in range(1, upper_limit):
    kMeans = KMeans(i, init = 'k-means++', random_state = 42)
    kMeans.fit(scaled_data)
    wcss.append(kMeans.inertia_)

  return wcss

def degreeToRadian(degree):
    return (degree * math.pi) / 180

'''
# computes the haversine distance using latitude and longitude coordinates of source and destination
'''
def haversineDist(lat1, long1, lat2, long2):
  R = 6371.071

  lat1 = degreeToRadian(lat1)
  long1 = degreeToRadian(long1)
  lat2 = degreeToRadian(lat2)
  long2 = degreeToRadian(long2)

  diffLat = lat2 - lat1
  diffLong = long2 - long1

  distance = 2 * R * math.asin(
    math.sqrt(math.sin(diffLat / 2) * math.sin(diffLat / 2) + math.cos(lat1) * math.cos(lat2) * math.sin(diffLong / 2) * math.sin(diffLong / 2)))

  return distance

'''
# computes average distance of data points from centroid of the cluster
'''
def calClusterMean(centroid, data):
  meanDist = 0
  latitude = (list(data['Latitude']))
  longitude = (list(data['Longitude']))

  for i in range(0, len(data)):
    meanDist += haversineDist(centroid[0], centroid[1], latitude[i], longitude[i])

  if(len(data) == 0):
    return 0

  return meanDist / len(data)

'''
# computes average size of all clusters
'''
def calMeanDistance(cluster, cluster_centers):
  mean = 0
  for i in range(0, len(cluster_centers)):
    mean += calClusterMean(cluster_centers[i], cluster[cluster['prediction'] == i])

  return mean / len(cluster_centers)

def compute_k(optimal_k, data_points, scaled_data, data_frame):
  cluster_centers = []
  cluster = data_frame.copy()

  for k in range(optimal_k, data_points + 1):
    kMeans = KMeans(k, init = 'k-means++', random_state = 42)
    kMeans.fit(scaled_data)

    cluster['prediction'] = kMeans.fit_predict(data_frame)
    cluster_centers = kMeans.cluster_centers_
    mean = (calMeanDistance(cluster, cluster_centers))

    if(mean <= 2):
        break

  if(k == data_points + 1):
    return data_points

  return k
