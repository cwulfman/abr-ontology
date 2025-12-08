# Michigan (MI) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Michigan Absent Voter Ballot Application (Rev. 08/25). All registered voters can use this form. Can request ballot for specific election(s) or join permanent mail ballot list. Application can be returned by mail, email (scanned with visible signature), delivered in person to clerk/office/authorized assistant/drop box. Immediate family or household members can help deliver; otherwise any MI registered voter can assist (must complete certificate). US Postal Service will not forward ballot; can provide up to 2 temporary addresses with dates. Military/Merchant Marine members can provide CAC signature to return ballot electronically. Not for Address Confidentiality Program participants.

## Fields Found: 38

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address to Mail Ballot 1 - City | BallotMailingAddress | City |
| Address to Mail Ballot 1 - Date Departing | BallotMailingAddress | Departure date for address 1 |
| Address to Mail Ballot 1 - Date of Return | BallotMailingAddress | Return date for address 1 |
| Address to Mail Ballot 1 - State | BallotMailingAddress | State |
| Address to Mail Ballot 1 - Street Address | BallotMailingAddress | Street address for ballot delivery |
| Address to Mail Ballot 1 - ZIP | BallotMailingAddress | Zip code |
| Address to Mail Ballot 2 - City | BallotMailingAddress | City |
| Address to Mail Ballot 2 - Date Departing | BallotMailingAddress | Departure date for address 2 |
| Address to Mail Ballot 2 - Date of Return | BallotMailingAddress | Return date for address 2 |
| Address to Mail Ballot 2 - State | BallotMailingAddress | State |
| Address to Mail Ballot 2 - Street Address | BallotMailingAddress | Second temporary address |
| Address to Mail Ballot 2 - ZIP | BallotMailingAddress | Zip code |
| Certificate - Address | BallotDeliveryAgent | Address of assisting person |
| Certificate - Date | BallotDeliveryAgent | Date certificate signed |
| Certificate - Date of Birth | BallotDeliveryAgent | DOB of assisting person |
| Certificate - Name of Person Assisting | BallotDeliveryAgent | Name of person returning application |
| Certificate - Name of Voter Being Assisted | BallotDeliveryAgent | Voter name |
| Certificate - Signature of Person Assisting | BallotDeliveryAgent | Signature |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| August Election | ElectionDate | August election |
| Automatically send absent voter ballot for future elections | ElectionRangeRequest | Join permanent mail ballot list |
| May Election | ElectionDate | May election |
| November Election | ElectionDate | November election |
| Other Elections | ElectionDate | Specify other election |

### Eligibility Criteria

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| CAC Signature | MilitaryOrOverseasStatus | For uniformed service/Merchant Marine to return ballot electronically |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Year of Birth | DateOfBirth | Year only |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| City | ResidentialAddress | City name |
| City or Township | ResidentialAddress | Checkbox for City or Township; Jurisdiction |
| County | ResidentialAddress | County of registration |
| Email Address | EmailAddress | Used only for official election purposes |
| First Name | FirstName | Required |
| Last Name | LastName | Required |
| M.I. | MiddleName | Middle initial |
| Phone Number | PhoneNumber | Used only for official election purposes |
| State | ResidentialAddress | MI |
| Street Address | ResidentialAddress | Street address |
| ZIP | ResidentialAddress | Zip code |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date signed |
| Handwritten Signature | VoterSignature | Required; power of attorney not acceptable |

