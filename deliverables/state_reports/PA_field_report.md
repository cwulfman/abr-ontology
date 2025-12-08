# Pennsylvania (PA) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Pennsylvania Application for Mail-in Ballot (M, Page 1-2, 05.2024). Deadline to apply: 5:00PM on Tuesday before election; must be received by county board (postmarks don't count). Deadline to return ballot: 8:00PM on election day; must be received by county board (postmarks don't count). Must be registered voter. Must provide PA Driver's License or PennDOT ID card number, OR last 4 of SSN if no DL/ID. If no valid ID, check box and enclose photocopy of acceptable ID. Annual mail-in ballot request available: receive application to renew each year; once approved, automatically receive ballots for remainder of year without additional applications. If update voter registration due to relocation out of county after annual request, ensure annual status transferred. WARNING: If receive mail-in ballot and return by deadline, may not vote at polling place on election day. If unable to return voted mail-in ballot by deadline, may only vote provisional ballot at polling place unless surrender mail-in ballot and return envelope with Voter's Declaration to judge of elections to be voided. Deadline 15 days before election to update address. Return to local county board of elections. Bilingual notice available in Spanish and Chinese.

## Fields Found: 33

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Mailing address - City | BallotMailingAddress | City |
| Mailing address - State | BallotMailingAddress | State |
| Mailing address - Zip | BallotMailingAddress | Zip code |
| This address is my | BallotMailingAddress | e.g. vacation home, temporary residence, etc. |
| Where to mail ballot - Address or PO Box | BallotMailingAddress | Different address or PO Box |
| Where to mail ballot - Same as above | BallotMailingAddress | Same as registration address |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Annual mail-in request | ElectionRangeRequest | Receive mail-in ballots this year and receive annual applications each year; automatic if 65+ or have disability |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I have lived at this address since | ResidencyRequirement | Date moved to address |
| Voting district or precinct | RegistrationLocation | If known |
| Ward | RegistrationLocation | If known |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Birth date | DateOfBirth | Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address (not PO Box) | ResidentialAddress | Required; print exactly as registered; if changed, update voter registration first |
| Apt. number | ResidentialAddress | Apartment number |
| City | ResidentialAddress | City |
| County | ResidentialAddress | County |
| Email | EmailAddress | Optional; used if information missing on form |
| First name | FirstName | Required; print exactly as registered |
| Last name | LastName | Required; print exactly as registered |
| Middle name or initial | MiddleName | Middle name or initial |
| Municipality | ResidentialAddress | Municipality |
| Phone number | PhoneNumber | Optional; used if information missing on form |
| State | ResidentialAddress | PA |
| Suffix | NameSuffix | Jr, Sr, II, III, IV |
| Zip | ResidentialAddress | Zip code |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Last four digits of Social Security number | Last4SSN | If no PA DL or PennDOT ID |
| PA driver's license or PennDOT ID card number | DriverLicenseNumber | Required if have PennDOT number; must use it |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| I do not have PA driver's license or PennDOT ID or SSN | StatementNoIDAvailable | Must enclose photocopy of acceptable ID |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date signed |
| Help with form - Address of witness | WitnessInformation | Witness address |
| Help with form - Date | SignatureDate | Date marked |
| Help with form - Mark of voter | VoterSignature | If unable to sign due to illness or physical disability; make mark in lieu of signature |
| Help with form - Signature of witness | WitnessInformation | Witness signature |
| Voter signature | VoterSignature | Required; original signature signed in ink; declare eligible to vote; information true and correct |

