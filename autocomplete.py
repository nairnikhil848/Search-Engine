# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from fast_autocomplete import demo
from fast_autocomplete import AutoComplete
from fast_autocomplete.misc import read_csv_gen
import csv
quote = input("enter the search")
quote = quote.lower()
with open('data1.txt', 'r') as f:
    file = f.readlines()
    for line in file:
        if quote in line:
            if('\n' in line):
                print(line)
                break
            else:
                print(line)


# %%


def get_words(path):

    csv_gen = read_csv_gen(path, csv_func=csv.DictReader)

    words = {}

    for line in csv_gen:
        make = line['make']
        model = line['model']
        count = line['count']
        if make != model:
            #local_words = [model, '{}{}'.format(make,model)]
            # print(local_words)
            # while local_words:
            #    word = local_words.pop()
            #    if word not in words:
            words['{}{}'.format(make, model)] = {}
        # if make not in words:
            #words[make] = {}
    return words


synonyms = {
    "alfa romeo 4c coupe": ["the alfa", "hello"],
    "bmw": ["beemer", "bimmer"]

}
words = get_words("autocomp.csv")
autocomplete = AutoComplete(words=words, synonyms=synonyms)

autocomplete.search(word='the ', max_cost=3, size=5)


# %%
auto_complete.update_count_of_word(word='toyota aygo', count=10000)
autocomplete.get_count_of_word('toyota aygo')


# %%


# %%
