class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap = {}

        for letter in t:
            hashMap[letter] = hashMap.get(letter,0) + 1

        for letter in s:
            hashMap[letter] = hashMap.get(letter,0) - 1
        
        for count in hashMap.values():
            if count != 0:
                return False
        return True