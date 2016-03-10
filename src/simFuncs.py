from vehicleLists import *
from llf_constants import *
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

def plotPower( sim_data ):

	t = sim_data.time 
	llf_demand = sim_data.llf_demand
	ic_demand = sim_data.ic_demand

	hours = HourLocator()   # every hour
	minutes = MinuteLocator(arange(1, 61, 15))
	HourFmt = DateFormatter('%H:%M')

	fig, ax = plt.subplots()
	ax.plot( t, llf_demand )
	ax.plot( t, ic_demand )
	plt.axhline( y=max_pwr/3600.0)


	# format the ticks
	ax.xaxis.set_major_locator(hours)
	ax.xaxis.set_major_formatter(HourFmt)
	ax.xaxis.set_minor_locator(minutes)

	ax.set_xlim(t[0], t[-1])

	plt.show()

