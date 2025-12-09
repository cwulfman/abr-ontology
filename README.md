# ABR Forms Analysis

**Date**: 2025-12-09
**Prepared by**: Clifford Wulfman, OSET Institute <cliff@osetinstitute.org>

---

## ABR Ontology

An OWL ontology of US absentee ballot request (ABR) form types and the information types they capture.

- **abr_ontology.ttl**: The ontology.  Each state's ABR form is defined as a restriction on a general ABRForm class, one that declares what specific information it requires.

- **states.ttl**: supplementary definition of states

---

## Supporting Documentation

**Primary Deliverable**:
- **ABR_State_Requirements_Analysis.xlsx** 
  - 34 states analyzed
  - 74 information type columns
  - Color-coded for easy reading
  - Summary statistics included

**Per-State Reports** (state_reports/):
- 34 markdown files, one per state
- Fields organized by ontology category
- Detailed notes and requirements
- Section information preserved

**JSON Analyses** (form_analyses/):
- 34 JSON files with structured field data
- Machine-readable format
- Complete field metadata
- Zero unclassifiable fields

---

