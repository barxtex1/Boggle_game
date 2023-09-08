import numpy as np


def adjacentLettersMatrix(boggle_matrix, h, w):
    boggle_matrix[h, w] = "*"
    if h == 0 and w == 0:
        return boggle_matrix[h:h+2, w:w+2], [h, w]
    elif h == 0 and w != len(boggle_matrix)-1 and w != 0:
        return boggle_matrix[h:h+2, w-1:w+2], [h, w-1]
    elif h == len(boggle_matrix)-1 and w != 0 and w != len(boggle_matrix)-1:
        return boggle_matrix[h-1:, w-1:w+2], [h-1, w-1]
    elif h == len(boggle_matrix)-1 and w == 0:
        return boggle_matrix[h-1:, w:w+2], [h-1, w]
    elif h != 0 and h != len(boggle_matrix)-1 and w == len(boggle_matrix)-1:
        return boggle_matrix[h-1:h+2, w-1:], [h-1, w-1]
    elif h != 0 and h != len(boggle_matrix)-1 and w != 0 and w != len(boggle_matrix)-1:
        return boggle_matrix[h-1:h+2, w-1:w+2], [h-1, w-1]
    elif h != 0 and h != len(boggle_matrix)-1 and w == 0:
        return boggle_matrix[h-1:h+2, w:w+2], [h-1, w]
    elif h == 0 and w == len(boggle_matrix)-1:
        return boggle_matrix[h:h+2, w-1:], [h, w-1]
    else:
        return boggle_matrix[h-1:,w-1:], [h-1, w-1]
    

def checkMatrix(word, boggle_matrix, i, j, index, match_word):
    # Set the match word
    if match_word == "":
        match_word = boggle_matrix[i][j]
    # Check if index of letter is correct
    if word[index] != boggle_matrix[i][j]:
        return False
    else: 
        # Check if the word matches the matching word
        if word == match_word:
            return True

        temp_boggle_matrix = boggle_matrix.copy()
        # Try to find next letter in the matrix
        index += 1
        # Extract only the matrix of adjacent letters
        matrix, indexes = adjacentLettersMatrix(temp_boggle_matrix, i, j)  # 'indexes' is the index of top left letter of matrix
        # If the next letter of the word you are looking for is in the matrix go ahead
        if word[index] in matrix:
            # Find only the indexes of the searched letters
            index_arr = np.where(matrix == word[index])
            index_arr = [[index_arr[0][i], index_arr[1][i]] for i in range(len(index_arr[0]))]
            for x, y in index_arr:
                match_word += temp_boggle_matrix[indexes[0]+x][indexes[1]+y]
                # Try to find the next one letter of the word
                if not checkMatrix(word, temp_boggle_matrix, indexes[0]+x, indexes[1]+y, index, match_word):
                    # Try next letter in the matrix of adjacent letters if exist
                    match_word = match_word[:-1]
                    continue
                else:
                    # Search word found, move on to the next one
                    return True          
        else:
            return False


def MatrixChallenge(strArr):
    # Create matrix of given words
    boggle_matrix = strArr[0].split(", ")
    boggle_matrix = [list(word) for word in boggle_matrix]
    boggle_matrix = np.array(boggle_matrix)
    
    wordsToCheck = strArr[1].split(",")
    correctWords = []
    for word in wordsToCheck:
        nextWord = False
        for i in range(4):
            if not nextWord:
                for j in range(4):
                    if not nextWord:
                        # Try to find the following letters of the word
                        if not checkMatrix(word, boggle_matrix, i, j, index=0, match_word=""):
                            # If given index of letter isn't correct try next one
                            continue
                        else:
                            # The word appears in a matrix - move on to the next word
                            correctWords.append(word)
                            nextWord = True
    
    wordsNotFound = [item for item in wordsToCheck if item not in correctWords]
    if len(wordsNotFound) > 0:
        return ','.join([str(word) for word in wordsNotFound])
    else:
        return True
    
if __name__ == '__main__':
    # Load the configuration files - boggle board and search words
    with open('boggle_board.txt', 'r') as file:
        boggle_board = file.read()
    
    with open('dictionary.txt', 'r') as file:
        dictionary = file.read()

    # Let's start the game!
    print(MatrixChallenge([boggle_board, dictionary]))

