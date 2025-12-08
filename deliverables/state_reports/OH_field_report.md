# Ohio (OH) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Ohio Absentee Ballot Application (Form 11-A, Prescribed by Ohio Secretary of State, 04/2025; R.C. 3509.03, 3505.24). Must be received by county board of elections no later than close of business 7 days before Election Day. Must be registered voter. If absentee ballot mailed and voter changes mind to vote at polling place on Election Day, must vote provisional ballot. Must provide required information or application cannot be processed. Must provide ONE form of identification: last 4 of SSN, OR Ohio DL/state ID number, OR copy of current photo ID (must include front and back; list of acceptable IDs specified). Separate application required for each election. If primary, partisan ballot will include all questions and issues voter is eligible to vote. If returning ballot in person, must be received by county board before close of polls on Election Day. If returning by mail, must be postmarked no later than day before Election Day and received no later than 4 days after election. Only voter, spouse, child, or near relative may deliver ballot to board for voter. Disabled voter may select any person except employer or union officer. Person delivering for family/disabled voter must complete Form 12-P attestation. Election falsification is felony of fifth degree. Can track application at VoteOhio.gov/track.

## Fields Found: 29

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Mailing Address - City | BallotMailingAddress | City |
| Mailing Address - State | BallotMailingAddress | State |
| Mailing Address - Street Address (or P.O. Box) | BallotMailingAddress | If different than home address |
| Mailing Address - ZIP | BallotMailingAddress | Zip code |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| November General Election | ElectionType | Separate application for each election |
| Primary Election | ElectionDate | Specify date |
| Special Election | ElectionDate | Specify date |

### Party Affiliation Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Democratic | PartyAffiliation | If primary, select ONE party |
| Issues Only | PartyAffiliation | If primary; ballot includes all questions and issues voter is eligible to vote |
| Libertarian | PartyAffiliation | If primary, select ONE party |
| Republican | PartyAffiliation | If primary, select ONE party |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Your date of birth | DateOfBirth | Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | Required |
| County | ResidentialAddress | Required |
| Email | EmailAddress | Recommended; used by board if application incomplete |
| First | FirstName | Required |
| Last | LastName | Required |
| Middle | MiddleName | Middle name |
| State | ResidentialAddress | OH - Required |
| Street Address | ResidentialAddress | Required; no P.O. Boxes or polling place addresses |
| Suffix | NameSuffix | Suffix |
| Telephone Number | PhoneNumber | Recommended; used by board if application incomplete |
| ZIP | ResidentialAddress | Required |

### Personal Information - ID Numbers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Last four digits of Social Security number | Last4SSN | Provide ONE of three options |
| Ohio driver license number or state ID card number | DriverLicenseNumber | Provide ONE of three options |

### Reason for Absentee Request

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Interested in serving as poll worker on Election Day | ElectionOfficialDutiesReason | Optional - Yes/No |

### Required Documentation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Copy of different form of current photo identification | CopyOfPhotoID | DL, state ID, interim ID from OH BMV; US passport/passport card; US military ID, OH National Guard ID, US Dept of Veterans Affairs ID; must include front and back except passport |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Signature | VoterSignature | Required; declare under penalty of election falsification; qualified elector; statements true |
| Today's Date | SignatureDate | Date signed |

