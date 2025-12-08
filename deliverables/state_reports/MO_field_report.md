# Missouri (MO) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Missouri absentee ballot request form (§§ 115.279, 115.283, 115.284, 115.427, effective 8/2022). Requests must be received by 5:00 p.m. on second Wednesday prior to election day if ballot is mailed. Deadline for in-person absentee voting is 5:00 p.m. on day before election. First-time mail voters must provide copy of: (1) nonexpired MO driver's/nondriver's license, (2) nonexpired military ID including veteran's ID, (3) nonexpired US passport, or (4) other photo ID issued by US or Missouri that is either not expired or expired after most recent general election. Six reasons allowed for requesting absentee ballot.

## Fields Found: 17

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Mailing Address - City, State, Zip | BallotMailingAddress | City, State, Zip Code for mailing |
| Mailing Address - Street or PO Box | BallotMailingAddress | Where ballot should be mailed |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Election Date | ElectionDate | Date of election |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address Confidentiality Program | AddressConfidentialityProgramParticipation | Certified participation in address confidentiality program due to safety concerns |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Political Party Ballot | PartyAffiliation | Name of political party ballot for primary |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Printed Name | PersonName | Full name - Required |
| Registration Address - City, State, Zip | ResidentialAddress | City, State, Zip Code |
| Registration Address - Street | ResidentialAddress | Street address where registered |
| Telephone Number | PhoneNumber | Include area code |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Last Four Digits of Social Security Number | Last4SSN | For identification purposes |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Absence on Election Day | OutOfCountyTravelReason | Absence from jurisdiction on election day |
| Employment as Election Authority/First Responder/Health Care/Law Enforcement | WorkConflictReason | Employment as election authority or by election authority at location other than polling place; first responder; health care worker; law enforcement |
| Incapacity or Confinement Due to Illness or Physical Disability | IllnessOrDisabilityReason | Illness/disability including caring for person with illness/disability at same address |
| Incarceration | IncarcerationReason | Incarceration with retained voting qualifications |
| Religious Belief or Practice | ReligiousConflictReason | Religious belief or practice |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date signed |
| Signature of Registered Voter | VoterSignature | Required; sworn statement |

