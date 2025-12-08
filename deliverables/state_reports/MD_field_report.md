# Maryland (MD) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Maryland mail-in ballot request form. Any registered voter can use this form. Can be returned by mail, fax, email, or in-person drop-off. Deadlines vary by election and delivery method. Three ballot delivery options: (A) mail to any address, (B) email link to print ballot, (C) fax. If choosing option B or C, voter must use own envelope and postage to return ballot. Can also request ballots for all future elections. Assistance allowed except from candidates, employers, or union officers/agents.

## Fields Found: 40

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Email Address | BallotEmailAddress | For option B - email link |
| Email a link to print my ballot | BallotDeliveryMethod | Option B - Print ballot from emailed link; must use own envelope and stamp |
| Fax Number | BallotFaxNumber | For option C |
| Fax my ballot | BallotDeliveryMethod | Option C - Fax ballot |
| Mailing Address - City | BallotMailingAddress | City |
| Mailing Address - State | BallotMailingAddress | State |
| Mailing Address - Street | BallotMailingAddress | If different from residential |
| Mailing Address - Unit # | BallotMailingAddress | Apartment or unit number |
| Mailing Address - Zip | BallotMailingAddress | Zip code |
| Send ballot by U.S. Mail - Different address | BallotMailingAddress | Option A - Mail to different address or P.O. Box |
| Send ballot by U.S. Mail - Same as residential | BallotMailingAddress | Option A - Mail to registration address |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| All future federal and state elections | ElectionRangeRequest | Permanent mail-in ballot for all future elections |
| Both Primary and General Elections | ElectionRangeRequest | Both 2026 Primary and General Elections |
| General Election only | ElectionDate | November 3, 2026 General Election only |
| Primary Election only | ElectionDate | June 23, 2026 Primary Election only |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Democratic | PartyAffiliation | Party for primary election |
| Green | PartyAffiliation | Green party |
| Other Party | PartyAffiliation | Write-in for other party |
| Republican | PartyAffiliation | Party for primary election |
| Unaffiliated (independent) | PartyAffiliation | Independent of any party |
| Working Class | PartyAffiliation | Working Class party |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | mm/dd/yyyy format - Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Ballot status updates - Email | EmailAddress | Email for updates |
| Ballot status updates - Text message | PhoneNumber | Cell phone for text updates |
| First Name | FirstName | Required |
| Last Name | LastName | Required |
| Middle Name or Initial | MiddleName | Optional |
| Residential Address - City | ResidentialAddress | City |
| Residential Address - State | ResidentialAddress | MD |
| Residential Address - Street | ResidentialAddress | Must match voter registration; no P.O. Boxes |
| Residential Address - Unit # | ResidentialAddress | Apartment or unit number |
| Residential Address - Zip | ResidentialAddress | Zip code |
| Suffix | NameSuffix | Jr., Sr., III, IV, if applicable |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Issue date | DriverLicenseNumber | mm/dd/yyyy - Issue date of MD DL or ID |
| Last 4 digits of Social Security # | Last4SSN | Alternative to DL/ID for option B |
| MD Driver's License or ID Card # | DriverLicenseNumber | Required for option B |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Assistant Signature | AssistantInformation | Required if voter received help; under penalty of perjury |
| Date | SignatureDate | Date form signed - mm/dd/yyyy |
| Print voter name | AssistantInformation | Assistant prints voter's name |
| Voter Signature | VoterSignature | Required; use pen, no electronic signatures |

