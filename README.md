# Shipment Rate Audit

`shipment-rate-audit` validates shipment records, detects duplicate identifiers and malformed pricing inputs, and renders a deterministic exception summary for rate reviews.

## Setup

```sh
python3 -m unittest discover -s tests -v
```

## Usage

```sh
python3 -m shipment_rate_audit fixtures/shipments.csv
```

## CSV format

```csv
shipment_id,origin,destination,weight_kg,rate_usd
SHP-1001,MEL,BNE,12.50,4.20
```
