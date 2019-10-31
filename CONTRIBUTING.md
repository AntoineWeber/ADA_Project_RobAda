# Contributing to the project

## Git workflow

* Always add a clear commit message (git commit -m "what has been changed")
* To simplify the merging process, only commit Notebooks without output cells
(`Cell > All Output > Clear` before commiting).

## Storing data

The datasets we use are quite large, hence they must be excluded from the
git repository.

The openfoodfacts dataset (~2GB) is added to the .gitignore, thus you need to
download it from this [link](https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv)
and saved it to the `data` folder. It must be named `en.openfoodfacts.org.products.csv`

## Coding conventions

* Name variables using the underscore separation convention:
``` python
my_variable = 3
```
* For easier understanding, use a suffix for dataframes:
``` python
bacteria_df = pd.read_csv('file.csv')
```
