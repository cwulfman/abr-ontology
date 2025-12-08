# New Jersey (NJ) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
New Jersey Application For Vote by Mail Ballot (02/28/21). Ballot can only be sent to mailing address supplied on application. Voters have option of automatically receiving Mail-In Ballot for all future elections. Must be registered voter to apply. Once applied for Mail-In Ballot, cannot vote by machine at polling place in same election. Application must be received by County Clerk no later than 7 days prior to election; can also apply in person to County Clerk until 3 p.m. day before election; via authorized messenger during office hours but no later than 3 p.m. day prior to election. If returning ballot in person, must be received by County Board of Elections before close of polls on Election Day. If returning by mail, must be postmarked no later than Election Day and received no later than 144 hours (6 days) after close of polls. Military/overseas voters should not use this form unless they are Military or Overseas Voter. Authorized Messenger must be family member or registered voter of county; cannot be candidate in election; max 3 voters per election except 5 if immediate family in same household. Contact info used to contact about acceptance/rejection of ballot and how to cure defect. Do not fax or email unless Military or Overseas Voter.

## Fields Found: 48

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Authorized Messenger - Address | BallotDeliveryAgent | Street address |
| Authorized Messenger - Apt. | BallotDeliveryAgent | Apartment |
| Authorized Messenger - Date of Birth | BallotDeliveryAgent | MM/DD/YYYY |
| Authorized Messenger - I designate (name) | BallotDeliveryAgent | Name of authorized messenger; family member or registered voter of county; max 3 voters except 5 if immediate family in same household |
| Authorized Messenger - Municipality | BallotDeliveryAgent | City/Town |
| Authorized Messenger - Print Name | BallotDeliveryAgent | Messenger name |
| Authorized Messenger - Signature of Messenger | BallotDeliveryAgent | Messenger must sign and show photo ID to County Clerk; certify will deliver directly to voter |
| Authorized Messenger - State | BallotDeliveryAgent | State |
| Authorized Messenger - Zip | BallotDeliveryAgent | Zip code |
| Mail ballot to - Different Address | BallotMailingAddress | Include any PO Box, RD#, State/Province, Zip/Postal Code & Country if outside US |
| Mail ballot to - Same Address as Section 3 | BallotMailingAddress | Same as registration address |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| ALL FUTURE ELECTIONS | ElectionRangeRequest | Until request otherwise in writing |
| Fire | ElectionType | Fire election |
| General (November) | ElectionDate | General election |
| Municipal | ElectionType | Municipal election |
| Primary (June) | ElectionDate | Primary election |
| School | ElectionType | School election |
| Special | ElectionDate | Specify date - MM/DD/YYYY |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Military/Overseas - U.S. Citizen residing outside U.S., do not intend to return | MilitaryOrOverseasStatus | Overseas citizen not intending to return |
| Military/Overseas - U.S. Citizen residing outside U.S., intend to return | MilitaryOrOverseasStatus | Overseas citizen intending to return |
| Military/Overseas - U.S. Citizen residing outside U.S., never lived in U.S. | MilitaryOrOverseasStatus | Overseas citizen never lived in US |
| Military/Overseas - Uniformed Services or Merchant Marine | MilitaryOrOverseasStatus | Active duty member or eligible spouse/dependent |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | MM/DD/YYYY - Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address at which you are registered - Apt. | ResidentialAddress | Apartment number |
| Address at which you are registered - Municipality | ResidentialAddress | City/Town |
| Address at which you are registered - State | ResidentialAddress | State |
| Address at which you are registered - Street Address or RD# | ResidentialAddress | Required |
| Address at which you are registered - Zip | ResidentialAddress | Zip code |
| Day Time Phone Number | PhoneNumber | Used to contact about acceptance/rejection and how to cure defect |
| E-Mail Address | EmailAddress | Used to contact about acceptance/rejection and how to cure defect |
| First Name | FirstName | Type or print - Required |
| Last Name | LastName | Type or print - Required |
| Middle Name or Initial | MiddleName | Type or print |
| Suffix | NameSuffix | Jr., Sr., III |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Assistor - Address | AssistantInformation | Street address |
| Assistor - Apt. | AssistantInformation | Apartment |
| Assistor - Date | AssistantInformation | MM/DD/YYYY |
| Assistor - Municipality | AssistantInformation | City/Town |
| Assistor - Name of Assistor | AssistantInformation | Any person providing assistance must complete this section |
| Assistor - Signature of Assistor | AssistantInformation | Signature |
| Assistor - State | AssistantInformation | State |
| Assistor - Zip | AssistantInformation | Zip code |
| Authorized Messenger - Date | SignatureDate | MM/DD/YYYY |
| Authorized Messenger - Date | SignatureDate | MM/DD/YYYY |
| Authorized Messenger - Signature of Voter | VoterSignature | Voter signature authorizing messenger |
| Date Signature of Voter | SignatureDate | MM/DD/YYYY |
| Today's Date | SignatureDate | MM/DD/YYYY |
| Voter Signature | VoterSignature | Required; affirm I am person applying and live at address in box 3 |

