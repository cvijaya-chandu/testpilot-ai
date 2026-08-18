
import json
import csv

def save_testcase(filename,response):
    with open(filename,"w") as f:
        output = response["test_cases"]
        fields = [
            "id",
            "description",
            "priority",
            "pre_requisite",
            "steps",
            "expected_result"
        ]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for testcase in output:
            writer.writerow(testcase)


