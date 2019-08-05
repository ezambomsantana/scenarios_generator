# simtrip: methods for generate and manipulate trips for InterSCSimulator
import numpy as np

# Generates trips between 'origin' and 'destination' (starting at 'link_origin')
# distributed uniformly during 'time_span_seconds', starting at 'time_offset_seconds'
def generate_trips_uniform(name, origin, destination, link_origin, time_span_seconds, cars_per_hour, time_offset_seconds=3600, cars_per_trip=1, digital_rails_capable='false'):
  total_trips = int((time_span_seconds / 3600) * cars_per_hour)
  start_times = np.sort(np.random.randint(time_span_seconds, size=total_trips))

  return _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds, digital_rails_capable, 'car')
  

# Generates trips between 'origin' and 'destination' (starting at 'link_origin')
# in convoys during 'time_span_seconds', starting at 'time_offset_seconds'
# 'cycle_seconds' is the traffic signals cycle duration
def generate_trips_convoy(name, origin, destination, link_origin, cycle_seconds, time_span_seconds, cars_per_hour, time_offset_seconds=3600, cars_per_trip=1):
  if cars_per_trip == 0:
    return []
  
  total_trips = int((time_span_seconds / 3600) * cars_per_hour / cars_per_trip)
  start_times = np.sort(np.random.randint(time_span_seconds, size=total_trips))

  return _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds, 'true','car')

def generate_trips_convoy_dr(name, origin, destination, link_origin, cycle_seconds, time_span_seconds, cars_per_hour, time_offset_seconds=3600, cars_per_trip=1):
  if cars_per_trip == 0:
    return []

  if cars_per_hour == 0:
    return []
  
  start_times = list(range(0, cars_per_hour * time_offset_seconds, time_offset_seconds))

  return _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds, 'true', 'platoon')


def _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds, digital_rails_capable, type):
  generated = 0
  trips = []

  for start_time in start_times:
    trip = (name + str(generated), origin, destination, link_origin, cars_per_trip, time_offset_seconds + start_time, type, digital_rails_capable)
    trips.append(trip)

    generated += 1

  return trips


def trip_to_xml(trip):
  return '<trip name="{}" origin="{}" destination="{}" link_origin="{}" count="{}" start="{}" mode="{}" digital_rails_capable="{}"/>'.format(*trip)
