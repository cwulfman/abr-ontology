# Delaware (DE) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Delaware form can be submitted by email, FAX, or mail. Must be received no later than 4 days before election. Members of Uniformed Services and citizens outside US should use Federal Post Card Application. Can apply online at ivote.de.gov. Social Security Number disclosure is voluntary.

## Fields Found: 34

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address where you want your absentee ballot sent | BallotMailingAddress | If different than home address |
| EMAIL for ballot delivery | BallotEmailAddress | Required if want ballot emailed |
| FAX # | BallotFaxNumber | Required if want ballot faxed |
| Send my ballot by: mail, fax, or email | BallotDeliveryMethod | Only for reason 4 voters |
| Where You Expect to be on Election Day | TemporaryAbsenceAddress | Optional - City & State or City & Country |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| All elections | ElectionRangeRequest | Request for all elections |
| General | ElectionType | Checkbox for general election |
| Make me a permanent absentee voter | ElectionRangeRequest | For reasons 1, 2, 4, 7, 8, or caregiver business/occupation |
| Presidential Primary | ElectionType | Checkbox for presidential primary |
| Primary | ElectionType | Checkbox for primary election |
| Special | ElectionType | Checkbox for special election |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Authorized pursuant to Federal UOCAVA | MilitaryOrOverseasStatus | Reason 7: Uniformed and Overseas Citizens Absentee Voting Act |
| I am in public service of the United States or State of Delaware | MilitaryOrOverseasStatus | Reason 1: Public service, US citizen temporarily outside US, spouse/dependent, or absent due to illness while serving armed forces |
| I am in the armed forces or merchant marine | MilitaryOrOverseasStatus | Reason 2: Armed forces, merchant marine, Red Cross, or USO |
| Otherwise authorized by federal law | MilitaryOrOverseasStatus | Reason 8 |
| Students | StudentStatus | Sub-reason under 3 |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Political Party Affiliation | PartyAffiliation | Party affiliation |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Birth date | DateOfBirth | Date of birth |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | Part of home address |
| Election Day phone # | PhoneNumber | Optional |
| Email address | EmailAddress | Optional - used to update application and ballot status |
| Full name | PersonName | Full name field |
| House or Apartment # and Street | ResidentialAddress | Delaware home address |
| Phone # | PhoneNumber | Phone number |
| Zip Code | ResidentialAddress | Part of home address |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Social Security Number | Last4SSN | Optional - see disclosure on reverse |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Business or occupation of providing care | CaregiverForDisabledPersonReason | Sub-reason under 3: Caring for parent/spouse/child at home requiring constant care |
| Due to the nature of my business or occupation | WorkConflictReason | Reason 3: Includes providing care, students, incarcerated persons |
| I am absent from the district while on vacation | OutOfCountyTravelReason | Reason 5 |
| I am sick or physically disabled | IllnessOrDisabilityReason | Reason 4: Temporarily or permanently |
| Otherwise eligible persons who are incarcerated | IncarcerationReason | Sub-reason under 3 |
| Unable to vote due to religious tenets or teachings | ReligiousConflictReason | Reason 6: At certain time or on certain day |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date signed |
| Signature | VoterSignature | Required signature under penalty of perjury |

