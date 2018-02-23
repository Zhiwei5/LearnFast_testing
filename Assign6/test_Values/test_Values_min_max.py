def test_min_max_list():
    """
    Tests the min_max in class Values
    """
    try:
        import pytest
        from values import Values
    except ImportError:
        print("Necessary imports for this test function failed")
        return
    test_data1 = [0, -3, -1.2, 10]
    test_data2 = [1, 3, 2, 5]
    test_data3 = [-3/2, -9, -3, -7, -1]
    test_answer1 = (-3, 10)
    test_answer2 = (1, 5)
    test_answer3 = (-9, -1)
    output1 = Values(test_data1)
    output2 = Values(test_data2)
    output3 = Values(test_data3)
    assert test_answer1 == output1.max_mi
    assert test_answer2 == output2.max_mi
    assert test_answer3 == output3.max_mi
    with pytest.raises(TypeError):
        Values(5)
    with pytest.raises(TypeError):
        Values('abc')
    with pytest.raises(TypeError):
        Values({1: 4})
    with pytest.raises(ValueError):
        Values(['s', 's'])
    with pytest.raises(ValueError):
        Values(['-inf', 5])
    with pytest.raises(ValueError):
        Values(['+inf', 5])
    with pytest.raises(ValueError):
        Values([float('inf'), 5])
    with pytest.raises(ValueError):
        Values([float('-inf'), 5])