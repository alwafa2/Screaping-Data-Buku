# Import modul webdriver dari Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Inisialisasi WebDriver (Chrome)
driver = webdriver.Chrome()
products_list = []
# Buka URL
#driver.get("https://www.gramedia.com/categories/buku/fiksi-sastra")
# Loop melalui halaman 1 hingga 2
for halaman in range(1, 50):
    # Ubah nomor halaman dalam URL
    print(f"Halaman {halaman}")
    url = f"https://www.gramedia.com/categories/buku/fiksi-sastra?page={halaman}"
    driver.get(url)
# Dapatkan elemen produk menggunakan XPath
    products = driver.find_elements(By.XPATH,
                                './/*[@id="results-container"]/div[2]/div/gm-product-list/div')

# Daftar untuk menyimpan informasi produk

# Loop melalui elemen produk
    for product in products:
        # Dapatkan atribut href dari elemen tag <a> (judul buku)
        title = product.find_element(By.CLASS_NAME, 'list-title').text

        # Dapatkan teks dari elemen dengan kelas 'price_color' (harga buku)
        price = product.find_element(By.CLASS_NAME, 'formats-price').text

        # Bentuk dictionary untuk setiap produk dan tambahkan ke daftar
        product_item = {
            'title': title,
            'price': price
        }
        products_list.append(product_item)
        print(product_item)
time.sleep(5)
# Buat DataFrame dari daftar produk
df = pd.DataFrame(products_list)
# Cetak DataFrame
print(df)

# Simpan DataFrame ke file CSV
df.to_csv('Data_buku.csv', sep=',')

driver.quit()
