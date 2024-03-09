#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self._value = value
        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("Value must be a string")
        self._value = new_value
        
    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
       return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')
      
      
    def count_sentences(self):
        if not self._value:
            return 0
        # Split the string into sentences based on period, exclamation mark, or question mark
        sentences = re.split(r'[.!?]', self._value)
        # Filter out empty strings and count the number of non-empty sentences
        return len([sentence for sentence in sentences if sentence.strip()])



string = MyString()
string.value = ""
print("Number of sentences:", string.count_sentences())