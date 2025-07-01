# Baby_MSD [crypto warmup]
[IERAE CTF 2025](https://ierae-ctf.com/challenges)

## Problem Description
> 👶 < Guess the most significant digit!


Below is the code provided in the challenge :

<details>
<summary> chal.py </summary>

```python 
#!/usr/bin/env python3

from sys import exit
from random import randint

def stage():
  digit_counts = [0 for i in range(10)]

  for i in range(2000):
    secret = randint(10 ** 60, 10 ** 100)
    M = int(input("Enter mod: "))
    if M < 10 ** 30:
      print("Too small!")
      exit(1)

    msd = str(secret % M)[0]
    digit_counts[int(msd)] += 1

  choice = int(input("Which number (1~9) appeared the most? : "))
  for i in range(10):
    if digit_counts[choice] < digit_counts[i]:
      print("Failed :(")
      exit(1)

  print("OK")

def main():
  for i in range(100):
    print("==== Stage {} ====\n".format(i+1))
    stage()

  print("You did it!")
  with open("flag.txt", "r") as f:
    print(f.read())

if __name__ == '__main__':
  main()
```
</details>

## 🚀 Solution

The following Python script was used to solve the challenge.


<details>
<summary> solver.py </summary>

```python
import socket

def recv_until(sock, targets):
    data = b''
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            break
        data += chunk
        if any(t in data for t in targets):
            break
    return data

def solve_stage(sock, stage_no):
    M = 20 ** 30

    for i in range(2000):
        recv_until(sock, [b'Enter mod'])
        sock.sendall(str(M).encode() + b'\n')
        # 進捗表示
        if i % 500 == 0:
            print(f"  Stage {stage_no+1}: Sent mod {i+1}/2000")

    data = recv_until(sock, [b'Which number'])
    print(f"Stage {stage_no+1} prompt: {data.decode(errors='ignore').strip()}")

    sock.sendall(b'1\n')

def main():
    host = "**.**.**.**"
    port = * 

    with socket.create_connection((host, port)) as sock:
        for stage_no in range(100):
            print(f"==== Stage {stage_no+1} ====")
            solve_stage(sock, stage_no)

        # FLAG受け取り
        final_output = b''
        while True:
            chunk = sock.recv(1024)
            if not chunk:
                break
            final_output += chunk

        print("\n[✔] Final Output:")
        print(final_output.decode(errors="ignore"))

if __name__ == "__main__":
    main()
```

</details>

This challenge required us to predict the most significant digit of a remainder.
The target digit was between `1` and `9`.

To solve it, we noticed that if we set `M = 2`, the remainder would always be either 0 or 1.
This is helpful because it simplifies the problem and avoids leaking the actual remainder directly.

Since the constraint was `M > 10 ** 30`, we chose `M = 20 ** 30` which satisfies the condition and keeps things manageable.

With this approach, we were able to retrieve the FLAG.


✅ Thank you LLM! 🙂