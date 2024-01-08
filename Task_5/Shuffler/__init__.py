# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

def main(params):
    shuffle_dict = {}
    for key, value in params:
        if key in shuffle_dict:
            shuffle_dict[key].append(value)
        else:
            shuffle_dict[key] = [value]
    return shuffle_dict