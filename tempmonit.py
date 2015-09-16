import ConfigParser
import rrdtool
import os

# Create Round Robin Database
def create_rrd(rrdfile):
	rrdtool.create(rrdfile, '--start', 'now', '--step', '60', 'RRA:AVERAGE:0.5:1:1200', 'DS:temp:GAUGE:600:-273:5000')
	print "dwa ",rrdfile

# Feed updates to the RRD
def update_rrd(rrdfile,rrddata):
	rrdtool.update(rrdfile, rrddata)

def read_temp(section,detector):
	print section,' ',detector
	tmp = open(detector)
	txt = tmp.read()
	tmpdata = txt.split("\n")[1].split(" ")[9]
	temp = float(tmpdata[2:])
	temp = temp/1000
	return temp



config = ConfigParser.ConfigParser()
config.read('temperature.cfg')

for section in config.sections():
	print section
	filename=section+'.rrd'
	detector=config.get(section,'detector')
	# read_temp(section,detector)

	if (not os.path.isfile(filename)):
		print "nie ma"
		create_rrd(filename)

	rrddata = 'N:32'


	update_rrd(filename,rrddata)
