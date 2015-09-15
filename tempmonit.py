import ConfigParser
import rrdtool
import os

# Create Round Robin Database
def create_rrd(rrdfile):
	rrdtool.create(rrdfile, '--start', 'now', '--step', '60', 'RRA:AVERAGE:0.5:1:1200', 'DS:temp:GAUGE:600:-273:5000')
	print "dwa ",rrdfile

# Feed updates to the RRD
def update_rrd(rrdfile,rrddata):
	rrdtool.update(rrdfile, 'N:32')

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
	detector=config.get(filename,'detector')
	# read_temp(section,detector)

	if (not os.path.isfile(section)):
		print "nie ma"
		create_rrd(section)

	temp = read_temp(section,detector)
	
	update_rrd(filename,rrddata)
