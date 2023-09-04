# Boggle Game
Boggle Game is a Python script that helps you find words in a 4x4 matrix of letters using a user-provided dictionary of words. It simulates the popular word game Boggle, where players try to find as many words as possible by connecting adjacent letters on a grid.

Unlike some other solutions, this script employs a unique approach to word search. It traverses the Boggle board from one letter to the next, only considering adjacent letters as valid steps in forming words. This approach mirrors the rules of the traditional Boggle game!

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system.
- The numpy library installed. You can install it using pip:
```
pip install numpy
```

## Getting Started
1. Clone the repository to your local machine:
  ```
   git clone https://github.com/barxtex1/Boggle_game.git
  ```
2. Navigate to the project directory:
  ```
   cd Boggle_game
  ```
3. Place your 4x4 Boggle board in a file named `boggle_board.txt` as follows:
  ```
   aaey, rrum, tgmn, ball
  ```
  The board should consist of a list of words separated by commas.
4. Place your words you want to find in the Boggle board in a dictionary file named `dictionary.txt` as follows:
  ```
  all,ball,mur,raeymnl,tall,true,trum
  ```

## Usage
1. Run the script with the following command:
  ```
  python main.py
  ```
2. The script will read the Boggle board from `boggle_board.txt` and the list of words from `dictionary.txt`.
3. It will then search for each word in the Boggle board.
4. If all the words exist in the board, the program will return a True value.
5. If all the words cannot be found, then the program will return a comma-separated string of the words that cannot be found, in the order they appear in the dictionary.
   
**Enjoy playing Boggle and finding words in the grid!**

