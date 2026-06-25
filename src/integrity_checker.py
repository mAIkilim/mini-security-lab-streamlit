import hashlib

def generate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


filename = "dokumen.txt"

hash_awal = generate_hash(filename)

print("\nHash Awal")
print(hash_awal)

input(
    "\nUbah isi dokumen.txt lalu tekan ENTER..."
)

hash_baru = generate_hash(filename)

print("\nHash Baru")
print(hash_baru)

if hash_awal == hash_baru:
    print("\nFile tidak berubah")
else:
    print("\nFile telah berubah")