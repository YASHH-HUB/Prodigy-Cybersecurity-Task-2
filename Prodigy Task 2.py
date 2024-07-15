from PIL import Image

def encrypt_image(input_path, output_path, key=None):
    try:
        img = Image.open(input_path)
        pixels = img.getdata()

        encrypted_pixels = []
        for r, g, b in pixels:
            # Swapping red and blue channels
            encrypted_pixel = (b, g, r)
            encrypted_pixels.append(encrypted_pixel)

        img.putdata(encrypted_pixels)
        img.save(output_path)
        print("Image encrypted successfully!")

        # Open encrypted image
        encrypted_img = Image.open(output_path)
        encrypted_img.show()
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image(input_path, output_path, key=None):
    try:
        img = Image.open(input_path)
        pixels = img.getdata()

        decrypted_pixels = []
        for r, g, b in pixels:
            # Swapping red and blue channels back
            decrypted_pixel = (b, g, r)
            decrypted_pixels.append(decrypted_pixel)

        img.putdata(decrypted_pixels)
        img.save(output_path)
        print("Image decrypted successfully!")

        # Open decrypted image
        decrypted_img = Image.open(output_path)
        decrypted_img.show()
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

# File paths
input_image = r"D:\Python programs\pythonProject\Input.jpg"
encrypted_image = r"D:\Python programs\pythonProject\Encrypted_image.jpg"
decrypted_image = r"D:\Python programs\pythonProject\decrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)