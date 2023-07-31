from gempa_news.GempaNews import GempaNewsClass

# Membuat instance dari GempaNewsClass
gempanews_instance = GempaNewsClass()

# Mengambil data gempa menggunakan metode getNews()
data_gempa = gempanews_instance.getNews()

# Mencetak data_gempa untuk melihat hasilnya
print(data_gempa)