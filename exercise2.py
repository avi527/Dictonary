def wordCount(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count
print(wordCount('sudheer'))
