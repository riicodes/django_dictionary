from django.shortcuts import render
from PyDictionary import PyDictionary


def index(request):
    return render(request, 'dictionary/index.html')


def result(request):
    dictionary = PyDictionary()
    word = request.GET.get('word')
    word_meaning = dictionary.meaning(word)
    synonyms = dictionary.synonym(word)
    antonyms = dictionary.antonym(word)
    if word_meaning is not None:
        context = {
            'result': word_meaning.get('Noun')[0],
            'synonyms': synonyms,
            'antonyms': antonyms,
        }
    else:
        context = {'error': 'Meaning not found for the word: {}'.format(word)}
    return render(request, 'dictionary/index.html', context)
