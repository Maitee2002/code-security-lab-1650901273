import subprocess
import ast
import json

# FIX B602: ไม่ใช้ shell=True
def run_cmd(host):
    return subprocess.check_output(['ping', '-c', '1', host], shell=False)

# FIX B307: ไม่ใช้ eval
def calc(expr):
    return ast.literal_eval(expr)

# FIX B301: ไม่ใช้ pickle
def load(data):
    return json.loads(data)
