import qrcode

BASE_URL = "https://markospanagiotou.github.io/crypto_escape_game"

qr_data = {
    "level1_qr.png": f"{BASE_URL}/level1.html",
    "level2_qr.png": f"{BASE_URL}/level2.html",
    "level3_qr.png": f"{BASE_URL}/level3.html",
    "level4_qr.png": f"{BASE_URL}/level4.html",
    "level5_qr.png": f"{BASE_URL}/level5.html",
}

for filename, url in qr_data.items():
    img = qrcode.make(url)
    img.save(filename)

print("QR codes created successfully.")