# Kansas (KS) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Kansas form requires current valid KS driver's license or nondriver ID number, OR copy of acceptable photo ID from extensive list (DL from any state, passport, concealed carry license, US military ID, student ID from accredited KS institution, employee badge from government, public assistance ID, Indian tribe ID). Ballot can only be mailed to specific addresses (residential, mailing, temporary residential, or medical care facility) unless voter has illness, disability, or lacks English proficiency. Ballots cannot be mailed until 20 days before election. False statement is severity level 9 nonperson felony.

## Fields Found: 25

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Mailing Address | BallotMailingAddress | If different from residential address |
| Mailing City | BallotMailingAddress | Part of mailing address |
| Mailing State | BallotMailingAddress | Part of mailing address |
| Mailing Zip Code | BallotMailingAddress | Part of mailing address |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Democratic | PartyAffiliation | Party affiliation to receive proper ballot |
| Libertarian | PartyAffiliation | Party affiliation |
| No Labels Kansas | PartyAffiliation | Party affiliation |
| Republican | PartyAffiliation | Party affiliation |
| Unaffiliated | PartyAffiliation | Party affiliation |
| United Kansas | PartyAffiliation | Party affiliation |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | MM/DD/YY format |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | Part of residential address |
| County | ResidentialAddress | County of elector |
| First Name | FirstName | Please print |
| Last Name | LastName | Please print |
| M.I. | MiddleName | Middle initial |
| Phone Number | PhoneNumber | Contact phone |
| Residential Address | ResidentialAddress | Required |
| State | ResidentialAddress | Part of residential address |
| State (where application completed) | ResidentialAddress | State where application completed |
| Zip Code | ResidentialAddress | Part of residential address |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Current Kansas driver's license or nondriver's ID card number | DriverLicenseNumber | Required to receive ballot |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Copy of photo identification | CopyOfPhotoID | If no KS DL or ID; must provide copy from acceptable list |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | MM/DD/YY format |
| Signature of Voter | VoterSignature | Required under penalty of perjury; or authorized person for voter with disability |

