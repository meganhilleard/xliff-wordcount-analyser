
import argparse
from xliff_parser import extract_source_segments
from analysis import analyse_segments


def main():
    parser = argparse.ArgumentParser(
        description="Analyse an XLIFF file and output localisation metrics."
    )
    parser.add_argument("xliff_path", help="Path to the .xlf/.xliff file")
    parser.add_argument(
        "--csv", dest="csv_path", default=None, help="Optional: write results to a CSV file"
    )
    args = parser.parse_args()

    segments = extract_source_segments(args.xliff_path)
    results = analyse_segments(segments)

    print("\n=== XLIFF Analysis Results ===")
    for k, v in results.items():
        print(f"{k}: {v}")

    if args.csv_path:
        import csv
        with open(args.csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["metric", "value"])
            for k, v in results.items():
                writer.writerow([k, v])
        print(f"\nSaved CSV to: {args.csv_path}")


if __name__ == "__main__":
    main()

