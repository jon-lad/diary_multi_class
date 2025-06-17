from lib.diary import Diary
from lib.dairy_entry import DiaryEntry

'''
Given multiple diary entries
all returns a list of those entries
'''
def test_after_adding_diary_entries_all_returns_list_of_entries():
    diary = Diary()

    diary_entry_1 = DiaryEntry("Title1", "Contents1")
    diary_entry_2 = DiaryEntry("Title2", "Contents2")

    diary.add(diary_entry_1)
    diary.add(diary_entry_2)

    actual = diary.all()

    expected = [diary_entry_1, diary_entry_2]

    assert actual == expected

#Testing count_words

'''
Given multiple diary entries
count_words returns the amount of words
'''
def test_count_words_in_all_entries():
    diary = Diary()

    diary_entry_1 = DiaryEntry("Title1", "one two")
    diary_entry_2 = DiaryEntry("Title2", "one two three")

    diary.add(diary_entry_1)
    diary.add(diary_entry_2)

    actual = diary.count_words()

    expected = 5

    assert actual == expected

'''
Given multiple diary entries including empty ones
count_words returns the amount of words
'''
def test_count_words_in_all_entries_including_empty():
    diary = Diary()

    diary_entry_1 = DiaryEntry("Title1", "one two")
    diary_entry_2 = DiaryEntry("Title2", "")

    diary.add(diary_entry_1)
    diary.add(diary_entry_2)

    actual = diary.count_words()

    expected = 2

    assert actual == expected

#Testing reading_time

'''
Given multiple diary entries
reading time estimates the amount of time to read all entries
'''
def test_reading_time_for_all_entries():
    diary = Diary()

    text_1 = " ".join(["word"] * 50)
    text_2 = " ".join(["word"] * 150)

    diary_entry_1 = DiaryEntry("Title1", text_1)
    diary_entry_2 = DiaryEntry("Title2", text_2)

    diary.add(diary_entry_1)
    diary.add(diary_entry_2)

    actual = diary.reading_time(200)

    expected = 1

    assert actual == expected

'''
Given multiple diary entries and wpm so that readingtime has a fractional part
greater than half
rounds up the estimate
'''
def test_reading_time_for_fractional_length_greater_than_half():
    diary = Diary()

    text_1 = " ".join(["word"] * 50)
    text_2 = " ".join(["word"] * 150)

    diary_entry_1 = DiaryEntry("Title1", text_1)
    diary_entry_2 = DiaryEntry("Title2", text_2)

    diary.add(diary_entry_1)
    diary.add(diary_entry_2)

    actual = diary.reading_time(300)

    expected = 1

    assert actual == expected

    '''
Given multiple diary entries and wpm so that readingtime has a fractional part
less than half
rounds down the estimate
'''
def test_reading_time_for_fractional_length_less_than_half():
    diary = Diary()

    text_1 = " ".join(["word"] * 50)
    text_2 = " ".join(["word"] * 150)

    diary_entry_1 = DiaryEntry("Title1", text_1)
    diary_entry_2 = DiaryEntry("Title2", text_2)

    diary.add(diary_entry_1)
    diary.add(diary_entry_2)

    actual = diary.reading_time(150)

    expected = 1

    assert actual == expected

'''
Given multiple empty diary entries
reading time estimates the amount of time to be 0
'''
def test_reading_time_for_empty_entries():
    diary = Diary()

    text_1 = ""
    text_2 = ""

    diary_entry_1 = DiaryEntry("Title1", text_1)
    diary_entry_2 = DiaryEntry("Title2", text_2)

    diary.add(diary_entry_1)
    diary.add(diary_entry_2)

    actual = diary.reading_time(200)

    expected = 0

    assert actual == expected

#Testing find_best_entry_for_reading_time

'''
Given multiple diary entries
find_best_entry_for_reading_time returns the entry with the closest match
to reading time
'''
def test_get_best_entry_for_reading_time():
    diary = Diary()

    text_1 = " ".join(["word"] * 150)
    text_2 = " ".join(["word"] * 50)
    text_3 = " ".join(["word"] * 90)
    text_4 = " ".join(["word"] * 70)

    diary_entry_1 = DiaryEntry("Title1", text_1)
    diary_entry_2 = DiaryEntry("Title2", text_2)
    diary_entry_3 = DiaryEntry("Title3", text_3)
    diary_entry_4 = DiaryEntry("Title4", text_4)

    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    diary.add(diary_entry_4)

    actual = diary.find_best_entry_for_reading_time(100, 1)

    expected = diary_entry_3

    assert actual == expected

'''
Given multiple unsuitable diary entries
returns None
'''
def test_no_suitable_entries_for_reading_time():
    diary = Diary()

    text_1 = " ".join(["word"] * 150)
    text_2 = " ".join(["word"] * 250)
    text_3 = " ".join(["word"] * 101)
    text_4 = " ".join(["word"] * 120)

    diary_entry_1 = DiaryEntry("Title1", text_1)
    diary_entry_2 = DiaryEntry("Title2", text_2)
    diary_entry_3 = DiaryEntry("Title3", text_3)
    diary_entry_4 = DiaryEntry("Title4", text_4)

    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    diary.add(diary_entry_4)

    actual = diary.find_best_entry_for_reading_time(100, 1)

    expected = None

    assert actual == expected

'''
Given multiple equally good diary entries
find_best_entry_for_reading_time returns the first entry with the closest match
'''
def test_get_best_entry_for_equally_good_entries():
    diary = Diary()

    text_1 = " ".join(["word"] * 150)
    text_2 = " ".join(["word"] * 90)
    text_3 = " ".join(["word"] * 90)
    text_4 = " ".join(["word"] * 70)

    diary_entry_1 = DiaryEntry("Title1", text_1)
    diary_entry_2 = DiaryEntry("Title2", text_2)
    diary_entry_3 = DiaryEntry("Title3", text_3)
    diary_entry_4 = DiaryEntry("Title4", text_4)

    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    diary.add(diary_entry_4)

    actual = diary.find_best_entry_for_reading_time(100, 1)

    expected = diary_entry_2

    assert actual == expected
    