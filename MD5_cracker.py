import hashlib

desired_hash = "cd0894152aa5eec36ec79eb2bcb90ca40f056804530f40732b4957a496b23dc8"
password_file = "rockyou.txt"

with open(password_file, "r", encoding="latin-1") as passwords:
    for i, line in enumerate(passwords):
        password = line.rstrip("\n")
        password_hex = hashlib.sha256(password.encode()).hexdigest()

        # Only print occasionally to speed things up
        if i % 100000 == 0:
            print(f"Checked {i} passwords...")

        if password_hex == desired_hash:
            print(f"PASSWORD CRACKED: {password}")
            break
