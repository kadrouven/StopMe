import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StopMeProject.settings')

import django
django.setup()

from StopMe.models import Station, Route, RouteStations

def add_station(stationName, lat, lng, transtype):
    p = Station.objects.get_or_create(stationName=stationName, lat=lat, lng=lng, transtype=transtype)[0]
    return p

def add_route(serviceNumber, origin, destination, via):
    p = Route.objects.get_or_create(serviceNumber=serviceNumber, origin=origin, destination=destination, via=via)[0]
    return p

def add_routestations(routeID, stationID):
    p = RouteStations.objects.get_or_create(routeID=Route.objects.get(id=routeID), stationID=Station.objects.get(id=stationID))[0]
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting StopMe population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StopMeProject.settings')
   
    # ADD IN OUR BUS STATIONS
    add_station('BUCHANAN STREET','55.858272','-4.255344','BUS') #SID 1
    add_station('ARGYLL ARCADE','55.858082','-4.253662','BUS') #SID 2
    add_station('SAUCHIEHALL LANE A','55.86422','-4.260189','BUS') #SID 3
    add_station('PITT STREET','55.8649','-4.265911','BUS') #SID 4
    add_station('KINGS THEATRE','55.865276','-4.269173','BUS') #SID 5
    add_station('COCHRANE ST','55.860376','-4.247408','BUS') #SID 6
    add_station('WEST GEORGE STREET A','55.86285','-4.26038','BUS') #SID 7
    add_station('GEORGE SQUARE','55.860801','-4.251086','BUS') #SID 8
    add_station('TRONGATE','55.857819','-4.249164','BUS') #SID 9
    add_station('WATSON STREET','55.856313','-4.242206','BUS') #SID 10
    add_station('CENTRAL STATION A','55.859771','-4.259126','BUS') #SID 11
    add_station('BOTHWELL STREET','55.860821','-4.258779','BUS') #SID 12
    add_station('ST VINCENT STREET','55.861896','-4.25833','BUS') #SID 13
    add_station('WEST REGENT LANE','55.86284','-4.258005','BUS') #SID 14
    add_station('WEST REGENT STREET','55.863074','-4.257922','BUS') #SID 15
    add_station('SAUCHIEHALL STREET A','55.864251','-4.257493','BUS') #SID 16
    add_station('SAUCHIEHALL STREET B','55.864541','-4.257407','BUS') #SID 17
    add_station('OPP THEATRE ROYAL','55.865941','-4.256858','BUS') #SID 18
    add_station('INGRAM ST','55.860081','-4.251277','BUS') #SID 19
    add_station('EURO HOSTEL GLASGOW','55.856882','-4.257253','BUS') #SID 20
    add_station('ARGYLE STREET','55.858046','-4.257061','BUS') #SID 21
    add_station('BROOMIELAW','55.857294','-4.259865','BUS') #SID 22
    add_station('CAMBRIDGE STREET','55.865753','-4.259146','BUS') #SID 23
    add_station('HOPE STREET','55.865572','-4.257618','BUS') #SID 24
    add_station('SAUCHIEHALL LANE B','55.863992','-4.25565','BUS') #SID 25
    add_station('BATH LANE','55.863256','-4.255969','BUS') #SID 26
    add_station('WEST GEORGE STREET B','55.862481','-4.256232','BUS') #SID 27
    add_station('RENFIELD STREET','55.861716','-4.256539','BUS') #SID 28
    add_station('SAUCHIEHALL STREET C','55.866276','-4.27037','BUS') #SID 29
    add_station('DENTAL HOSPITAL','55.865735','-4.265507','BUS') #SID 30
    add_station('ST ENOCH SHOPPING CENTRE','55.856041','-4.251319','BUS') #SID 31
    add_station('ST ENOCH SUBWAY','55.856691','-4.25505','BUS') #SID 32
    add_station('CANDLERIGGS','55.85724','-4.24681','BUS') #SID 33
    add_station('GLASGOW CROSS','55.856775','-4.244934','BUS') #SID 34
    add_station('STOCKWELL STREET','55.857361','-4.248746','BUS') #SID 35
    add_station('CENTRAL STATION B','55.859197','-4.256739','BUS') #SID 36
    add_station('NORTH COURT''','55.860987','-4.253129','BUS') #SID 37
    add_station('WELLINGTON STREET','55.861893','-4.260898','BUS') #SID 38
    add_station('DOUGLAS STREET','55.862252','-4.263852','BUS') #SID 39
    add_station('HOLLAND STREET','55.862656','-4.26749','BUS') #SID 40
    add_station('ELMBANK STREET','55.862824','-4.267681','BUS') #SID 41

    # ADD IN OUR TRAIN STATIONS

    add_station('ADDIEWELL','55.8434','-3.606552','TRAIN') #SID 42
    add_station('AIRDRIE','55.863998','-3.982932','TRAIN') #SID 43
    add_station('ANNIESLAND','55.889607','-4.321676','TRAIN') #SID 44
    add_station('ASHFIELD','55.88876','-4.248173','TRAIN') #SID 45
    add_station('BALLOCH','56.002376','-4.58347','TRAIN') #SID 46
    add_station('BELLGROVE','55.856732','-4.224058','TRAIN') #SID 47
    add_station('BELLSHILL','55.817072','-4.024479','TRAIN') #SID 48
    add_station('BISHOPBRIGGS','55.904245','-4.224722','TRAIN') #SID 49
    add_station('BLAIRHILL','55.866456','-4.043291','TRAIN') #SID 50
    add_station('BREICH','55.827286','-3.668087','TRAIN') #SID 51
    add_station('BURNSIDE','55.816954','-4.202817','TRAIN') #SID 52
    add_station('BUSBY','55.780338','-4.262187','TRAIN') #SID 53
    add_station('CAMBUSLANG','55.819539','-4.173281','TRAIN') #SID 54
    add_station('CARFIN','55.807348','-3.95624','TRAIN') #SID 55
    add_station('CARLUKE','55.731236','-3.848931','TRAIN') #SID 56
    add_station('CARNTYNE','55.854882','-4.178603','TRAIN') #SID 57
    add_station('CARSTAIRS','55.691034','-3.668481','TRAIN') #SID 58
    add_station('CHARING CROSS','55.864659','-4.269802','TRAIN') #SID 59
    add_station('CLARKSTON','55.789218','-4.275997','TRAIN') #SID 60
    add_station('CLELAND','55.804646','-3.910209','TRAIN') #SID 61
    add_station('COATBRIDGE SUNNYSIDE','55.866879','-4.028239','TRAIN') #SID 62
    add_station('COATDYKE','55.864348','-4.004959','TRAIN') #SID 63
    add_station('CORKERHILL','55.837496','-4.334216','TRAIN') #SID 64
    add_station('CROFTFOOT','55.818238','-4.228321','TRAIN') #SID 65
    add_station('CROOKSTON','55.842322','-4.364681','TRAIN') #SID 66
    add_station('CROSSMYLOOF','55.833964','-4.284289','TRAIN') #SID 67
    add_station('CROY','55.955819','-4.035501','TRAIN') #SID 68
    add_station('CURRIEHILL','55.90056','-3.318761','TRAIN') #SID 69
    add_station('DALMUIR','55.911957','-4.426748','TRAIN') #SID 70
    add_station('DUMBARTON CENTRAL','55.946668','-4.5669','TRAIN') #SID 71
    add_station('DUMBRECK','55.844952','-4.300909','TRAIN') #SID 72
    add_station('EAST KILBRIDE','55.766006','-4.180231','TRAIN') #SID 73
    add_station('EASTERHOUSE','55.85975','-4.107214','TRAIN') #SID 74
    add_station('EDINBURGH','55.951991','-3.189759','TRAIN') #SID 75
    add_station('FALKIRK HIGH','55.991819','-3.792513','TRAIN') #SID 76
    add_station('FAULDHOUSE','55.822476','-3.719278','TRAIN') #SID 77
    add_station('GARROWHILL','55.855236','-4.12945','TRAIN') #SID 78
    add_station('GIFFNOCK','55.80402','-4.293011','TRAIN') #SID 79
    add_station('GILSHOCHILL','55.897324','-4.282638','TRAIN') #SID 80
    add_station('GLASGOW CENTRAL','55.859136','-4.258109','TRAIN') #SID 81
    add_station('GLASGOW QUEEN STREET','55.862317','-4.251095','TRAIN') #SID 82
    add_station('HAIRMYRES','55.760624','-4.228339','TRAIN') #SID 83
    add_station('HARTWOOD','55.808693','-3.840682','TRAIN') #SID 84
    add_station('HAWKHEAD','55.84222','-4.398861','TRAIN') #SID 85
    add_station('HAYMARKET','55.945591','-3.218289','TRAIN') #SID 86
    add_station('HELENSBURGH CENTRAL','56.003932','-4.732176','TRAIN') #SID 87
    add_station('HIGH STREET','55.85967','-4.240342','TRAIN') #SID 88
    add_station('HOLYTOWN','55.812914','-3.973941','TRAIN') #SID 89
    add_station('HYNDLAND','55.879702','-4.3146','TRAIN') #SID 90
    add_station('KELVINDALE','55.893556','-4.309603','TRAIN') #SID 91
    add_station('KINGS PARK','55.81954','-4.246496','TRAIN') #SID 92
    add_station('KINGSKNOWE','55.918828','-3.264991','TRAIN') #SID 93
    add_station('KIRKHILL','55.813922','-4.167069','TRAIN') #SID 94
    add_station('KIRKNEWTON','55.88866','-3.432499','TRAIN') #SID 95
    add_station('LANGSIDE','55.821118','-4.277298','TRAIN') #SID 96
    add_station('LENZIE','55.921304','-4.153891','TRAIN') #SID 97
    add_station('LINLITHGOW','55.976433','-3.596683','TRAIN') #SID 98
    add_station('LIVINGSTON SOUTH','55.87168','-3.50145','TRAIN') #SID 99
    add_station('MARYHILL','55.897632','-4.30073','TRAIN') #SID 100
    add_station('MAXWELL PARK','55.837605','-4.28891','TRAIN') #SID 101
    add_station('MILNGAVIE','55.941282','-4.314344','TRAIN') #SID 102
    add_station('MOSSPARK','55.840814','-4.348301','TRAIN') #SID 103
    add_station('MOTHERWELL','55.791688','-3.994374','TRAIN') #SID 104
    add_station('NEWTON','55.818782','-4.133019','TRAIN') #SID 105
    add_station('PAISLEY CANAL','55.840082','-4.424121','TRAIN') #SID 106
    add_station('PARTICK','55.869919','-4.308879','TRAIN') #SID 107
    add_station('POLLOKSHAWS EAST','55.824642','-4.286859','TRAIN') #SID 108
    add_station('POLLOKSHAWS WEST','55.823814','-4.30159','TRAIN') #SID 109
    add_station('POLLOKSHIELDS WEST','55.83769','-4.275751','TRAIN') #SID 110
    add_station('POLMONT','55.984754','-3.714981','TRAIN') #SID 111
    add_station('POSSILPARK & PARKHOUSE','55.890146','-4.2585','TRAIN') #SID 112
    add_station('SHAWLANDS','55.829222','-4.292362','TRAIN') #SID 113
    add_station('SHETTLESTON','55.85353','-4.160041','TRAIN') #SID 114
    add_station('SHOTTS','55.818646','-3.79831','TRAIN') #SID 115
    add_station('SLATEFORD','55.926692','-3.243449','TRAIN') #SID 116
    add_station('SUMMERSTON','55.89883','-4.291531','TRAIN') #SID 117
    add_station('THORNLIEBANK','55.81109','-4.311701','TRAIN') #SID 118
    add_station('THORNTONHALL','55.768688','-4.251171','TRAIN') #SID 119
    add_station('UDDINGSTON','55.823532','-4.086712','TRAIN') #SID 120
    add_station('WEST CALDER','55.853794','-3.566999','TRAIN') #SID 121
    add_station('WESTER HAILES','55.91432','-3.284349','TRAIN') #SID 122
    add_station('WISHAW','55.772052','-3.92641','TRAIN') #SID 123

    # ADD IN BUS ROUTE NAMES

    add_route('2','BAILIESTON','FAIFLEY','') #RID 1
    add_route('2','FAIFLEY','BAILIESTON','') #RID 2
    add_route('3','GOVAN','DRUMCHAPEL','') #RID 3
    add_route('3','DRUMCHAPEL','GOVAN','') #RID 4
    add_route('6A','GLASGOW','DRUMCHAPEL','') #RID 5
    add_route('61','SUMMERSTON','SANDYHILLS','') #RID 6
    add_route('61','SANDYHILLS','SUMMERSTON','') #RID 7

    # ADD IN TRAIN ROUTE NAMES

    add_route('','GLASGOW CENTRAL','EDINBURGH','CARLUKE') #RID 8
    add_route('','GLASGOW QUEEN STREET','HELENSBURGH CENTRAL','') #RID 9
    add_route('','GLASGOW','AIRDRIE','') #RID 10
    add_route('','GLASGOW QUEEN STREET','EDINBURGH','FALKIRK HIGH') #RID 11
    add_route('','GLASGOW CENTRAL','EDINBURGH','SHOTTS') #RID 12
    add_route('','GLASGOW CENTRAL','NEWTON','') #RID 13
    add_route('','GLASGOW CENTRAL','EAST KILBRIDE','') #RID 14
    add_route('','GLASGOW QUEEN STREET','ANNIESLAND','MARYHILL') #RID 15
    add_route('','GLASGOW CENTRAL','PAISLEY CANAL','') #RID 16

    # BUILD THE BUS ROUTES

    #RID 1
    add_routestations(1,34)
    add_routestations(1,35)
    add_routestations(1,31)
    add_routestations(1,32)
    add_routestations(1,21)
    add_routestations(1,12)
    add_routestations(1,38)
    add_routestations(1,39)
    add_routestations(1,40)

    #RID2
    add_routestations(2,41)
    add_routestations(2,7)
    add_routestations(2,28)
    add_routestations(2,1)
    add_routestations(2,2)
    add_routestations(2,19)
    add_routestations(2,9)
    add_routestations(2,33)
    add_routestations(2,10)

    #RID3
    add_routestations(3,22)
    add_routestations(3,12)
    add_routestations(3,15)
    add_routestations(3,3)
    add_routestations(3,4)
    add_routestations(3,5)

    #RID4
    add_routestations(4,29)
    add_routestations(4,30)
    add_routestations(4,24)
    add_routestations(4,25)
    add_routestations(4,27)
    add_routestations(4,36)
    add_routestations(4,20)

    #RID5
    add_routestations(5,6)
    add_routestations(5,8)
    add_routestations(5,37)
    add_routestations(5,14)
    add_routestations(5,16)

    #RID6
    add_routestations(6,23)
    add_routestations(6,26)
    add_routestations(6,28)
    add_routestations(6,1)
    add_routestations(6,2)
    add_routestations(6,19)
    add_routestations(6,9)
    add_routestations(6,33)
    add_routestations(6,10)

    #RID7
    add_routestations(7,34)
    add_routestations(7,35)
    add_routestations(7,31)
    add_routestations(7,32)
    add_routestations(7,21)
    add_routestations(7,11)
    add_routestations(7,13)
    add_routestations(7,17)
    add_routestations(7,18)


    # BUILD THE TRAIN ROUTES

    #RID8
    add_routestations(8,81)
    add_routestations(8,104)
    add_routestations(8,123)
    add_routestations(8,56)
    add_routestations(8,58)
    add_routestations(8,86)
    add_routestations(8,75)

    #RID9
    add_routestations(9,82)
    add_routestations(9,59)
    add_routestations(9,107)
    add_routestations(9,90)
    add_routestations(9,102)
    add_routestations(9,70)
    add_routestations(9,71)
    add_routestations(9,46)
    add_routestations(9,87)

    #RID10
    add_routestations(10,82)
    add_routestations(10,88)
    add_routestations(10,47)
    add_routestations(10,57)
    add_routestations(10,114)
    add_routestations(10,78)
    add_routestations(10,74)
    add_routestations(10,50)
    add_routestations(10,62)
    add_routestations(10,63)
    add_routestations(10,43)

    #RID11
    add_routestations(11,82)
    add_routestations(11,49)
    add_routestations(11,97)
    add_routestations(11,68)
    add_routestations(11,76)
    add_routestations(11,111)
    add_routestations(11,98)
    add_routestations(11,86)
    add_routestations(11,75)

    #RID12
    add_routestations(12,81)
    add_routestations(12,54)
    add_routestations(12,120)
    add_routestations(12,48)
    add_routestations(12,89)
    add_routestations(12,55)
    add_routestations(12,61)
    add_routestations(12,84)
    add_routestations(12,115)
    add_routestations(12,77)
    add_routestations(12,51)
    add_routestations(12,42)
    add_routestations(12,121)
    add_routestations(12,99)
    add_routestations(12,95)
    add_routestations(12,69)
    add_routestations(12,122)
    add_routestations(12,93)
    add_routestations(12,116)
    add_routestations(12,86)
    add_routestations(12,75)

    #RID13
    add_routestations(13,81)
    add_routestations(13,110)
    add_routestations(13,101)
    add_routestations(13,113)
    add_routestations(13,108)
    add_routestations(13,96)
    add_routestations(13,92)
    add_routestations(13,65)
    add_routestations(13,52)
    add_routestations(13,94)
    add_routestations(13,105)

    #RID14
    add_routestations(14,81)
    add_routestations(14,67)
    add_routestations(14,109)
    add_routestations(14,118)
    add_routestations(14,79)
    add_routestations(14,60)
    add_routestations(14,53)
    add_routestations(14,119)
    add_routestations(14,83)
    add_routestations(14,73)

    #RID15
    add_routestations(15,82)
    add_routestations(15,45)
    add_routestations(15,112)
    add_routestations(15,80)
    add_routestations(15,117)
    add_routestations(15,100)
    add_routestations(15,91)
    add_routestations(15,44)

    #RID16
    add_routestations(16,81)
    add_routestations(16,72)
    add_routestations(16,64)
    add_routestations(16,103)
    add_routestations(16,66)
    add_routestations(16,85)
    add_routestations(16,106)

