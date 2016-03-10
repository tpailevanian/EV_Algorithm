from llf_constants import *
import csv
import os
import datetime
import vehicle

class CSV_Util:

	def __init__( self, data_path, data_filename ):

		
		cwd = os.getcwd()

		# Create and switch to Logs directory
		logPath = data_path + '/Logs/'
		folderName = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M_LOGS')

		self.logPath = logPath + folderName

		try:
			os.makedirs(self.logPath)

		except OSError:
			pass # already exists

		os.chdir(self.logPath)

		# Create CSV file to log vehicle data
		filename = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M_LOG_VEHICLES.csv')
		vehLogfile = open(filename, 'w')
		self.vehLogwriter = csv.writer(vehLogfile, delimiter=',', quotechar='\n')

		self.vehLogwriter.writerow( ['Date', 'Start Time', 'End Time', 'Duration', \
									'Charge Time', 'ID', 'Energy', 				\
									'Charge Rate', 	'Remaining Charge', 'Laxity' ] )

		# Create CSV file to log simulation data
		filename = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M_LOG_SIM.csv')
		simLogfile = open(filename, 'w')
		self.simLogwriter = csv.writer(simLogfile, delimiter=',', quotechar='\n')

		self.simLogwriter.writerow( ['Number of Vehicles', numVehicles ])
		self.simLogwriter.writerow( ['Start Date', simulation_start_date ])
		self.simLogwriter.writerow( ['Start Time', simulation_start_time ])
		self.simLogwriter.writerow( ['End Date', simulation_end_date ])
		self.simLogwriter.writerow( ['End Time', simulation_end_time ])
		self.simLogwriter.writerow( ['Max Power', max_pwr / 3600.0 ])

		self.simLogwriter.writerow( ['Date', 'Time', 'LLF Laxity', 'IC Laxity', \
										'LLF Demand', 'IC Demand' ])

		# Switch to data directory
		self.dataPath = data_path
		os.chdir(self.dataPath)

		try:
			datafile = open(data_filename, 'rU')
			self.sampleData = csv.reader(datafile, delimiter=',', quotechar='\n')

		except :
			print "Unexpected error:", sys.exc_info()[0]
		
		# Export the parameters for the data
		self.parameters = next(self.sampleData)

		# Switch back to original working path
		os.chdir(cwd)

	def addVehicle( self ):

		# Read one additional row from the data and return the vehicle parameters
		row = next(self.sampleData)

		# Process the data
		start_time = datetime.datetime.strptime(row[1], "%m/%d/%y %H:%M")
		end_time = datetime.datetime.strptime(row[3], "%m/%d/%y %H:%M")
		duration = datetime.datetime.strptime(row[5], '%H:%M:%S')
		charge_time = datetime.datetime.strptime(row[6], '%H:%M:%S')
		energy_needed = float(row[7])
		
		zero_time = datetime.datetime.strptime('00:00:00', '%H:%M:%S')
		charge_time_seconds = ( charge_time - zero_time ).total_seconds()
		if charge_time_seconds != 0:
			charge_rate = energy_needed / charge_time_seconds
		else:
			charge_rate = 0.00001

		# Create Vehicle object and return it with given parameters
		return vehicle.Vehicle( start_time, end_time, energy_needed, charge_rate )

	def exportVehicletoCSV( self, vehicle ):

		self.vehLogwriter.writerow([ vehicle.arrivalTime.strftime('%m/%d/%Y'), 	\
									vehicle.arrivalTime.strftime('%H:%M'),		\
									vehicle.endTime.strftime('%H:%M'),			\
									vehicle.duration,							\
									vehicle.chargeTimeNeeded,					\
									vehicle.id, 								\
									vehicle.chargeReq,							\
									vehicle.maxRate, 							\
									vehicle.chargeReq - vehicle.charged, 		\
									vehicle.laxity ])

	def exportSimtoCSV( self, sim_data ):
		
		for i in range(len(sim_data.time)):
			
			self.simLogwriter.writerow([ sim_data.time[i].strftime('%m/%d/%Y'), 	\
										sim_data.time[i].strftime('%H:%M'),			\
										sim_data.llf_avg_laxity[i],					\
										sim_data.ic_avg_laxity[i],					\
										sim_data.llf_demand[i],						\
										sim_data.ic_demand[i] ])

	def getLogPath( self ):

		return self.logPath




