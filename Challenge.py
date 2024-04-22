import string

print("\n \t\t Little sisters Vocabulary")
print(" \t\t ************************** \n")

un_word = 'believable'
prefix_group_words1 = ['en', 'close','joy', 'lighten']
prefix_group_words2 = ['pre', 'serve', 'dispose', 'position']
prefix_group_words3 = ['auto', 'didactic', 'graph', 'mate']
prefix_group_words4 = ['inter', 'twine', 'connected', 'dependent']
suffix_word1 = 'loneliness'
suffix_word2 = 'happiness'
suffix_word3 = 'laziness'
suffix_word4 = 'sharpness'
to_verb_word1 = 'I need to make that bright.'
to_verb_word2 = 'It got dark as the sun set.'

def add_prefix_un(word):
    """add the prefix un to the passed word

    Args:
        word (string) :  word that will be converted into the un word

    Returns:
        string : returns un prefixed string
    """
    return 'un' + word

def make_word_groups(vocab_words):
    
    """add the prefix 'en' to the group of words passed as argument

    Args:
        vocab_words (list): group of words passed as list 

    Returns:
        returns string: string returned in specific format after prefixed 'en'
    """
    word_groups = ''
    for word in vocab_words:
        if vocab_words.index(word) != 0:
            word_groups = word_groups + vocab_words[0] + vocab_words[vocab_words.index(word)]
            if len(vocab_words) != vocab_words.index(word) +1 :
                word_groups = word_groups + ' :: '
        else :
            word_groups = vocab_words[0] + " :: " 
        
    return word_groups
    
def remove_suffix_ness(word):
    """remove the suffix 'ness' and returns the root word

    Args:
        word (string): string which has the suffix 'ness'

    Returns:
        _string after removing 'ness' and if ends in 'i' after removing 'ness', then removes 'i' and replaces 'y'
    """
    word = word[ :len(word) -4]
    if word[len(word) -1] == 'i':
        return word.replace(word[len(word) -1], 'y')
    else:
        return word
    
def adjective_to_verb(adjective_word, index): 
    """verbifies the adjective word and reurn verb from of the word

    Args:
        adjective_word (string): string sentence with an adjective word
        index (int): index number of the adjective word

    Returns:
        string : verbifies the word by removing en and returns verb
    """
    
    adjective_word = adjective_word.translate(str.maketrans('', '', string.punctuation))
    to_verb =adjective_word.split()
    return to_verb[index].strip() + 'en'

print(f"The following are some of the word groups with prefixes added ")
print(f"-------------------------------------------------------------")
print(f"\n'en' prefixed words are {make_word_groups(prefix_group_words1)} ")
print(f"\n'pre' prefixed words are {make_word_groups(prefix_group_words2)} ")
print(f"\n'auto' prefixed words are {make_word_groups(prefix_group_words3)} ")
print(f"\n'inter' prefixed words are {make_word_groups(prefix_group_words4)} ")

print(f"\nThe following are some of the word groups with suffixes removed")
print(f"---------------------------------------------------------------")
print(f"\nRoot word of {suffix_word1} is {remove_suffix_ness(suffix_word1)}")
print(f"\nRoot word of {suffix_word2} is {remove_suffix_ness(suffix_word2)}")
print(f"\nRoot word of {suffix_word3} is {remove_suffix_ness(suffix_word3)}")
print(f"\nRoot word of {suffix_word4} is {remove_suffix_ness(suffix_word4)}")

print(f"\nAdding prefix 'Un' to a given word")
print(f"------------------------------------ \n")
user_word = input("Enter a word to add a prefix 'un': ")
print(f"\nWord with 'Un' prefix added: {add_prefix_un(user_word)}")

print(f"\nRemoving suffix 'ness' from a given word")
print(f"------------------------------------------ \n")
user_word_ness = input("Enter a word ending with 'ness': ")
print(f"\nWord after removing suffix 'ness': {remove_suffix_ness(user_word_ness)} \n")


