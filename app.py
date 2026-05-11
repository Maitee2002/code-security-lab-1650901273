import subprocess
import ast
import json

def run_cmd(host):
    return subprocess.check_output(['ping', '-c', '1', host], shell=False)

def calc(expr):
    return ast.literal_eval(expr)

def load(data):
    return json.loads(data)
