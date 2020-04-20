import pandas

headers = ['first name', 'last name', 'adress', 'city', 'state', 'number']
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"

data_frame = pandas.read_csv(url, header = None)
data_frame.columns = headers

print(data_frame)