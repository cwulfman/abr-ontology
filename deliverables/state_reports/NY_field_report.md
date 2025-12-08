# New York (NY) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
New York State Early Mail Ballot Application (2024 Early Vote By Mail Application – English). In-person application must be personally delivered no later than day before election. By mail application must be received no later than 10th day before election. Ballot must be personally delivered to board of elections no later than close of polls on election day, or postmarked by governmental postal service not later than day of election and received no later than 7 days after election. Each person must apply for themselves. Military and overseas voters should use Federal Postcard Application (FPCA). Can sign application or make mark if unable to write due to illness, physical disability, or inability to read (no power of attorney or preprinted name stamps). Voters with print disability can apply for accessible ballot online. Can designate someone to pick up ballot. Felony to make false statement or help anyone cast illegal ballot.

## Fields Found: 40

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| General - Deliver to me in person at board of elections | BallotDeliveryMethod | In-person pickup |
| General - I authorize (give name) to pick up | BallotDeliveryAgent | Authorized person name |
| General - Mail ballot to me at - Apt | BallotMailingAddress | Apartment |
| General - Mail ballot to me at - City | BallotMailingAddress | City |
| General - Mail ballot to me at - State | BallotMailingAddress | State |
| General - Mail ballot to me at - Street name | BallotMailingAddress | Street name |
| General - Mail ballot to me at - Street no. | BallotMailingAddress | Mailing address street number |
| General - Mail ballot to me at - Zip code | BallotMailingAddress | Zip code |
| Primary - Deliver to me in person at board of elections | BallotDeliveryMethod | In-person pickup |
| Primary - I authorize (give name) to pick up | BallotDeliveryAgent | Authorized person name |
| Primary - Mail ballot to me at - Apt | BallotMailingAddress | Apartment |
| Primary - Mail ballot to me at - City | BallotMailingAddress | City |
| Primary - Mail ballot to me at - State | BallotMailingAddress | State |
| Primary - Mail ballot to me at - Street name | BallotMailingAddress | Street name |
| Primary - Mail ballot to me at - Street no. | BallotMailingAddress | Mailing address street number |
| Primary - Mail ballot to me at - Zip code | BallotMailingAddress | Zip code |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| All elections this year | ElectionRangeRequest | All elections this calendar year |
| General Election only | ElectionDate | General election only |
| Primary Election only | ElectionDate | Primary election only |
| Special Election only | ElectionDate | Special election only |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of birth | DateOfBirth | MM/DD/YYYY - Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address where you are registered | ResidentialAddress | Street address - Required |
| Apt | ResidentialAddress | Apartment |
| City | ResidentialAddress | City |
| County where you live | ResidentialAddress | County - Required |
| Email | EmailAddress | Optional |
| First name | FirstName | Required |
| If unable to sign - Name of Voter | PersonName | Voter name |
| Last name or surname | LastName | Required |
| Middle initial | MiddleName | Middle initial |
| Phone number | PhoneNumber | Optional |
| State | ResidentialAddress | NY |
| Suffix | NameSuffix | Suffix |
| Zip code | ResidentialAddress | Zip code |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | MM/DD/YYYY |
| If unable to sign - Address of witness to mark | WitnessInformation | Witness address |
| If unable to sign - Date | SignatureDate | MM/DD/YYYY |
| If unable to sign - Mark | VoterSignature | Mark in lieu of signature; due to illness, disability, or inability to read |
| If unable to sign - Signature of witness to mark | WitnessInformation | Witness signature |
| Voter Signature | VoterSignature | Required; certify qualified and registered voter; information true and correct |

