#------------------------------------------------
# Phase 2 - Graded Challenge 7
# Name: Verren Monica
# Batch: RMT - 038
# Model Deployment - EDA Page
#------------------------------------------------

# Import Libraries
import os
import streamlit as st
import pandas as pd
from PIL import Image


def run():
    """This function is the main entry point for running the webapps."""

    # Display image
    image = Image.open('banner.jpg')
    st.image(image)

    # Make title
    st.title('Car vs Bike Classification - Exploratory Data Analysis')
    
    # Add text
    st.write('by **Verren Monica**\n\n*Hacktiv8 - Full Time Data Science - Batch RMT-038 - Graded Challenge 7 Project*')
    st.write('')
    st.write('Halaman ini berisi mengenai Exploratory Data Analysis (EDA) mengenai car vs bike dataset.')
    st.write('Dataset source: [click here](https://www.kaggle.com/datasets/utkarshsaxenadn/car-vs-bike-classification-dataset/data)')

    # Subheader
    st.subheader("Penjabaran EDA")
    # Menampilkan 75 gambar bike
    bikeFolder = "Car-Bike-Dataset/Bike"
    st.write("Berikut adalah 75 gambar dari dataset bike:")
    st.image("eda1.png")
    st.image("eda2.png")
    st.image("eda3.png")

    # Narasi mengenai analisa bike
    st.write("""
    Berdasarkan sumber yang saya baca ([Mengenal 8 Jenis Sepeda Motor](https://www.inews.id/otomotif/motor/mengenal-8-jenis-sepeda-motor-dari-model-skuter-hingga-touring/2)), ada 8 jenis sepeda motor yaitu:
    1. Motor bebek (cub)
    2. Skuter
    3. Dual-Sport
    4. Naked Bike
    5. Sport Bike
    6. Retro
    7. Cruiser
    8. Touring

    Jika dilihat dari 75 gambar dalam kategori bikes yang ditampilkan diatas, ditemukan bahwa gambar sepeda motor dalam dataset di dominasi oleh tipe Dual-Sport, Naked Bike, Sport Bike, Retro, Cruiser dan Touring. 
    Tidak ada gambar sepeda motor yang ditampilkan yang masuk ke dalam tipe Motor Bebek dan Skuter. 
    Model kemungkinan akan belajar lebih banyak gambar mengenai bentuk sepeda motor selain Motor Bebek dan Skuter.
             
    Dari segi warna, banyak sepeda motor dalam gambar yang dominan dengan warna hitam, putih, merah, biru. 
    Ditemukan pula bahwa dalam sebuah motor dapat mengandung 2 warna seperti merah dan hitam, biru dan hitam atau putih dan hitam.

    Selain itu, sudut pengambilan gambar dalam kategori bikes cukup variatif, ada yang memperlihatkan tampak depan, tampak samping (kanan dan kiri), tampak depan dan samping serta tampak belakang sepeda motor. 
    Hal ini memungkinkan model untuk belajar bentuk sepeda motor dari beberapa angle. Namun, ada beberapa gambar yang tampak terlalu jauh dari kamera pengambilan gambar hal ini dapat membuat model kesulitan untuk mengenali gambar sepeda motor.

    Dari beberapa gambar dalam kategori bikes yang ditampilkan ditemukan beberapa karakeristik lainnya seperti:
    - Beberapa gambar hanya menampilkan sebagian bagian dari sepeda motor seperti di bagian depan motor, bagian belakang motor dan tampak depan motor.
    - Beberapa gambar dalam dataset ada yang tidak memiliki background (hanya warna putih), ada yang dengan background jalan, pemandangan rumput yang luas, suasana arena balapan, halaman rumah dan bahkan dengan background suasana di dalam gedung seperti pameran.
    - Beberapa gambar sepeda motor ada yang diambil saat sedang dikendarai oleh manusia, diambil dengan foto seorang model dan ada yang hanya gambar sepeda motor tanpa gambar manusia.
    - Beberapa gambar sepertinya ada yang diambil dengan tujuan komersial dan ada yang memang hanya diambil untuk kebutuhan dokumentasi.
    - Bebreapa gambar memiliki lebih dari 1 sepeda motor di dalamnya.

    Hal ini memungkinkan model belajar mengenali bentuk sepeda motor dengan berbagai macam background dan kondisi. Namun juga dapat membuat model kesulitan mengenali gambar jika hanya bagian tertentu saja yang ada pada gambar.
    """)

    # Menampilkan 75 gambar car
    carFolder ="Car-Bike-Dataset/Car"
    st.write("Berikut adalah 75 gambar dari dataset car:")
    st.image("eda4.png")
    st.image("eda5.png")
    st.image("eda6.png")

    # Narasi mengenai analisa bike
    st.write("""
    Berdasarkan sumber yang saya baca ([Car Types](https://www.caranddriver.com/shopping-advice/g26100588/car-types/)), terdapat beberapa tipe mobil diantaranya adalah:
    1. Sedan
    2. Coupe
    3. Sports Car
    4. Station Wagon
    5. Hatchback
    6. Convertible
    7. Sport-utility Vehicle (SUV)
    8. Minivan
    9. Pickup Truck

    Jika dilihat dari 75 gambar dalam kategori cars, ditemukan bahwa gambar mobil dalam dataset cukup mewakili tipe-tipe mobil yang disebutkan, kecuali tipe mobil pickup truck. 
    Sehingga, model akan banyak belajar mengenai bentuk mobil dari tipe yang bermacam-macam, namun ketiadaan tipe mobil pickup truck mungkin akan membuat model kesulitan dalam mengenali object.

    Dari segi warna, gambar mobil yang ada di dominasi dengan warna merah, putih, hitam, biru dan orange. Jarang sekali di temukan sebuah gambar mobil dengan kombinasi 2 warna (tidak seperti dalam gambar sepeda motor).

    Selain itu, dari segi sudut pengambilan gambar sudah cukup variatif, ada mobil-mobil dengan tampak depan, tampak samping (kanan dan kiri), tampak belakang, tampak depan dan samping, dan tampak atas. 
    Hal ini memungkinkan model untuk belajar mengenal object model dari berbagai macam sisi(angle). 
    Namun, ada juga mobil yang jauh dari kamera pengambilan gambar yang mungkin akan menyebabkan model sulit mengenali bentuknya.

    Dari beberapa gambar dalam kateori cars yang ditampilkan ditemukan beberapa karakeristik lainnya seperti:
    - Beberapa gambar tidak memiliki background (hanya warna putih atau hitam saja), ada yang dengan background jalan, gedung, pemandangan, dan di dalam gedung dengan suasana pameran.
    - Beberapa gambar diambil terlihat seperti sedang bergerak dan ada juga yang diambil pada saat ada manusia di dekat mobil.
    - Beberapa gambar diambil sepertinya diambil untuk tujuan komersial dan ada pula yang diambil untuk dokumentasi.

    Hal ini mendukung model untuk mempelajari bentuk mobil dengan berbagai macam background.

    Secara keseluruhan, perbedaan yang dominan antara kategori bikes dan cars dalam dataset adalah bentuk objek. 
    Objek dalam dataset cars memiliki dimensi yang lebih besar dibandingkan dengan objek dalam dataset bikes. 
    Hal ini bisa mempengaruhi cara model computer vision mendeteksi dan mengenali objek, karena objek dengan dimensi yang lebih besar akan memiliki representasi visual yang berbeda, seperti ukuran pixel yang lebih besar dalam gambar.

    Selanjutnya, saya akan melakukan analisa ruang warna (color modes) pada dataset cars and bikes. Analisa ini dilakukan dengan tujuan menstandarkan input gambar ke model agar data gambar yang nantinya digunakan oleh model sehingga memiliki format yang konsisten dan mencegah terjadinya error.
    """)

    # Function to check color modes
    def listColorMode(folderPath):
        colorModesList = []
        for file in sorted(os.listdir(folderPath)):
            filePath = os.path.join(folderPath, file)
            with Image.open(filePath) as img:
                colorModesList.append(img.mode)
        return colorModesList

    # Check color modes for every image in each category
    bikeModeList = listColorMode(bikeFolder)
    carModeList = listColorMode(carFolder)
    st.write("Jenis color mode yang ada pada dataset bike: RGB, P, RGBA")
    st.write("Jenis color mode yang ada pada dataset car: RGB, P, RGBA")
    
    # Dataframe bike and car
    st.write("Berikut adalah tabel dari beberapa gambar dengan label beserta keterangan color modesnya:")
    bikesDF = pd.DataFrame({'images':sorted(os.listdir(bikeFolder)), 'label':'bikes', 'colorModes':bikeModeList})
    carsDF = pd.DataFrame({'images':sorted(os.listdir(carFolder)), 'label': 'cars', 'colorModes':carModeList})
    df = pd.concat([bikesDF, carsDF]).reset_index(drop=True)
    df = df.sample(len(df), random_state = 26).reset_index(drop=True)
    st.dataframe(df)

    # Jumlah color modes
    st.write('Jumlah total masing-masing color mode:')
    colorModes =["RGB", "RGBA", "P"]  
    count = [1982, 14, 4]
    dfColor = {"Color Modes": colorModes,
               "Count": count}
    st.dataframe(dfColor)
    st.write("""
    Dari perhitungan diatas, diperoleh informasi bahwa ditemukan total 16 gambar dengan color modes RGBA atau 0.4% dari total data dan ditemukan 7 gambar dengan color modes P atau 0.175% dari total data. 
    Sehingga 99.425% memiliki color modes RGB.
             
    Berdasarkan studi literatur yang saya lakukan, salah satu jurnal mengenai Color Spaces menyatakan bahwa hasil kualitatif dari pembuatan arsitektur yang penulis lakukan menunjukkan bahwa perhitungan loss sebaiknya dilakukan dalam ruang warna RGB.
    
    Journal link: [Influence of Color Spaces for Deep Learning Image Colorization](https://arxiv.org/abs/2204.02850).

    Karena data RGB yang tersedia sudah cukup banyak (99.425%). 
    Maka, di proses feature engineering akan dilakukan penghapusan untuk image dengan color modes P dan RGBA. 
    Sehingga, model akan belajar dengan gambar yang memiliki RGB color modes saja.

    Selanjutnya saya akan melakukan analisa mengenai ukuran dari file gambar yang ada dalam dataset.
    """)

    # Function to check image size
    def checkImageSize(folderPath):
        sizes = []
        for file in sorted(os.listdir(folderPath)):
            filePath = os.path.join(folderPath, file)
            with Image.open(filePath) as img:
                sizes.append(img.size)
        return set(sizes)

    # Check image size for each images file
    bikeSizes = checkImageSize(bikeFolder)
    carSizes = checkImageSize(carFolder)

    # Mengubah ke DataFrame
    dfBikeSize = pd.DataFrame(list(bikeSizes), columns=["Width", "Height"])
    st.write("Beberapa macam ukuran gambar pada dataset bike:")
    st.dataframe(dfBikeSize)
    st.write("Ditemukan jumlah unique size pada dataset bike adalah sebanyak 307.")

    # Mengubah ke DataFrame
    dfCarSize = pd.DataFrame(list(carSizes), columns=["Width", "Height"])
    st.write("")
    st.write("Beberapa macam ukuran gambar pada dataset car:")
    st.dataframe(dfCarSize)
    st.write("Ditemukan jumlah unique size pada dataset car adalah sebanyak 231.")
    st.write("""
    Dari hasil perhitungan diatas, ditemukan bahwa image dalam dataset memiliki ukuran yang berbeda-beda. 
    Untuk dataset Bike memiliki 307 ukuran yang berbeda dan untuk dataset Car memiliki 231 ukuran yang berbeda. 
    Sehingga, pada proses feature engineering akan dilakukan resizing untuk menstandarkan ukuran gambar.      
    Hal ini diperlukan agar input gambar konsisten, mengurangi beban komputasi, penyederhanaan gambar dan persiapan augmentasi.
    """)

    # Subheader
    st.subheader("Kesimpulan EDA")
    st.write("""
    Dari hasil EDA yang dilakukan, diperoleh informasi bahwa:
    - Dataset yang dimiliki dominan dengan tipe sepeda motor selain skuter dan motor bebek sedangkan untuk dataset cars sudah cukup mewakili berbagai macam tipe dan bentuk mobil kecuali tipe pickup truck.
    - Dari sudut pengambilan gambar mobil dan motor sudah cukup variatif namun ada yang terlalu jauh sehingga dapat membuat model kesulitan mengenali object.
    - Dari warna object juga sudah cukup variatif agar model dapat mengenali berbagai macam warna object.
    - Dari segi background gambar juga sudah sangat variatif dan dapat membantu model belajar mengenali object dengan berbagai macam background.
    - Ukuran gambar dalam dataset sangat beragam sehingga perlu dilakukan resizing pada saat preprocessing data.
    - Gambar dalam dataset memiliki 3 jenis color modes sehingga perlu diseragamkan dengan membersihkan dataset dari gambar yang memiliki color modes lain selain RGB.
    """)

if __name__ =='__main__':
    run()