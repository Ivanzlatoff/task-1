def direction(facing, turn):
    # your smart code here

    direction_dict = {
        'N' : 0,
        'NE' : 45,
        'E' : 90,
        'SE' : 135,
        'S' : 180,
        'SW' : 225,
        'W' : 270,
        'NW' : 315
    }
    
    if turn < -1080 or turn > 1080:
        raise Exception("Sorry, the turn must be between -1080 and 1080 degrees")

    if turn % 45 != 0:
        raise Exception("Sorry, degrees must be integers evenly divisible on 45")
    
    new_degree = direction_dict[facing] + turn
    processed_degree = new_degree % 360

    directions = list(direction_dict.keys())
    degress = list(direction_dict.values())

    return(directions[degress.index(processed_degree)])



        