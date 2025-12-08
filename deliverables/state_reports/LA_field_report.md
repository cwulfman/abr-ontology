# Louisiana (LA) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Louisiana GENERAL absentee form - NOT for military/overseas, senior citizens, disabled, or nursing home voters (they have separate forms). Voters with valid LA DL/ID may submit electronically via voter portal. Within parish or adjacent parish, ballot can only be sent to registration address, mailing address on file, or address where regularly receive mail. No person except immediate family can deliver or fax more than one voter's application. Faxed application cannot be sent from candidate's fax machine.

## Fields Found: 37

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Ballot Delivery Address | BallotMailingAddress | If different from residence address |
| Relationship to Applicant | AgentRelationship | If hand delivered or faxed |
| Submitted by | BallotDeliveryAgent | If hand delivered or faxed |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| General Election Date | ElectionDate | MM/DD/YYYY |
| Primary Election Date | ElectionDate | MM/DD/YYYY |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| HIGHER EDUCATION | StudentStatus | Student/instructor/professor or spouse/dependent outside parish |
| INVOLUNTARY CONFINEMENT | DisabilityStatus | Confined in mental treatment institution, not interdicted |
| MOVED OUT OF PARISH less than 30 days before election | ResidencyRequirement | Moved >100 miles from parish seat after books closed |
| Ward/Precinct | RegistrationLocation | Optional |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Democratic ballot | PartyAffiliation | For No Party voters in closed primary |
| No Party (Unaffiliated) ballot | PartyAffiliation | For No Party voters |
| Republican ballot | PartyAffiliation | For No Party voters in closed primary |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | Part of residence address |
| Email | EmailAddress | Email address |
| First Name | FirstName | Required |
| Last Name | LastName | Required |
| Middle Name/Initial | MiddleName | Middle name or initial |
| Mother's Maiden Name | FormerName | Required |
| Parish | ResidentialAddress | Louisiana county equivalent |
| Phone | PhoneNumber | Contact phone |
| Residence Address | ResidentialAddress | Required |
| Suffix | NameSuffix | Name suffix |
| Zip Code | ResidentialAddress | Part of residence address |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| LA DL/ID | DriverLicenseNumber | Louisiana driver's license or ID - Optional |
| SSN/Last 4 | Last4SSN | Optional |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Absence End Date | OutOfCountyTravelReason | Required if ballot mailed within parish |
| Absence Start Date | OutOfCountyTravelReason | Required if ballot mailed within parish |
| CLERGY | WorkConflictReason | Minister/priest/rabbi assigned outside parish or spouse/dependent |
| HOSPITALIZED | IllnessOrDisabilityReason | Various hospitalization scenarios; requires proof |
| INCARCERATED | IncarcerationReason | Not under imprisonment for felony conviction; requires sheriff certification |
| OFFSHORE | WorkConflictReason | Out of precinct upon waters of state due to employment |
| TEMPORARILY ABSENT | OutOfCountyTravelReason | Outside state/parish limits during early voting and election day |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date signed |
| Signature | VoterSignature | Required - penalty for false statements: fine up to $2,000 or 2 years imprisonment |
| Witness Signature #1 | WitnessInformation | If signature is a mark, 2 witnesses required; must be 18+ |
| Witness Signature #2 | WitnessInformation | Second witness if signature is a mark |

