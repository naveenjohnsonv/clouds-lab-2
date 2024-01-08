# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt
import re

def main(params):
    output_tuple = []
    _, line_string = params
    # Convert to lowercase
    line_string = line_string.lower()
    # Remove full stops and commas
    line_string = line_string.replace('.', '').replace(',', '')
    # Split words joined with hyphens
    words = re.split(r'-|\s', line_string)
    # Process words according to the specified rules
    processed_words = []
    for word in words:
        if word.startswith("'"):
            word = 'h' + word[1:]
        if word.endswith("'"):
            word = word[:-1] + 'g'
        # Handle contractions by splitting them into separate words
        word = re.sub(r"(\w+)'re", r'\1 are', word)
        word = re.sub(r"(\w+)'s", r'\1 us', word)
        # Split the processed contractions into separate words
        processed_words.extend(word.split())
    # Add (word, 1) pairs to the output list
    for word in processed_words:
        output_tuple.append((word, 1))
    return output_tuple
