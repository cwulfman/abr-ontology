# Nebraska (NE) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Nebraska Secretary of State Early Voting Ballot Application (Updated July 2024). Applications must be physically signed. Can scan/email, mail, or fax to county election office. Can request ballot starting 120 days before election; must submit by close of business on second Friday before election. Must provide Nebraska driver's license/state ID number OR photocopy of acceptable photo ID OR reasonable impediment certification - ballot will not be issued without ID. Acceptable photo IDs include Nebraska DL/ID, US passport, military/veteran's ID, tribal ID, Nebraska political subdivision ID, Nebraska college/university ID, or hospital/care facility record. Free state ID available at DMV for voting purposes; free birth certificates available from DHHS if needed for ID. Reasonable impediments: disability/illness preventing ID obtainment, lack of birth certificate with difficulty obtaining, or religious objection to photography. Contact info can be marked private. Agent may request ballots for up to 2 voters per election. Penalty for election falsification: up to 2 years imprisonment and 12 months post-release supervision, fine up to $10,000, or both. Check ballot status at ne.gov/go/votercheck.

## Fields Found: 24

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Mailing Address | BallotMailingAddress | Different mailing address |
| Mailing Apartment or Lot | BallotMailingAddress | Apartment or lot number |
| Mailing City, State, ZIP | BallotMailingAddress | City, State, ZIP for mailing |
| Printed Name of Agent | BallotDeliveryAgent | If applicable; agent may request ballots for up to 2 voters per election |
| Relationship to Voter | AgentRelationship | Agent's relationship to voter |
| Same as above | BallotMailingAddress | Same as residence address - Required (select one) |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Special Election on (Date) | ElectionDate | Specify date of special election |
| Statewide General Election | ElectionType | Checkbox for general election |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | mm/dd/yyyy format - Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address Where You Live (Residence) | ResidentialAddress | Street address where registered - Required |
| Apt. | ResidentialAddress | Apartment or lot number |
| City | ResidentialAddress | City - MN [should be NE] |
| Email Address | EmailAddress | County election office uses to contact about application; check box if private |
| First | FirstName | Required |
| Last | LastName | Required |
| Middle (name or initial) | MiddleName | Middle name or initial |
| Phone Number | PhoneNumber | County election office uses to contact about application; check box if private |
| Suffix | NameSuffix | Jr, III, if any |
| Zip Code | ResidentialAddress | Zip code |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Nebraska Driver's License or State ID Number | DriverLicenseNumber | Must provide one form of ID |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Enclosed Reasonable Impediment Certification | StatementNoIDAvailable | If reasonable impediment prevents obtaining photo ID |
| Enclosed photocopy of other acceptable photo identification | CopyOfPhotoID | See page 2 for acceptable ID list |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date signed |
| Signature of Voter or Agent | VoterSignature | Required; under penalty of election falsification |

