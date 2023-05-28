def select_diseases(symptoms):
    diseases = {
        "Allergies": ['sneezing', 'blocked nose', 'watery eyes', 'red eyes', 'coughing', 'red rash'],
        "Asthma": ['wheezing', 'shortness of breath', 'tight chest'],
        "Head Tumor": ['severe headaches', 'seizures', 'mental changes', 'vision problem'],
        "Chronic Pain": ['diabetes', 'arthritis', 'back pain'],
        "Dehydration": ['feeling thirsty', 'dry mouth', 'tiredness', 'strong smelling urine'],
        "Food Poisoning": ['nausea', 'vomiting', 'weakness', 'loss of appetite', 'aching muscles', 'chills']
    }

    matching_diseases = []
    
    for disease, disease_symptoms in diseases.items():
        if any(symptom in disease_symptoms for symptom in symptoms):
            matching_diseases.append(disease)

    return matching_diseases


# Prompt the user to enter symptoms
symptoms_input = input("Enter your symptoms (separated by commas): ")
symptoms = symptoms_input.split(',')

# Select the diseases based on symptoms
diagnosed_diseases = select_diseases(symptoms)

# Print the diagnosed diseases or an error message if no match found
if diagnosed_diseases:
    print("You may have the following disease(s):")
    for disease in diagnosed_diseases:
        print("- " + disease)
else:
    print("Unable to diagnose any disease based on the given symptoms.")

