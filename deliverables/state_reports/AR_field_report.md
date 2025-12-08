# Arkansas (AR) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Arkansas form requires photo ID for bearer/administrator/agent. Bearer may obtain ballots for no more than 2 voters per election. Application can be returned via mail, fax, email, or hand delivery. UOCAVA voters have special provisions for email ballot delivery and extended election coverage.

## Fields Found: 34

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Email ballot delivery | BallotEmailAddress | Only available for UOCAVA voters |
| I will pick up my ballot from county clerk office | BallotDeliveryMethod | Pickup option |
| Mail ballot to address | BallotMailingAddress | Mailing address for ballot |
| Printed Name of Bearer/Administrator/Agent | BallotDeliveryAgent | If picked up via designated bearer |
| Signature of Bearer/Administrator/Agent | BallotDeliveryAgent | If picked up via designated bearer |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| All elections for one calendar year | ElectionRangeRequest | Requires disability, long-term care, or living outside county |
| All elections through next Federal General Election Cycle | ElectionRangeRequest | UOCAVA voters only |
| Annual School Election | ElectionType | School election |
| November General Election/Nonpartisan Judicial Runoff | ElectionType | November election |
| Preferential Primary/Nonpartisan Judicial General | ElectionType | Spring of even-numbered years |
| Special Election | ElectionType | With date specification |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I am a United States citizen residing outside territorial limits | MilitaryOrOverseasStatus | UOCAVA voter |
| I am a spouse or dependent of active service member | MilitaryOrOverseasStatus | UOCAVA voter |
| I am an active service member of US armed services | MilitaryOrOverseasStatus | UOCAVA voter; residing outside county |
| I currently reside outside of the county | ResidencyRequirement | Checkbox option |
| I currently reside within the county | ResidencyRequirement | Checkbox option |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Party Preference: Democratic | PartyAffiliation | For primary election |
| Party Preference: Nonpartisan | PartyAffiliation | For primary election |
| Party Preference: Republican | PartyAffiliation | For primary election |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth of Absentee Voter | DateOfBirth | Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City, State, and Zip Code | ResidentialAddress | Part of residential address |
| Email Address of Absentee Voter | EmailAddress | Email address |
| Phone Number of Absentee Voter | PhoneNumber | Required |
| Printed Name of Absentee Voter | PersonName | Full name |
| Residential Address of Absentee Voter | ResidentialAddress | Required |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I am a resident of a long-term care or residential facility | NursingHomeReason | Checkbox reason; facility must be licensed by state |
| I will be unable to attend due to religious observance | ReligiousConflictReason | Religious discipline or holiday |
| I will be unable to attend the polls due to illness or physical disability | IllnessOrDisabilityReason | Checkbox reason |
| I will be unavoidably absent from my polling site on Election Day | OutOfCountyTravelReason | Checkbox reason |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I received assistance in completing application | AssistantInformation | Checkbox with assistant details required if checked |
| Printed Name of Person Giving Assistance | AssistantInformation | If assistance received |
| Residential Address of Person Giving Assistance | AssistantInformation | If assistance received |
| Signature of Absentee Voter | VoterSignature | Required signature |
| Signature of Person Giving Assistance | AssistantInformation | If assistance received |

