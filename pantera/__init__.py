import chaos
import random


__version__ = "0.1.1"


def run(*args, **kwargs):
    run_list = [chaos.Stop, chaos.Reboot, chaos.Terminate]
    random.choice(run_list)(*args, **kwargs)()
