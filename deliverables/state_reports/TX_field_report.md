# Texas (TX) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Texas Application for Ballot by Mail. Must provide ONE of following ID numbers: TX Driver's License, TX ID Card, or Election Identification Certificate number; if not issued, provide last 4 of SSN; if no valid ID, check box and must enclose photocopy of acceptable ID. Ballot mailed to residence, mailing address from voter registration, or another address that fits categories (hospital/nursing/care/retirement/assisted living facility or close relative; jail/civil commitment or close relative; other address outside county). Reasons for voting by mail: 65+, disability, expected to give birth within 3 weeks, confined in jail/civilly committed, expected absence from county (provide date range). Annual Application available for voters 65+ or with disability - receive ballot for all elections in voting year. If primary, select Democratic OR Republican (and any runoffs) OR do not send primary ballot. Select elections: May, November, any runoffs, special election. Witness must complete Section 5 if applicant unable to sign and makes mark OR applicant unable to sign/make mark. Assistant must complete if assisted in filling out or submitted on behalf. Failure to complete Section 5 is Class A Misdemeanor if signature/mark witnessed or applicant assisted. Fold and moisten shut to seal; do not use staples. Giving false information is crime. Print and reset buttons available.

## Fields Found: 56

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Mail ballot to mailing address | BallotMailingAddress | My mailing address from voter registration certificate |
| Mail ballot to other address - Number and Street | BallotMailingAddress | Another address that fits one of categories |
| Mail ballot to residence address | BallotMailingAddress | My residence address |
| Other address - Apt/Unit | BallotMailingAddress | Apartment or unit |
| Other address - City | BallotMailingAddress | City |
| Other address - State | BallotMailingAddress | State |
| Other address - Zip Code | BallotMailingAddress | Zip code |
| Other address type - Hospital/nursing home/care facility/retirement center/assisted living | BallotMailingAddress | State relationship if close relative |
| Other address type - Jail/civil commitment facility | BallotMailingAddress | State relationship if close relative |
| Other address type - Other address outside county | BallotMailingAddress | Outside county |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Annual Application - 65+ or have disability | ElectionRangeRequest | Want ballot for all elections in voting year; qualify if 65+ or have disability |
| Request ballot - Any resulting runoff (general) | ElectionDate | Runoff from general election |
| Request ballot - May Election | ElectionDate | May election |
| Request ballot - November Election | ElectionDate | November election |
| Request ballot - Special Election | ElectionDate | Special election - name or date if known |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Reason - 65 years of age or older | AgeRequirement | 65+ years old |
| Reason - Disability | DisabilityStatus | Sickness or physical condition prevents appearance at polling place without personal assistance or injury to health |
| Voter Registration Precinct Number | RegistrationLocation | Optional |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Request ballot - Any resulting runoff (Democratic) | PartyAffiliation | Democratic runoff |
| Request ballot - Any resulting runoff (Republican) | PartyAffiliation | Republican runoff |
| Request ballot - Democratic Primary | PartyAffiliation | Democratic primary |
| Request ballot - Do not send ballot for primary | PartyAffiliation | Do not want primary ballot |
| Request ballot - Republican Primary | PartyAffiliation | Republican primary |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | mm/dd/yyyy |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Apt/Unit | ResidentialAddress | Apartment or unit |
| City | ResidentialAddress | City |
| Email Address | EmailAddress | Optional |
| First Name | FirstName | Required |
| Last Name | LastName | Required |
| Middle Name | MiddleName | If any |
| Residence Address (Number and Street) | ResidentialAddress | Required |
| State | ResidentialAddress | State |
| Suffix | NameSuffix | Jr., Sr., III |
| Telephone Number | PhoneNumber | Optional |
| Zip Code | ResidentialAddress | Zip code |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Last 4 digits of Social Security Number | Last4SSN | If no TX DL/ID/EIC |
| Texas Driver's License/ID/EIC number | DriverLicenseNumber | TX DL, TX ID Card, or Election Identification Certificate - must provide one |
| VUID Number | VoterPIN | Voter unique ID number - optional |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Expected absence - Date range from | OutOfCountyTravelReason | Start date: mm/dd/yyyy |
| Expected absence - Date range to | OutOfCountyTravelReason | End date: mm/dd/yyyy |
| Reason - Confined in jail or involuntarily civilly committed | IncarcerationReason | Confined in jail or committed |
| Reason - Expected absence from county | OutOfCountyTravelReason | Dates during which can receive mail at address outside county |
| Reason - Expected to give birth | ExpectedChildbirthReason | Within 3 weeks before or after Election Day |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I have not been issued TX DL/ID/EIC or SSN | StatementNoIDAvailable | Checkbox |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Applicant Signature | VoterSignature | Required; original signature in ink; certify information true; giving false information is crime |
| Assistant - Check box if assisted | AssistantInformation | If assisted applicant in filling out application in presence or submitted on behalf (by mail, email, fax) |
| Date | SignatureDate | mm/dd/yyyy |
| Witness - Check box if witnessed mark | WitnessInformation | If witnessed applicant make mark or could not sign; state relationship |
| Witness/Assistant - Apt/Unit | AssistantInformation | Apartment or unit |
| Witness/Assistant - Check box if unable to make mark | AssistantInformation | If applicant unable to make mark in Section 4 |
| Witness/Assistant - City | AssistantInformation | City |
| Witness/Assistant - Printed name | AssistantInformation | Name of witness or assistant |
| Witness/Assistant - Residence Address | AssistantInformation | Address |
| Witness/Assistant - Signature | AssistantInformation | Signature; Class A Misdemeanor if fail to complete when applicable |
| Witness/Assistant - State | AssistantInformation | State |
| Witness/Assistant - Zip Code | AssistantInformation | Zip code |

