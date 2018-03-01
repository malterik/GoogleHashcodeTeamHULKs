from functools import reduce


def distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def score_vehicle(city, vehicle):
    total_points = 0
    t = 0

    for ride in vehicle.ride_queue:
        # durations
        duration_drive_to_start = distance(ride.start_from, vehicle.current_position)
        duration_ride = distance(ride.start_from, ride.end_at)
        is_punctual = t + duration_drive_to_start <= ride.earliest_start

        # update state
        t = t + duration_ride + duration_drive_to_start
        vehicle.current_position = ride.end_at

        # calculate points per ride
        ride_points = duration_ride
        if is_punctual:
            ride_points = ride_points + city.bonus

        print("Ride %s = %s pts." % (ride.id, ride_points))

        # add to points
        total_points = total_points + ride_points

    return total_points


def score_solution(city):
    total_score = 0
    for vehicle in city.vehicles:
        total_score += score_vehicle(city, vehicle)

    return total_score