import matplotlib.pyplot as plt

def get_ap_list():
	data_list = []
	for i in range(-9,10):
		data_list.append(i)
	return data_list

def get_square(x_list):
	y_list = []
	for i in  range(len(x_list)):
		y_list.append(x_list[i]**2)
	return y_list

x_list = get_ap_list()

'''
matplotlib.pyplot.plot(x_list, get_square(x_list))
matplotlib.pyplot.show()
'''