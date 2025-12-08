#!/usr/bin/env python3
"""
Generate a comprehensive spreadsheet showing ABR form requirements by state.
This script parses the ontology files and creates a CSV with:
- One row per state
- Columns for each information category
- Boolean values indicating whether each state requires that information
"""

import re
import csv
from collections import defaultdict
from pathlib import Path

# Define the information type hierarchy based on the ontology
INFO_HIERARCHY = {
    'Election Context': [
        'ElectionDate',
        'ElectionType',
        'ElectionParty',
        'ElectionRangeRequest',
        'SpecificElectionIdentifier',
        'ElectionContext',  # Generic parent class
    ],
    'Eligibility Criteria': [
        'CitizenshipStatus',
        'AgeRequirement',
        'ResidencyRequirement',
        'RegistrationLocation',
        'MilitaryOrOverseasStatus',
        'DisabilityStatus',
        'StudentStatus',
        'AddressConfidentialityProgramParticipation',
    ],
    'Reason for Absentee Request': [
        'OutOfCountyTravelReason',
        'IllnessOrDisabilityReason',
        'CaregiverForDisabledPersonReason',
        'WorkConflictReason',
        'ReligiousConflictReason',
        'ElectionOfficialDutiesReason',
        'IncarcerationReason',
        'NursingHomeReason',
        'ExpectedChildbirthReason',
    ],
    'Personal Information - Direct Identifiers': [
        'PersonName',
        'FirstName',
        'LastName',
        'MiddleName',
        'NameSuffix',
        'FormerName',
        'ResidentialAddress',
        'MailingAddress',
        'PhoneNumber',
        'EmailAddress',
    ],
    'Personal Information - ID Numbers': [
        'DriverLicenseNumber',
        'StateIDNumber',
        'Last4SSN',
        'VoterPIN',
        'TribalID',
        'PassportOrMilitaryID',
        'IdentificationNumbers',  # Generic parent class
    ],
    'Personal Information - Demographics': [
        'DateOfBirth',
        'PlaceOfBirth',
        'Gender',
    ],
    'Ballot Delivery Information': [
        'BallotMailingAddress',
        'BallotEmailAddress',
        'BallotFaxNumber',
        'BallotDeliveryAgent',
        'AgentName',
        'AgentRelationship',
        'AgentContactInformation',
        'BallotDeliveryMethod',
        'TemporaryAbsenceAddress',
    ],
    'Party Affiliation Information': [
        'PartyAffiliation',
        'PrimaryBallotChoice',
        'BallotStyleRequest',
    ],
    'Signature and Attestation': [
        'VoterSignature',
        'SignatureDate',
        'WitnessInformation',
        'WitnessName',
        'WitnessAddress',
        'NotaryInformation',
        'NotaryName',
        'NotaryCommissionExpiration',
        'AssistantInformation',
        'AttesterInformation',
    ],
    'Required Documentation (Form Fields)': [
        'CopyOfPhotoID',
        'ProofOfResidence',
        'IDNumbersProvided',
        'StatementNoIDAvailable',
    ],
    'Required Accompanying Documentation': [
        'RequiredPhotoID',
        'RequiredProofOfResidence',
        'RequiredWitnessSignature',
        'RequiredNotary',
        'RequiredAgentCertification',
    ],
}

# All US states
ALL_STATES = [
    'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
    'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD',
    'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH',
    'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WI', 'WV', 'WY'
]

def parse_ontology(ontology_file):
    """Parse the ontology file and extract information types captured by each state form."""
    state_info = defaultdict(set)

    with open(ontology_file, 'r') as f:
        content = f.read()

    # Find all state form definitions
    # Pattern: oset:XX_Form (where XX is state postal code)
    state_forms = re.findall(r'oset:([A-Z]{2})_Form', content)
    state_forms = list(set(state_forms))  # Remove duplicates

    for state in state_forms:
        # Extract the entire form definition for this state
        # Look for the form definition starting with "oset:XX_Form a owl:Class"
        # and ending before the next form definition or end of section
        pattern = rf'oset:{state}_Form\s+(?:a\s+owl:Class\s*;)?\s*rdfs:subClassOf.*?(?=(?:oset:[A-Z]{{2}}_Form|#{{50,}}|\Z))'
        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            # Find all information types this form captures or requires
            # Look for owl:someValuesFrom followed by an information type
            info_types = re.findall(r'owl:someValuesFrom\s+oset:(\w+)', match)
            state_info[state].update(info_types)

    return state_info

def generate_spreadsheet(state_info, output_file):
    """Generate a CSV spreadsheet showing which information each state requires."""

    # Prepare column headers
    headers = ['State', 'State Code', 'Form Defined']

    # Add columns for each information category and type
    for category, info_types in INFO_HIERARCHY.items():
        for info_type in info_types:
            headers.append(f"{category}|{info_type}")

    # Prepare rows
    rows = []
    for state_code in sorted(ALL_STATES):
        row = {
            'State': get_state_name(state_code),
            'State Code': state_code,
            'Form Defined': 'Yes' if state_code in state_info else 'No'
        }

        # For each information type, check if this state requires it
        for category, info_types in INFO_HIERARCHY.items():
            for info_type in info_types:
                column_name = f"{category}|{info_type}"
                if state_code in state_info:
                    row[column_name] = 'Yes' if info_type in state_info[state_code] else 'No'
                else:
                    row[column_name] = 'N/A'

        rows.append(row)

    # Write to CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Spreadsheet generated: {output_file}")
    print(f"Total states: {len(ALL_STATES)}")
    print(f"States with forms defined: {len(state_info)}")
    print(f"States without forms: {len(ALL_STATES) - len(state_info)}")

def get_state_name(state_code):
    """Return the full name of a state given its postal code."""
    state_names = {
        'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AZ': 'Arizona',
        'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
        'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'IA': 'Iowa',
        'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas',
        'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland',
        'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri',
        'MS': 'Mississippi', 'MT': 'Montana', 'NC': 'North Carolina', 'ND': 'North Dakota',
        'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico',
        'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma',
        'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
        'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
        'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WI': 'Wisconsin',
        'WV': 'West Virginia', 'WY': 'Wyoming'
    }
    return state_names.get(state_code, state_code)

def main():
    # File paths
    script_dir = Path(__file__).parent
    ontology_file = script_dir / 'rdf' / 'abr_ontology.ttl'
    output_file = script_dir / 'abr_state_requirements.csv'

    print("Parsing ontology...")
    state_info = parse_ontology(ontology_file)

    print(f"\nFound {len(state_info)} states with defined forms:")
    for state in sorted(state_info.keys()):
        print(f"  {state}: {len(state_info[state])} information types")

    print("\nGenerating spreadsheet...")
    generate_spreadsheet(state_info, output_file)

    print("\nDone!")

if __name__ == '__main__':
    main()
