# 1. Add a prefix to a word
print("\nAdd a prefix to a word:")

def add_prefix_un(words):
    prefix_word = []
    for word in words:
        prefix_word.append("un" + word) 
    
    print(prefix_word)

words = ["do", "break", "mute"]
add_prefix_un(words)


# 2. Add prefixes to word groups
print("\nAdd prefixes to word groups:")

def make_word_groups(vocab_words):
    prefixes_word_groups = []
    first_word = vocab_words[0]
    if first_word:
        for index,words in enumerate(vocab_words):
            while index > 0 and index <= index:
                prefixes_word_groups.append(first_word + words)
                break
        
        print(prefixes_word_groups)

make_word_groups(['en', 'close', 'joy', 'lighten'])
make_word_groups(['pre', 'serve', 'dispose', 'position'])
make_word_groups(['auto', 'didactic', 'graph', 'mate'])
make_word_groups(['inter', 'twine', 'connected', 'dependent'])


# 3. Remove a suffix from a word
print("\nRemove a suffix from a word:")

def remove_suffix_ness(word):
    word = word
    consonant = ['a', 'e', 'i', 'o', 'u', 'y']
    suffix = "ness"
    consonant_char_locator = word.find("ness") 
    identify_consonant = consonant_char_locator - 1
    char = word[identify_consonant]

    if char in consonant: 
        removed_suffix = word.replace(
            char, "y").replace(suffix, "")
        print(removed_suffix)
    else:
        removed_suffix = word.replace(suffix, "")

        print(removed_suffix)

remove_suffix_ness('heaviness')
remove_suffix_ness('sadness')
remove_suffix_ness('happiness')
remove_suffix_ness('toughness')


# 4. Extract and transform a word
print("\nExtract and transform a word:")

def adjective_to_verb(sentence, index):
    split_sentence_words = sentence.split()
    adjective = split_sentence_words[index]
    if '.' not in adjective:
        adjective = adjective + 'en'
        split_sentence_words[index] = adjective
    else:
        adjective = adjective.replace('.', 'en.') 
        split_sentence_words[index] = adjective

    sentence_is_verb = ' '.join(split_sentence_words) 
    print(sentence_is_verb)

adjective_to_verb('I need to make that bright.', -1 ) # 'brighten'
adjective_to_verb('It got dark as the sun set.', 2) # 'darken'