# South Dakota (SD) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
South Dakota Absentee Ballot Application Form (October 2020). New application must be completed EACH calendar year. May apply for absentee ballot before 5:00 p.m. day before election for any or all general, primary, municipal, school, or any other elections with one request. Must be registered voter; if not registered or military elector, submit Voter Registration Application (EL-131) with this form. Copy of photo ID required OR notarized signature. Acceptable photo IDs: SD DL/non-driver ID, passport, US govt picture ID, tribal photo ID, current SD high school/postsecondary student photo ID. If address changes after submission, must submit new form. For primary, receive ballot of party registration if available; independents/no party can choose Democratic, Libertarian, or Non-Political (only one). Municipal/school elections: must have lived in jurisdiction 30 days in last year OR be full-time student who resided there before leaving. Military and Overseas Citizens: member of Uniformed Services/Merchant Marine on active duty OR spouse/dependent OR US citizen outside US. Military/overseas may request electronic ballot delivery (email; Primary and General only) - not required to submit photo ID; may submit application by fax or email. Authorized Messenger Request (due to sickness or disability only): deadline 3:00 p.m. on Election Day; voter must be confined due to sickness/disability; unable to vote at polling place; messenger acknowledges receipt and indicates if serving for other voters. Return to county auditor in county where registered. Additional information at sdsos.gov.

## Fields Found: 49

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Absentee ballot mailing address | BallotMailingAddress | If different from registration address |
| Authorized Messenger - Address | BallotDeliveryAgent | Messenger address |
| Authorized Messenger - Apt. or Lot # | BallotDeliveryAgent | Apartment or lot |
| Authorized Messenger - City, State | BallotDeliveryAgent | City and state |
| Authorized Messenger - Daytime telephone | BallotDeliveryAgent | Messenger phone |
| Authorized Messenger - First Name | BallotDeliveryAgent | Messenger first name |
| Authorized Messenger - Last Name | BallotDeliveryAgent | Due to sickness or disability only; deadline 3:00 p.m. on Election Day |
| Authorized Messenger - Receipt Date | BallotDeliveryAgent | Date messenger received ballot |
| Authorized Messenger - Receipt Time | BallotDeliveryAgent | Time messenger received ballot |
| Authorized Messenger - Serving for other voter? | BallotDeliveryAgent | Yes/No |
| Authorized Messenger - Zip Code | BallotDeliveryAgent | Zip code |
| Authorized Messenger's Signature | BallotDeliveryAgent | Messenger signature |
| Mailing City, State | BallotMailingAddress | City and state |
| Mailing Zip Code | BallotMailingAddress | Zip code |
| Military/Overseas - E-mail address | BallotEmailAddress | For electronic ballot delivery (Primary and General only); not required to submit photo ID; may submit application by fax or email |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| All | ElectionRangeRequest | All elections this calendar year |
| Any Other | ElectionType | Any other election |
| General | ElectionType | General election |
| Municipal | ElectionType | Municipal election |
| Primary | ElectionType | Primary election |
| School | ElectionType | School election |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Military - Spouse or dependent | MilitaryOrOverseasStatus | Eligible spouse or dependent of member on active duty - Yes/No |
| Military - Uniformed Services or Merchant Marine | MilitaryOrOverseasStatus | Member on active duty - Yes/No |
| Municipal/School - full-time student | StudentStatus | If municipal or school election: full-time student who resided in jurisdiction prior to leaving - Yes/No |
| Municipal/School - lived in jurisdiction 30 days | ResidencyRequirement | If municipal or school election: lived in jurisdiction at least 30 days in last year - Yes/No |
| Overseas - U.S. citizen outside U.S. | MilitaryOrOverseasStatus | U.S. citizen residing outside United States - Yes/No |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Democratic | PartyAffiliation | Democratic primary; receive ballot of party registration if available; if independent/no party can choose party |
| Libertarian | PartyAffiliation | Libertarian primary |
| Non-Political | PartyAffiliation | Non-political; can only mark one |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Apt. or Lot # | ResidentialAddress | Apartment or lot number |
| City, State | ResidentialAddress | City and state |
| County | ResidentialAddress | County where registered |
| Daytime telephone number | PhoneNumber | Daytime phone |
| First Name | FirstName | Required |
| Last Name | LastName | Required |
| Middle Name(s)/Initial | MiddleName | Middle name or initial |
| Suffix | NameSuffix | Suffix |
| Voter Registration Address | ResidentialAddress | Required |
| Zip Code | ResidentialAddress | Zip code |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Copy of photo identification attached | CopyOfPhotoID | SD DL/non-driver ID, passport, US govt picture ID, tribal photo ID, or SD high school/postsecondary student photo ID |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Notarized - Month | NotaryInformation | Month |
| Notarized - Sworn day of | NotaryInformation | Day sworn |
| Notarized - Year | NotaryInformation | Year |
| Notary - My commission expires | NotaryCommissionExpiration | Commission expiration date |
| Notary Seal | NotaryInformation | Seal |
| Notary Signature | NotaryInformation | Notary signature |
| Voter's Date of Signing | SignatureDate | Month/Day/Year |
| Voter's Signature | VoterSignature | Required |
| Voter's Signature (for messenger authorization) | VoterSignature | Voter certifies confined due to sickness/disability; unable to vote at polling place |

