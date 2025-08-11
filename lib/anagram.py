class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))

    def is_anagram(self, candidate):
        return candidate.lower() != self.word and \
               ''.join(sorted(candidate.lower())) == self.sorted_word

    def match(self, candidates):
        matches = []
        for candidate in candidates:
            if isinstance(candidate, str) and self.is_anagram(candidate):
                matches.append(candidate)
        return matches
