'''
1. Line-position estimation: Given five calibrated, non-negative sensor readings at positions [-2,
-1, 0, 1, 2] , compute the weighted centroid to estimate line position. Handle the all-zero
case explicitly.
'''

sensor_positions = [-2, -1, 0, 1, 2] #im assuming these are actually 1 unit apart if not we can make necessary changes in the code too

dist_bw_sensors = abs(sensor_positions[1] - sensor_positions[0])

sensor_readings = [0, 0, 1, 2, 4]  #non negetive sensor readings basically suppose these .... necessary changes can be made afterwards

def weighted_centroid_func(position, reading):
    zipped_both = tuple(zip(position, reading))
    temp_numerator = 0
    for a, b in zipped_both:
        temp_numerator += a * b
    if sum(reading) != 0:
        weighted_centroid = temp_numerator / sum(reading)
        return weighted_centroid
    elif sum(reading) == 0:
        return None

def kiske_paas_he(weighted, sensor):
    if weighted == None:
        return None
    else:
        for i in sensor:
            if abs(weighted - i) <= dist_bw_sensors/2:
                return i
            else:
                continue


print(f'''The weighted centroid is {weighted_centroid_func(sensor_positions, sensor_readings)}, and the line basically is closer to the sensor {kiske_paas_he(weighted_centroid_func(sensor_positions, sensor_readings), sensor_positions)}''')

'''
This will work for all evenly spaces sensors and whenever their readings are positive basically
'''




'''
My 2 cents to this ..

In this project .. the ir sensors will give ouptut as only higs and low or 0 / 1 in binary basically
say one output case [0, 0, 1, 1, 0] --- is one case .. with this we can defnitely say that the line is somewhere between
the sensor 0 and 1 but exactly where we cannot say .. and my the weighted mean formula gives us the mean to
be 0.5 which says the line is exactly in between sensor 0 and 1 .. which may not be the case .. 
only if the reading is like say [0, 0, 1, 0, 0] .. i.e the line is exactly below sensor 0 .. ands here the
weighted mean also gives 0 .. which corresponds to the actual things 

so basically what i mean to say is until the data/ sensor readings  is not just 0 and 1  but in discrete
values like the example i took .. the weighted mean can make very accurate prdictions .. if not ..then
it can still make predictions .. but may not be very very accurate .. but can be usable ig??
'''