import streamlit as st
import bcrypt
import hashlib

from cryptography.fernet import Fernet

from cryptography.hazmat.primitives.asymmetric import (
    rsa,
    padding
)

from cryptography.hazmat.primitives import hashes

st.title("Mini Security Lab")

menu = st.sidebar.selectbox(
    "Pilih Praktikum",
    [
        "Password Hashing",
        "File Hash Checker",
        "Digital Signature",
        "File Encryption"
    ]
)

if menu == "Password Hashing":

    st.header("Password Hashing dengan bcrypt")

    password = st.text_input(
        "Masukkan password",
        type="password"
    )

    if st.button("Generate Hash"):

        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        st.write("Hash password:")
        st.code(hashed.decode())

elif menu == "File Hash Checker":

    st.header("File Integrity Checker")

    uploaded_file = st.file_uploader(
        "Upload file"
    )

    if uploaded_file:

        data = uploaded_file.read()

        file_hash = hashlib.sha256(
            data
        ).hexdigest()

        st.write("SHA-256 Hash:")
        st.code(file_hash)

elif menu == "Digital Signature":

    st.header("Digital Signature Demo")

    uploaded_file = st.file_uploader(
        "Upload file untuk ditandatangani"
    )

    if uploaded_file:

        data = uploaded_file.read()

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        public_key = private_key.public_key()

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

        st.success(
            "File berhasil ditandatangani"
        )

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

            st.success(
                "Signature VALID. File asli."
            )

            st.download_button(
                "Download Signature",
                signature,
                file_name=uploaded_file.name + ".sig"
            )

        except Exception:

            st.error(
                "Signature TIDAK VALID"
            )

elif menu == "File Encryption":

    st.header(
        "File Encryption dengan Fernet"
    )

    uploaded_file = st.file_uploader(
        "Upload file untuk dienkripsi"
    )

    if uploaded_file:

        key = Fernet.generate_key()

        fernet = Fernet(key)

        data = uploaded_file.read()

        encrypted_data = fernet.encrypt(
            data
        )

        st.write("Encryption Key:")
        st.code(key.decode())

        st.download_button(
            "Download File Terenkripsi",
            encrypted_data,
            file_name=uploaded_file.name + ".enc"
        )