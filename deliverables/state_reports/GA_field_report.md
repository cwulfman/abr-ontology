# Georgia (GA) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Georgia form requires date of birth AND either GA DL/ID number OR copy of acceptable identification. Form includes extensive list of acceptable IDs (passport, voter ID card, military ID, employee ID, tribal ID, utility bill, paycheck, government check, bank statement). Application must be received 11 days before election. Can be returned by mail, email (as attachment), fax, or in-person. Specific restrictions on who can request ballot on behalf of voter and who can handle completed applications.

## Fields Found: 39

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Email for UOCAVA ballot electronic transmission | BallotEmailAddress | Optional for UOCAVA voters to request electronic ballot |
| Relationship to voter | AgentRelationship | Must specify relationship (mother, father, grandparent, etc.) |
| Signature of authorized and eligible requestor | BallotDeliveryAgent | Must be eligible relative; swears relationship under penalty |
| Temporary ballot mailing address | BallotMailingAddress | Must be in different county unless physically disabled or detained; full address with city, state, zip |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Primary, Election, or Runoff | ElectionDate | MM/DD/YYYY format; must be received 11 days before election |
| I opt-in to receive absentee ballot for rest of election cycle | ElectionRangeRequest | Optional; must be eligible |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| D - Disabled: I am physically disabled | DisabilityStatus | Eligibility reason for opt-in |
| E - Elderly: I am 65 years of age or older | AgeRequirement | Eligibility reason for opt-in |
| I swear voter is physically disabled | DisabilityStatus | Checkbox option for eligibility |
| I swear voter is temporarily residing out of county | ResidencyRequirement | Checkbox option for eligibility |
| U - UOCAVA: uniformed service member or overseas citizen | MilitaryOrOverseasStatus | Eligibility reason for opt-in |
| UOCAVA Status: MOS - Military Overseas | MilitaryOrOverseasStatus | UOCAVA voter status option |
| UOCAVA Status: MST - Military Stateside | MilitaryOrOverseasStatus | UOCAVA voter status option |
| UOCAVA Status: OSP - Overseas Permanent Resident | MilitaryOrOverseasStatus | May vote for federal offices only |
| UOCAVA Status: OST - Overseas Temporary Resident | MilitaryOrOverseasStatus | UOCAVA voter status option |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Democratic ballot type | PartyAffiliation | Required in primary |
| Non Partisan ballot type | PartyAffiliation | Will not have ANY party candidates listed |
| Republican ballot type | PartyAffiliation | Required in primary |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of birth | DateOfBirth | MM/DD/YYYY - Required; must provide AND DL/ID or copy of acceptable ID |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | Part of residential address |
| County | ResidentialAddress | Part of residential address in GA |
| Email address | EmailAddress | Recommended |
| First Name | FirstName | As appears on voter registration |
| Last Name | LastName | As appears on voter registration |
| Middle Name | MiddleName | As appears on voter registration |
| Phone number | PhoneNumber | Recommended |
| Residential Address | ResidentialAddress | Must be on voter registration; no P.O. Box |
| Suffix | NameSuffix | As appears on voter registration |
| Voter name (Page 2 Section 9) | PersonName | First, Middle, Last, Suffix - if someone else requesting on behalf |
| Zip | ResidentialAddress | Part of residential address |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Georgia Driver's License Number | DriverLicenseNumber | Required if have one |
| State Identification Card Number | StateIDNumber | Required if have one and no DL |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I do not have a Georgia Driver's License or Identification Card | StatementNoIDAvailable | If checked, must provide copy of acceptable identification |
| Place identification here | CopyOfPhotoID | Space to attach copy of acceptable ID if no GA DL or ID number |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Assistant's name | AssistantInformation | If voter is illiterate or physically disabled |
| Assistant's signature | AssistantInformation | Required if assisting |
| Date of assistant signature | AssistantInformation | MM/DD/YYYY |
| Date of signature | SignatureDate | MM/DD/YYYY |
| Voter Signature | VoterSignature | Required; use pen, no electronic signatures; swears eligibility under penalty |

