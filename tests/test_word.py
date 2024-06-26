from lib.word import Word

def test_word_consructs():
    test_word = Word(1, 'English', 'French', 'Apple', 'Pomme', '00000', 1)
    assert test_word.id == 1
    assert test_word.source_language == 'English'
    assert test_word.target_language == 'French'
    assert test_word.word_source_language == 'Apple'
    assert test_word.word_target_language == 'Pomme'
    assert test_word.timestamp == '00000'
    assert test_word.user_id == 1
    