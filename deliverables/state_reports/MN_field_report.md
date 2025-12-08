# Minnesota (MN) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
2025 Minnesota Absentee Ballot Application. Must be registered to vote in Minnesota. Requires voter verification number (MN driver's license/ID OR last 4 of SSN). ID number will be compared to absentee ballot envelope. Application must be received no later than 5:00 p.m. 15 days before election. Can submit online at mnvotes.gov/absentee or return paper application by mail, fax, or email. Ballots sent at least 46 days before election (30 days for March town elections). Powers of attorney do not have legal authority to request on behalf of another. Can become permanent absentee voter by marking optional box. Active duty military and overseas voters should use Federal Postcard Application instead. False statement is a felony punishable by up to 5 years imprisonment and/or $10,000 fine.

## Fields Found: 34

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address Where Ballot Should Be Sent | BallotMailingAddress | If different than residential |
| Apt. (mailing) | BallotMailingAddress | Apartment number |
| City (mailing) | BallotMailingAddress | City |
| Country (mailing) | BallotMailingAddress | If outside USA |
| State (mailing) | BallotMailingAddress | State |
| Zip Code (mailing) | BallotMailingAddress | Zip code |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| 11/4 General Election | ElectionDate | Checkbox for general election |
| 2/11 Special Election | ElectionDate | Checkbox for specific election |
| 3/11 Township Election | ElectionDate | Checkbox for township election |
| 4/8 Special Election | ElectionDate | Checkbox for specific election |
| 5/13 Special Election | ElectionDate | Checkbox for specific election |
| 8/12 Primary Election | ElectionDate | Checkbox for primary |
| Both 8/12 & 11/4 Elections | ElectionRangeRequest | Both primary and general |
| Other (specify date) | ElectionDate | Specify other election date |
| Permanent Absentee Voter | ElectionRangeRequest | Mark to have ballot mailed before each election to residence address |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Democratic Party | PartyAffiliation | Party ballot for primary |
| Republican Party | PartyAffiliation | Party ballot for primary |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | mm/dd/yyyy format |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address Where You Live (Residence) | ResidentialAddress | Street address |
| Apt. | ResidentialAddress | Apartment number |
| City | ResidentialAddress | City - MN |
| County Where You Live | ResidentialAddress | County |
| Email Address | EmailAddress | Email address |
| First Name | FirstName | Required |
| Last Name or Surname | LastName | Required |
| Middle Name | MiddleName | Middle name |
| Phone Number | PhoneNumber | Phone number |
| Suffix | NameSuffix | Jr., Sr., etc. |
| Zip Code | ResidentialAddress | Zip code |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Last Four Digits of Social Security Number | Last4SSN | XXX-XX-#### |
| MN-issued Driver's License or MN ID Card Number | DriverLicenseNumber | Minnesota driver's license or ID card |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Do Not Have ID | StatementNoIDAvailable | Checkbox if no MN DL, MN ID, or SSN |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date signed |
| Signature | VoterSignature | Required; under penalty of perjury |

