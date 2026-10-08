"""Assignment 2 — mean/median/mode imputation for missing Titanic data."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from titanic_cleaning import DEFAULT_INPUT, clean_missing_data, load_data


if __name__ == "__main__":
    titanic = load_data(DEFAULT_INPUT)
    print("Missing values before cleaning:\n", titanic.isna().sum())
    cleaned_titanic = clean_missing_data(titanic)
    print("\nMissing values after cleaning:\n", cleaned_titanic.isna().sum())
    print("\nAge is filled with its median; Fare is filled with its mean.")
