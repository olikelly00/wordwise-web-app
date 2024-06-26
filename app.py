from flask import Flask, render_template, request, session, redirect, url_for
from lib.user_repository import *
from lib.user import *
from lib.database_connection import *
from lib.vocab_fetcher import *
from lib.word import *
from lib.word_repository import *



app = Flask(__name__)
app.secret_key = 'wordwise_app_flask' 

@app.route('/', methods=['GET'])
def get_login_page():
    return render_template('login.html'), 200


@app.route('/logout', methods=['GET'])
def get_logout_page():
    session.pop('user_id', None)
    return redirect("login.html"), 200

@app.route('/signup', methods=['GET'])
def get_signup_page():
    return render_template('signup.html'), 200

@app.route('/signup', methods=['POST'])
def get_create_account_page():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    user = User(
        None,
        request.form['email_address'],
        request.form['username'],
        request.form['password'],
        request.form['confirmPassword']
    )
    repo.create(user)
    return redirect("login.html"), 200


@app.route('/welcome')
def welcome():
    return render_template("welcome.html", options=language_menu.keys())

@app.route('/word', methods=['POST'])
def word():
    word = request.form.get('word')
    target_lang = request.form.get('language-menu')
    translated_word = display_word_target_language(fetch_vocab_from_api(word, target_lang))
    print(type(translated_word))
    word_object = fetch_vocab_from_api(word, target_lang)
    session['word_object'] = word_object.to_dict()
    return render_template("word.html", target_lang = f"{target_lang} {language_menu[target_lang]['flag_emoji']}", word = display_word_target_language(fetch_vocab_from_api(word, target_lang)), translated_word=translated_word)
    

@app.route('/add_to_wordbank', methods=['POST'])
def add_to_wordbank():
    word_dict = session.get('word_object') 
    if not word_dict:
        return "Word not provided in request", 400
    word_object = Word(**word_dict)
    connection = get_flask_database_connection(app)
    repository = WordRepository(connection)
    repository.add(word_object)


    target_language = request.form.get('target_language')
    source_language = request.form.get('source_language')
    # sort_source = request.form.get('sort_source')
    # sort_target = request.form.get('sort_target')
    sorted_chronoogically = request.form.get('sorted_chronologically')

    words = repository.all()

    if target_language:
        words = [word for word in words if word.target_language == target_language]
    if source_language:
        words = [word for word in words if word.source_language == source_language]
    # if sort_source:
    #     words = repository.alphabetise_wordbank_by_word_in_source_language(words)
    # if sort_target:
    #     words = repository.alphabetise_wordbank_by_word_in_target_language(words)
    if sorted_chronoogically:
        words = repository.sort_wordbank_by_time_stamp(words)


    return render_template('wordbank.html', words=words, language_menu=language_menu, options=language_menu.keys())


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))