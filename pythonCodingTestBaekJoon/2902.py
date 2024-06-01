word = input()
wordArray = word.split('-')

# end=''는 줄바꿈 없이 바로 옆에 붙어서 출력
def printFirstAlphas(wordArray):
    for text in wordArray:
        print(text[0], end='')

printFirstAlphas(wordArray)
