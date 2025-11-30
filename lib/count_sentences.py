#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self.value = value  # uses the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        parts = re.split(r'[.?!]', self.value)
        sentences = [p for p in parts if p.strip()]
        return len(sentences)

