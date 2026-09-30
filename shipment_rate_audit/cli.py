"""Command-line interface for shipment rate audits."""

import csv
import sys
from pathlib import Path

from .analysis import analyze_shipments


def main(argv=None) -> int:
    arguments = sys.argv[1:] if argv is None else argv
    if len(arguments) != 1:
        print("usage: shipment-rate-audit SHIPMENTS.csv", file=sys.stderr)
        return 2
    with Path(arguments[0]).open(newline="", encoding="utf-8") as handle:
        report = analyze_shipments(csv.reader(handle))
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
