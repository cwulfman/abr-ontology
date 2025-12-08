# Alaska (AK) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Alaska form also requires submission of copy of ID (driver's license, state ID, passport, birth certificate, hunting and fishing license, or current and valid photo ID) when registering to vote. This is mentioned in instructions but not a form field itself.

## Fields Found: 38

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Ballot mailing address | BallotMailingAddress | Address where ballot will be sent if different from permanent mailing address |
| Fax | BallotDeliveryMethod | Checkbox for fax delivery (requires fax in box 13) |
| Fax No. | BallotFaxNumber | Fax number for ballot delivery |
| Mail | BallotDeliveryMethod | Checkbox for mail delivery |
| Online | BallotDeliveryMethod | Checkbox for online delivery (requires email in box 13) |
| Yes, I will be in remote Alaska or overseas where mail service is limited | TemporaryAbsenceAddress | Checkbox indicating need for 45-day advance ballot |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| All in Calendar Year | ElectionRangeRequest | Checkbox to request absentee ballot for all elections in calendar year |
| General (November) | ElectionType | Checkbox for general election |
| Primary (August) | ElectionType | Checkbox for primary election |
| REAA (October) | ElectionType | Checkbox for REAA election |
| Special | ElectionType | Checkbox for special election |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Active member of the Uniformed Services, Merchant Marine, or commissioned corps or an eligible spouse or dependent | MilitaryOrOverseasStatus | Checkbox for military status |
| Are you a citizen of the United States? | CitizenshipStatus | Yes/No checkbox |
| Are you at least 18 years of age or within 90 days of your 18th birthday? | AgeRequirement | Yes/No checkbox |
| I am residing temporarily or permanently overseas and I intend to return to Alaska | MilitaryOrOverseasStatus | Checkbox for overseas voter status |
| Keep my residence address confidential | AddressConfidentialityProgramParticipation | Checkbox to request confidential address |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Write political affiliation | PartyAffiliation | Text field for party affiliation |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Birthdate | DateOfBirth | Required field |
| Gender | Gender | Male/Female selection |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Apt # | ResidentialAddress | Part of residential address |
| City | ResidentialAddress | Part of residential address |
| Day Phone | PhoneNumber | Daytime phone number |
| Email | EmailAddress | Email address |
| Evening Phone | PhoneNumber | Evening phone number |
| First Name | FirstName | Text field for first name |
| Former name (if changed) | FormerName | Text field for previous name if changed |
| House # | ResidentialAddress | Part of residential address |
| Last Name | LastName | Text field for last name |
| Middle Name | MiddleName | Text field for middle name |
| Name Suffix | NameSuffix | Text field for suffix (Jr., Sr., III, etc.) |
| Street Name | ResidentialAddress | Part of residential address |
| The address where you receive mail (Permanent) | MailingAddress | Permanent mailing address (can be different from residence) |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Alaska driver's license or State ID No. | DriverLicenseNumber | Alaska DL or State ID number |
| SSN or Last 4 | Last4SSN | Social Security Number or last 4 digits |
| Voter number (if known) | VoterPIN | Text field for voter registration number |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I do not have an SSN or AK driver's license or State ID | StatementNoIDAvailable | Checkbox if no standard ID available |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date of signature |
| Signature | VoterSignature | Required handwritten signature (not digital) |

