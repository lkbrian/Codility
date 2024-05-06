import re


def solution(text):
    # Finding Vowels
    vowels_pattern = r"[aeiouAEIOU]"
    text_without_vowels = re.sub(vowels_pattern, "", text)

    # Stripping
    sentence = text_without_vowels.strip()
    print("Sentence:", sentence)



def disemvowel(string_):
    vowel_pattern = r"[aeiouAEIOU]"
    non_vowel = re.sub(vowel_pattern, "", string_)
    string = non_vowel.strip()
    return string_


text = "Hello, this is a sample text with some numbers 12345 and vowels AEIOU"
solution(text)
