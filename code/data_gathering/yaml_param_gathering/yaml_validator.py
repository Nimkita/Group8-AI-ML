# Checks if the values of the yaml file parameters are in between the typical ranges (as per the website: https://unity-technologies.github.io/ml-agents/Training-Configuration-File/#common-trainer-configurations)
# These ranges are SAC specific
def validate_range(parameter, value):
    value = float(str(value).strip())

    match parameter:
        case "learning_rate":
            if not 1e-5 <= value <= 1e-3:
                return False

        case "batch_size":
            if not 32 <= value <= 1024:
                return False

        case "buffer_size":
            if not 50000 <= value <= 1000000:
                return False

        case "gamma":
            if not 0.8 <= value <= 0.995:
                return False

        case "lambd":
            if not 0.9 <= value <= 0.95:
                return False

        case "hidden_units":
            if not 32 <= value <= 512:
                raise Exception("hidden_units value is not in the typical range 32 and 512")

        case "num_layers":
            if not 1 <= value <= 3:
                return False

        # out of range on default 3DBall yaml file (changed min from 5e5 to 2e5)
        case "max_steps":
            if not 5e5 <= value <= 1e7:
                return False

    return True