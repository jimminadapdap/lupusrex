"""
Nama : Jimmi Nadapdap
NIM  : 14S21016
"""
def is_valid_assignment(assignment):
    a, b, c = assignment
    return a > b and b != c and a != c

def backtrack(assignment, domain, solutions):
    if len(assignment) == 3:
        if is_valid_assignment(assignment):
            solutions.append(assignment.copy())
        return

    for value in domain:
        new_assignment = assignment + [value]
        backtrack(new_assignment, domain, solutions)

if __name__ == "__main__":
    domain = [2, 3, 5]
    initial_assignment = []
    all_solutions = []

    backtrack(initial_assignment, domain, all_solutions)

    if all_solutions:
        print("Semua solusi yang memenuhi constraint:")
        for idx, solution in enumerate(all_solutions):
            A, B, C = solution
            print(f"Solusi {idx+1}: A = {A}, B = {B}, C = {C}")
    else:
        print("Tidak ada solusi yang memenuhi constraint.")
