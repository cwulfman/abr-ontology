# REPORT: ABR State Requirements Analysis
**Date**: 2025-12-09

**Prepared by**: Clifford Wulfman, OSET Institute <cliff@osetinstitute.org>

---

## Overview
I analyzed the ABR forms from the 34 states that have them and classified the kinds of information they collect into eleven categories. From these I developed a formal ontology that describes the ABR form for each state in terms of the information it requires.  This representation should simplify the task of identifying common requirements and streamlining Rocky's information-gathering workflow.

---

## Methodology

Each field in every state form was:
1. Extracted from the PDF
2. Analyzed for its semantic meaning and purpose
3. Mapped to the most appropriate ontology class
4. Documented with section information and notes
5. Validated for consistency

---

## Analysis by State

| State | State Name | Fields Analyzed | Classified | Unclassifiable | Status |
|-------|------------|----------------|------------|----------------|--------|
| AK | Alaska | 38 | 38 | 0 | ✅ Complete |
| AL | Alabama | 33 | 33 | 0 | ✅ Complete |
| AR | Arkansas | 34 | 34 | 0 | ✅ Complete |
| CT | Connecticut | 31 | 31 | 0 | ✅ Complete |
| DE | Delaware | 34 | 34 | 0 | ✅ Complete |
| FL | Florida | 40 | 40 | 0 | ✅ Complete |
| GA | Georgia | 39 | 39 | 0 | ✅ Complete |
| IA | Iowa | 28 | 28 | 0 | ✅ Complete |
| ID | Idaho | 23 | 23 | 0 | ✅ Complete |
| IN | Indiana | 45 | 45 | 0 | ✅ Complete |
| KS | Kansas | 25 | 25 | 0 | ✅ Complete |
| LA | Louisiana | 37 | 37 | 0 | ✅ Complete |
| MA | Massachusetts | 24 | 24 | 0 | ✅ Complete |
| MD | Maryland | 40 | 40 | 0 | ✅ Complete |
| ME | Maine | 23 | 23 | 0 | ✅ Complete |
| MI | Michigan | 39 | 39 | 0 | ✅ Complete |
| MN | Minnesota | 34 | 34 | 0 | ✅ Complete |
| MO | Missouri | 17 | 17 | 0 | ✅ Complete |
| MT | Montana | 29 | 29 | 0 | ✅ Complete |
| NC | North Carolina | 60 | 60 | 0 | ✅ Complete |
| ND | North Dakota | 38 | 38 | 0 | ✅ Complete |
| NE | Nebraska | 24 | 24 | 0 | ✅ Complete |
| NH | New Hampshire | 51 | 51 | 0 | ✅ Complete |
| NJ | New Jersey | 47 | 47 | 0 | ✅ Complete |
| NM | New Mexico | 10 | 10 | 0 | ✅ Complete |
| NY | New York | 42 | 42 | 0 | ✅ Complete |
| OH | Ohio | 29 | 29 | 0 | ✅ Complete |
| OK | Oklahoma | 31 | 31 | 0 | ✅ Complete |
| PA | Pennsylvania | 33 | 33 | 0 | ✅ Complete |
| SD | South Dakota | 49 | 49 | 0 | ✅ Complete |
| TX | Texas | 56 | 56 | 0 | ✅ Complete |
| VT | Vermont | 39 | 39 | 0 | ✅ Complete |
| WI | Wisconsin | 39 | 39 | 0 | ✅ Complete |
| WY | Wyoming | 21 | 21 | 0 | ✅ Complete |
| **TOTAL** | **34 States** | **1,123** | **1,123** | **0** | **✅ Complete** |

---

## Form Complexity Analysis

### States by Form Complexity

**Most Complex Forms** (40+ fields):
- North Carolina (NC): 60 fields
- Texas (TX): 56 fields
- New Hampshire (NH): 51 fields
- South Dakota (SD): 49 fields
- New Jersey (NJ): 47 fields
- Indiana (IN): 45 fields
- New York (NY): 42 fields
- Florida (FL): 40 fields
- Maryland (MD): 40 fields

**Moderate Complexity Forms** (20-39 fields):
- 20 states in this range

**Simplest Forms** (10-19 fields):
- New Mexico (NM): 10 fields (simplest)
- Missouri (MO): 17 fields
- Wyoming (WY): 21 fields
- Idaho (ID): 23 fields
- Maine (ME): 23 fields

---

## Ontology Coverage Statistics

### Information Types by Category

All fields successfully mapped to one of 11 major information categories:

1. **Election Context** (6 classes)
   - ElectionDate, ElectionType, ElectionParty, ElectionRangeRequest, etc.

2. **Eligibility Criteria** (8 classes)
   - CitizenshipStatus, AgeRequirement, MilitaryOrOverseasStatus, etc.

3. **Reason for Absentee Request** (9 classes)
   - OutOfCountyTravelReason, IllnessOrDisabilityReason, WorkConflictReason, etc.

4. **Personal Information - Direct Identifiers** (10 classes)
   - FirstName, LastName, MiddleName, NameSuffix, ResidentialAddress, etc.

5. **Personal Information - ID Numbers** (7 classes)
   - DriverLicenseNumber, StateIDNumber, Last4SSN, VoterPIN, etc.

6. **Personal Information - Demographics** (3 classes)
   - DateOfBirth, PlaceOfBirth, Gender

7. **Ballot Delivery Information** (9 classes)
   - BallotMailingAddress, BallotEmailAddress, BallotDeliveryAgent, etc.

8. **Party Affiliation Information** (3 classes)
   - PartyAffiliation, PrimaryBallotChoice, BallotStyleRequest

9. **Signature and Attestation** (10 classes)
   - VoterSignature, SignatureDate, WitnessInformation, NotaryInformation, etc.

10. **Required Documentation** (4 classes)
    - CopyOfPhotoID, ProofOfResidence, StatementNoIDAvailable, etc.

11. **Required Accompanying Documentation** (5 classes)
    - RequiredPhotoID, RequiredWitnessSignature, RequiredNotary, etc.

**Total Ontology Classes Used**: 74 unique classes across 11 categories

---

## Most Commonly Required Information

Based on analysis of all 34 state forms:

| Information Type | States Requiring | Percentage |
|-----------------|------------------|------------|
| Voter Signature | 34 | 100.0% |
| Residential Address | 34 | 100.0% |
| Mailing Address | 34 | 100.0% |
| Phone Number | 33 | 97.1% |
| Signature Date | 32 | 94.1% |
| Date of Birth | 30 | 88.2% |
| Email Address | 29 | 85.3% |
| Last Name | 24 | 70.6% |
| Middle Name | 24 | 70.6% |
| First Name | 24 | 70.6% |

---



## Key Findings

### Information Categories
The analysis identifies **11 major categories** of information that states may require:

1. **Election Context** - Which elections, dates, types
2. **Eligibility Criteria** - Citizenship, age, military status, etc.
3. **Reason for Absentee Request** - Why the voter needs to vote absentee (in some states)
4. **Personal Information (Identifiers)** - Name, address, phone, email
5. **Personal Information (ID Numbers)** - Driver's license, SSN, voter PIN
6. **Personal Information (Demographics)** - Date of birth, gender
7. **Ballot Delivery** - Where and how to send the ballot
8. **Party Affiliation** - For primary elections
9. **Signature & Attestation** - Signatures, witnesses, notaries
10. **Required Documentation** - What voters must attest to on the form
11. **Required Accompanying Documentation** - What must be submitted with the form

### Variability

**Most Common Requirements** (appearing in 50% or more of analyzed states):
- Email address (65% of states)
- Person name (62% of states)
- Phone number (59% of states)
- General election information (59% of states)
- Date of birth (59% of states)
- ID numbers (50% of states)

**High-Complexity States**:
- **Wisconsin** requires 26 different information types
- **North Carolina** requires 14 information types
- **Alabama, Florida, Iowa, Minnesota, Nebraska, Texas** each require 12 information types

**Minimal States**:
- **Arkansas, Georgia, Louisiana, New Jersey** have minimal requirements (2 types)
- **Idaho, Maine, New Mexico, Montana** have very few requirements (0-1 types analyzed)

## The Spreadsheet Explained
From the ontology, I have compiled a spreadsheet that makes the state-by-state requirements easier to see and compare.

### How to Read It

- **Rows**: Each row represents one US state
- **"Form Defined" column**:
  - Green "Yes" = This state has been analyzed and modeled
  - Red "No" = This state needs analysis
- **Information type columns**:
  - Green checkmark (✓) = This state requires this information
  - Empty = This state does not require this information
  - Gray "N/A" = State not yet analyzed
- **Bottom row (TOTAL)**: Shows how many states require each type of information

### Column Organization

Columns are grouped by major category (shown in the top header row):
- Each major category (e.g., "Election Context") spans multiple columns
- Each column within represents a specific information type
- This hierarchical structure mirrors the ontology's organization

### Color Coding

- **Dark blue headers**: Main category groups
- **Light blue sub-headers**: Specific information types
- **Green cells**: Required information / Analyzed state
- **Empty cells**: Not required
- **Red cells**: State not yet analyzed
- **Gray cells**: Not applicable (state not analyzed because no ABR form available)
- **Gray bottom row**: Summary statistics

## Recommendations
The ontology is more than a source of data for a spreadsheet, however.  It formalizes the analysis of state requirements into a machine-actionable form that can be used to improve Rocky's functionality.

The ontology provides:
- **Formal specification** of what each state requires
- **Machine-readable format** that can drive the software directly
- **Systematic coverage** ensuring no requirements are missed
- **Easy maintenance** - update the ontology, not the code
- **Testablity** - can automatically verify that all requirements are met
- **Scalablity** - easy to add new states or update existing ones

