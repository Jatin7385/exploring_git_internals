import zlib

with open(f'./.git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4', 'rb') as f:
        comp_obj = f.read()
        print("Initial Blob : ", comp_obj)
        # The blob is compressed using zlib, so first we need to decompress it.
        obj = zlib.decompress(comp_obj)
        print("Decompressed Blob : ", obj)
        first_null = obj.index(b'\x00')
        print("First Null : ", first_null)
        type_ = obj[:first_null].decode()
        print("Type_ : ", type_)
        content = obj[first_null + 1:]
        print("Final Content : " , content)
