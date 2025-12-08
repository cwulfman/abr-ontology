# Vermont (VT) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Vermont Absentee Ballot Request (2025.06). Use form to request absentee ballots for elections in 1 calendar year. All absentee voters must submit new request each year. Can save time by requesting online at vote.vermont.gov. Can choose specific elections (Annual Town Meeting, All local elections, General, Primary, Presidential Primary with party choice) OR can choose period within 1 calendar year (start/stop dates). Military, overseas civilian, ill or with disability voters: select voter type (Military active US/overseas, Overseas voter, Ill/with disability) and ballot delivery method (Email - ballots cannot be returned electronically, Fax, Mail, or Two Justices of Peace - only if ill/with disability). Contact information (phone/email) helpful if have question; confidential. Can request ballot for someone else: requester must complete section with name, organization if applicable, phone, address, and relationship (Family member, Health care provider, Person authorized by voter). Return completed and signed form to Town Clerk by mail, drop off, or email. Find Town Clerk mailing address and email at tinyurl.com/vttcclerks. Track request and ballot at vote.vermont.gov.

## Fields Found: 36

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Ballot delivery - Email | BallotEmailAddress | Ballots cannot be returned electronically |
| Ballot delivery - Fax | BallotFaxNumber | Fax number |
| Ballot delivery - Mail | BallotDeliveryMethod | Mail delivery |
| Ballot delivery - Two Justices of Peace | BallotDeliveryMethod | Only if ill or with disability |
| Mailing City or Town | BallotMailingAddress | City or town |
| Mailing State | BallotMailingAddress | State |
| Mailing Zip | BallotMailingAddress | Zip code |
| Mailing address - Address or P.O. Box | BallotMailingAddress | Where receive mail; where ballot will be sent |
| Mailing address - Same as residential | BallotMailingAddress | Same as section 2 |
| Organization name | BallotDeliveryAgent | If applicable |
| Relationship to voter | AgentRelationship | Family member, Health care provider, or Person authorized by voter |
| Requester's address | BallotDeliveryAgent | Requester address |
| Requester's name | BallotDeliveryAgent | If requesting ballot for someone else |
| Requester's phone | BallotDeliveryAgent | Requester phone |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Election - All local elections | ElectionRangeRequest | All local elections |
| Election - Annual Town Meeting | ElectionType | Vote by mail in following elections |
| Election - General Election | ElectionType | General election |
| Election - Primary Election | ElectionType | Primary election |
| Election period - Start sending ballots on | ElectionRangeRequest | Start date mm/dd/yyyy; within 1 calendar year |
| Election period - Stop sending ballots on | ElectionRangeRequest | End date mm/dd/yyyy; within 1 calendar year |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Military/Overseas/Ill/Disability - Voter type | MilitaryOrOverseasStatus | Military (active US or overseas), Overseas voter, or Ill/with disability - check one |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Election - Presidential Primary - Democratic | PartyAffiliation | Choose party for presidential primary |
| Election - Presidential Primary - Republican | PartyAffiliation | Choose party for presidential primary |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address (not P.O. Box) | ResidentialAddress | Where currently live and registered to vote |
| Ballot delivery - Phone | PhoneNumber | Phone number for Two Justices delivery |
| City or Town | ResidentialAddress | City or town |
| Email | EmailAddress | Helpful if have question; confidential |
| First name | FirstName | Required |
| Former name | FormerName | If name has changed |
| Last name | LastName | Required |
| Middle name | MiddleName | Middle name |
| Phone | PhoneNumber | Helpful if have question; confidential |
| State | ResidentialAddress | VT |
| Zip | ResidentialAddress | Zip code |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | mm/dd/yyyy |
| Voter or requester signature | VoterSignature | Required |

