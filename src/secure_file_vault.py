import os
from cryptography.fernet import Fernet


def generate_key_if_not_exists():

    if not os.path.exists(
            "secret.key"
    ):

        key = Fernet.generate_key()

        with open(
                "secret.key",
                "wb"
        ) as key_file:
            key_file.write(key)

        print("Key baru dibuat")

    else:
        print(
            "Key sudah tersedia"
        )


def load_key():
    with open(
            "secret.key",
            "rb"
    ) as key_file:
        return key_file.read()


def encrypt_file(filename):

    key = load_key()

    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    with open(
            filename + ".enc",
            "wb"
    ) as file:
        file.write(encrypted_data)

    print("File berhasil dienkripsi")


def decrypt_file(
        encrypted_filename,
        output_filename
):

    key = load_key()

    fernet = Fernet(key)

    with open(
            encrypted_filename,
            "rb"
    ) as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(
        encrypted_data
    )

    with open(
            output_filename,
            "wb"
    ) as file:
        file.write(decrypted_data)

    print("File berhasil didekripsi")


generate_key_if_not_exists()

encrypt_file("dokumen.txt")

decrypt_file(
    "dokumen.txt.enc",
    "dokumen_decrypted.txt"
)