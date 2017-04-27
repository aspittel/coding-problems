"""
Check to see if a string can be made from a combination of given substrings

From https://www.hackerrank.com/challenges/password-cracker
"""

def password_hack(p_words, p_word):
    all_pwords = ''
    word = ''
    for l in p_word:
        word += l
        if word in p_words:
            all_pwords += word + ' '
            word = ''
            
    if word:
        return 'WRONG PASSWORD'
        
    return all_pwords
