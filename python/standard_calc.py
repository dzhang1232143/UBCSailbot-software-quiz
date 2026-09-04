def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """
    while angle < -180:
        angle += 360
    while angle >= 180:
        angle -= 360
    return angle

def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """
    dif_angle_between = abs(bound_to_180(first_angle - second_angle))
    dif_angle_from_first = abs(bound_to_180(first_angle - middle_angle))
    dif_angle_from_second = abs(bound_to_180(second_angle - middle_angle))
    return dif_angle_from_first + dif_angle_from_second <= dif_angle_between