import csv
import json
import os
from datetime import datetime

INPUT = r"gisoutput.csv"
OUTDIR = "G:\BU_CS781-master\Risk_Assessment"
os.makedirs(OUTDIR, exist_ok=True)

for i, row in enumerate(csv.DictReader(open(INPUT))):
    patient_id = row["patient_id"]
    vector = row["Name"]
    disease = row["Transmits"]

    risk_assessment = {
        "resourceType": "RiskAssessment",
        "status": "final",
        "subject": {"reference": f"Patient/{patient_id}"},
        "occurrenceDateTime": datetime.now().isoformat(),
        "prediction": [
            {
                "outcome": {"text": "Likely transmission vector"},
                "qualitativeRisk": {"text": vector}
            },
            {
                "outcome": {"text": "Likely disease"},
                "qualitativeRisk": {"text": disease}
            }
        ]
    }

    # Unique filename even for duplicate patient IDs
    filename = f"{patient_id}_risk_assessment_{i}.json"
    with open(os.path.join(OUTDIR, filename), "w") as f:
        json.dump(risk_assessment, f, indent=2)

print("Done generating FHIR RiskAssessment resources.")
