LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def word_has_character(word, character_list):

    for character in word:
        if character in character_list:
            return True
        
    return False 


def word_complexity(word):

    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1