# File: lib/diary.py

class Diary:
    def __init__(self):
        self._diary_entries = []

    def add(self, entry):
        self._diary_entries.append(entry)

    def all(self):
        return self._diary_entries

    def count_words(self):
        return sum(entry.count_words() for entry in self._diary_entries)

    def reading_time(self, wpm):
        if not isinstance(wpm , int):
            raise TypeError("wpm must be an integer.")
        return int(round(self.count_words() / wpm, 0))
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        if not isinstance(wpm , int) or not isinstance(minutes , int):
            raise TypeError("wpm and minutes must be integers.")
        
        max_readable_words = wpm * minutes

        # Find entries that can be read within the time limit
        suitable_entries = [
            entry for entry in self._diary_entries 
            if entry.count_words() <= max_readable_words
        ]

        if not suitable_entries:
            return None

        # Return the entry with the highest word count that still fits
        return max(suitable_entries, key=lambda entry: entry.count_words())


