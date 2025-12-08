# North Dakota (ND) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
North Dakota Absentee/Mail Ballot Application (SFN 51468, 10-2023). Must be for at least one election. Applicant must have resided or will reside in precinct 30 days before election. All fields in Applicant Information section required. Must provide North Dakota ID (driver's license, non-driver ID, long-term care certificate, tribal ID) or passport/military ID (only for voters outside US). Applicants without ID due to disability can have another qualified elector attest (max 4 attestations per election). If unable to sign, can make mark or use signature stamp with disinterested witness. Active military and overseas voters check applicable status and indicate preferred ballot delivery method (mail, email, or fax). Signature compared to affidavit on ballot envelope. Submit to county auditor or appropriate election officer. See North Dakota Century Code, Chapter 16.1-07.

## Fields Found: 39

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Applicant Without ID - Printed Name of Attester | BallotDeliveryAgent | Qualified elector attesting applicant's qualifications |
| Applicant Without ID - Signature of Attester | BallotDeliveryAgent | Attester signature |
| Ballot Delivery Address | BallotMailingAddress | If different from residential |
| Delivery City | BallotMailingAddress | City |
| Delivery State | BallotMailingAddress | State |
| Delivery ZIP Code | BallotMailingAddress | Zip code |
| Military/Overseas - Email | BallotEmailAddress | Provide email address for delivery |
| Military/Overseas - Fax | BallotFaxNumber | Provide fax number for delivery |
| Military/Overseas - Mail | BallotDeliveryMethod | Preferred ballot delivery method |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City or City Special Election | ElectionType | City or city special election |
| June (Primary) Election | ElectionDate | Checkbox for primary election |
| November (General) Election | ElectionDate | Checkbox for general election |
| School or School Special Election | ElectionType | School or school special election |
| State or County Special Election | ElectionType | State or county special election |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Military/Overseas - Citizen Living Outside US | MilitaryOrOverseasStatus | US citizen outside US |
| Military/Overseas - Uniformed Service or Family Member (outside US) | MilitaryOrOverseasStatus | Living away from residence, outside US |
| Military/Overseas - Uniformed Service or Family Member (within US) | MilitaryOrOverseasStatus | Living away from residence, yet within US |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Applicant Without ID - Daytime Telephone Number | PhoneNumber | Attester phone number |
| City | ResidentialAddress | City |
| Daytime Telephone Number | PhoneNumber | Required |
| Residential Address | ResidentialAddress | Required |
| State | ResidentialAddress | State (ND) |
| Voter's Name | PersonName | Required |
| ZIP Code | ResidentialAddress | Zip code |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Applicant Without ID - Attester's Driver's/Non-driver's/Tribal ID Number | IdentificationNumbers | Attester's ND ID number |
| Driver's License | DriverLicenseNumber | Check one ID type |
| ID Number | IdentificationNumbers | Required only if DL, non-driver ID, tribal, passport, or military ID selected |
| Non-driver's ID | StateIDNumber | Non-driver's ID |
| Passport or Military ID | PassportOrMilitaryID | Only for voters living outside US |
| Tribal ID | TribalID | Tribal ID |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Applicant Without ID | StatementNoIDAvailable | If applicant has no ID |
| Long-term Care Certificate | CopyOfPhotoID | Include with application |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Applicant Without ID - Date | SignatureDate | Date attester signed |
| Date | SignatureDate | Date signed |
| Printed Name of Person Making Mark | AssistantInformation | Name of person making mark or using signature stamp |
| Signature | VoterSignature | Required; affirm resided/will reside in precinct 30 days before election |
| Signature of Witness to the Mark | WitnessInformation | Disinterested individual witnesses mark |
| Voter's Mark | VoterSignature | If unable to sign; mark or signature stamp in presence of disinterested individual |

