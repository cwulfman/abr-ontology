# ABR State Requirements Analysis
## Prepared by: Clifford Wulfman, OSET Institute
---

## Overview
I analyzed the ABR forms from the 34 states that have them and classified the kinds of information they collect into eleven categories. From these I developed a formal ontology that describes the ABR form for each state in terms of the information it requires.  This representation should simplify the task of identifying common requirements and streamlining Rocky's information-gathering workflow.

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

