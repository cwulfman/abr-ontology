#!/usr/bin/env python3
"""
Update the ABR ontology with complete field information from all 34 state analyses.
"""

import json
import os
from collections import defaultdict
from pathlib import Path

# Map ontology classes to their parent information types
# This determines which owl:Restriction to add for each class
CLASS_TO_INFO_TYPE = {
    # Election Context
    'ElectionDate': 'oset:ElectionDate',
    'ElectionType': 'oset:ElectionType',
    'ElectionParty': 'oset:ElectionParty',
    'ElectionRangeRequest': 'oset:ElectionRangeRequest',
    'SpecificElectionIdentifier': 'oset:SpecificElectionIdentifier',
    'ElectionContext': 'oset:ElectionContext',

    # Eligibility Criteria
    'CitizenshipStatus': 'oset:CitizenshipStatus',
    'AgeRequirement': 'oset:AgeRequirement',
    'ResidencyRequirement': 'oset:ResidencyRequirement',
    'RegistrationLocation': 'oset:RegistrationLocation',
    'MilitaryOrOverseasStatus': 'oset:MilitaryOrOverseasStatus',
    'DisabilityStatus': 'oset:DisabilityStatus',
    'StudentStatus': 'oset:StudentStatus',
    'AddressConfidentialityProgramParticipation': 'oset:AddressConfidentialityProgramParticipation',

    # Reason for Absentee Request
    'OutOfCountyTravelReason': 'oset:OutOfCountyTravelReason',
    'IllnessOrDisabilityReason': 'oset:IllnessOrDisabilityReason',
    'CaregiverForDisabledPersonReason': 'oset:CaregiverForDisabledPersonReason',
    'WorkConflictReason': 'oset:WorkConflictReason',
    'ReligiousConflictReason': 'oset:ReligiousConflictReason',
    'ElectionOfficialDutiesReason': 'oset:ElectionOfficialDutiesReason',
    'IncarcerationReason': 'oset:IncarcerationReason',
    'NursingHomeReason': 'oset:NursingHomeReason',
    'ExpectedChildbirthReason': 'oset:ExpectedChildbirthReason',

    # Personal Information - Direct Identifiers
    'PersonName': 'oset:PersonName',
    'FirstName': 'oset:FirstName',
    'LastName': 'oset:LastName',
    'MiddleName': 'oset:MiddleName',
    'NameSuffix': 'oset:NameSuffix',
    'FormerName': 'oset:FormerName',
    'ResidentialAddress': 'oset:ResidentialAddress',
    'MailingAddress': 'oset:MailingAddress',
    'PhoneNumber': 'oset:PhoneNumber',
    'EmailAddress': 'oset:EmailAddress',

    # Personal Information - ID Numbers
    'DriverLicenseNumber': 'oset:DriverLicenseNumber',
    'StateIDNumber': 'oset:StateIDNumber',
    'Last4SSN': 'oset:Last4SSN',
    'VoterPIN': 'oset:VoterPIN',
    'TribalID': 'oset:TribalID',
    'PassportOrMilitaryID': 'oset:PassportOrMilitaryID',
    'IdentificationNumbers': 'oset:IdentificationNumbers',

    # Personal Information - Demographics
    'DateOfBirth': 'oset:DateOfBirth',
    'PlaceOfBirth': 'oset:PlaceOfBirth',
    'Gender': 'oset:Gender',

    # Ballot Delivery Information
    'BallotMailingAddress': 'oset:BallotMailingAddress',
    'BallotEmailAddress': 'oset:BallotEmailAddress',
    'BallotFaxNumber': 'oset:BallotFaxNumber',
    'BallotDeliveryAgent': 'oset:BallotDeliveryAgent',
    'AgentName': 'oset:AgentName',
    'AgentRelationship': 'oset:AgentRelationship',
    'AgentContactInformation': 'oset:AgentContactInformation',
    'BallotDeliveryMethod': 'oset:BallotDeliveryMethod',
    'TemporaryAbsenceAddress': 'oset:TemporaryAbsenceAddress',

    # Party Affiliation Information
    'PartyAffiliation': 'oset:PartyAffiliation',
    'PrimaryBallotChoice': 'oset:PrimaryBallotChoice',
    'BallotStyleRequest': 'oset:BallotStyleRequest',

    # Signature and Attestation
    'VoterSignature': 'oset:VoterSignature',
    'SignatureDate': 'oset:SignatureDate',
    'WitnessInformation': 'oset:WitnessInformation',
    'WitnessName': 'oset:WitnessName',
    'WitnessAddress': 'oset:WitnessAddress',
    'NotaryInformation': 'oset:NotaryInformation',
    'NotaryName': 'oset:NotaryName',
    'NotaryCommissionExpiration': 'oset:NotaryCommissionExpiration',
    'AssistantInformation': 'oset:AssistantInformation',
    'AttesterInformation': 'oset:AttesterInformation',

    # Required Documentation
    'CopyOfPhotoID': 'oset:CopyOfPhotoID',
    'ProofOfResidence': 'oset:ProofOfResidence',
    'IDNumbersProvided': 'oset:IDNumbersProvided',
    'StatementNoIDAvailable': 'oset:StatementNoIDAvailable',
}

def load_state_analysis(state_code):
    """Load the JSON analysis for a state."""
    path = Path(f'form_analyses/{state_code}_analysis.json')
    with open(path, 'r') as f:
        return json.load(f)

def get_info_types_for_state(state_code):
    """Extract all information types captured by a state's form."""
    analysis = load_state_analysis(state_code)
    info_types = set()

    for field in analysis['fields']:
        ontology_class = field['ontology_class']
        if ontology_class in CLASS_TO_INFO_TYPE:
            info_types.add(CLASS_TO_INFO_TYPE[ontology_class])

    return sorted(info_types)

def generate_restrictions(state_code, info_types):
    """Generate OWL restriction blocks for a state."""
    restrictions = []

    restrictions.append(f"oset:{state_code}_Form a owl:Class ;")
    restrictions.append(f"    rdfs:subClassOf oset:ABRForm")

    if info_types:
        for info_type in info_types:
            restrictions.append("        ,")
            restrictions.append("        [ a owl:Restriction ;")
            restrictions.append("          owl:onProperty oset:capturesInformationType ;")
            restrictions.append(f"          owl:someValuesFrom {info_type}")
            restrictions.append("        ]")

    restrictions.append("        ;")
    restrictions.append(f'    rdfs:label "{state_code} Absentee Voter Registration Form" .')

    return "\n".join(restrictions)

def main():
    """Main function to update the ontology."""

    # Get all state codes
    state_codes = []
    for filename in sorted(os.listdir('form_analyses')):
        if filename.endswith('_analysis.json'):
            state_code = filename.replace('_analysis.json', '')
            state_codes.append(state_code)

    print(f"Found {len(state_codes)} states to process\n")

    # Generate new form definitions
    new_definitions = []

    for state_code in state_codes:
        print(f"Processing {state_code}...")
        info_types = get_info_types_for_state(state_code)
        print(f"  Found {len(info_types)} information types")

        restrictions = generate_restrictions(state_code, info_types)
        new_definitions.append(restrictions)

    print(f"\n✅ Generated definitions for all {len(state_codes)} states")

    # Write to a new file
    output_path = 'updated_form_definitions.ttl'
    with open(output_path, 'w') as f:
        f.write("# Updated State Form Definitions\n")
        f.write("# Generated from comprehensive form analyses\n\n")
        f.write("\n\n".join(new_definitions))

    print(f"\n📝 Wrote new definitions to {output_path}")
    print("\nNext steps:")
    print("1. Review the generated definitions")
    print("2. Replace the old form definitions in rdf/abr_ontology.ttl")
    print("3. Keep the existing state linkages (oset:hasState) and documentation requirements")

if __name__ == '__main__':
    main()
