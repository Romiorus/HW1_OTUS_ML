def get_least(*args):
    return min(el for el in args if el >= 0)


def test_success_get_least():
    args = [0, 1, 2, 3]
    result = get_least(*args)
    exp_result = 0
    assert result == exp_result, 'fail success_get_least'


def test_success_get_least_2():
    args = [-1, 0, 1, 2, 3]
    result = get_least(*args)
    exp_result = 0
    assert result == exp_result


def test_fail_get_least():
    args = ['-1', '0', 1, 2, 3]
    # args = [-1, 0, 1, 2, 3]
    try:
        get_least(*args)
    except TypeError:
        pass
    else:
        raise Exception('no exception raised')


test_success_get_least()
test_success_get_least_2()
test_fail_get_least()
