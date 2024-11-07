-- # Class: "Patient" Description: "FHIR resource for patient demographics and identifiers."
--     * Slot: id Description: Unique Identifier for Resource
--     * Slot: gender Description: Administrative Gender - the gender that the patient is considered to have for administration and record keeping purposes.
--     * Slot: birthDate Description: Date of birth of the patient
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Condition" Description: "A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern."
--     * Slot: id Description: Unique Identifier for Resource
--     * Slot: subject Description: Reference to the subject (patient) of the observation
--     * Slot: onsetDateTime Description: Date and time when the condition started.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: code_id Description: Code identifying condition
-- # Class: "Container" Description: ""
--     * Slot: id Description: 
-- # Class: "CodeableConcept" Description: "A concept that may be coded with one or more coding systems."
--     * Slot: id Description: 
--     * Slot: text Description: Plain text representation of the concept.

CREATE TABLE "Container" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CodeableConcept" (
	id INTEGER NOT NULL, 
	text TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Patient" (
	id TEXT NOT NULL, 
	gender VARCHAR(7), 
	"birthDate" TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "Condition" (
	id TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	"onsetDateTime" TEXT, 
	"Container_id" INTEGER, 
	code_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Patient" (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id), 
	FOREIGN KEY(code_id) REFERENCES "CodeableConcept" (id)
);
