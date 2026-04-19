FHIR-TO-GIS Takes patient record data and converts it into GIS compatible .csv (PatientData_Input.csv)  
The CSV goes through a GIS pipeline seeing where the patient zipcode intercepts with tick distribution  
Reports back a output .csv (GIS_Output.csv)   
GIS-TO-FHIR turns the output .csv back into FHIR standard for Risk Assessment (https://build.fhir.org/riskassessment.html#:~:text=Risk%20of%20health%20outcome%20(heart,the%20Patient%20or%20Group%20resources)
