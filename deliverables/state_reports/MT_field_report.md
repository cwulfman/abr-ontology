# Montana (MT) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Montana Request to be Added/Removed from the Absentee List (2025-10). Registered Montana electors can request to be added to permanent absentee list (all elections), upcoming election only, or be removed from list. Must reside in precinct for at least 30 days before next election. Cannot be serving felony conviction or found to be of unsound mind. Can provide seasonal mailing address with date ranges that can recur annually. Optional designation of another person to pick up ballot. False information may result in fine or imprisonment under federal/state law. Submit to local county elections office.

## Fields Found: 29

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date Ballot Received by Designee | BallotDeliveryAgent | Receipt confirmation |
| Designate person to pick up ballot - Name | BallotDeliveryAgent | Name of designee |
| Does Seasonal Mailing Address occur annually? | BallotMailingAddress | Yes/No checkbox |
| Mailing Address | BallotMailingAddress | Required if different from residence |
| Mailing City and State | BallotMailingAddress | Part of mailing address |
| Mailing Zip Code | BallotMailingAddress | Part of mailing address |
| Seasonal Address Date Range - From | BallotMailingAddress | mm/dd/yyyy - start date for seasonal address |
| Seasonal Address Date Range - To | BallotMailingAddress | mm/dd/yyyy - end date for seasonal address |
| Seasonal City and State | BallotMailingAddress | Part of seasonal address |
| Seasonal Mailing Address | BallotMailingAddress | Optional - for part of year only |
| Seasonal Zip Code | BallotMailingAddress | Part of seasonal address |
| Signature of Designee | BallotDeliveryAgent | Designee signature |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Request absentee ballot for ALL elections | ElectionRangeRequest | Permanent absentee list |
| Request absentee ballot for upcoming election | ElectionDate | Single election only |
| Request to be removed from absentee list | ElectionRangeRequest | Become polling place elector |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Birthdate | DateOfBirth | Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | Required |
| County | ResidentialAddress | Required - verify registration at votemt.gov |
| Email Address | EmailAddress | Optional |
| First Name | FirstName | Required |
| Last Name | LastName | Required |
| Middle Name | MiddleName | Optional |
| Montana Residence Address | ResidentialAddress | Required |
| Phone Number | PhoneNumber | Optional |
| Zip Code | ResidentialAddress | Required |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Required |
| Date Signed (for designation) | SignatureDate | Date of designation |
| Signature of Elector | VoterSignature | Required; under penalty of perjury |
| Signature of Elector (for designation) | VoterSignature | Elector signature for designation |

