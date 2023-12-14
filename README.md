# Automated name selection for the Network Scale-Up Method

This code implements the approach described in the paper [Automated name selection for the Network Scale-Up Method](https://doi.org/10.31235/osf.io/t6pk2).


## Usage

1. Arrange the data in a Excel `xlsx` file in a single spreadsheet in a flattened form such that names are in rows and all the combinations of variables of interest correspond to columns. See the files in `data` folder for examples.
2. Run the command such as (values of `-S` and `-N` options are examples, `--verbose` is optional):

```bash
python3 main.py --file-path ./path/to/file.xlsx -S 20 -N 10 --verbose
```

- `--file-path` : Path to ".xlsx" file. 
- `--low` : Lower frequency threshold for the selection of candidate names (default is 0.001).
- `--high` : Higher frequency threshold for the selection of candidate names (default is 0.002).
- `-S` : Size of the subset of names.
- `-N` : Number of solutions provided by the approach.
- `--verbose` : Use if information of the running approach is desired.

3. Inspect the solutions in the original ".xlsx" file.



## Development notes

See [wiki on GitHub](https://github.com/coalesce-lab/nsum-name-selection/wiki).


## License

The code is released under GNU GPLv2 license. See `LICENSE` for further details.
