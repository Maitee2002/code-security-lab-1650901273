import subprocess
import pickle

def run_cmd(host):
    return subprocess.check_output(f"ping -c 1 {host}", shell=True)  # B602

def calc(expr):
    return eval(expr)  # B307

def load(data):
    return pickle.loads(data)  # B301
