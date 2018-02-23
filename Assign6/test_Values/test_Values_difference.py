def test_difference():
    """
    To test the max_difference function in the class Values
    """
    try:
        import pytest
        from values import Values
    except ImportError:
        print("The necessary module for this test failed to import")
        return
    test_data1 = [1, 5, 6, 7, 12]
    test_data2 = [3, 4, 5, 56, 45]
    test_data3 = [6, 34, 23, 45, 57]

    output1 = Values(test_data1)
    output2 = Values(test_data2)
    output3 = Values(test_data3)

    assert output1.max_diff == 5
    assert output2.max_diff == 51
    assert output3.max_diff == 28
    with pytest.raises(TypeError):
        Values(2)
    with pytest.raises(ValueError):
        Values(['inf', 3, 4.0])
    with pytest.raises(ValueError):
        Values(['-inf', 3, 4.0])
    with pytest.raises(ValueError):
        Values([float('-inf'), 3, 4.0])
    with pytest.raises(ValueError):
        Values([float('inf'), 3, 4.0])