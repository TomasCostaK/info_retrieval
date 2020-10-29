# RI_Assignment1

## Requirements
You need to install the requirements with pip:
```
    pip install -r requirements.txt
```

## How to Run
```python
    cd code
    python3 main.py <tokenizer_mode> <number_lines>
```

 * The tokenizer mode specifies if the tokenizer is **simple** or **complex**, and we know the complex one is better to analyze the text, since it deletes pronouns and commonly used words that are not related to the theme of the corpus.  

 * The number_lines defines the amount of lines you want to read at once, we recommend 8000-10000 for this document, since it doesnt slow down a lot but loads way less data into memory.

## Details
The code provided is in the **/code** folder, the answers to the questions are printed by the code, but are also located in answers.txt  
**/content** provides the datasets and texts used.  

