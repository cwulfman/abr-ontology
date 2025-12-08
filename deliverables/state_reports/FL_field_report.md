# Florida (FL) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Florida form is very simple and streamlined. Request is valid for all elections through end of calendar year of next general election unless specific elections listed. Voter signature not required for absent uniformed services/overseas voters or if request made by designee. Designee relationships are very specifically enumerated with many family relationship options.

## Fields Found: 40

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Country, if outside US | BallotMailingAddress | For overseas mailing address |
| Designee City, State, Zip | BallotDeliveryAgent | Part of designee address |
| Designee Date | BallotDeliveryAgent | Date designee signed |
| Designee Email address (optional) | BallotDeliveryAgent | Designee email |
| Designee Phone number (optional) | BallotDeliveryAgent | Designee phone |
| Designee's Home Address | BallotDeliveryAgent | Designee address |
| Designee's Name | BallotDeliveryAgent | Person requesting ballot for someone else |
| Designee's Signature | BallotDeliveryAgent | Designee must sign and affirm voter directly instructed them |
| Designee's driver license or ID card number | BallotDeliveryAgent | Designee DL or ID |
| Designee's last 4 digits of Social Security Number | BallotDeliveryAgent | If no DL or ID |
| Designee's relationship: Child | AgentRelationship | Relationship option |
| Designee's relationship: Child of voter's spouse | AgentRelationship | Relationship option |
| Designee's relationship: Designee for a voter with a disability | AgentRelationship | Relationship option |
| Designee's relationship: Grandchild | AgentRelationship | Relationship option |
| Designee's relationship: Grandchild of voter's spouse | AgentRelationship | Relationship option |
| Designee's relationship: Grandparent | AgentRelationship | Relationship option |
| Designee's relationship: Grandparent of voter's spouse | AgentRelationship | Relationship option |
| Designee's relationship: Parent | AgentRelationship | Relationship option |
| Designee's relationship: Parent of voter's spouse | AgentRelationship | Relationship option |
| Designee's relationship: Sibling | AgentRelationship | Relationship option |
| Designee's relationship: Sibling of voter's spouse | AgentRelationship | Relationship option |
| Designee's relationship: Spouse | AgentRelationship | Relationship option |
| Designee's relationship: Voter's legal guardian | AgentRelationship | Relationship option |
| Voter's mailing address for ballot | BallotMailingAddress | Only if different than home address |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| List specific elections | SpecificElectionIdentifier | If only want ballot for specific elections |
| Request good for all elections through end of calendar year | ElectionRangeRequest | Through end of calendar year of next general election |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Voter's Date of Birth | DateOfBirth | MM/DD/YYYY format |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | Part of home address |
| Email address (optional) | EmailAddress | Optional email |
| Phone number (optional) | PhoneNumber | Optional phone |
| Please update my mailing address | MailingAddress | Checkbox to update voter record |
| Please update my residential address | ResidentialAddress | Checkbox to update voter record |
| State | ResidentialAddress | Part of home address |
| Voter's Home Address | ResidentialAddress | Home address |
| Voter's Name | PersonName | Full name |
| Zip code | ResidentialAddress | Part of home address |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Last 4 digits of Social Security Number | Last4SSN | If no FL DL or FL ID |
| Voter's Florida driver license or FL ID card number | DriverLicenseNumber | FL DL or FL ID number |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date of signature |
| Voter's Signature | VoterSignature | Not required if absent uniformed services/overseas voter or if request made by designee |

