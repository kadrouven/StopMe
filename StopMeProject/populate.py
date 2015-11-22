import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StopMeProject.settings')

import django
django.setup()

from StopMe.models import Station, Route, RouteStation

def add_stations(filename):
    print "Opening station file..."
    f = open(filename, 'rU')

    print "Reading in stations..."
    for line in f:
        line_list = line.strip('\n').split(",")
        print "Adding station to database..."
        p = Station.objects.get_or_create(stationName=line_list[0], lat=float(line_list[1]), lng=float(line_list[2]), type=line_list[3])

    print "Closing file...\n"
    f.close()

def add_route(filename):
    print "Opening route file..."
    f = open(filename, 'rU')

    print "Reading in routes..."
    for line in f:
        line_list = line.strip('\n').split(",")
        print "Adding route to database..."
        p = Route.objects.get_or_create(serviceNumber=line_list[0], origin=Station.objects.get(stationName=line_list[1]), destination=Station.objects.get(stationName=line_list[2]), via=Station.objects.get(stationName=line_list[3]))

    print "Closing file...\n"
    f.close()

def add_routestations(filename):
    print "Opening routeStations file..."
    f = open(filename, 'rU')
    
    split = f.readline().strip("\n").split(",")
    print split
    print Station.objects.get(stationName=split[0])
    print Station.objects.get(stationName=split[1])
    print Station.objects.get(stationName=split[2])
    
    route = Route.objects.get(origin=Station.objects.get(stationName=split[0]), destination=Station.objects.get(stationName=split[2]), via=Station.objects.get(stationName=split[1]))

    print "Reading in routeStations..."
    for line in f:
        line = line.strip('\n')
        station = Station.objects.get(stationName=line)
        print "Adding routeStations to database..."
        p = RouteStation.objects.get_or_create(route=route, station=station)
        
    print "Closing file...\n"
    f.close()

# Start execution here!
if __name__ == '__main__':
    print "Starting StopMe population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StopMeProject.settings')
   
    ######### Train #########
   
    # Read train stations from file and add them to the db

    add_stations('Data/Train/Stations/TrainStations.txt')


    # Read train routes from file and add them to the db

    add_route('Data/Train/Routes/Routes.txt')
    
    # Read train RouteStations from file and add them to the db
    
    add_routestations('Data/Train/RouteStations/HelensburghCentral_Glasgow_Edinburgh.txt')
    
    
    ########## Bus ##########
    
    
    # Read train stations from file and add them to the db

    add_stations('Data/Bus/Stops/77_BusStops_To_And_From.txt')


    # Read train routes from file and add them to the db

    add_route('Data/Bus/Routes/Routes.txt')
    
    # Read train RouteStations from file and add them to the db
    
    add_routestations('Data/Bus/RouteStops/77_BusStops_To_Airport.txt')
    add_routestations('Data/Bus/RouteStops/77_BusStops_To_BusStation.txt')
    
    
    