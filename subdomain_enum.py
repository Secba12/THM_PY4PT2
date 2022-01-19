import requests
import sys

sub_domain_list = open("wordlist2.txt").read()
subdoms = sub_domain_list.splitlines()

for sub in subdoms:
    sub_domain_request = f"http://{sub}.{sys.argv[1]}"  # sys.argv allows input from the cli example >python <script> <arguments>
    print(sub_domain_request)
    try:
        requests.get(sub_domain_request)


    except requests.ConnectionError:
        pass

    else:
        print(f"Valid domain {sub_domain_request}")

# if __name__ == "__main__":
