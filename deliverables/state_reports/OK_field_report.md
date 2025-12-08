# Oklahoma (OK) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Oklahoma Application for Absentee Ballot (2023 State of Oklahoma). Applications must be received by County Election Board by 5 p.m. on third Monday (15 days) before election. Valid for up to one calendar year. Uniformed Services/spouses/dependents and Overseas Citizens should use oklahoma.gov/elections/ovp.html or fvap.gov. Must submit own application by mail, email, or fax, or hand deliver to County Election Board. If no ID number or DOB on file, must submit in person, by mail, or fax. EXCEPTION: Voter confined to nursing home/veterans center, physically incapacitated voter, or voter charged with care of physically incapacitated person may choose agent to deliver application. Must provide ID number matching voter registration (OK DL/State ID number OR last 4 of SSN; if unknown, provide both). If inactive voter, identified by National Change of Address as moved, invalid address for USPS mailing, or voter ID card returned as undeliverable, must confirm registration address. Can request for specific elections or all elections in calendar year. Independent voters may request Democratic Primary/Runoff Primary ballot (only Democratic Party allows). Agent delivering application for physically incapacitated/caregiver must be 16+, not employed by/related within 3rd degree to person on ballot, not agent for another person. Felony to knowingly execute false or fraudulent application (26 O.S. § 16-101 and 102.2). Includes separate Address Confirmation Form for certain applicants.

## Fields Found: 31

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Caregiver - Agent signature | BallotDeliveryAgent | Agent must be 16+; not employed by/related within 3rd degree to person on ballot; not agent for another person |
| Caregiver - Print agent name | BallotDeliveryAgent | If selecting agent to hand deliver application |
| Mail ballots to address below - City/Town | BallotMailingAddress | City or town |
| Mail ballots to address below - State | BallotMailingAddress | State |
| Mail ballots to address below - Street | BallotMailingAddress | Different mailing address |
| Mail ballots to address below - ZIP code | BallotMailingAddress | Zip code |
| Mail ballots to address of registration | BallotMailingAddress | Same as registration address |
| Physically incapacitated - Agent signature | BallotDeliveryAgent | Agent must be 16+; not employed by/related within 3rd degree to person on ballot; not agent for another person |
| Physically incapacitated - Print agent name | BallotDeliveryAgent | If selecting agent to hand deliver application |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Request absentee ballots for all elections in calendar year | ElectionRangeRequest | All elections this calendar year |
| Request absentee ballots for only election date(s) listed | ElectionDate | Specific election dates - MM/DD/YYYY |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address confirmation checkbox | ResidencyRequirement | Confirm read/understand address confirmation requirements for certain absentee applicants; understand application cannot be approved if unable to confirm address |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Independent voter requesting Democratic Primary and/or Runoff Primary | PartyAffiliation | Only Democratic Party currently allows Independents to vote in primary/runoff |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of birth | DateOfBirth | MM/DD/YYYY - Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address of registration | ResidentialAddress | Required |
| City/Town | ResidentialAddress | City or town |
| County of registration | ResidentialAddress | County - Required |
| First name | FirstName | Required |
| Last name | LastName | Required |
| M.I. | MiddleName | Middle initial |
| State | ResidentialAddress | State |
| ZIP code | ResidentialAddress | Zip code |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Driver's license number or State ID number | DriverLicenseNumber | If don't know which used for registration, provide both |
| Last four digits of SSN | Last4SSN | If don't know which used for registration, provide both |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Charged with care of physically incapacitated person | CaregiverForDisabledPersonReason | Caregiver for person who cannot be left unattended |
| Incapacitated and confined to nursing facility or veterans center | NursingHomeReason | Nursing home or veterans center |
| None of the above but wish to vote by absentee ballot | OutOfCountyTravelReason | Standard no-excuse absentee |
| Physically incapacitated and cannot vote in person | IllnessOrDisabilityReason | Physical incapacitation |
| Print name of facility | NursingHomeReason | Facility name |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date signed | SignatureDate | Date signed |
| Voter's signature | VoterSignature | Required; swear/affirm eligible to receive ballots requested; confirm registration address and information true and correct |

