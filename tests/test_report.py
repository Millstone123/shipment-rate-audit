import unittest
from decimal import Decimal

from shipment_rate_audit.analysis import analyze_shipments


class ShipmentAuditTests(unittest.TestCase):
    def test_balanced_fixture_rendering(self):
        report = analyze_shipments([
            ("shipment_id", "origin", "destination", "weight_kg", "rate_usd"),
            ("SHP-1", "MEL", "BNE", "12.50", "4.20"),
            ("SHP-2", "BNE", "SYD", "8.00", "5.75"),
            ("SHP-3", "SYD", "MEL", "4.25", "8.00"),
        ])
        self.assertEqual(
            str(report),
            "shipments=3\nvalid=3\nduplicates=-\ninvalid=0\ntotal=132.50",
        )

    def test_duplicate_identifier_rendering(self):
        report = analyze_shipments([
            ("SHP-1", "MEL", "BNE", "1.00", "2.00"),
            ("SHP-1", "BNE", "SYD", "2.00", "3.00"),
        ])
        self.assertEqual(report.duplicate_ids, ("SHP-1",))
        self.assertEqual(report.total_charge, Decimal("8.00"))
        self.assertIn("duplicates=SHP-1", str(report))

    def test_invalid_rate_rendering(self):
        report = analyze_shipments([
            ("SHP-9", "MEL", "BNE", "1.00", "not-a-rate"),
        ])
        self.assertEqual(report.valid_count, 0)
        self.assertEqual(len(report.invalid_rows), 1)
        self.assertIn("invalid=1", str(report))


if __name__ == "__main__":
    unittest.main()
