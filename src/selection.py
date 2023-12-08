import pandas as pd
import numpy as np
import cvxpy as cp
import time

def selection(filepath, low, high, subset_size, num_solutions, verbose=True):
    if verbose:
        print('Preparing data...')
    
    names = pd.read_excel(filepath, index_col=0, engine='openpyxl')

    f_names = names.sum(axis=1, numeric_only=True)
    f_cat = names.sum(axis=0, numeric_only=True)
    norm = f_names.sum()

    candidates = names[(f_names > low) & (f_names < high)]
    candidates_size = len(candidates)

    try:
        if candidates_size < subset_size:
            raise ValueError()
    except ValueError:
        exit('Number of candidates ({0}) too low for the size of the subset ({1}). \nConsider reducing the subset size or increasing the low and high frequency thresholds.'.format(candidates_size, subset_size))

    alpha_min, alpha_max = norm / (subset_size * high), norm / (subset_size * low)
    alpha_space = np.linspace(alpha_min, alpha_max, num_solutions)

    if verbose:
        print('Generating solutions...')

    start = time.time()
    for i, alpha in enumerate(alpha_space, 1):
        A = alpha * candidates.select_dtypes(np.number).to_numpy().T
        b = f_cat.to_numpy()
        x = cp.Variable(len(candidates), boolean=True)

        objective = cp.Minimize(cp.sum_squares(A @ x - b))
        prob = cp.Problem(objective, [cp.sum(x) == subset_size])
        prob.solve(solver = cp.SCIP)

        solution = candidates[x.value != 0]
        f_solution = solution.sum(axis=0, numeric_only=True)
        real_alpha = norm / f_solution.sum()

        with pd.ExcelWriter(filepath, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            (real_alpha * solution).to_excel(
                writer, sheet_name='Solution{}'.format(i))

        if verbose:
            print(' - Solution {0} generated after {1} seconds'.format(i, time.time() - start))
        start = time.time()

    if verbose:
        print('COMPLETED! Solutions added as new sheets in {}'.format(filepath))
