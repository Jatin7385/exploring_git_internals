import hashlib
import zlib
import os

# 1. The content to store
content = b"test content...."

# 2. Create header: "blob <size>\0"
header = f"blob {len(content)}\0".encode()

print("Header : ", header)

# 3. Concatenate header and content
store = header + content

print("Final concatenated string : ", store)

# 4. Calculate SHA-1
sha1 = hashlib.sha1(store).hexdigest()
print(f"SHA-1: {sha1}")

# 5. Compress using zlib
zlib_content = zlib.compress(store)
print("Compressed blob contents : ", zlib_content)

# 6. Determine Git object path
dir_name = f".git/objects/{sha1[:2]}"
file_name = sha1[2:]
path = os.path.join(dir_name, file_name)

# 7. Make sure directory exists
os.makedirs(dir_name, exist_ok=True)

# 8. Write the object to disk
with open(path, "wb") as f:
    f.write(zlib_content)

print(f"Git object written to {path}")
