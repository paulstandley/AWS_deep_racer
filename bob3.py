def reward_function(params):
    '''
    rewarding the agent, wheels on track, follow center line, STEERING THRESHOLD
    '''    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    #steering = abs(params['steering_angle']) # Only need the absolute steering angle
    # Give a very low reward by default
    reward = 1e-3
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.3 * track_width
    marker_3 = 0.6 * track_width
    
    # Give a high reward if no wheels go off the track and
    # Give higher reward if the car is closer to center line and vice versa
    
    if all_wheels_on_track:
        if distance_from_center <= marker_1:
            reward = 1.0
        elif distance_from_center <= marker_2:
            reward = 0.1
        elif distance_from_center <= marker_3:
            reward = 0.01
    else:
        reward = 1e-3  # did crashed/ wheels off track
        
    # Steering penality threshold, change the number based on your action space setting
    #ABS_STEERING_THRESHOLD = 20

    # Penalize reward if the agent is steering too much
    #if steering > ABS_STEERING_THRESHOLD:
    #    reward *= 0.6
            
    return float(reward)