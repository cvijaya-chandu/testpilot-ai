
import json

def save_testcase(filename,response):
    with open(filename,"w") as f:
        json_op = json.dumps(response,indent=4)
        f.write(json_op)