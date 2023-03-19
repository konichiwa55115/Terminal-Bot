import os
import re

id_pattern = re.compile(r'^.\d+$')


token = "5714654934:AAH0p16rz-w-wRuEUYu9KCBLrfqlEIITrB0"
app_id = int(17983098)
app_hash = "ee28199396e0925f1f44d945ac174f64"
allowed = [int(user) if id_pattern.search(user) else user for user in os.environ.get('AUTH_USERS', '6234365091').split()]

help_text = """
Hello I'm Terminal Bot which will Execute your Commands.

With this bot you can execute system commands on your server.

**if you not owner of this bot You can not use me because I'm private...
So you run one of these for yourself [here](https://github.com/moshe-coh/Terminal-Bot)**

**My Commands For Owner Only:**

🔹 /st - speed test
🔹 /ip - ip details
🔹 /stats - disk space
🔹 /cd - change working dir
🔹 /my_files - file manager
🔹 And All System Commands...

"""
