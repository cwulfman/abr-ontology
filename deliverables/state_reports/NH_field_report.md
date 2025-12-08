# New Hampshire (NH) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
New Hampshire Application for State Election Absentee Ballot-RSA 657:4 (September 30, 2025). For Absence, Religious Observance, or Disability. Uniformed and overseas citizen voters residing outside US use federal post card application. Application forms must be received or postmarked within 6 months of election; applications received/postmarked before 6-month period not accepted. Separate form required for each election. Power of attorney not acceptable for signature. Voter must sign and verify identity by one of three methods: (1) include copy of photo ID meeting RSA 659:13,II(a), (2) personally present qualifying photo ID to clerk/designee before ballot issuance, or (3) include notarized signature. Can be used Monday before election for winter storm emergency if elderly/infirm/disabled with safety concerns, or if school/childcare/adult care canceled. Employment obligation includes care of children and infirm adults, with or without compensation. False statement is misdemeanor. Track absentee ballot at https://app.sos.nh.gov. Mail or hand deliver to local city/town clerk.

## Fields Found: 48

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Mail Ballot To - Apt/Unit | BallotMailingAddress | Apartment or unit |
| Mail Ballot To - City/Town | BallotMailingAddress | City or town |
| Mail Ballot To - Street Name | BallotMailingAddress | Street name |
| Mail Ballot To - Street Number | BallotMailingAddress | If different from domicile |
| Mail Ballot To - Ward | BallotMailingAddress | Ward |
| Mail Ballot To - Zip Code | BallotMailingAddress | Zip code |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Requesting for presidential primary (may be absent) | ElectionDate | Date not announced; request 14 days after filing period; only if will be absent |
| State General or Special General Election | ElectionDate | Date of general election |
| State Primary or Special Primary Election | ElectionDate | Date of primary election; Section V required |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Absent from town/city or unable to register due to disability | ResidencyRequirement | Request absentee voter registration forms with ballot |
| Cannot appear on Monday before election - elderly/infirm/disability storm concerns | DisabilityStatus | Winter storm/blizzard/ice storm warning; safety concerns |
| Currently registered to vote | RegistrationLocation | Duly qualified voter currently registered |
| Unable to vote due to disability | DisabilityStatus | Cannot appear in person |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Registered as undeclared, declaring Democratic party | PartyAffiliation | Undeclared now declaring affiliation |
| Registered as undeclared, declaring Republican party | PartyAffiliation | Undeclared now declaring affiliation |
| Registered with Democratic party | PartyAffiliation | Currently registered with party; requesting ballot |
| Registered with Republican party | PartyAffiliation | Currently registered with party; requesting ballot |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Email Address | EmailAddress | Email address |
| First Name | FirstName | Required |
| Last Name | LastName | Required |
| Middle Name | MiddleName | Middle name |
| Phone Number | PhoneNumber | Cell or number for contact before and on election day preferred |
| Suffix | NameSuffix | Jr., Sr., II, III |
| Voting Domicile - Apt/Unit | ResidentialAddress | Apartment or unit |
| Voting Domicile - City/Town | ResidentialAddress | City or town |
| Voting Domicile - Street Name | ResidentialAddress | Street name |
| Voting Domicile - Street Number | ResidentialAddress | Home address where registered |
| Voting Domicile - Ward | ResidentialAddress | Ward |
| Voting Domicile - Zip Code | ResidentialAddress | Zip code |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Cannot appear due to employment obligation | WorkConflictReason | Any time during polling hours; includes care of children and infirm adults |
| Cannot appear due to religious observance | ReligiousConflictReason | Religious commitment |
| Cannot appear on Monday before election - school/childcare/adult care canceled | CaregiverForDisabledPersonReason | Winter storm/blizzard/ice storm warning; need to care for children/infirm adults |
| Confined in penal institution | IncarcerationReason | For misdemeanor or awaiting trial |
| Plan to be absent on election day | OutOfCountyTravelReason | Absent from city, town, or unincorporated place |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| ID Verification - Include copy of photo ID | CopyOfPhotoID | ID meeting RSA 659:13,II(a) requirements |
| ID Verification - Personally present qualifying photo ID | CopyOfPhotoID | To clerk or designee prior to ballot issuance |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Applicant's Signature | VoterSignature | Required |
| Date Signed | SignatureDate | Date applicant signed |
| ID Verification - Notarized signature | NotaryInformation | Notarize signature on application |
| Notarization - Commission Expires | NotaryCommissionExpiration | Notary commission expiration |
| Notarization - County | NotaryInformation | County where notarized |
| Notarization - Date | NotaryInformation | Date signed or attested |
| Notarization - Printed Name of Notarial Officer | NotaryName | Notary name |
| Notarization - Seal | NotaryInformation | Notary seal |
| Notarization - Signature of Notarial Officer | NotaryInformation | Notary signature |
| Notarization - State | NotaryInformation | State where notarized |
| Witness/Assistant Print Name | AssistantInformation | Name of assisting person |
| Witness/Assistant Signature | AssistantInformation | Person assisting voter with disability |

