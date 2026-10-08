"""Assignment 1 — load Titanic data and print .info()/.describe() summaries."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from titanic_cleaning import DEFAULT_INPUT, load_data, print_basic_statistics


if __name__ == "__main__":
    titanic = load_data(DEFAULT_INPUT)
    print_basic_statistics(titanic)
