# North Carolina (NC) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
North Carolina Absentee Ballot Request Form for 2025 Municipal Elections (2025.01). One voter per form, one election at a time. Information updates current voter record if signed by voter; cannot change party using this form. Must be returned by 5 p.m. on second Tuesday before election. Can be dropped off in person or mailed. Form can only be returned by: voter, voter's near relative or verifiable legal guardian, Multipartisan Assistance Team, or person who assisted due to disability. Near relatives include spouse, brother/sister, parent/stepparent, mother/father-in-law, child/stepchild, son/daughter-in-law, grandparent/grandchild. Voters in facilities have specific assistance limitations. Fraudulently or falsely completing form is Class I felony. Unaffiliated voters can choose party primary without changing registration. Can request accessible electronic ballot for visual impairment. Do not email or fax completed form.

## Fields Found: 59

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Ballot Delivery - Address indicated in section 5 | BallotMailingAddress | US mail to section 5 address |
| Ballot Delivery - Email | BallotEmailAddress | Email delivery for military/overseas |
| Ballot Delivery - Fax | BallotFaxNumber | Fax delivery for military/overseas |
| Ballot Delivery - Overseas address | BallotMailingAddress | US mail to overseas address |
| Overseas Full Address | BallotMailingAddress | Overseas address |
| Relationship to Voter or Status | AgentRelationship | Relationship or status as legal guardian/disability requester |
| Requester's Address - City | BallotDeliveryAgent | City |
| Requester's Address - State | BallotDeliveryAgent | State |
| Requester's Address - Street | BallotDeliveryAgent | Street address |
| Requester's Address - Unit # | BallotDeliveryAgent | Unit number |
| Requester's Address - ZIP | BallotDeliveryAgent | Zip code |
| Requester's Date | BallotDeliveryAgent | Date signed - mm/dd/yyyy |
| Requester's Full Name | BallotDeliveryAgent | Near relative, legal guardian, or disability requester |
| Requester's Phone | BallotDeliveryAgent | Phone number |
| Requester's Signature | BallotDeliveryAgent | Required if requesting on behalf of voter |
| Send ballot to address below - City | BallotMailingAddress | City |
| Send ballot to address below - State | BallotMailingAddress | State |
| Send ballot to address below - Street | BallotMailingAddress | Alternative address |
| Send ballot to address below - Unit # | BallotMailingAddress | Unit number |
| Send ballot to address below - ZIP | BallotMailingAddress | Zip code |
| Send ballot to home address | BallotMailingAddress | Required - select one option |
| Send ballot to mailing address | BallotMailingAddress | From section 4 |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| 09/09/2025 Partisan Primary | ElectionDate | Partisan primary election |
| 10/07/2025 Election or Primary | ElectionDate | Election or primary |
| 11/04/2025 Election or Runoff | ElectionDate | Election or runoff |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Have you moved in the last 30 days? | ResidencyRequirement | Yes/No |
| If yes, date moved? | ResidencyRequirement | mm/dd/yyyy |
| Military - Uniformed Services or Merchant Marines on Active Duty | MilitaryOrOverseasStatus | Uniformed services/Merchant Marines |
| Overseas - U.S. Citizen Outside the U.S. | MilitaryOrOverseasStatus | Overseas address required |
| Require accessible electronic ballot due to visual impairment | DisabilityStatus | Provide email in section 6 |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Unaffiliated voters - Democratic | PartyAffiliation | Unaffiliated voters choosing Democratic primary |
| Unaffiliated voters - Libertarian | PartyAffiliation | Unaffiliated voters choosing Libertarian primary |
| Unaffiliated voters - Republican | PartyAffiliation | Unaffiliated voters choosing Republican primary |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | mm/dd/yyyy format - Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Email | EmailAddress | Optional but helpful; required for accessible electronic ballot |
| First Name | FirstName | Required |
| Former Name | FormerName | If name has changed |
| Home Address - City | ResidentialAddress | City - NC |
| Home Address - County | ResidentialAddress | County |
| Home Address - Street | ResidentialAddress | Residential address - Required |
| Home Address - Unit # | ResidentialAddress | Unit number |
| Home Address - ZIP | ResidentialAddress | Zip code |
| Last Name | LastName | Required |
| Mailing Address - City | ResidentialAddress | City |
| Mailing Address - State | ResidentialAddress | State |
| Mailing Address - Street | ResidentialAddress | If different from home address |
| Mailing Address - Unit # | ResidentialAddress | Unit number |
| Mailing Address - ZIP | ResidentialAddress | Zip code |
| Middle Name | MiddleName | Required |
| Phone | PhoneNumber | Optional but helpful |
| Suffix | NameSuffix | Jr, Sr., III, IV, if applicable |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Last Four Digits of Social Security Number | Last4SSN | Required (alternative to DL/ID) |
| N.C. Driver's License/DMV ID Number | DriverLicenseNumber | Required (one form of ID) |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Due to continued or expected illness or disability, requesting all elections this year | IllnessOrDisabilityReason | Request for all 2025 elections due to illness/disability |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Assistant's Full Address | AssistantInformation | Assistant's address |
| Assistant's Full Name | AssistantInformation | If helping voter fill out or return form |
| Date | SignatureDate | Date signed - mm/dd/yyyy |
| Facility Name | AssistantInformation | If voter in care facility |
| Voter Signature | VoterSignature | Required unless ballot requested by near relative/guardian/disability requester; use pen, no electronic signatures |

