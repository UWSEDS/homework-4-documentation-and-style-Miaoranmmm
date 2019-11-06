"""
This module contains 4 tests, including:
1. Check that the dataframe statisfies that
    (1)it contains only specified columns
    (2)the values in each column have the same python type
    (3)there are at least 10 rows in the dataframe.
2. Check that all columns have values of the corect type.
3. Check for nan values.
4. Verify that the dataframe has at least one row.
"""

def test_create_dataframe(df_test, columns):
    """
    This function can check that the dataframe statisfies that
        (1)it contains only specified columns
        (2)the values in each column have the same python type
        (3)there are at least 10 rows in the dataframe.
    Input: DataFrame, specified columns
    Output: Boolean value (If dataframe satisfies the requirement,
        then return True, otherwise return False)
    """
    df_col = list(df_test)
    # check that the dataframe contains only specified columns
    if df_col != columns:
        return False
    # check that there are at least 10 rows in the dataframe
    if df_test.shape[0] < 10:
        return False
    # check that the values in each column have the same python type
    for col in df_col:
        types = []
        for element in list(df_test[col]):
            types.append(type(element))
        if len(set(list(types))) == 1:
            continue
        else:
            return False

def detect_nan_values(df_test):
    """
    This function can check for nan values
    Input: dataframe
    Output: Boolean value (If the dataframe does not have nan values,
        then return True, otherwise return False)
    """
    if df_test.isnull().values.any():
        return False
    return True

def check_more_than_one_row(df_test):
    """
    This function can verify that the dataframe has at least one row
    Input: dataframe
    Output: Boolean value (If the dataframe has at least one row,
        then return True, otherwise return False)
    """
    if df_test.shape[0] < 1:
        return False
    return True

def check_type(df_test):
    """
    This function can check that all columns have values of the corect type
    Input: dataframe
    Output: Boolean value (If all columns have values of the corect type,
        then return True, otherwise return False)
    """
    df_col = list(df_test)
    for col in df_col:
        types = []
        for element in list(df_test[col]):
            types.append(type(element))
        if len(set(list(types))) == 1:
            continue
        else:
            return False
    return True


def test_data_type(df_test):
    """Test check_type function"""
    assert check_type(df_test)
def test_nan_value(df_test):
    """Test detect_nan_values function"""
    assert detect_nan_values(df_test)
def test_more_than_one_row(df_test):
    """Test test_more_than_one_row function"""
    assert check_more_than_one_row(df_test)
