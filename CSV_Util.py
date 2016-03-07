import csv
import os
import datetime

class Csv_Util:

	def __init__( self , data_path , data_filename ):

		
		cwd = os.getcwd()

		# Switch to Logs directory
		logPath = data_path + '/Logs'
		os.chdir(logPath)

		# Create CSV file to log data
		filename = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M_LOG.csv')
		logfile = open(filename, 'w')
		self.logwriter = csv.writer(logfile, delimiter=',', quotechar='\n')

		# Switch to data directory
		self.dataPath = data_path
		os.chdir(self.data_path)

		try:
			datafile = open(data_filename, 'rU')
			self.sampleData = csv.reader(datafile, delimiter=',', quotechar='\n')

		except :
			print "Unexpected error:", sys.exc_info()[0]
		
		# Export the parameters for the data
		self.parameters = next(self.sampleData)

		# Switch back to original working path
		os.chdir(cwd)

	def addVehicle():

		# Read one additional row from the data and return the vehicle parameters
		row = next(self.sampleData)
		start_time = datetime.datetime.strptime(row[1], "%m/%d/%y %H:%M")
		duration = datetime.datetime.strptime(row[5], '%H:%M:%S')
		charge_time = datetime.datetime.strptime(row[6], '%H:%M:%S')
		energy_needed = float(row[7])

		return [start_time, duration.time(), charge_time.time(), energy_needed]

	def exportVehicletoCSV(vehicle):

		self.logwriter.writerow(vehicle)