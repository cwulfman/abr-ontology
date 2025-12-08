# Iowa (IA) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Iowa form uses note 'IO' in PDF but this is Iowa (IA). Form requires voter verification number (Iowa DL/Non-Operator ID OR four-digit Voter PIN from Voter ID Card). Any voter may request an Iowa Voter ID Card by contacting County Auditor. Application must be received by County Auditor no later than 5:00 p.m. 15 days before election. Powers of attorney do not have legal authority to request absentee ballot on behalf of another. Contact info can be kept off voter record by checking box.

## Fields Found: 28

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Country (other than USA) | BallotMailingAddress | If mailing address outside USA |
| Mailing Address/P.O. Box | BallotMailingAddress | If different than residential address above |
| Mailing City | BallotMailingAddress | Part of mailing address |
| Mailing State | BallotMailingAddress | Part of mailing address |
| Mailing Zip | BallotMailingAddress | Part of mailing address |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City/School Election | ElectionType | Checkbox for city or school election |
| Election Date | ElectionDate | Specific date of election |
| General Election | ElectionType | Checkbox for general election |
| Primary Election | ElectionType | Checkbox for primary |
| Special Election | ElectionType | Checkbox with date field |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Democratic Party | PartyAffiliation | Party selection for primary |
| Republican Party | PartyAffiliation | Party selection for primary |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | Month, day, year format - Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | Part of residential address |
| County | ResidentialAddress | Must be registered to vote in county to receive absentee ballot |
| Email | EmailAddress | Important - with DO NOT ADD TO VOTER RECORD option |
| First Name | FirstName | Required |
| Home Street Address | ResidentialAddress | Include apt, lot, etc. if applicable - Required |
| Last Name | LastName | Required |
| Middle Name | MiddleName | Middle name |
| Phone | PhoneNumber | Important - with DO NOT ADD TO VOTER RECORD option |
| Suffix | NameSuffix | Jr., Sr., etc. |
| Zip | ResidentialAddress | Part of residential address |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Four-digit Voter PIN | VoterPIN | Found only on Voter Identification Card - Option 2 for voter verification |
| Iowa Driver's License or Non-Operator ID Number | DriverLicenseNumber | Option 1 for voter verification |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| DO NOT ADD THIS INFORMATION TO MY VOTER RECORD | StatementNoIDAvailable | Checkbox to keep contact info private |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date form was signed |
| Signature | VoterSignature | Required signature affirming eligibility |

