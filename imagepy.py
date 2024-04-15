from PIL import Image

def encrypt_image(image_path, key):
    try:
        # Open the image
        image = Image.open(image_path)
        width, height = image.size
        
        # Convert the image to RGB mode
        rgb_image = image.convert("RGB")
        
        # Encrypt each pixel
        encrypted_pixels = []
        for y in range(height):
            for x in range(width):
                r, g, b = rgb_image.getpixel((x, y))
                encrypted_r = r ^ key
                encrypted_g = g ^ key
                encrypted_b = b ^ key
                encrypted_pixels.append((encrypted_r, encrypted_g, encrypted_b))
        
        # Create a new image with the encrypted pixels
        encrypted_image = Image.new("RGB", (width, height))
        encrypted_image.putdata(encrypted_pixels)
        
        # Save the encrypted image
        encrypted_file_path = "encrypted_image.png"
        encrypted_image.save(encrypted_file_path)
        print("Image encrypted successfully! Encrypted image saved at:", encrypted_file_path)
        return encrypted_file_path
    except Exception as e:
        print("An error occurred:", e)

def decrypt_image(encrypted_image_path, key):
    try:
        # Open the encrypted image
        encrypted_image = Image.open(encrypted_image_path)
        width, height = encrypted_image.size
        
        # Decrypt each pixel
        decrypted_pixels = []
        for y in range(height):
            for x in range(width):
                r, g, b = encrypted_image.getpixel((x, y))
                decrypted_r = r ^ key
                decrypted_g = g ^ key
                decrypted_b = b ^ key
                decrypted_pixels.append((decrypted_r, decrypted_g, decrypted_b))
        
        # Create a new image with the decrypted pixels
        decrypted_image = Image.new("RGB", (width, height))
        decrypted_image.putdata(decrypted_pixels)
        
        # Save the decrypted image
        decrypted_image.save("decrypted_image.png")
        print("Image decrypted successfully!")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
try:
    image_path = input("Enter the path to the image file: ")
    encryption_key = int(input("Enter the encryption key (an integer): "))
    encrypted_image_path = encrypt_image(image_path, encryption_key)
    decrypt_image(encrypted_image_path, encryption_key)
except ValueError:
    print("Encryption key must be an integer.")
