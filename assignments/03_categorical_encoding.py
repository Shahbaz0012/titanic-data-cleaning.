"""Assignment 3 — LabelEncoder and OneHotEncoder for Titanic categories."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from titanic_cleaning import DEFAULT_INPUT, clean_missing_data, encode_categoricals, load_data


if __name__ == "__main__":
    titanic = load_data(DEFAULT_INPUT)
    cleaned_titanic = clean_missing_data(titanic)
    encoded_titanic = encode_categoricals(cleaned_titanic)
    print(encoded_titanic[["Sex", "Embarked_C", "Embarked_Q", "Embarked_S"]].head())
