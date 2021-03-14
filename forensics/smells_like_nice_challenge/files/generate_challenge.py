import wave
import dotenv

dotenv.load('resources/challenge.env')
SSTV_FILE = dotenv.get('SSTV_FILE') or 'flag.wav'
SONG_FILE = dotenv.get('SONG_FILE') or 'resources/nirvana.wav'
CHALLENGE_FILE = dotenv.get('CHALLENGE_FILE') or 'challenge.wav'

# Read wave song audio file
with wave.open(SONG_FILE, mode='rb') as song:
    print(f"Reading \"{SONG_FILE}\"")

    # Read wave sstv audio file
    with wave.open(SSTV_FILE, mode='rb') as sstv_audio:
        print(f"Reading \"{SSTV_FILE}\"")

        # Read frames and convert to byte array
        song_bytes = bytearray(list(song.readframes(song.getnframes())))

        # Read frames from messge and convert to list of integers
        sstv_list_of_bytes = list(sstv_audio.readframes(sstv_audio.getnframes()))

        # Prepare string that will contain bits from the list above
        sstv_binary_string = ''
        # Fill string with bits from list: [0b1,0b0] -> '0000000100000000'
        for integer in sstv_list_of_bytes:
            sstv_binary_string = sstv_binary_string +  bin(integer).lstrip('0b').ljust(8, '0')

        # Shorten song so it matches length of sstv message
        song_bytes = song_bytes[:len(sstv_binary_string)]

        # Set LSB
        for i, bit in enumerate(sstv_binary_string):
            song_bytes[i] = (song_bytes[i] & 254) | int(bit)
        print("Sucessfully set all LSB")

        # Get bytes of modified song
        song_modified_bytes = bytes(song_bytes)

        print(f"Writing to \"{CHALLENGE_FILE}\"")
        # Write bytes to a new wave audio file
        with wave.open(CHALLENGE_FILE, 'wb') as fd:
            fd.setparams(sstv_audio.getparams())
            fd.writeframes(song_modified_bytes)
            print(f"Sucessfully saved bytes as \"{CHALLENGE_FILE}\"")
            try:
                import os
                os.remove(SSTV_FILE)
                os.remove(dotenv.get('FLAG_IMAGE_FILE'))
            except Exception as e:
                print(e)