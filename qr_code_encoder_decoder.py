import qrcode
import cv2

# QR Code Encoder
def qr_code_generator(data, filename='qrcode.png'):
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, 
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR Code generated and saved as {filename}.")

# QR Code Decoder
def qr_code_decoder(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, vertices_array, _ = detector.detectAndDecode(img)
    
    if vertices_array is not None:
        print(f"Decoded data: {data}")
    else:
        print("QR code not detected.")
        
if __name__ == "__main__":
    choice = input("Do you want to generate or decode QR Code? (g/d): ").lower()
    
    if choice == 'g':
        data = input("Enter the data to encode in the QR code: ")
        qr_code_generator(data)
    elif choice == 'd':
        image_path = input("Enter the path of the QR code image to decode: ")
        qr_code_decoder(image_path)
    else:
        print("Invalid choice. Please choose 'g' to generate or 'd' to decode.")
