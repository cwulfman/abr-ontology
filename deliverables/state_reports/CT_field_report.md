# Connecticut (CT) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Connecticut requires separate application for each election, primary, and referendum. Application can be faxed but must also mail with original signature, or ballot won't be counted. Blank ballots can be sent to military beginning 90 days before regular election and to overseas citizens/military 45 days before regular election, ~30 days before primary.

## Fields Found: 31

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| E-mailed to me (Accessible ballot) | BallotEmailAddress | For accessible ballot only |
| E-mailed to me (Section V) | BallotEmailAddress | For Section V military/overseas applicants only |
| Given to me personally | BallotDeliveryMethod | Must apply in person; not mailed |
| Mailed to me personally | BallotDeliveryMethod | With mailing address if different |
| Mailing Address | BallotMailingAddress | If different from home address |
| Supervised Ballot | BallotDeliveryMethod | For institution residents where supervised balloting conducted |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Election, Primary or Referendum | ElectionDate | Specific date |
| Election | ElectionType | Checkbox for election |
| Primary | ElectionType | Checkbox for primary |
| Referendum | ElectionType | Checkbox for referendum |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I am a member of the armed forces needing additional time | MilitaryOrOverseasStatus | Due to military contingencies; blank ballot 90 days before election |
| I am an elector temporarily living overseas | MilitaryOrOverseasStatus | Or member of armed forces/spouse/dependent; blank ballot ~45 days before |
| My active service in the Armed Forces | MilitaryOrOverseasStatus | Reason checkbox |
| Physical disability | DisabilityStatus | Reason checkbox |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Party for Primary | PartyAffiliation | Specify which party if primary |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| E-mail Address | EmailAddress | Email address |
| Home Address | ResidentialAddress | Number, Street, Town |
| Name | PersonName | Full name |
| Telephone No. | PhoneNumber | Contact phone |
| Zip Code | ResidentialAddress | Part of address |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| My absence from my town of residence | OutOfCountyTravelReason | Reason checkbox |
| My duties as election official | ElectionOfficialDutiesReason | At polling place other than own; reason checkbox |
| My religious tenets forbid secular activity | ReligiousConflictReason | Reason checkbox |
| Sickness | IllnessOrDisabilityReason | Reason checkbox |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date Signed | SignatureDate | Date of signature |
| Printed Name of Person Providing Assistance | AssistantInformation | If assistance provided |
| Residence Address of Person Providing Assistance | AssistantInformation | If assistance provided |
| Signature of Applicant | VoterSignature | Required signature |
| Signature of Person Providing Assistance | AssistantInformation | If assistance provided |
| Tel. No. of Person Providing Assistance | AssistantInformation | If assistance provided |

