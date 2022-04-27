from sum import sum_self_made as sm


def test_sum():
    result = sm([2, 3, 5])
    assert result == 10, "should be 10"


if __name__ == "__main__":
    test_sum()
    print("Everything passed")