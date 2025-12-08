# ABR State Requirements Analysis - Presentation Notes

## For: Rock the Vote Administrators
## Prepared by: OSET Institute

---

## Overview

This analysis demonstrates the complexity and systematic approach needed for overhauling the Rocky absentee ballot request module. The spreadsheet (`ABR_State_Requirements_Analysis.xlsx`) shows what information each state requires on their absentee ballot request forms.

## Key Findings

### Coverage
- **34 of 50 states** have been analyzed and modeled in the ontology
- **16 states** still need to be analyzed
- This represents **68% coverage** of all US states

### Complexity
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

## Why a Systematic Approach is Needed

### Problem: Current Ad-Hoc System

Without a systematic ontology-based approach:
- Each state's requirements must be handled as a special case
- Changes in state laws require manual code updates throughout the system
- No consistent way to validate completeness of data collection
- Difficult to maintain and test
- High risk of errors and omissions

### Solution: Ontology-Based System

The ontology provides:
- **Formal specification** of what each state requires
- **Machine-readable format** that can drive the software directly
- **Systematic coverage** ensuring no requirements are missed
- **Easy maintenance** - update the ontology, not the code
- **Testable** - can automatically verify that all requirements are met
- **Scalable** - easy to add new states or update existing ones

## The Spreadsheet Explained

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
- **Gray cells**: Not applicable (state not analyzed)
- **Gray bottom row**: Summary statistics

## Business Case for Rewrite

### Current Situation
The existing Rocky module likely handles state requirements through:
- Hard-coded logic for each state
- Difficult-to-maintain configuration files
- Incomplete or outdated state requirements
- Manual updates when state laws change

### Proposed Approach
A systematic rewrite based on this ontology would:
1. **Use formal specifications** (the ontology) as the single source of truth
2. **Generate forms dynamically** based on state requirements
3. **Ensure completeness** - systematic approach catches all requirements
4. **Simplify maintenance** - update ontology, not code
5. **Enable validation** - automatically verify forms collect all required data
6. **Support scalability** - easy to add remaining 16 states

### Return on Investment

**Short-term benefits**:
- Correct and complete forms for all 50 states
- Reduced development and testing time
- Fewer errors and user complaints

**Long-term benefits**:
- Easy updates when state laws change
- Scalable to new requirements
- Reusable ontology for other voting initiatives
- Professional, systematic approach demonstrates OSET's technical capability

## Questions & Answers

**Q: Why do some states show "N/A" for everything?**
A: Those 16 states haven't been analyzed yet. They need to be added to complete the system.

**Q: Why do requirements vary so much across states?**
A: Each state sets its own election laws and absentee ballot requirements. This variability is exactly why a systematic approach is needed.

**Q: How does this help voters?**
A: By ensuring Rocky collects exactly the information each state requires - no more, no less - we reduce errors and rejections of absentee ballot requests.

**Q: What's next?**
A:
1. Complete analysis of remaining 16 states
2. Design software architecture based on ontology
3. Implement dynamic form generation
4. Test with actual state forms
5. Deploy updated Rocky module

---

## Contact

For technical questions about this analysis:
- John Sebes, CIO, OSET Institute
- [Contact information]

For questions about Rock the Vote's absentee ballot program:
- [Rock the Vote contact]
