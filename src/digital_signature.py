from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


def sign_file(
        private_key,
        filename
):
    with open(filename, "rb") as file:
        data = file.read()

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(
                hashes.SHA256()
            ),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    with open(
            filename + ".sig",
            "wb"
    ) as sig_file:
        sig_file.write(signature)

    print("Dokumen berhasil ditandatangani")


def verify_file(
        public_key,
        filename,
        signature_file
):
    with open(filename, "rb") as file:
        data = file.read()

    with open(signature_file, "rb") as file:
        signature = file.read()

    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(
                    hashes.SHA256()
                ),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        print("Signature VALID")

    except Exception:
        print("Signature TIDAK VALID")


private_key, public_key = generate_keys()

filename = "dokumen.txt"

sign_file(
    private_key,
    filename
)

verify_file(
    public_key,
    filename,
    filename + ".sig"
)

input(
    "\nUbah dokumen.txt lalu tekan ENTER..."
)

verify_file(
    public_key,
    filename,
    filename + ".sig"
)