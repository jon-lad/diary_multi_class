from lib.diary import Diary
from lib.dairy_entry import DiaryEntry

diary = Diary()
text_1 = " ".join(["word" * 150])
text_2 = " ".join(["word" * 90])
text_3 = " ".join(["word" * 90])
text_4 = " ".join(["word" * 70])

diary_entry_1 = DiaryEntry("Title1", text_1)
diary_entry_2 = DiaryEntry("Title2", text_2)
diary_entry_3 = DiaryEntry("Title3", text_3)
diary_entry_4 = DiaryEntry("Title4", text_4)

diary.add(diary_entry_1)
diary.add(diary_entry_2)
diary.add(diary_entry_3)
diary.add(diary_entry_4)

diary.find_best_entry_for_reading_time(100, 1)