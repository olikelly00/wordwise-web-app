
class Word():
    def __init__(self, id, source_language, target_language, word_source_language, word_target_language, time_stamp, user_id):
        self.id = id
        self.source_language = source_language
        self.target_language = target_language
        self.word_source_language = word_source_language
        self.word_target_language = word_target_language
        self.timestamp = time_stamp
        self.user_id = user_id


    def to_dict(self):
        return {
            'id': self.id,
            'source_language': self.source_language,
            'target_language': self.target_language,
            'word_source_language': self.word_source_language,
            'word_target_language': self.word_target_language,
            'time_stamp': self.timestamp.isoformat() if self.timestamp else None,
            'user_id': None
        }

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Word({self.source_language}, {self.target_language}, {self.word_source_language}, {self.word_target_language}, {self.timestamp}"

