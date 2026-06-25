import bcrypt

users = {}

def register(username, password):
    password_bytes = password.encode()

    hashed = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )

    users[username] = hashed

    print("\nUser berhasil didaftarkan")
    print("Hash tersimpan:")
    print(hashed.decode())


def login(username, password):
    if username not in users:
        print("User tidak ditemukan")
        return

    password_bytes = password.encode()
    stored_hash = users[username]

    if bcrypt.checkpw(
        password_bytes,
        stored_hash
    ):
        print("Login berhasil")
    else:
        print("Login gagal")


register("andi", "rahasia123")

print("\n=== Simulasi Login ===")

login("andi", "rahasia123")
login("andi", "passwordsalah")