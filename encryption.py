my_identity= "9c0092761c9d119d25868776761c9d929d491143a322251a9c81254d902b04"
jens_identity = "8028952d5a952806327a372d818e04090e0498095da2a23f"
victors_identity = "797d6506590536055e0e66051e70352a055e6c00607778"
izzies_identity = "4fb099959d99b02d7aaf5f950a43b79c81b70d9c11d2d2b3"

my_decrypted_message = []
jens_decrypted_message = []
victors_decrypted_message =[]
izzies_decrypted_message = []

n = 2

def convertToString(decrypted_message):
    s = ""
    for x in s:
        s += x 
    return s
for index in range(0, len(my_identity), n):
    # a = 110
    # a^-1 = 34
    #b = 81
    #c = 191
    x = (34 * (int(my_decrypted_message[index: index+n], 16)-81)) % 191
    my_decrypted_message.append(chr(x))

print(convertToString(my_decrypted_message))

for index in range(0,len(jens_identity), n):
    # a = 84
    # a^-1 = 33
    # b = 42
    # c = 163
    x = (33 * (int(jens_identity[index: index+n],16)-42)) % 163
    jens_decrypted_message.append(chr(x))

print(convertToString(jens_decrypted_message))

# TODO ADD VICTOR AND IZZI'S IMPLEMENTATION
