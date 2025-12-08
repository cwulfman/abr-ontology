# Idaho (ID) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
Idaho form is very simple and streamlined. Must be received by County Clerk before 5:00 pm on deadline date (15 days before election for November election, 11 days before for May election). Can also request online at voteidaho.gov. Warning: false information punishable by imprisonment and fine up to $50,000. Contact information optional but becomes public record.

## Fields Found: 23

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Country (if outside USA) | BallotMailingAddress | For international mailing addresses |
| Mailing Address | BallotMailingAddress | If different than residence; ballot will be sent to this address |
| Mailing City | BallotMailingAddress | Part of mailing address |
| Mailing State | BallotMailingAddress | Part of mailing address |
| Mailing Zip Code | BallotMailingAddress | Part of mailing address |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| All Elections in 2025 | ElectionRangeRequest | Including any special or emergency election |
| May 20, 2025 | ElectionDate | Specific election date with request deadline |
| November 4, 2025 | ElectionDate | Specific election date with request deadline |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Birth Year | DateOfBirth | Year only |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Apt./Unit # | ResidentialAddress | Apartment or unit number |
| City | ResidentialAddress | Part of residence address |
| County | ResidentialAddress | County of residence |
| Email Address | EmailAddress | Optional - will become public record |
| First Name | FirstName | Required |
| Last Name | LastName | Required |
| Middle Initial | MiddleName | MI |
| Phone Number | PhoneNumber | Optional - will become public record |
| Residence Address | ResidentialAddress | Street address |
| State | ResidentialAddress | Part of residence address |
| Suffix | NameSuffix | Jr., Sr., etc. |
| Zip Code | ResidentialAddress | Part of residence address |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Date | SignatureDate | Date form was completed |
| Signature of Voter | VoterSignature | Required under penalty of perjury |

