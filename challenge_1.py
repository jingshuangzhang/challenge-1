# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020
# to analyze supply and demand for bikes in the system.

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import simplejson as json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and
# available bikes (num_bikes_available) at all stations in the system

sumdoc = 0
sumbike = 0
countdoc = 0
countbike = 0

for x in divvy_stations:
	countdoc += 1
	countbike += 1
	sumdoc = sumdoc + x['num_docks_available']
	sumbike = sumbike + x['num_bikes_available']
	print(x)

avadoc = sumdoc / countdoc
avabike = sumbike / countbike

print(avadoc)
print(avabike)

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

totalbike = 0
rentbike = 0
counttotal = 0
countrent = 0

for a in divvy_stations:
	counttotal +=1
	countrent +=1
	totalbike = totalbike + a['num_bikes_available'] + a['is_installed'] + a['is_returning'] + a['is_renting'] + a['num_bikes_disabled']
	rentbike = rentbike + a['is_renting']
	print(a)

rentratio = rentbike / totalbike


# PROBLEM 3
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows
# the percentage of bikes available at each individual station (again ignore ebikes).
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

str = '%'

for b in divvy_stations:
	b['num_bikes_total'] = b['num_bikes_available'] + b['is_installed'] + b['is_returning'] + b['is_renting'] + b['num_bikes_disabled']
	b['percent_bikes_remaining'] = (float(b['num_bikes_available']) / float(b['num_bikes_total'])) * 100
	b['percent_bikes_remaining'] = '{:.2f}%'.format(b['percent_bikes_remaining'])
	print(b)
