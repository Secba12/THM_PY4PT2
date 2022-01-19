import requests
import sys

dir_list = open("wordlist2.txt").read()
directories = dir_list.splitlines()
invalid_dir_count = 0

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"
    dir_request = requests.get(dir_enum)
    # print(dir_enum)
    if dir_request.status_code == 404:
        invalid_dir_count += 1
    else:
        print(f"Valid dir {dir_enum}")

print(invalid_dir_count)