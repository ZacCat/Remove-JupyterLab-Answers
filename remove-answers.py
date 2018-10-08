import json
import re
import sys

regex_vals = {'markdown': r'^\s*#+\s+answer\s+\d+',
              'code':  r'^\s*#+\s*answer'}

req_ext = '.ipynb'

def isNotAnswerCell(cell):
    """ Determines if the provided cell is an answer cell """
    if(len(cell['source']) == 0 or cell['cell_type'] not in regex_vals.keys()):
        return True

    return re.match(regex_vals[cell['cell_type']], cell['source'][0], flags=re.I) == None

def main(argv):
    # Handles incorrect command line arguments
    if(len(argv) != 2):
        print('Correct usage is:\npython3 remove_answers.py <inputfile> <outputfile>')
        return
    if(not all([f_name.endswith(req_ext) for f_name in argv])):
        print(f'Currently this program only supports {req_ext} files')
        return

    # Open the notebook
    with open(argv[0], 'r') as f:
        js = json.loads(f.read())
    # Remove the answer cells
    js['cells'] = list(filter(isNotAnswerCell, js['cells']))
    # Save the notebook without answer cells
    with open(argv[1], 'w+') as f:
        json.dump(js, f)

    print(f'Successfully generated {argv[1]}')

main(sys.argv[1:])