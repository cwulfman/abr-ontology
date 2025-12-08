#!/usr/bin/env python3
"""
Analyze ABR form PDFs and extract all form fields.
This script will be used interactively with Claude to analyze each PDF.
"""

import json
from pathlib import Path
from collections import defaultdict

# Information type classifications based on ontology
FIELD_CLASSIFICATIONS = {
    # Election Context
    'ElectionDate': 'Election Context',
    'ElectionType': 'Election Context',
    'ElectionParty': 'Election Context',
    'ElectionRangeRequest': 'Election Context',
    'SpecificElectionIdentifier': 'Election Context',
    'ElectionContext': 'Election Context',

    # Eligibility Criteria
    'CitizenshipStatus': 'Eligibility Criteria',
    'AgeRequirement': 'Eligibility Criteria',
    'ResidencyRequirement': 'Eligibility Criteria',
    'RegistrationLocation': 'Eligibility Criteria',
    'MilitaryOrOverseasStatus': 'Eligibility Criteria',
    'DisabilityStatus': 'Eligibility Criteria',
    'StudentStatus': 'Eligibility Criteria',
    'AddressConfidentialityProgramParticipation': 'Eligibility Criteria',

    # Reason for Absentee Request
    'OutOfCountyTravelReason': 'Reason for Absentee Request',
    'IllnessOrDisabilityReason': 'Reason for Absentee Request',
    'CaregiverForDisabledPersonReason': 'Reason for Absentee Request',
    'WorkConflictReason': 'Reason for Absentee Request',
    'ReligiousConflictReason': 'Reason for Absentee Request',
    'ElectionOfficialDutiesReason': 'Reason for Absentee Request',
    'IncarcerationReason': 'Reason for Absentee Request',
    'NursingHomeReason': 'Reason for Absentee Request',
    'ExpectedChildbirthReason': 'Reason for Absentee Request',

    # Personal Information - Identifiers
    'PersonName': 'Personal Information - Direct Identifiers',
    'FirstName': 'Personal Information - Direct Identifiers',
    'LastName': 'Personal Information - Direct Identifiers',
    'MiddleName': 'Personal Information - Direct Identifiers',
    'NameSuffix': 'Personal Information - Direct Identifiers',
    'FormerName': 'Personal Information - Direct Identifiers',
    'ResidentialAddress': 'Personal Information - Direct Identifiers',
    'MailingAddress': 'Personal Information - Direct Identifiers',
    'PhoneNumber': 'Personal Information - Direct Identifiers',
    'EmailAddress': 'Personal Information - Direct Identifiers',

    # Personal Information - ID Numbers
    'DriverLicenseNumber': 'Personal Information - ID Numbers',
    'StateIDNumber': 'Personal Information - ID Numbers',
    'Last4SSN': 'Personal Information - ID Numbers',
    'VoterPIN': 'Personal Information - ID Numbers',
    'TribalID': 'Personal Information - ID Numbers',
    'PassportOrMilitaryID': 'Personal Information - ID Numbers',
    'IdentificationNumbers': 'Personal Information - ID Numbers',

    # Personal Information - Demographics
    'DateOfBirth': 'Personal Information - Demographics',
    'PlaceOfBirth': 'Personal Information - Demographics',
    'Gender': 'Personal Information - Demographics',

    # Ballot Delivery Information
    'BallotMailingAddress': 'Ballot Delivery Information',
    'BallotEmailAddress': 'Ballot Delivery Information',
    'BallotFaxNumber': 'Ballot Delivery Information',
    'BallotDeliveryAgent': 'Ballot Delivery Information',
    'AgentName': 'Ballot Delivery Information',
    'AgentRelationship': 'Ballot Delivery Information',
    'AgentContactInformation': 'Ballot Delivery Information',
    'BallotDeliveryMethod': 'Ballot Delivery Information',
    'TemporaryAbsenceAddress': 'Ballot Delivery Information',

    # Party Affiliation Information
    'PartyAffiliation': 'Party Affiliation Information',
    'PrimaryBallotChoice': 'Party Affiliation Information',
    'BallotStyleRequest': 'Party Affiliation Information',

    # Signature and Attestation
    'VoterSignature': 'Signature and Attestation',
    'SignatureDate': 'Signature and Attestation',
    'WitnessInformation': 'Signature and Attestation',
    'WitnessName': 'Signature and Attestation',
    'WitnessAddress': 'Signature and Attestation',
    'NotaryInformation': 'Signature and Attestation',
    'NotaryName': 'Signature and Attestation',
    'NotaryCommissionExpiration': 'Signature and Attestation',
    'AssistantInformation': 'Signature and Attestation',
    'AttesterInformation': 'Signature and Attestation',

    # Required Documentation
    'CopyOfPhotoID': 'Required Documentation',
    'ProofOfResidence': 'Required Documentation',
    'IDNumbersProvided': 'Required Documentation',
    'StatementNoIDAvailable': 'Required Documentation',

    # Required Accompanying Documentation
    'RequiredPhotoID': 'Required Accompanying Documentation',
    'RequiredProofOfResidence': 'Required Accompanying Documentation',
    'RequiredWitnessSignature': 'Required Accompanying Documentation',
    'RequiredNotary': 'Required Accompanying Documentation',
    'RequiredAgentCertification': 'Required Accompanying Documentation',
}

def create_state_analysis_template():
    """Create a template for state analysis."""
    return {
        'state_code': '',
        'state_name': '',
        'form_analyzed': True,
        'fields': [],  # List of {'field_name': '', 'ontology_class': '', 'notes': ''}
        'unclassifiable_fields': [],
        'notes': ''
    }

def save_state_analysis(state_code, analysis, output_dir='form_analyses'):
    """Save state analysis to JSON file."""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    filename = output_path / f'{state_code}_analysis.json'
    with open(filename, 'w') as f:
        json.dump(analysis, f, indent=2)

    return filename

def load_all_analyses(analyses_dir='form_analyses'):
    """Load all state analyses."""
    analyses_path = Path(analyses_dir)
    if not analyses_path.exists():
        return {}

    analyses = {}
    for json_file in analyses_path.glob('*_analysis.json'):
        state_code = json_file.stem.replace('_analysis', '')
        with open(json_file, 'r') as f:
            analyses[state_code] = json.load(f)

    return analyses

def generate_state_report(state_code, analysis, output_dir='state_reports'):
    """Generate a human-readable report for a state."""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    report_file = output_path / f'{state_code}_field_report.md'

    with open(report_file, 'w') as f:
        f.write(f"# {analysis['state_name']} ({state_code}) - ABR Form Field Analysis\n\n")
        f.write(f"**Form Analyzed:** {'Yes' if analysis.get('form_analyzed', False) else 'No'}\n\n")

        if analysis.get('notes'):
            f.write(f"## Notes\n{analysis['notes']}\n\n")

        # Group fields by category
        fields_by_category = defaultdict(list)
        for field in analysis.get('fields', []):
            ontology_class = field.get('ontology_class', 'UNCLASSIFIED')
            category = FIELD_CLASSIFICATIONS.get(ontology_class, 'UNCLASSIFIED')
            fields_by_category[category].append(field)

        f.write(f"## Fields Found: {len(analysis.get('fields', []))}\n\n")

        # Write fields by category
        for category in sorted(fields_by_category.keys()):
            f.write(f"### {category}\n\n")
            f.write("| Field Name | Ontology Class | Notes |\n")
            f.write("|------------|----------------|-------|\n")

            for field in sorted(fields_by_category[category], key=lambda x: x.get('field_name', '')):
                field_name = field.get('field_name', 'N/A')
                ontology_class = field.get('ontology_class', 'N/A')
                notes = field.get('notes', '').replace('\n', ' ')
                f.write(f"| {field_name} | {ontology_class} | {notes} |\n")

            f.write("\n")

        # Write unclassifiable fields
        if analysis.get('unclassifiable_fields'):
            f.write("## Unclassifiable Fields\n\n")
            f.write("These fields could not be classified into existing ontology categories:\n\n")
            for field in analysis['unclassifiable_fields']:
                f.write(f"- **{field.get('field_name', 'N/A')}**: {field.get('description', 'No description')}\n")
            f.write("\n")

    return report_file

def main():
    """Main function - placeholder for interactive use."""
    print("This script is designed to be used interactively.")
    print("Use the functions to create, save, and load state analyses.")

    # Example usage
    print("\nExample usage:")
    print("analysis = create_state_analysis_template()")
    print("analysis['state_code'] = 'AK'")
    print("analysis['state_name'] = 'Alaska'")
    print("analysis['fields'].append({'field_name': 'First Name', 'ontology_class': 'FirstName', 'notes': 'Section 3'})")
    print("save_state_analysis('AK', analysis)")
    print("generate_state_report('AK', analysis)")

if __name__ == '__main__':
    main()
