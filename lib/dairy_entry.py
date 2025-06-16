import math

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        if not isinstance(title, str) or not isinstance(contents, str):
            raise TypeError("Diary entry title and contents must be strings.")
        self._title = title
        self._contents = contents
        self._words = contents.split()
        self._current_chunk_index = 0
        self._last_chunk_size = 0

    #if title is modified we need to make sure it is updated with 
    # a string so it is set to a property
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        self._title = title
    
    #If contents is modified we need to update self._words and
    #_current_chunk_index so is set as a property
    @property
    def contents(self):
        return self._contents
    
    @contents.setter
    def contents(self, contents):
        if not isinstance(contents, str):
            raise TypeError("Contents must be a string")
        self._contents = contents
        self._words = contents.split()
        self._current_chunk_index = 0

    #Methods:

    def count_words(self):
        return len(self._words)

    def reading_time(self, wpm):
        return int(round(self.count_words() / wpm, 0))
        

    def reading_chunk(self, wpm, minutes):
        chunk_size = wpm * minutes

        #If called with a new chunk_size reset the index
        if self._last_chunk_size != chunk_size:
            self._current_chunk_index = 0
        self._last_chunk_size = chunk_size

        total_chunks = math.ceil(self.count_words() / chunk_size)
        chunk_start = self._current_chunk_index * chunk_size
        chunk_end = min(chunk_start + chunk_size, len(self._words))

        chunk_words = self._words[chunk_start:chunk_end]

        #Update the index
        if self._current_chunk_index < total_chunks - 1:
            self._current_chunk_index += 1
        else:
            self._current_chunk_index = 0

        return " ".join(chunk_words)
