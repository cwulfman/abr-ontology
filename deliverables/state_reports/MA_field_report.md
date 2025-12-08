# Massachusetts (MA) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Massachusetts form can be completed by registered voter OR voter's family member (spouse, roommate, parent, sibling, child, aunt, uncle, niece, nephew, grandparent, grandchild, in-law). Use for registered voter unable to vote at polls due to absence, disability, or religious beliefs, OR non-registered voter who is MA citizen absent from state, active armed forces/merchant marines/spouse/dependent, or person confined except for felony. Applications can be mailed, hand-delivered, faxed, or emailed (signature must be visible). Independent voters may vote in primary without registering with party.

## Fields Found: 24

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Application being made by family member | BallotDeliveryAgent | Checkbox if family member making application |
| Designated person to hand-deliver | BallotDeliveryAgent | Person designated to hand-deliver ballot |
| Mail Ballot to | BallotMailingAddress | Address where ballot should be mailed |
| Relationship to voter | AgentRelationship | Relationship if family member |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| A specific election | ElectionDate | Date of specific election |
| All elections this year | ElectionRangeRequest | Request for all elections; valid one calendar year |
| All general elections (No primaries) | ElectionRangeRequest | Only general elections |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Voter is Massachusetts citizen residing overseas | MilitaryOrOverseasStatus | Overseas citizen |
| Voter is member of military or dependent | MilitaryOrOverseasStatus | Military on active duty or dependent |
| Voter required assistance due to physical disability | DisabilityStatus | Required assistance in completing application |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Party (for primary) | PartyAffiliation | Only if requesting primary ballot; independent voters may vote in primary without registering |
| Presidential Primary | PartyAffiliation | Party for presidential primary |
| State Primaries | PartyAffiliation | Party for state primary |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| E-mail Address | EmailAddress | Optional |
| Full Name | PersonName | Required |
| Legal Voting Residence | ResidentialAddress | Required |
| Telephone Number | PhoneNumber | Optional |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Voter admitted to healthcare facility within 7 days | IllnessOrDisabilityReason | Admitted to healthcare facility; designated person to hand-deliver |
| Voter is incarcerated (not for felony) | IncarcerationReason | Incarcerated but not for felony conviction |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Assisting person's address | AssistantInformation | Address of assisting person |
| Assisting person's name | AssistantInformation | Name of assisting person |
| Date | SignatureDate | Date signed |
| Signed | VoterSignature | Signed under penalty of perjury |

