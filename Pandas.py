import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data(input_file, index):
	input_data = np.loadtxt(input_file, delimiter=',')

	to_date = lambda x, y: str(int(x)) + '-' + str(int(y))

	start = to_date(input_data[0, 0], input_data[0, 1])
	if input_data[-1, 1] == 12:
		year = input_data[-1, 0] + 1
		month = 1
	else:
		year = input_data[-1, 0]
		month = input_data[-1, 1] + 1
	end = to_date(year, month)
	date_indices = pd.date_range(start, end, freq='M')
	output = pd.Series(input_data[:, index], index=date_indices)
	return output

if __name__=='__main__':
	input_file = 'data_2D.txt'
	indices = [2, 3]
	for index in indices:
		timeseries = read_data(input_file, index)
		plt.figure()
		timeseries.plot()
		plt.title('Dimension ' + str(index - 1))
	plt.show()