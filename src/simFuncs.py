from vehicleLists import *
from sim_constants import *
from numpy import arange
from matplotlib.dates import HourLocator, MinuteLocator, DateFormatter
import matplotlib.pyplot as plt
import vehicle

def averageLaxity( lists ):

	averageLaxity = 0

	for vehicle in lists.chargeQueue:
		averageLaxity += vehicle.laxity 

	if len(lists.chargeQueue) == 0:
		averageLaxity =0
	else:
		averageLaxity / len( lists.chargeQueue )

	return averageLaxity

def plotPower( sim_data, path ):

	t = sim_data.time 
	llf_demand = sim_data.llf_demand 
	ic_demand = sim_data.ic_demand 

	hours = HourLocator()   # every hour
	minutes = MinuteLocator(arange(1, 61, 15))
	HourFmt = DateFormatter('%H:%M')

	fig, ax = plt.subplots()
	ax.plot( t, llf_demand , label='LLF' )
	ax.plot( t, ic_demand , label= 'IC' )
	plt.axhline( y=max_pwr)


	# format the ticks
	ax.xaxis.set_major_locator(hours)
	ax.xaxis.set_major_formatter(HourFmt)
	ax.xaxis.set_minor_locator(minutes)

	ax.set_xlim(t[0], t[-1])

	fig.suptitle('Power Demand', fontsize=20)
	plt.xlabel('Time HH:MM', fontsize = 14)
	plt.ylabel('Power', fontsize=14)

	ax.legend( fancybox=True, shadow=True, ncol=2 )

	fig.autofmt_xdate()

	#plt.ion()

	plt.show()

	fig.savefig((path+'/power_demand.jpg'))

	#plt.close(fig) 

def plotLaxity( sim_data, path ):

	t = sim_data.time 
	llf_laxity = sim_data.llf_avg_laxity 
	ic_laxity = sim_data.ic_avg_laxity 

	hours = HourLocator()   # every hour
	minutes = MinuteLocator(arange(1, 61, 15))
	HourFmt = DateFormatter('%H:%M')

	fig, ax = plt.subplots()
	ax.plot( t, llf_laxity , label='LLF' )
	ax.plot( t, ic_laxity , label= 'IC' )
	plt.axhline( y=max_pwr)


	# format the ticks
	ax.xaxis.set_major_locator(hours)
	ax.xaxis.set_major_formatter(HourFmt)
	ax.xaxis.set_minor_locator(minutes)

	ax.set_xlim(t[0], t[-1])

	fig.suptitle('Average Laxity', fontsize=20)
	plt.xlabel('Time HH:MM', fontsize = 14)
	plt.ylabel('Average Laxity', fontsize=14)

	# Shrink current axis's height by 10% on the bottom
	box = ax.get_position()
	#ax.set_position([box.x0, box.y0 + box.height * 0.1, \
    #             box.width, box.height * 0.85])

	# Put a legend below current axis
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.17), \
          fancybox=True, shadow=True, ncol=2 )

	fig.autofmt_xdate()

	#plt.ion()

	plt.show()

	fig.savefig((path+'/average_laxity.jpg'))

	#plt.close(fig) 

