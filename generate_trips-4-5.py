import sys
import simtrip
import math

from random import randrange

# Script that generates trips for Av. Paulista
# TODO: Document better

cycle = 1

for x in range(0,21):

  file1 = open("scenario-4-5/trips" + str(x) + ".xml","w") 
  file1.write("<scsimulator_matrix>\n")

  dr_ratio = 0.05 * x
  #float(sys.argv[1])

  paraiso_regular_cars = 2359 * (1-dr_ratio)
  paraiso_dr_cars = 2359 * dr_ratio
  paraiso_randon = 2359 * 0.3 * (1-dr_ratio)
  paraiso_randon_dr = 2359 * 0.3 * dr_ratio

  consolacao_regular_cars = 3067 * (1-dr_ratio)
  consolacao_dr_cars = 3067 * dr_ratio
  consolacao_randon = 3067 * 0.1 * (1-dr_ratio)
  consolacao_randon_dr = 3067 * 0.1 * dr_ratio

  par_nodes = [1953466363, 1953466367, 1990911135, 1990934598, 303863453, 60609874]
  par_links = [4341, 4345, 4349, 5498, 4390, 3357]

  cons_nodes = [60609811, 1953466378, 1990934597, 1990911134, 1953466375, 165459105]
  cons_links = [3346, 4343, 4360, 4355, 4408, 4410]

  num_dr_paraiso = int(math.ceil(paraiso_dr_cars / 30))
  num_dr_consolacao = int(math.ceil(consolacao_dr_cars / 30))

  interval_dr_paraiso = 0
  interval_dr_consolacao = 0

  if num_dr_paraiso > 0:
    interval_dr_paraiso = int(math.ceil(3600 / num_dr_paraiso))
    interval_dr_consolacao = int(math.ceil(3600 / num_dr_consolacao))

  print("NUM PAR: " + str(num_dr_paraiso))
  print("NUM CONS: " + str(num_dr_consolacao))
  print("INTER PAR: " + str(interval_dr_paraiso))
  print("INTER CONS: " + str(interval_dr_consolacao))

  paraiso_offset = cycle - 8 + 13  # Cycle time - time to get to first signalized intersection + start time
  consolacao_offset = cycle - 8 + 13

  # These link IDs can be generated differently for each osm -> matsim conversion.
  # The values hardcoded here match the network at the master branch of the scenarios repository
  paraiso_regular_trips = simtrip.generate_trips_uniform(
    name='paraiso_regular_', 
    origin='165466550', 
    destination='60609874', 
    link_origin='2105', 
    cars_per_trip=1, 
    time_span_seconds=3600, 
    time_offset_seconds=paraiso_offset, 
    cars_per_hour=paraiso_regular_cars
  )
  for trip_xml in map(simtrip.trip_to_xml, paraiso_regular_trips):
    file1.write(trip_xml + "\n")  

  for x in range(0, int(paraiso_randon)):
    origin = randrange(6)
    dest = randrange(6)
    while origin <= dest:
      origin = randrange(6)
      dest = randrange(6)
    paraiso_random_walk = simtrip.generate_trips_uniform(
      name='paraiso_random_walk_' + str(x), 
      origin=par_nodes[origin], 
      destination=par_nodes[dest], 
      link_origin=par_links[origin], 
      cars_per_trip=1, 
      time_span_seconds=3600, 
      time_offset_seconds=paraiso_offset, 
      cars_per_hour=1
    )
    for trip_xml in map(simtrip.trip_to_xml, paraiso_random_walk):
      file1.write(trip_xml + "\n")  

  for x in range(0, int(paraiso_randon_dr)):
    origin = randrange(6)
    dest = randrange(6)
    while origin <= dest:
      origin = randrange(6)
      dest = randrange(6)
    paraiso_random_walk_dr = simtrip.generate_trips_convoy(
      name='paraiso_random_walk_dr' + str(x), 
      origin=par_nodes[origin], 
      destination=par_nodes[dest], 
      link_origin=par_links[origin], 
      cycle_seconds=cycle,
      cars_per_trip=1, 
      time_span_seconds=3600, 
      time_offset_seconds=paraiso_offset, 
      cars_per_hour=1
    )
    for trip_xml in map(simtrip.trip_to_xml, paraiso_random_walk_dr):
      file1.write(trip_xml + "\n")        

  paraiso_dr_trips = simtrip.generate_trips_convoy_dr(
    name='paraiso_dr_', 
    origin='165466550', 
    destination='60609874', 
    link_origin='2105', 
    cycle_seconds=cycle,
    cars_per_trip=1, 
    time_span_seconds=3600, 
    time_offset_seconds=interval_dr_paraiso, 
    cars_per_hour=num_dr_paraiso
  )
  for trip_xml in map(simtrip.trip_to_xml, paraiso_dr_trips):
    file1.write(trip_xml + "\n")   

  consolacao_regular_trips = simtrip.generate_trips_uniform(
    name='consolacao_regular', 
    origin='60609959', 
    destination='1819616337', 
    link_origin='3345', 
    cars_per_trip=1, 
    time_span_seconds=3600, 
    time_offset_seconds=consolacao_offset, 
    cars_per_hour=consolacao_regular_cars
  )
  for trip_xml in map(simtrip.trip_to_xml, consolacao_regular_trips):
    file1.write(trip_xml + "\n")  

  for x in range(0, int(consolacao_randon)):
    origin = randrange(6)
    dest = randrange(6)
    while origin <= dest:
      origin = randrange(6)
      dest = randrange(6)
    consolacao_random_walk = simtrip.generate_trips_uniform(
      name='consolacao_random_walk_' + str(x), 
      origin=cons_nodes[origin], 
      destination=cons_nodes[dest], 
      link_origin=cons_links[origin], 
      cars_per_trip=1, 
      time_span_seconds=3600, 
      time_offset_seconds=paraiso_offset, 
      cars_per_hour=1
    )
    for trip_xml in map(simtrip.trip_to_xml, consolacao_random_walk):
      file1.write(trip_xml + "\n")  

  for x in range(0, int(consolacao_randon_dr)):
    origin = randrange(6)
    dest = randrange(6)
    while origin <= dest:
      origin = randrange(6)
      dest = randrange(6)
    consolacao_random_walk_dr = simtrip.generate_trips_convoy(
      name='consolacao_random_walk_dr' + str(x), 
      origin=cons_nodes[origin], 
      destination=cons_nodes[dest], 
      link_origin=cons_links[origin], 
      cycle_seconds=cycle,
      cars_per_trip=1, 
      time_span_seconds=3600, 
      time_offset_seconds=paraiso_offset, 
      cars_per_hour=1
    )
    for trip_xml in map(simtrip.trip_to_xml, consolacao_random_walk_dr):
      file1.write(trip_xml + "\n")          

  consolacao_dr_trips = simtrip.generate_trips_convoy_dr(
    name='consolacao_dr_', 
    origin='60609959', 
    destination='1819616337', 
    link_origin='3345',
    cycle_seconds=cycle, 
    cars_per_trip=1, 
    time_span_seconds=3600,     
    time_offset_seconds=interval_dr_consolacao, 
    cars_per_hour=num_dr_consolacao
  )
  for trip_xml in map(simtrip.trip_to_xml, consolacao_dr_trips):
    file1.write(trip_xml + "\n")   

  file1.write("</scsimulator_matrix>")
  file1.close()