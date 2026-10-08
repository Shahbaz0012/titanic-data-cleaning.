# Titanic Survival Prediction — Data Cleaning Project

A beginner-friendly data-cleaning mini-project based on the Titanic passenger dataset. It completes all three assignment exercises and saves a machine-learning-ready CSV.

## Assignment coverage

| Requirement | Where it is completed |
| --- | --- |
| Load a dataset with Pandas | `load_data()` |
| Summarize data with `.info()` and `.describe()` | `print_basic_statistics()` |
| Handle missing values using mean/median imputation | `clean_missing_data()` |
| Encode categorical columns with `LabelEncoder` | `Sex` becomes `0` (female) / `1` (male) |
| Encode categorical columns with `OneHotEncoder` | `Embarked_C`, `Embarked_Q`, and `Embarked_S` |
| Visualize age distribution with Matplotlib/Seaborn | `figures/age_distribution.png` |
| Export a cleaned dataset | `data/processed/cleaned_titanic.csv` |

## Cleaning decisions

- `Age`: missing ages are replaced by the **median**, which is less sensitive to unusually high or low ages.
- `Fare`: missing values are replaced by the **mean**.
- `Embarked`: missing values are replaced by the most common port.
- `Cabin`: dropped because the column has too many missing values to impute reliably.
- `Sex`: label encoded.
- `Embarked`: one-hot encoded, then the original text column is removed.

## Project layout

```text
.
├── data/
│   ├── raw/                 # original CSV created on first run (ignored by Git)
│   └── processed/           # cleaned_titanic.csv
├── figures/                 # age_distribution.png
├── assignments/             # three standalone assignment scripts
│   ├── 01_pandas_basics.py
│   ├── 02_missing_data_imputation.py
│   └── 03_categorical_encoding.py
├── notebooks/
│   └── Titanic_Data_Cleaning.ipynb
├── src/
│   └── titanic_cleaning.py
├── requirements.txt
└── README.md
```

## Run locally

1. Clone or download this repository.
2. Create and activate a virtual environment (recommended):

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install packages and run the project:

   ```powershell
   pip install -r requirements.txt
   python src/titanic_cleaning.py
   ```

On the first run, the script downloads the public Titanic CSV automatically. If your network blocks the download, save the Kaggle/CSV dataset as `data/raw/titanic.csv` and run the command again.

> The raw source file is intentionally not committed; it is recreated automatically so the repository stays lightweight and reproducible.

## Outputs

The script produces:

- `data/processed/cleaned_titanic.csv` — cleaned, encoded dataset
- `figures/age_distribution.png` — passenger age histogram with KDE curve

To explore the same steps cell-by-cell, open `notebooks/Titanic_Data_Cleaning.ipynb` in Jupyter Notebook or VS Code.

Each standalone assignment can also be run on its own:

```powershell
python assignments/01_pandas_basics.py
python assignments/02_missing_data_imputation.py
python assignments/03_categorical_encoding.py
```

## Dataset attribution

The script uses the public Titanic dataset mirrored by [Data Science Dojo](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv). The original assignment points to the Titanic dataset on Kaggle.

## Upload to GitHub

Create an empty GitHub repository, then run these commands inside this project folder:

```powershell
git init
git add .
git commit -m "Add Titanic data cleaning assignment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with the values from your GitHub repository URL. GitHub may open a browser to sign in during the final command.
