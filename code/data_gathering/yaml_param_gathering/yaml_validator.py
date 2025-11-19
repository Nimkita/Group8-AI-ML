# Note: keep_checkpoints and summary_frequency typical ranges unspecified

def is_number(input):
    try:
        float(input)
        return True
    except (ValueError, TypeError):
        return False

# Checks if the values of the yaml file parameters are in between the typical ranges or if they correspond to accepted strings(as per the website: https://unity-technologies.github.io/ml-agents/Training-Configuration-File/#common-trainer-configurations)
def validate_range(parameter, value):
    if is_number(value):
        value = float(str(value).strip())

        match parameter:
            case "learning_rate":
                if not 1e-5 <= value <= 1e-3:
                    return False

            case "batch_size":
                if not 32 <= value <= 1024:
                    return False

            case "buffer_size":
                if not 2048 <= value <= 1000000:
                    return False

            # Typical range = 1000 - 10000 BUT default = 0
            case "buffer_init_steps":
                if not 0 <= value <= 10000:
                    return False

            case "gamma":
                if not 0.8 <= value <= 0.995:
                    return False

            case "beta":
                if not 1e-4 <= value <= 1e-2:
                    return False

            case "epsilon":
                if not 0.1 <= value <= 0.3:
                    return False

            case "lambd":
                if not 0.9 <= value <= 0.95:
                    return False

            case "hidden_units":
                if not 32 <= value <= 512:
                    return False

            case "num_layers":
                if not 1 <= value <= 3:
                    return False

            case "num_epoch":
                if not 3 <= value <= 10:
                    return False

            # out of range on default 3DBall yaml file (changed min from 5e5 to 2e5)
            case "max_steps":
                if not 5e5 <= value <= 1e7:
                    return False

            # typical range = 0.1 - 0.5 BUT default = 1.0
            case "strength":
                if not 0.1 <= value <= 1:
                    return False

            case "time_horizon":
                if not 32 <= value <= 2048:
                    return False

            case "tau":
                if not 0.005 <= value <= 0.01:
                    return False

            case "steps_per_update" | "reward_signal_steps_per_update":
                if not 1 <= value <= 20:
                    return False

            case "init_entcoef":
                if not 0.05 <= value <= 1.0:
                    return False
    else:
        match parameter:
            case "trainer_type":
                if value not in ("ppo", "sac"):
                    return False

            case "learning_rate_schedule":
                if value not in ("linear", "constant"):
                    return False

            case "normalize" | "save_replay_buffer":
                if value not in ("true", "false"):
                    return False

            case "vis_encode_type":
                if value not in ("simple", "nature_cnn", "resnet", "match3", "fully_connected"):
                    return False
    return True
