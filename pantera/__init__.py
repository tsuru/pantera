import chaos
import random

def run(*args, **kwargs):
  run_list = [chaos.Stop, chaos.Reboot, chaos.Terminate]
  random.choice(run_list)(*args, **kwargs)()
