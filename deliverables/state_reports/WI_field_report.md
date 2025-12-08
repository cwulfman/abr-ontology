# Wisconsin (WI) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Wisconsin Application for Absentee Ballot (Municipal Clerk) (EL-121, Rev 2020-06). Can also request at MyVote.wi.gov. PHOTO ID REQUIRED unless qualify for exception. Must be registered to vote before receiving ballot. Confirm registration at https://myvote.wi.gov. Exceptions to photo ID: indefinitely-confined voters (witness signature on envelope), care facility residents served by Special Voting Deputies (both deputies' signatures), care facilities not served by SVDs (authorized representative signature; if also indefinitely confined, no representative needed), Military/Permanent Overseas/Confidential Electors (exempt). Detailed instructions on back. Application must be received by county board by 5:00 p.m. day before election (in-person); by mail must be received no later than 10th day before election. Military and Overseas voters: member of uniformed service/merchant marine on active duty (or spouse/dependent), civilian employee of US, civilian officially attached to uniformed service outside US, Peace Corp volunteer. Permanent Overseas: US citizen, 18+, resided in Wisconsin before leaving US, now living outside US with no intent to return, not registered elsewhere, OR adult child of US citizen who resided in WI before establishing residency abroad (federal offices only; must be registered). Temporary Overseas: US citizen, 18+, WI resident overseas temporarily; intends to return. Military/Overseas may receive ballot by fax or email (must have computer/printer; voted ballots must return by mail). Indefinitely-confined: due to age, illness, infirmity, or disability; receive ballots automatically until no longer confined or fail to return ballot. False statements to obtain ballot: fine up to $1,000 or imprisonment up to 6 months or both. If in-person voter, check box at top.

## Fields Found: 39

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Ballot delivery - C / O | BallotMailingAddress | If someone receiving on voter's behalf |
| Ballot delivery - Care Facility Name | BallotMailingAddress | If applicable |
| Ballot delivery - EMAIL - Email Address | BallotEmailAddress | For Military and Overseas Voters Only; must have computer/printer; voted ballots must return by mail |
| Ballot delivery - FAX - Fax Number | BallotFaxNumber | For Military and Overseas Voters Only; must have computer/printer; voted ballots must return by mail |
| Ballot delivery - MAIL | BallotDeliveryMethod | Default if no preference; ballot will be mailed to address above; cannot be forwarded |
| Ballot delivery - Mailing Address - Street Number & Name | BallotMailingAddress | If different than residence |
| Ballot delivery - Mailing Apt. Number | BallotMailingAddress | Apartment |
| Ballot delivery - Mailing City | BallotMailingAddress | City |
| Ballot delivery - Mailing State & ZIP | BallotMailingAddress | State and ZIP |
| Ballot delivery - VOTE IN CLERK'S OFFICE | BallotDeliveryMethod | Vote in clerk's office |
| Temporarily Hospitalized - Agent Address | BallotDeliveryAgent | Agent address |
| Temporarily Hospitalized - Agent First Name | BallotDeliveryAgent | Agent first name |
| Temporarily Hospitalized - Agent Last Name | BallotDeliveryAgent | If cannot appear due to hospitalization; appoint agent |
| Temporarily Hospitalized - Agent Middle Name | BallotDeliveryAgent | Agent middle name |
| Temporarily Hospitalized - Agent Signature | BallotDeliveryAgent | Agent certifies duly appointed; ballot received solely for elector; will promptly transmit |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Request ballot for all elections through end of calendar year | ElectionRangeRequest | All elections from today through 12/31 |
| Request ballot for election(s) on following date(s) | ElectionDate | Specific election dates |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Indefinitely-confined voters - Request automatic ballots | DisabilityStatus | Certify indefinitely confined due to age, illness, infirmity or disability; request ballots automatically until no longer confined or fail to return ballot; false statements: fine up to $1,000 or imprisonment up to 6 months or both |
| Military | MilitaryOrOverseasStatus | If applicable |
| Permanent Overseas | MilitaryOrOverseasStatus | If applicable |
| Temporary Overseas | MilitaryOrOverseasStatus | If applicable |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date of Birth | DateOfBirth | MM/DD/YYYY - Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Apt. Number | ResidentialAddress | Apartment number |
| City | ResidentialAddress | City |
| County | ResidentialAddress | Required |
| Email | EmailAddress | Optional |
| Fax | PhoneNumber | Fax number - Optional |
| First Name | FirstName | Required |
| Last Name | LastName | Required |
| Middle Name | MiddleName | Middle name |
| Municipality | ResidentialAddress | Town, Village, or City - Required |
| Phone | PhoneNumber | Optional |
| Residence Address - Street Number & Name | ResidentialAddress | Required |
| State & ZIP | ResidentialAddress | State and ZIP code |
| Suffix | NameSuffix | e.g. Jr, Sr, II, etc. |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Assistant - Today's Date | SignatureDate | Date assistant signed |
| Assistant Signature | AssistantInformation | If required; certify application made on request by elector unable to sign due to physical disability |
| Voter - Today's Date | SignatureDate | Date voter signed |
| Voter Signature | VoterSignature | Required for all voters; certify qualified elector, US citizen, 18+ years, resided at address 28+ days, not serving sentence for felony, not disqualified |

