


def save_testcase(filename,response):
    with open(filename,"w") as f:
        f.write(response.strip("\n"))
