def shortestDetour(points):
    """Calculate the detour distance between two different rides. 

    Given four latitude / longitude pairs, where driver one is traveling 
    from point A to point B and driver two is traveling from point C to point D, 
    write a function (in your language of choice) to calculate the shorter of the 
    detour distances the drivers would need to take to pick-up and drop-off the other driver.
    """

    trip_a_start, trip_a_stop, trip_b_start, trip_b_stop = points
    print trip_a_start, trip_a_stop, trip_b_start, trip_b_stop

shortestDetour([(3, 5), (2, 4), (5, 8), (7, 9)])