# CPSC 485 Computational Bioinformatics - Edit Distance

# Brandon Capparelli 
# brandon.capparelli@csu.fullerton.edu

# To run: Enter 'python3 EditDistance.py' into your terminal

def EditDistance(input1, input2):
    # Create the empty matrix
    matrix = [[0 for _ in range(len(input1) + 1)] for _ in range(len(input2) + 1)]

    # Fill first row with numbers 0 to length word 1 and first column with numbers 0 to length word 2
    for i in range(0, len(input1) + 1): matrix[0][i] = i
    for j in range(1, len(input2) + 1): matrix[j][0] = j
    
    # Fill in remaining positions
    for i in range(1, len(input1) + 1):
        for j in range(1, len(input2) + 1):
            up = matrix[j - 1][i]
            left = matrix[j][i - 1]
            diag = matrix[j - 1][i - 1]
            dist = [up + 1, left + 1, diag + 1]
            if input1[i - 1] == input2[j - 1]: dist[2] -= 1
            matrix[j][i] = min(dist)

    print('-----------------------------------------------------------------------\n')
    print(f'Edit Distance: {matrix[len(input2)][len(input1)]}\n')
    print('Matrix:')
    for i in range(0, len(input2)+1):
        print(matrix[i])
    print()
    
    # Calculate the alignment
    i = len(input2)
    j = len(input1)
    word1 = ''
    word2 = ''

    while True:
        up = matrix[i - 1][j]
        left = matrix[i][j - 1]
        diag = matrix[i - 1][j - 1]

        if i != 0 and j != 0:
            # Checks if diagonal position is lowest value
            if diag <= left and diag <= up:
                word1 = input1[j-1] + word1
                word2 = input2[i-1] + word2 
                i -= 1
                j -= 1

            # Checks if left position is lowest value
            elif left <= diag and left <= up:
                word1 = input1[j-1] + word1
                word2 = '_' + word2 
                j -= 1

            # Checks if up position is lowest value
            elif up <= diag and up <= left:
                word1 = '_' + word1
                word2 = input2[i-1] + word2 
                i -= 1

            # Default State
            else:
                word1 = input1[j-1] + word1
                word2 = input2[i-1] + word2 
                i -= 1
                j -= 1
        
        # Fills in remainder of word1 with '_' if word2 has reached its end
        if i > 0 and j == 0:
            word1 = '_' + word1
            word2 = input2[i-1] + word2 
            i -= 1
        
        # Fills in remainder of word2 with '_' if word1 has reached its end
        if j > 0 and i == 0:
            word1 = input1[j-1] + word1
            word2 = '_' + word2 
            j -= 1
        
        if i <=0 and j <=0:
            break
    print(word1)
    print(word2)
    print('\n-----------------------------------------------------------------------')

def main():
    print('\n-----------------------------------------------------------------------')
    print('Welcome to the Edit Distance Calculator')
    print('Enter 2 words to check edit distance\n')
    word1 = input('Word 1: ')
    word2 = input('Word 2: ')
    print()
    EditDistance(word1, word2)

if __name__ == '__main__':
    main()