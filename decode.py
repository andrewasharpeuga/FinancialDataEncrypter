from encode import nth_fibonacci, nth_prime

def prime_fibonacci_to_char(product):
    for i in range(1, 27):
        fib_number = nth_fibonacci(i)
        prime_number = nth_prime(i)
        if (fib_number * prime_number) % 62 == product:
            return chr(i + 96)
    return '?'

def decode_message(obfuscated_message):
    parts = obfuscated_message.split()
    decoded_message = ''.join([prime_fibonacci_to_char(len(part)) if part != ' ' else ' ' for part in parts])
    return decoded_message

def receive_data(encoded_data):
    decoded_data = decode_message(encoded_data)
    return decoded_data

def main():
    encoded_data = input("Enter the encoded message: ")
    decrypted_data = receive_data(encoded_data)
    print("Decrypted Data:", decrypted_data)

if __name__ == "__main__":
    main()
