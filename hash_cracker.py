import hashlib, pyfiglet

ascii_banner = pyfiglet.figlet_format("MD5\n CRACKER")
print(ascii_banner)

word_list_location = f"{input('Enter wordlist location: ')}"
hash_to_crack = f"{input('Input hash: ')}"

with open(word_list_location, 'r') as file:
    for line in file.readlines():
        #hash_object = hashlib.md5(line.strip().encode())
        hash_object = hashlib.sha256(line.strip().encode())
        hashed_pass = hash_object.hexdigest()
        if hashed_pass == hash_to_crack:
            print(f"Found clear text {line.strip()}")
            exit(0)