from lib.word import Word

class WordRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM words')
        words = []
        for row in rows:
            item = Word(row["id"], row["source_language"], row['target_language'], row['word_source_language'], row['word_target_language'], row['time_stamp'], row['user_id'])
            words.append(item)
        return words


    def add(self, word):
        self._connection.execute('INSERT INTO words (source_language, target_language, word_source_language, word_target_language, time_stamp, user_id) VALUES (%s, %s, %s, %s, %s, %s)', [word.source_language, word.target_language, word.word_source_language, word.word_target_language, word.timestamp, word.user_id])
        print("added successfully")
        return None
    
    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * FROM words WHERE id = %s', (id,)) 
        row = rows[0]
        item = Word(row["id"], row["source_language"], row['target_language'], row['word_source_language'], row['word_target_language'], row['time_stamp'], row['user_id'])
        return item


    def find_by_userid(self, id):
        rows = self._connection.execute('SELECT * FROM words WHERE user_id = %s', (id,))
        words = []
        for row in rows:
            item = Word(row["id"], row["source_language"], row['target_language'], row['word_source_language'], row['word_target_language'], row['time_stamp'], row['user_id'])
            words.append(item)
        return words

    

    def find_by_target_language(self, target_language):
        rows = self._connection.execute('SELECT * from words WHERE target_language = %s', (target_language,))
        words = []
        for row in rows:
            item = Word(row["id"], row["source_language"], row['target_language'], row['word_source_language'], row['word_target_language'], row['time_stamp'], row['user_id'])
            words.append(item)
        return words


    def find_by_source_language(self, source_language):
        rows = self._connection.execute('SELECT * from words WHERE source_language = %s', (source_language,))
        words = []
        for row in rows:
            item = Word(row["id"], row["source_language"], row['target_language'], row['word_source_language'], row['word_target_language'], row['time_stamp'], row['user_id'])
            words.append(item)
        return words


    def alphabetise_wordbank_by_word_in_source_language(self, word_list):
        return sorted(word_list, key=lambda word: word.word_source_language)


    def alphabetise_wordbank_by_word_in_target_language(self, word_list):
        return sorted(word_list, key=lambda word: word.word_target_language)


    def sort_wordbank_by_time_stamp(self, word_list):
        return sorted(word_list, key=lambda word: word.timestamp)