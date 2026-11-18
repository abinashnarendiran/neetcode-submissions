class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        anagramCharacters = {}

        if(len(s) != len(t)):
            return False

        for i in range(len(s)):
            characters[s[i]] = 1 + characters.get(s[i], 0) 
            anagramCharacters[t[i]] = 1 + anagramCharacters.get(t[i], 0) 
        


        return characters == anagramCharacters