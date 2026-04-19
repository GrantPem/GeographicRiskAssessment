import json
import os
import csv

FOLDER = r""
OUTPUT = ""

rows = []

for filename in os.listdir(FOLDER):
    if not filename.endswith(".json"):
        continue

    filepath = os.path.join(FOLDER, filename)

    with open(filepath, "r") as f:
        bundle = json.load(f)

    # Find the Patient resource in the bundle
    for entry in bundle.get("entry", []):
        resource = entry.get("resource", {})
        if resource.get("resourceType") == "Patient":
            patient_id = resource.get("id", "")

            # Address is an array; postalCode may or may not exist
            address = resource.get("address", [{}])
            zipcode = address[0].get("postalCode", "")

            rows.append([patient_id, zipcode])
            break  # Only one Patient per file, so stop searching

# Write CSV
with open(OUTPUT, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["patient_id", "zipcode"])
    writer.writerows(rows)

print(f"Done. Wrote {len(rows)} rows to {OUTPUT}")
