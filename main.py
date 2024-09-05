#import re

def main():
    path_to_file = 'books/frankenstein.txt'
    file_content = read_file(path_to_file) 
    words_len = word_count(file_content)
    chars_dict = char_count(file_content)
    char_list = chars_list(chars_dict)
    #char_list = filter_chars(char_list) 
    print(f'--- Begin report of {path_to_file} .txt ---')
    print(f'{words_len} words found in the document')
    print()
    for char in char_list:
        print(f"The '{char['name']}' character was found '{char['num']}' times")
    
    print('--- End report ---')

'''
def filter_chars(chars):
    new_chars = []
    for char in chars:
        if re.match(r'[a-z]',char['name']):
            new_chars.append(char)
    return new_chars
'''

def chars_list(chars):
    chars_list = []
    for key,value in chars.items():
        chars_list.append({'name':key,'num':value})

    chars_list.sort(reverse=True, key=lambda x:x['num'])
    return chars_list
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    for ch in text:
        curr = ch.lower()
        if not curr.isalpha():
            continue
        if curr not in chars:
            chars[curr] = 0
        chars[curr] += 1
    return chars
def read_file(file):
    with open(file) as f:
        return f.read()


if __name__ == '__main__':
    main()
