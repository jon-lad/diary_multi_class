import pytest
from lib.dairy_entry import DiaryEntry

#Test class is intialized

'''
On initialization
Title is set
'''
def test_title_is_set_on_initialisation():
    diary_entry = DiaryEntry("Title", "Contents")

    actual = diary_entry.title

    expected = "Title"

    assert actual == expected

'''
On initialization
Test contents are set
'''
def test_contents_are_set_on_initialisation():
    diary_entry = DiaryEntry("title", "Contents")

    actual = diary_entry.contents

    expected = "Contents"

    assert actual == expected

'''
Given non string title
throws an error
'''
def test_none_string_title_raises_error():
    with pytest.raises(TypeError) as err:
        diary_entry = DiaryEntry(None , "hello")
    
    error_message = str(err.value)

    expected = ("Diary entry title and contents must be strings.")

    assert error_message == expected

'''
Given non string contents 
throws an error
'''
def test_none_string_contents_raises_error():
    with pytest.raises(TypeError) as err:
        diary_entry = DiaryEntry("title", ["hello"])
    
    error_message = str(err.value)

    expected = ("Diary entry title and contents must be strings.")

    assert error_message == expected

#Testing count_words

'''
Given some contents
Test count_words returns the amount of words
'''
def test_count_words_counts_words():

    diary_entry = DiaryEntry("title", "one two three four five six")

    actual = diary_entry.count_words()

    expected = 6

    assert actual == expected

'''
Given an empty string
count_words returns 0
'''
def test_empty_string_returns_zero():

    diary_entry = DiaryEntry("title", "")

    actual = diary_entry.count_words()

    expected = 0

    assert actual == expected

#Testing reading_time

'''
Given some contents
reading_time returns an estimate of the time to read in minutes
'''
def test_reading_gives_estimate():

    text = "word" + " word" * 99

    diary_entry = DiaryEntry("title", text)

    actual = diary_entry.reading_time(50)

    expected = 2

    assert actual == expected

'''
Given contents and wpm so reading time has frational part greater than half 
reading_time rounds up to 2 minute
'''
def test_fractional_reading_time_is_rounded_down():

    text = " ".join(["word"] * 3)

    diary_entry = DiaryEntry("title", text)

    actual = diary_entry.reading_time(2)

    expected = 2

    assert actual == expected

'''
Given one word and a wpm of 1
reading_time returns an estimate of 1 minutes
'''
def test_one_word_and_one_wpm_makes_reading_time_returns_one():

    text = "word"

    diary_entry = DiaryEntry("title", text)

    actual = diary_entry.reading_time(1)

    expected = 1

    assert actual == expected

'''
Given an empty string
reading_time returns an estimate of 0 minutes
'''
def test_empty_string_reading_time_returns_zero():

    text = ""

    diary_entry = DiaryEntry("title", text)

    actual = diary_entry.reading_time(1)

    expected = 0

    assert actual == expected

#testing reading_chunk

'''
Given a diary entry
Get a chunk of words that could be read in a set amont of time
'''
def test_reading_first_chunk():
    text = " ".join(['a'] * 10 + ['b'] * 10 + ['c'] * 10)

    diary_entry = DiaryEntry("Today", text)

    actual = diary_entry.reading_chunk(10, 1)

    chunk_text = " ".join(['a'] * 10)

    expected = chunk_text

    assert actual == expected 

'''
Given a short diary entry
Get all words
'''
def test_short_chunk_returns_all():
    text = "one two three"

    diary_entry = DiaryEntry("Today", text)

    actual = diary_entry.reading_chunk(10, 1)

    chunk_text = "one two three"

    expected = chunk_text

    assert actual == expected 

'''
Given an empty string
Get an empty string
'''
def test_empty_string_returns_empty():
    text = ""

    diary_entry = DiaryEntry("Today", text)

    actual = diary_entry.reading_chunk(10, 1)

    chunk_text = ""

    expected = chunk_text

    assert actual == expected 

'''
Given a diary entry
Get a chunk of words that could be read in a set amont of time
'''
def test_reading_last_chunk():
    text = " ".join(['a'] * 10 + ['b'] * 10 + ['c'] * 7)
    diary_entry = DiaryEntry("Today", text)

    diary_entry.reading_chunk(10, 1)
    diary_entry.reading_chunk(10, 1)
    actual = diary_entry.reading_chunk(10, 1)

    chunk_text = " ".join(['c'] * 7)

    expected = chunk_text

    assert actual == expected 

'''
Given a diary entry
Get a chunk of words that could be read in a set amont of time
'''
def test_reading_short_chunk_multiple_times():
    text = " ".join(['a'] * 7)
    diary_entry = DiaryEntry("Today", text)

    diary_entry.reading_chunk(10, 1)
    diary_entry.reading_chunk(10, 1)
    actual = diary_entry.reading_chunk(10, 1)

    chunk_text = " ".join(['a'] * 7)

    expected = chunk_text

    assert actual == expected 

'''
Given reading chunk called one more times than there are chunks
Get a first chunk
'''
def test_reading_over_last_chunk():
    text = " ".join(['a'] * 10 + ['b'] * 10 + ['c'] * 7)
    diary_entry = DiaryEntry("Today", text)

    diary_entry.reading_chunk(10, 1)
    diary_entry.reading_chunk(10, 1)
    diary_entry.reading_chunk(10, 1)
    actual = diary_entry.reading_chunk(10, 1)

    chunk_text = " ".join(['a'] * 10)

    expected = chunk_text

    assert actual == expected

'''
Given reading chunk called with new wpm
return the first chunk
'''
def test_reading_with_differnt_wpm():
    text = " ".join(['a'] * 10 + ['b'] * 10 + ['c'] * 7)
    diary_entry = DiaryEntry("Today", text)

    diary_entry.reading_chunk(10, 1)
    actual = diary_entry.reading_chunk(20, 1)

    chunk_text = " ".join(['a'] * 10 + ['b'] * 10)

    expected = chunk_text

    assert actual == expected

'''
Modifing the title to a non string 
throws an error
'''
def modifying_title_to_non_string_trows_error():
    diary_entry = DiaryEntry("title", "Contents")
    with pytest.raises(TypeError) as err:
        diary_entry.title = 3

    error_message = str(err.value)

    expected = ("Title must be a string.")

    assert error_message == expected

'''
Modifing the title to a non string 
throws an error
'''
def modifying_contents_to_non_string_trows_error():
    diary_entry = DiaryEntry("title", "Contents")
    with pytest.raises(TypeError) as err:
        diary_entry.contents = [1, "hello"]

    error_message = str(err.value)

    expected = ("Contents must be a string.")

    assert error_message == expected