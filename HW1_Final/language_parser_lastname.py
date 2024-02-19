import sys

# to get you started, here is sample code that reads the file and outputs an output file that is 0% correct (all empty arrays). You don't need to use this skeleton, feel free to start over and do it another way.

def parse_language(user_input):
    '''
    Description:
    This method is designed to parse a single user input regarding language proficiencies. It processes free-form inputs provided by users and categorizes their language proficiency into different levels based on the Common European Framework of Reference for Languages (CEFR). The method extracts information about the user's native languages and their proficiency levels in various languages.
    Parameters:
    user_input: A string representing the user's input regarding their language proficiencies.
    Returns:
    native_langs: A list containing the user's native languages.
    C2: A list containing languages in which the user is proficient at the C2 level.
    C1: A list containing languages in which the user is proficient at the C1 level.
    B2: A list containing languages in which the user is proficient at the B2 level.
    B1: A list containing languages in which the user is proficient at the B1 level.
    A2: A list containing languages in which the user is proficient at the A2 level.
    A1: A list containing languages in which the user is proficient at the A1 level.
    '''

    native_langs = []
    N = []
    C2 = []
    C1 = []
    B2 = []
    B1 = []
    A2 = []
    A1 = []
    # YOUR CODE HERE
    return native langs, C2, C1, B2, B1, A2, A1
    
    
    
if __name__ == "__main__":
    # Check if filename argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 language_parser_lastname.py input_file.csv output_file.csv")
        sys.exit(1)

        # Get filename from command line argument
    infile = sys.argv[1]
    outfile = sys.argv[2]

    # read in the file, line by line
    with open(outfile, 'w') as out:
        out.write('username,N,C2,C1,B2,B1,A2,A1\n')
        with open(infile, 'r') as file:
            headers = next(file) # 'username,user_input'
            for line in file:
                line = line.strip().split(',') # ['username','user_input']
                username = line[0]
                user_input = line[1]
                parsed = parse_language(user_input) # 'user_input'
                # convert parsed to a string
                s = ','.join(str(lang_level) for lang_level in parsed) + '\n'
                out.write(username + ',' + s)
    
