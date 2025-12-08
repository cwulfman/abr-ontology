# Wyoming (WY) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Wyoming Absentee Ballot Request Form (08/2025). Must be registered voter to request Absentee Ballot. For Primary Election, political party is required and must be same political party currently registered with. To change political party, contact county clerk. If not registered voter, use Wyoming Voter Registration Form and send to county clerk when completed. Check all elections that apply: 2026 PRIMARY (specify Political Party) and/or 2026 GENERAL. If want someone to pick up ballot and deliver to you, MUST fill in section and designate individual by granting permission to named person. Voter signature required; certify registered voter and entitled to vote in election indicated above. To receive Absentee Ballot, form must be completed and returned to County Clerk. Wyoming County Clerk Contact Information available. Office Use Only section: Precinct, Entered in WyoReg, Mailed, Status (Accepted/Rejected), Rejection Reason.

## Fields Found: 21

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I hereby grant (name) permission to pick up ballot | BallotDeliveryAgent | If want someone to pick up and deliver ballot; MUST fill in and designate individual |
| Mail My Ballot To | BallotMailingAddress | Address where ballot should be mailed |
| Mailing City | BallotMailingAddress | City |
| Mailing State | BallotMailingAddress | State |
| Mailing Zip | BallotMailingAddress | Zip code |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| 2026 GENERAL | ElectionDate | Check for 2026 General |
| 2026 PRIMARY | ElectionDate | Check for 2026 Primary; Political Party required |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Active Military? | MilitaryOrOverseasStatus | Y / N |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Political Party | PartyAffiliation | Required for Primary; must be same as currently registered |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | City |
| Contact Phone Number | PhoneNumber | Required |
| County Residential Address | ResidentialAddress | Required |
| Email | EmailAddress | Optional |
| First Name | FirstName | Required |
| Last Name | LastName | Required |
| Middle | MiddleName | Middle name or initial |
| State | ResidentialAddress | State |
| Zip | ResidentialAddress | Zip code |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date signed |
| Voter Signature | VoterSignature | Required; state registered voter and entitled to vote in election indicated |

