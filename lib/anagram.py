# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, word_list):
        matches = []
        sorted_word = sorted(self.word)
        
        for candidate in word_list:
            candidate_lower = candidate.lower()
            # Check if it's not the same word and has the same sorted letters
            if candidate_lower != self.word and sorted(candidate_lower) == sorted_word:
                matches.append(candidate)
        
        return matches