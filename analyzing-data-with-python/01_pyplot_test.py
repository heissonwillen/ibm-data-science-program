import matplotlib.pyplot as plt
import pandas

csv_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv'

data_frame = pandas.read_csv(csv_url)
'''
new_header = data_frame.iloc[0]
data_frame.columns = new_header
print(data_frame)
'''
print(data_frame["name"])
'''
plt.plot(data_frame['Height (in)'], data_frame['Weight (lbs)'])
plt.show()
'''