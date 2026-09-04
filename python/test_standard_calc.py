from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """

def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(1) == 1
    assert bound_to_180(-1) == -1
    assert bound_to_180(-12.5) == -12.5
    assert bound_to_180(12.5) == 12.5
    assert bound_to_180(135) == 135.0
    assert bound_to_180(200) == -160.0

def test_bound_boundary1():
    assert bound_to_180(180) == -180
    assert bound_to_180(181) == -179
    assert bound_to_180(179) == 179
    assert bound_to_180(540) == -180
    assert bound_to_180(541) == -179
    assert bound_to_180(539) == 179

def test_bound_boundary2():
    assert bound_to_180(-180) == -180
    assert bound_to_180(-181) == 179
    assert bound_to_180(-179) == -179
    assert bound_to_180(-540) == -180
    assert bound_to_180(-541) == 179
    assert bound_to_180(-539) == -179

def test_bound_multiple_revo1():
    assert bound_to_180(20 + 4 * 360) == 20
    assert bound_to_180(-45 + 7 * 360) == -45
    assert bound_to_180(-540 - 90 * 360) == -180

""" Tests for is_angle_between() """

def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert is_angle_between(0, 45, 90)
    assert is_angle_between(90, 45, 0)
    assert not is_angle_between(0, 45, -90)

def test_between_bounds1():
    assert is_angle_between(0, 67, 180)
    assert not is_angle_between(0, 67, 181)
    assert is_angle_between(0, 67, 179)
    assert is_angle_between(1, 67, 180)
    assert not is_angle_between(-1, 67, 181)

def test_between_bounds2():
    assert is_angle_between(35, 36, 200)
    assert is_angle_between(35, 35, 200)
    assert not is_angle_between(35, 34, 200)
    assert is_angle_between(35, 199, 200)
    assert is_angle_between(35, 200, 200)
    assert not is_angle_between(35, 201, 200)

def test_between_large_vals1():
    assert is_angle_between(-160, 2, -355)
    assert not is_angle_between(5404, -3030, 6000)
    assert not is_angle_between(6002, 6003, 6000)
    assert is_angle_between(-98982, -24413, 23909)
    assert is_angle_between(-22295, -50068, -28866)