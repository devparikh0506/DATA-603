# Text Analysis using MapReduce

This project implements a MapReduce algorithm to perform word count analysis on text files. It includes functionality to count all words and specifically non-English words (such as names, places, and spells) in the input text.

## Features

- Count occurrences of all words in a text file
- Count occurrences of non-English words in a text file
- Remove special characters from text
- Utilize MapReduce for efficient processing of large datasets

## Requirements

- Python 3.x
- Jupyter Notebook
- mrjob library
- enchant library

## Installation

1. Clone this repository or download the Jupyter Notebook file.
2. Install the required libraries:
  `pip install mrjob pyenchant`

## Usage

1. Open the Jupyter Notebook `DATA_603_assignment_2.ipynb`.
2. Run the cells in order to execute the word count analysis.
3. Modify the input file paths as needed for your specific text files.

## Functions

### WordCount

Counts occurrences of all words in the input text file.

### NonEnglishWordCount

Counts occurrences of non-English words (names, places, spells, etc.) in the input text file.

### remove_special_chars

Removes special characters from the input text, preserving only alphanumeric characters and spaces.

## Output

The notebook will generate output files containing the word count results. These files will show each word and its frequency in the format:

`"word" count`

## Notes

- The non-English word detection uses the `enchant` library with the US English dictionary. Some common names or places might be recognized as English words.
- The special character removal function can be adjusted to keep certain characters if needed.

## License

This project is open-source and available under the MIT License.
