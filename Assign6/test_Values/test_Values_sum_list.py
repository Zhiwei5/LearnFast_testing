def test_sum_list():
    """
    Tests the sum_list function in the class Values
    """
    try:
        import pytest
        from values import Values
        from list_module.sum_list import (sum_list, EmptyError)
    except ImportError as e:
        print("Necessary imports failed")
        return
    test_data1 = ([1, 1, 1, 1])
    test_data2 = [0,0]
    test_data3 = [5,-1-10]
    test_data4 = [-9, -4]
    test_answer1 = 4
    test_answer2 = 0
    test_answer3 = -6
    test_answer4 = -13
    output1 = Values(test_data1)
    output2 = Values(test_data2)
    output3 = Values(test_data3)
    output4 = Values(test_data4)
    assert test_answer1 == output1.sum_l
    assert test_answer2 == output2.sum_l
    assert test_answer3 == output3.sum_l
    assert test_answer4 == output4.sum_l
    with pytest.raises(EmptyError):
        Values([])
    with pytest.raises(ValueError):
        Values([float('inf'), 2])
    with pytest.raises(ValueError):
        Values([float('-inf'), 3.0])