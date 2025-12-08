# Maine (ME) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Maine absentee ballot application for November 4, 2025 Referendum Election. Must be received by Municipal Clerk by close of business on Thursday, October 30, 2025, unless special circumstances exist. Voted ballots must be received by 8 p.m. on election day. Ballot can be delivered to voter, immediate family member, or designated 3rd person. Aide certificate required if applicant received assistance.

## Fields Found: 23

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| 3rd Person Name | AgentName | Name of designated person |
| 3rd Person Telephone # | AgentContactInformation | Phone number of designated person |
| By 3rd Person | BallotDeliveryAgent | Designated by voter |
| By Immediate Family Member of Voter | BallotDeliveryAgent | Delivered to immediate family member |
| By Mail to this Address | BallotMailingAddress | Mailing address for ballot |
| Family Member Name | AgentName | Name of family member |
| Issued to Voter | BallotDeliveryMethod | Application required if voter will vote outside Municipal Clerk's presence |
| Relationship to Voter | AgentRelationship | Family relationship |
| Relationship to Voter (returning ballot) | AgentRelationship | Relationship of person returning ballot |
| Signature of Immediate Family Member Returning Ballot | BallotDeliveryAgent | If ballot delivered to voter or different family member |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Voter's Date of Birth | DateOfBirth | mm-dd-yyyy format |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Daytime Phone Number | PhoneNumber | Contact phone; clerk will use only to notify voter if problem with application or ballot |
| Email Address | EmailAddress | Contact email; clerk will use only to notify voter if problem |
| Full Name of Registered Voter | PersonName | Full name - Required |
| Municipality | ResidentialAddress | City/town |
| Residence Address (Street Address) | ResidentialAddress | Street address where registered |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Aide helped read and sign the application | AssistantInformation | Checkbox if aide helped both read and sign |
| Aide helped read the application | AssistantInformation | Checkbox if aide helped read |
| Aide helped sign the application | AssistantInformation | Checkbox if aide helped sign |
| Date | SignatureDate | Date application signed |
| Printed Name of Aide | AssistantInformation | Aide name |
| Signature of Aide | AssistantInformation | Aide signature |
| Signature of Voter OR Immediate Family Member | VoterSignature | Required |

