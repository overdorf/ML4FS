import pandas as pd
import ast
import sys
import subprocess

def compute_correct(x):
    for a,s in x:
        a = eval(a)
        s = eval(s)
        a = [i.lower() for i in a]
        s = [i.lower() for i in s]
        if set(s) != set(a):
            return 0
    return 1
    
def print_incorrect(x):
    if x.all_correct == 0:
        print(f'for user {x.username[1]}\nsolution given: N:{x.N}, C2:{x.C2}, C1:{x.C1}, B2:{x.B2}, B1:{x.B1}, A2:{x.A2}, A1:{x.A1}\nsolution expected: N:{x.cor_N}, C2:{x.cor_C2}, C1:{x.cor_C1}, B2:{x.cor_B2}, B1:{x.cor_B1}, A2:{x.cor_A2}, A1:{x.cor_A1}\n\n')

def check(f1):
    outfile_name = 'output_file.csv'
    try:
        subprocess.run(['python3', f1, 'input_file.csv', outfile_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    
    correct_df = pd.read_csv('expected_output_file.csv')
    correct_df.rename(columns={'N':'cor_N', 'C2':'cor_C2','C1':'cor_C1','B2':'cor_B2','B1':'cor_B1','A2':'cor_A2','A1':'cor_A1'}, inplace=True)
    
    student_df = pd.read_csv(outfile_name)
    
    together = pd.concat([correct_df,student_df], axis=1)

    together['all_correct'] = together.apply(lambda x: compute_correct([(x.N,x.cor_N),(x.C2,x.cor_C2),(x.C1,x.cor_C1),(x.B2,x.cor_B2),(x.B1,x.cor_B1),(x.A2,x.cor_A2),(x.A1,x.cor_A1)]), axis=1)
    
    together.apply(lambda x: print_incorrect(x), axis=1)
    print(f"{together['all_correct'].sum()} out of {together.shape[0]} correct")

if __name__ == "__main__":
    # Check if filename argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 checker.py lastname.py")
        sys.exit(1)
    # Get filename from command line argument
    f1 = sys.argv[1]
    check(f1)
