''' Program that able to parse data from snelheidscamera's_met_lus_120601.csv'''
#!usr/local/bin/python3.6
import argparse

parser = argparse.ArgumentParser(description = 'Queries input text files for Cameras, based on certain criteria')

parser.add_argument('--cameras', dest = 'CAMERA_FILE',required= True,  help='A properly formatted file containing locations of cameras')
parser.add_argument('--cameras-in-city',dest ='CITY', help='Queries input files for all cameras in a city')
parser.add_argument('--camera-on_ROAD', dest ='ROAD', help='Queries input files for all cameras on a certain road')


args = parser.parse_args()

def parse(File):
	'''Function that parses data in a file'''
	''' Initialize variables '''
	count = 0
	s = ''
	T = ()

	''' Open the file '''
	f = open(File,'r')

	''' Count the number of line in a file '''
	for line in f:
		count+=1

	''' return to the first line '''
	f.seek(0)

	''' starting to parse the file '''
	for i in range(count): 
		'''2,count-9'''
		ligne =f.readline()
		s = ligne.strip('\n')
		T += (tuple(s.split(',')),)

	''' close the file '''
	f.close()

	return T


def filtreT(x,T):
	'''Filter function: this function has to be improved using map, filter and lambda'''
	T1 = ()
	for i in T:
		for j in i:
			if j == x:
				T1+=(i,)
	return T1

print('List of camera', parse(args.CAMERA_FILE))
print('List of camera in ', args.CITY, filtreT(args.CITY,parse(args.CAMERA_FILE)))
print('List of camera on ', args.ROAD, filtreT(args.ROAD,parse(args.CAMERA_FILE)))
