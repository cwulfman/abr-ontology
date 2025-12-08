# Indiana (IN) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Indiana form can be mailed, e-mailed, faxed, or hand-delivered. Must be received by 11:59 p.m. (local time) 11-12 days before election. Military and overseas voters should use Federal Post Card Application (FPCA). Application may be delayed if county election board cannot match ID information. Perjury punishable by up to 2.5 years imprisonment and/or $10,000 fine.

## Fields Found: 45

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Mailing Address | BallotMailingAddress | If different from registration address; number and street or P.O. Box |
| Mailing City/Town | BallotMailingAddress | Part of mailing address |
| Mailing Country | BallotMailingAddress | If outside USA |
| Mailing State | BallotMailingAddress | Part of mailing address |
| Mailing Zip Code | BallotMailingAddress | Part of mailing address |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Eligible to vote under fail safe procedures | RegistrationLocation | IC 3-10-11 or IC 3-10-12 |
| Member of Indiana National Guard deployed or public safety officer | MilitaryOrOverseasStatus | National Guard or public safety officer |
| Prevented from voting due to unavailability of transportation | DisabilityStatus | Transportation unavailability |
| Voter at least sixty-five (65) years of age | AgeRequirement | Age 65+ |
| Voter with disabilities | DisabilityStatus | Must contact county election board if unable to mark ballot or sign envelope |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| DEMOCRATIC PARTY ballot | PartyAffiliation | Party ballot request |
| PUBLIC QUESTION ONLY | PartyAffiliation | Do not wish to vote in party's primary |
| REPUBLICAN PARTY ballot | PartyAffiliation | Party ballot request |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City/Town | ResidentialAddress | Part of registration address |
| E-mail Address | EmailAddress | Optional if not filing online |
| Former Name | FormerName | If name changed |
| Indiana County of Residence | ResidentialAddress | County |
| Name | PersonName | Please print |
| Phone Number | PhoneNumber | Optional if not filing online |
| Registration Address | ResidentialAddress | Number and street; no PO Boxes |
| State | ResidentialAddress | Part of registration address |
| Zip Code | ResidentialAddress | Part of registration address |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| IN Driver's License or IN Identification Card Number | DriverLicenseNumber | Required to complete Option 1 or Option 2 |
| Last 4 Digits of SSN | Last4SSN | Alternative ID option |
| Unique Voter ID Number from Voter Registration | VoterPIN | Alternative ID option |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Caring for individual confined due to illness or injury | CaregiverForDisabledPersonReason | Private residence |
| Expect to be absent from county on election day | OutOfCountyTravelReason | Entire 12 hours polls are open |
| Have official election duties outside voting precinct | ElectionOfficialDutiesReason | Election official |
| Scheduled to work at regular place of employment | WorkConflictReason | Entire 12 hours polls are open |
| Serious sex offender | IncarcerationReason | As defined in IC 35-42-4-14(a) |
| Unable to vote due to observance of religious discipline or holiday | ReligiousConflictReason | Entire 12 hours polls are open |
| Will be confined due to illness or injury | IllnessOrDisabilityReason | Residence, health care facility, or hospital |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Photocopy of valid IN driver's license or ID | CopyOfPhotoID | Must comply with state's photo ID law |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date Assistance Provided | AssistantInformation | Date |
| Date Received | SignatureDate | For person who receives completed application from voter |
| Date signed | SignatureDate | Date of signature |
| Date signed by assistant | AssistantInformation | Date assistant signed |
| Mailing Address of assistant | AssistantInformation | Assistant's mailing address |
| Name of person providing assistance | AssistantInformation | If voter needs help completing sections 2-6 |
| Phone Number (day) of assistant | AssistantInformation | Daytime phone |
| Phone Number (night) of assistant | AssistantInformation | Evening phone |
| Registration Address of assistant | AssistantInformation | Assistant's registration address |
| Signature of Person Assisting Voter | AssistantInformation | Assistant's signature |
| Signature of Voter | VoterSignature | Required; or person designated to sign for voter with disabilities |

