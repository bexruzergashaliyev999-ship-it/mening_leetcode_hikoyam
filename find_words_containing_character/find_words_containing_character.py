class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index = []

        for i, word in enumerate(words):
            if x in word:
                index.append(i)

        return index
        