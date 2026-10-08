"""Titanic data-cleaning assignment: reusable, command-line version."""

from __future__ import annotations

from pathlib import Path
import argparse

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "raw" / "titanic.csv"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "processed" / "cleaned_titanic.csv"
DEFAULT_FIGURE = PROJECT_ROOT / "figures" / "age_distribution.png"
DATA_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"


def load_data(input_path: Path) -> pd.DataFrame:
    """Load a local CSV; download the public training data when it is absent."""
    if not input_path.exists():
        input_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Raw CSV not found. Downloading it from: {DATA_URL}")
        frame = pd.read_csv(DATA_URL)
        frame.to_csv(input_path, index=False)
        return frame
    return pd.read_csv(input_path)


def print_basic_statistics(df: pd.DataFrame) -> None:
    """Assignment 1: show structure and descriptive statistics."""
    print("\n--- Dataset information ---")
    df.info()
    print("\n--- Descriptive statistics ---")
    print(df.describe(include="all").transpose())
    print("\n--- Missing values before cleaning ---")
    print(df.isna().sum().sort_values(ascending=False))


def clean_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """Assignment 2: impute numeric and categorical missing values.

    Age uses median because passenger ages are skewed; Fare uses mean; Embarked
    uses its most frequent value. Cabin is dropped because most values are absent.
    """
    cleaned = df.copy()
    cleaned["Age"] = cleaned["Age"].fillna(cleaned["Age"].median())
    cleaned["Fare"] = cleaned["Fare"].fillna(cleaned["Fare"].mean())
    cleaned["Embarked"] = cleaned["Embarked"].fillna(cleaned["Embarked"].mode()[0])
    cleaned = cleaned.drop(columns=["Cabin"], errors="ignore")
    return cleaned


def encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """Assignment 3: LabelEncoder for Sex and OneHotEncoder for Embarked."""
    encoded = df.copy()

    sex_encoder = LabelEncoder()
    encoded["Sex"] = sex_encoder.fit_transform(encoded["Sex"])
    print("\nSex encoding:", dict(zip(sex_encoder.classes_, sex_encoder.transform(sex_encoder.classes_))))

    embark_encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    embark_values = embark_encoder.fit_transform(encoded[["Embarked"]])
    embark_columns = embark_encoder.get_feature_names_out(["Embarked"])
    embark_df = pd.DataFrame(embark_values, columns=embark_columns, index=encoded.index).astype(int)
    encoded = pd.concat([encoded.drop(columns=["Embarked"]), embark_df], axis=1)
    print("Embarked one-hot columns:", ", ".join(embark_columns))
    return encoded


def save_age_chart(df: pd.DataFrame, figure_path: Path) -> None:
    """Create the requested Matplotlib/Seaborn age-distribution visualization."""
    figure_path.parent.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(9, 5))
    sns.histplot(df["Age"], bins=30, kde=True, color="#2563eb", edgecolor="white")
    plt.title("Titanic Passenger Age Distribution")
    plt.xlabel("Age (years)")
    plt.ylabel("Number of passengers")
    plt.tight_layout()
    plt.savefig(figure_path, dpi=160)
    plt.close()


def run_pipeline(input_path: Path, output_path: Path, figure_path: Path) -> pd.DataFrame:
    raw = load_data(input_path)
    print_basic_statistics(raw)
    cleaned = clean_missing_data(raw)
    encoded = encode_categoricals(cleaned)
    save_age_chart(cleaned, figure_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded.to_csv(output_path, index=False)
    print("\n--- Missing values after cleaning ---")
    print(encoded.isna().sum()[encoded.isna().sum() > 0])
    print(f"\nSaved cleaned CSV: {output_path}")
    print(f"Saved age chart: {figure_path}")
    return encoded


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean and encode the Titanic dataset.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--figure", type=Path, default=DEFAULT_FIGURE)
    args = parser.parse_args()
    run_pipeline(args.input, args.output, args.figure)


if __name__ == "__main__":
    main()
