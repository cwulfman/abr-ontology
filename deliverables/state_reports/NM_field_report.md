# New Mexico (NM) - ABR Form Field Analysis

**Form Analyzed:** Yes

## Notes
New Mexico Application for Absentee Ballot / Solicitud para la Boleta de Ausente (NMAV-1, Rev. December 2023). Bilingual form (English/Spanish). Can complete online at NMVote.org. Only one application necessary. County clerk automatically sends ballot to mailing address on certificate of voter registration each time there is statewide election that includes precinct. Email and telephone are optional and only for county clerk use for questions related to application. Can request to be added to voluntary permanent absentee voter list. Fold, seal and mail or deliver application card to Office of the Clerk (County Clerk/Escribano del Condado).

## Fields Found: 10

### Ballot Delivery Information

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Mail ballot to address below | BallotMailingAddress | Complete if different than registered address |

### Election Context

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Permanent Absentee List | ElectionRangeRequest | Request to be added to voluntary permanent absentee voter list; county clerk will automatically send ballot for each statewide election |

### Personal Information - Demographics

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Year of Birth | DateOfBirth | YYYY format - Required |

### Personal Information - Direct Identifiers

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| Address as registered: Street-City-State-Zip | ResidentialAddress | Complete address - Required |
| County | ResidentialAddress | County - Required |
| Email address | EmailAddress | Optional; for county clerk questions about application |
| Print or type voter's name as registered | PersonName | Full name as registered - Required |
| Telephone | PhoneNumber | Optional; for county clerk questions about application |

### Signature and Attestation

| Field Name | Ontology Class | Notes |
|------------|----------------|-------|
| SIGNATURE of registered voter | VoterSignature | Required |
| TODAY'S DATE | SignatureDate | Date application completed - Required |

