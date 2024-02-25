from flask import Flask
from flask import request

import pandas as pd
from sklearn import preprocessing
from kneed import KneeLocator
from utility.helper import *

pyServer = Flask(__name__)

@pyServer.route('/getOptimumK', methods=['POST'])
def getOptimumK():
  reqPayload = request.json

  latitude = reqPayload['lat']
  longitude = reqPayload['long']

  if(len(latitude) > 10):
    upper_limit = 11
  else:
    upper_limit = len(latitude) + 1

  data_frame = pd.DataFrame({"Latitude": latitude, "Longitude": longitude})
  scaled_data = preprocessing.scale(data_frame)

  wcss = compute_wcss(scaled_data, len(latitude))
  optimal_k = KneeLocator(range(1, upper_limit), wcss, curve="convex", direction="decreasing")

  if(optimal_k.elbow == None):
    elbow = 1
  else:
    elbow = optimal_k.elbow

  k = compute_k(elbow, len(latitude), scaled_data, data_frame)
  return {"numClusters": k}

if __name__ == '__main__':
  pyServer.run()
