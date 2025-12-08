# Alabama (AL) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Alabama requires photo ID copy for most absentee ballot reasons (except elderly 65+, voters with disabilities, and military/overseas). Form explicitly states only medical emergency applications may be submitted by voter's designee. Witness signature required only if voter signs by mark rather than signature.

## Fields Found: 33

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Mail my ballot to this address | BallotMailingAddress | Ballot mailing address if different from street address |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Amendments Only | ElectionType | Option to vote on amendments only |
| General Election | ElectionType | Election held in November |
| Primary Election | ElectionType | Checkbox for primary election |
| Primary Runoff Election | ElectionType | Checkbox for primary runoff with party selection |
| Special Election | ElectionType | Special election with date to specify |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I am a member of the Armed Forces | MilitaryOrOverseasStatus | Or spouse/dependent; UOCAVA voter; Photo ID NOT required |
| I am a student at an educational institution | StudentStatus | Outside county of permanent residence; Photo ID required |
| I am a voter with a disability | DisabilityStatus | Photo ID NOT required; detailed disability description provided |
| I am an elderly voter aged 65 or older | AgeRequirement | Photo ID NOT required for this reason |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Select Party: Democratic Party | PartyAffiliation | Party selection for primary |
| Select Party: Republican Party | PartyAffiliation | Party selection for primary |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | Month/Day/Year format |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | Part of residential address |
| Email | EmailAddress | Email address |
| First Name | FirstName | Required field |
| Home/Cell Telephone Number | PhoneNumber | Contact phone number |
| Last Name | LastName | Required field |
| Middle or Maiden Name | MiddleName | Middle or maiden name |
| State | ResidentialAddress | Part of residential address |
| Street Address (Physical Address) | ResidentialAddress | Physical address where registered to vote, no P.O. Box |
| Zip Code | ResidentialAddress | Part of residential address |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Driver's License Number | DriverLicenseNumber | Alabama driver's license number |
| Last 4 digits of SSN if no AL Driver's License | Last4SSN | Alternative to driver's license |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I am a caregiver for a family member | CaregiverForDisabledPersonReason | Family member confined to home; Photo ID required |
| I am currently incarcerated | IncarcerationReason | Must not be convicted of felony involving moral turpitude; Photo ID required |
| I am physically incapacitated | IllnessOrDisabilityReason | Multiple variations of this reason with different photo ID requirements |
| I expect to be out of the county or the state on election day | OutOfCountyTravelReason | Photo ID will be required |
| I expect to work a shift which has at least ten (10) hours | WorkConflictReason | Photo ID required |
| I have been appointed as an election officer | ElectionOfficialDutiesReason | At polling place other than regular; Photo ID required |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Print Witness Name | WitnessName | Required if voter signs by mark |
| Voter's Signature or Mark | VoterSignature | Required signature |
| Witness Signature | WitnessInformation | Required if voter signs by mark |

