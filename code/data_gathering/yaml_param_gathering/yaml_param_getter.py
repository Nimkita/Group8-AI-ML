import yaml_validator

# TODO is this still the case ? IMPORTANT NOTE: in our documentation we called it "steps_planned" but in yaml it is called "max_steps" (which is the naming convention here)

# Reads the yaml parameters of the run and returns them as a dictionary
def get_yaml_param(yaml_directory):
    txt_yaml = open(yaml_directory) # Open the txt file with the parameters

    # Create the dictionary with key=param_type and value=param_value
    params = {}
    params.setdefault("notes", [])

    # Strip the param_type
    for line in txt_yaml:
        words = line.strip().split()
        param_type = words[0].replace(":","")

        # Ignore sections (no parameters there)
        if len(words) == 1:
            continue

        param_value = words[1]

        params.update({param_type: param_value})
        if not yaml_validator.validate_range(param_type, param_value): # Check if value is in typical range, if not: append it to the notes key of params
            params["notes"].append(f"{param_type} out of range or invalid")

    txt_yaml.close()
    return params
