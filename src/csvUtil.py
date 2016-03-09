import csv
import os
import datetime
import vehicle

class CSV_Util:

	def __init__( self, data_path, data_filename ):

		
		cwd = os.getcwd()

		# Switch to Logs directory
		logPath = data_path + '/Logs'
		os.chdir(logPath)

		# Create CSV file to log data
		filename = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M_LOG.csv')
		logfile = open(filename, 'w')
		self.logwriter = csv.writer(logfile, delimiter=',', quotechar='\n')

		self.logwriter.writerow( ['Date', 'Start Time', 'End Time', 'Duration', \
									'Charge Time', 'ID', 'Energy', 				\
									'Charge Rate', 	'Remaining Charge', 'Laxity' ] )

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
		charge_rate = energy_needed / charge_time_seconds

		# Create Vehicle object and return it with given parameters
		return vehicle.Vehicle( start_time, end_time, energy_needed, charge_rate )

	def exportVehicletoCSV( self, vehicle ):

		self.logwriter.writerow([ vehicle.arrivalTime.strftime('%m/%d/%Y'), 	\
									vehicle.arrivalTime.strftime('%H:%M'),		\
									vehicle.endTime.strftime('%H:%M'),			\
									vehicle.duration,							\
									vehicle.chargeTimeNeeded,					\
									vehicle.id, 								\
									vehicle.chargeReq,							\
									vehicle.maxRate, 							\
									vehicle.chargeReq - vehicle.charged, 		\
									vehicle.laxity ])





