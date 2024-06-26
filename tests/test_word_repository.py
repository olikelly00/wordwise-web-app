from lib.word import Word
from lib.word_repository import WordRepository

def test_all_words(db_connection):
    db_connection.seed('../seeds/seeds_words.sql')
    repo = WordRepository(db_connection)

    assert repo.all() == [
        Word(1, 'English', 'French', 'Apple', 'Pomme', '00000', 1),
        Word(2, 'English', 'Italian', 'Apple', 'Mela', '00000', 2),
        Word(3, 'French', 'English', 'Pomme', 'Apple', '00000', 1),
        Word(4, 'French', 'Italian', 'Pomme', 'Mela', '00000', 2)
        ]
    
def test_add_word(db_connection):
    db_connection.seed('../seeds/seeds_words.sql')
    repo = WordRepository(db_connection)
    new_word = Word(5, 'English', 'German', 'Apple', 'Apfel', '00000', 3)

    repo.add(new_word)
    assert repo.all() == [
        Word(1, 'English', 'French', 'Apple', 'Pomme', '00000', 1),
        Word(2, 'English', 'Italian', 'Apple', 'Mela', '00000', 2),
        Word(3, 'French', 'English', 'Pomme', 'Apple', '00000', 1),
        Word(4, 'French', 'Italian', 'Pomme', 'Mela', '00000', 2),
        Word(5, 'English', 'German', 'Apple', 'Apfel', '00000', 3)
        ]
    

def test_find_word_by_userid(db_connection):
    db_connection.seed('../seeds/seeds_words.sql')
    repo = WordRepository(db_connection)
    assert repo.find_by_userid(2) == [
        Word(2, 'English', 'Italian', 'Apple', 'Mela', '00000', 2),
        Word(4, 'French', 'Italian', 'Pomme', 'Mela', '00000', 2)
    ]


def test_find_word_by_target_language(db_connection):
    db_connection.seed('../seeds/seeds_words.sql')
    repo = WordRepository(db_connection)
    assert repo.find_by_target_language('Italian') == [
        Word(2, 'English', 'Italian', 'Apple', 'Mela', '00000', 2),
        Word(4, 'French', 'Italian', 'Pomme', 'Mela', '00000', 2)
    ]

def test_find_word_by_source_language(db_connection):
    db_connection.seed('../seeds/seeds_words.sql')
    repo = WordRepository(db_connection)
    assert repo.find_by_source_language('English') == [
        Word(1, 'English', 'French', 'Apple', 'Pomme', '00000', 1),
        Word(2, 'English', 'Italian', 'Apple', 'Mela', '00000', 2)
    ]
       
def test_alphabetise_wordbank_by_word_in_source_language(db_connection):
    db_connection.seed('../seeds/seeds_words.sql')
    repo = WordRepository(db_connection)
    new_word = Word(5, 'English', 'Italian', 'Banana', 'Banana', '00000', 3)
    repo.add(new_word)
    word_list = repo.all()
    result = repo.alphabetise_wordbank_by_word_in_source_language(word_list)
    assert result == [
        Word(1, 'English', 'French', 'Apple', 'Pomme', '00000', 1),
        Word(2, 'English', 'Italian', 'Apple', 'Mela', '00000', 2),
        Word(5, 'English', 'Italian', 'Banana', 'Banana', '00000', 3),
        Word(3, 'French', 'English', 'Pomme', 'Apple', '00000', 1),
        Word(4, 'French', 'Italian', 'Pomme', 'Mela', '00000', 2)
        ]


def test_alphabetise_wordbank_by_word_target_language(db_connection):
    db_connection.seed('../seeds/seeds_words.sql')
    repo = WordRepository(db_connection)
    word_list = repo.all()
    result = repo.alphabetise_wordbank_by_word_in_target_language(word_list)
    assert result == [
        Word(3, 'French', 'English', 'Pomme', 'Apple', '00000', 1),
        Word(2, 'English', 'Italian', 'Apple', 'Mela', '00000', 2),
        Word(4, 'French', 'Italian', 'Pomme', 'Mela', '00000', 2),
        Word(1, 'English', 'French', 'Apple', 'Pomme', '00000', 1)
    ]
