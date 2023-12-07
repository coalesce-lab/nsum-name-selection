# Automated name selection for the Network Scale-Up Method

This code implements the approach described in the paper [Automated name selection for the Network Scale-Up Method](https://doi.org/10.31235/osf.io/t6pk2).

## Usage

1. Sort the name statistics in a ".xlsx" file as done in the exampes inside the data folder.

2. Run the command:

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

## License

The code is released under GNU GPLv2 license. See license.txt for further details.
