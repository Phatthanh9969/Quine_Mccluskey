import os
os.system("cls")

# Step 1: Input Minterms
def input_minterms(data):
    minterms = list(set(map(int, data.split())))
    return minterms

# Step 2: Group Minterms by Number of 1s
def group_minterms(minterms):
    num_vars = len(bin(max(minterms))) - 2
    groups = [[] for _ in range(num_vars + 1)]
    for minterm in minterms:
        binary_rep = bin(minterm)[2:].zfill(num_vars)
        groups[binary_rep.count('1')].append(binary_rep)
    return groups

# Step 3: Combine Pairs of Terms
def combine_terms(a, b):
    diff_count = 0
    diff_index = -1
    combined = list(a)
    for i in range(len(a)):
        if a[i] != b[i]:
            diff_count += 1
            diff_index = i
            if diff_count > 1:
                return None
    combined[diff_index] = '-'
    return ''.join(combined)

# Step 4: Repeat Combination Process
def get_prime_implicants(minterms):
    groups = group_minterms(minterms)
    num_vars = len(bin(max(minterms))) - 2
    all_combinations = True
    prime_implicants = set()
    while all_combinations:
        all_combinations = False
        new_groups = [[] for _ in range(num_vars + 1)]
        combined = set()
        for i in range(len(groups) - 1):
            for a in groups[i]:
                for b in groups[i + 1]:
                    combined_term = combine_terms(a, b)
                    if combined_term:
                        new_groups[combined_term.count('1')].append(combined_term)
                        combined.add(a)
                        combined.add(b)
                        all_combinations = True
        for group in groups:
            for term in group:
                if term not in combined:
                    prime_implicants.add(term)
        groups = new_groups
    return list(prime_implicants)

# Step 6: Create a Coverage Table
def create_coverage_table(prime_implicants, minterms):
    num_vars = len(prime_implicants[0])
    cover_table = {minterm: [] for minterm in minterms}
    for pi in prime_implicants:
        for minterm in minterms:
            binary_minterm = bin(minterm)[2:].zfill(num_vars)
            if all(pi[i] == '-' or pi[i] == binary_minterm[i] for i in range(num_vars)):
                cover_table[minterm].append(pi)
    return cover_table

# Step 7: Select Essential Prime Implicants
def find_essential_prime_implicants(prime_implicants, minterms):
    cover_table = create_coverage_table(prime_implicants, minterms)
    essential_prime_implicants = set()
    while cover_table:
        for minterm, pis in cover_table.items():
            if len(pis) == 1:
                essential_prime_implicants.add(pis[0])
                remove_pi = pis[0]
                break
        else:
            break
        new_cover_table = {}
        for m, pis in cover_table.items():
            if remove_pi not in pis:
                new_cover_table[m] = pis
        cover_table = new_cover_table
    return list(essential_prime_implicants)

# Step 9: Convert to Boolean Expression
def convert_binary_x(n, data):
    temp = []
    for i in range(n):
        for x in data[i]:
            if x == "0":
                temp.append("X'")
            elif x == "-":
                temp.append("-")
            elif x == "1":
                temp.append("X")
    return temp

def input_letter(var):
    data = var.upper()
    data = list(data.replace(",", ""))
    return data

def list_to_string(data, n, length):
    m = 0
    for i in range(length - 1):
        data.insert(((i + 1) * n) + m, "+")
        m += 1
    filtered_list = [item for item in data if item]
    result_string = ''.join(filtered_list)
    return result_string

def finding_unique_minterms(data, letter):
    num = convert_binary_x(len(data), data)
    j = 0
    tx = True
    k = 1
    while tx:
        for i in range(len(num)):
            if num[i] == "X":
                num[i] = letter[j]
                j += 1
            if num[i] == "X'":
                num[i] = letter[j] + "'"
                j += 1
            if num[i] == "-":
                num[i] = ""
                j += 1
            if j == len(letter) and i < (len(num) - 1):
                j = 0
                k += 1
            else:
                tx = False
    result = list_to_string(num, len(letter), len(data))
    
    return result

# Main function to run the Quine-McCluskey algorithm
def quine_mccluskey(minterms):
    prime_implicants = get_prime_implicants(minterms)
    essential_prime_implicants = find_essential_prime_implicants(prime_implicants, minterms)
    return essential_prime_implicants

# Example usage:
if __name__ == "__main__":
    data = "2 3 4 5"
    vars = "A,B,C"
    
    temp=[]
    data = input_minterms(data)
    minterms = quine_mccluskey(data)
    
    letters = input_letter(vars)
    results = finding_unique_minterms(minterms, letters)
    # print(minterms)

    print(f"Quine Mccluskey: {results}")