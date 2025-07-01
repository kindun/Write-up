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

  #  result = recv_until(sock, [b'OK', b'Failed'])
  #  print(f"Stage {stage_no+1} result: {result.decode(errors='ignore').strip()}")

def main():
    host = "35.200.10.230"
    port = 12343

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

