import pytest
from lib.diary import Diary

'''
On initialization
diary_entries is empty
'''
def test_diary_entries_is_empty_on_initialisation():
    diary = Diary()

    actual = diary.all()

    expected = []

    assert actual == expected

'''
For count_words if no entries have been added 
returns 0
'''
def test_count_words_returns_zero_with_no_entries():
    diary = Diary()

    actual = diary.count_words()

    expected = 0

    assert actual == expected

'''
For reading time if no entries have been added 
returns 0
'''
def test_reading_time_returns_zero_with_no_entries():
    diary = Diary()

    actual = diary.reading_time(1)

    expected = 0

    assert actual == expected


'''
for reading_time and wpm is not int
throws error
'''
def test_reading_time_wpm_not_integer():
    diary = Diary()

    with pytest.raises(TypeError) as err:
        diary.reading_time("three")

    error_message = str(err.value)

    expected = "wpm must be an integer."

    assert error_message == expected

'''
for find_best_entries and diary_entries is empty
returns None
'''
def test_no_entries_find_best_entry_returns_none():
    diary = Diary()

    actual =  diary.find_best_entry_for_reading_time(10, 1)

    expected = None

    assert actual == expected

'''
for find_best_entry_for_reading_time and wpm is not int
throws error
'''
def test_best_entry_time_wpm_not_integer():
    diary = Diary()

    with pytest.raises(TypeError) as err:
        diary.find_best_entry_for_reading_time("three" ,1)

    error_message = str(err.value)

    expected = "wpm and minutes must be integers."

    assert error_message == expected

    '''
for find_best_entry_for_reading_time and wpm is not int
throws error
'''
def test_best_entry_minutes_not_integer():
    diary = Diary()

    with pytest.raises(TypeError) as err:
        diary.find_best_entry_for_reading_time(10, [1])

    error_message = str(err.value)

    expected = "wpm and minutes must be integers."

    assert error_message == expected


