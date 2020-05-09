import pandas_datareader.data as web
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

def source_stock_price(symbol, start = datetime.datetime(2007, 1, 1)):
    end = datetime.datetime.now()
    df = web.DataReader(symbol, "yahoo", start, end)
    df.reset_index(inplace = True)
    df.set_index("Date", inplace = True)

    return df

def plot_pnl(symbol, bench):
	df = source_stock_price(symbol)
	date = df.index
	closep = df['Adj Close']

	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))
	ax1.plot_date(date, closep, 'b-', label = 'Price')

	for label in ax1.xaxis.get_ticklabels():
	    label.set_rotation(45)
	ax1.grid(True, color='g', linestyle=':', linewidth=1)

	ax1.fill_between(date, bench, closep, where=(closep > bench), facecolor='g', alpha=0.5)
	ax1.fill_between(date, bench, closep, where=(closep < bench), facecolor='r', alpha=0.5)
	# smart way to display legend with empty plot
	ax1.plot([],[],linewidth=5, label='loss', color='r',alpha=0.5)
	ax1.plot([],[],linewidth=5, label='gain', color='g',alpha=0.5)
	ax1.axhline(bench, color='k', linewidth=1)

	ax1.tick_params(axis='x', colors='#f06215')
	ax1.tick_params(axis='y', colors='#f06215')
	ax1.spines['left'].set_linewidth(1)	
	ax1.spines['left'].set_color('c')
	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)

	ax1.xaxis.label.set_color('b')
	ax1.yaxis.label.set_color('b')
	#ax1.set_yticks([0,50,100,150, 200, 250, 300, 350])    

	plt.xlabel('Trade Date')
	plt.ylabel('Adj Close')
	plt.title(symbol, fontdict = {'color':'blue'})
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
	plt.show()


if __name__ == '__main__':
	import sys
	try:
		if len(sys.argv) > 2:
			plot_pnl(sys.argv[1], float(sys.argv[2]))
	except Exception as e:
		print(f'Exception: {str(e)}')
