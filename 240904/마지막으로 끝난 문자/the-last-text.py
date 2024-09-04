import sys

input = sys.stdin.readline

def findMatchedWords(words, n, key):
    keyLen = len(key)
    result = []

    for word in words:
        wordLen = len(word)
        if word[wordLen-keyLen:wordLen] == key:
            result.append(word)

    return result


if __name__=="__main__":
    n = int(input())
    words = [
        input().strip()
        for _ in range(n)
    ]
    key = input().strip()

    result = findMatchedWords(words, n, key)
    
    print(len(result))
    for word in result:
        print(word)