import wave

CHALLENGE_FILE = 'challenge.wav'
DECODED_FILE = 'decoded.wav'

# Read wave challenge audio file
with wave.open(CHALLENGE_FILE, mode='rb') as song:
    print(f"Reading \"{CHALLENGE_FILE}\"")

    # Read frames and convert to byte array
    chall_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Extract the LSB of each byte
    extracted = [chall_bytes[i] & 1 for i in range(len(chall_bytes))]
    print(f"Extracted LSB from {len(chall_bytes)} bytes")

    # Convert list of extracted bytes to 
    string_bytes = "".join(map(str,extracted))

    print(f"Creating list of output file's bytes")
    # Prepare list of extracted bytes
    output_list = []
    # Prepare byte string '1111110100010001' -> [ 0b11111101, 0b00010001 ]
    byte = ''
    # Create list of bytes 
    for i,bit in enumerate(string_bytes, 1):
        if i % 8 == 0:
            byte += bit
            output_list.append(int(byte, 2))
            byte = ''
        else:
            byte += bit
    print(f"Created list of {len(output_list)} bytes")

    print(f"Writing to \"{DECODED_FILE}\"")
    # Save list of bytes as wav audio file with params from challenge file
    with wave.open(DECODED_FILE, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(bytes(output_list))
        print(f"Sucessfully saved bytes as \"{DECODED_FILE}\"")