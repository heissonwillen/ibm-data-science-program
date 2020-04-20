import pandas
import matplotlib
from matplotlib import pyplot
import numpy

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

data_frame = pandas.read_csv(filename, names=headers)
data_frame.replace('?', numpy.nan, inplace = True)

avg_horsepower = data_frame['horsepower'].astype('float').mean(axis=0)

data_frame['horsepower'].replace(numpy.nan, avg_horsepower, inplace=True)
data_frame['horsepower'] = data_frame['horsepower'].astype(int, copy=True)

matplotlib.pyplot.hist(data_frame['horsepower'])


matplotlib.pyplot.xlabel('horsepower')
matplotlib.pyplot.ylabel('count')
matplotlib.pyplot.title('horsepower bins')

matplotlib.pyplot.show()
