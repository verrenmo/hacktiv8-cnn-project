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
    st.write('This page contains Exploratory Data Analysis (EDA) about Car and Bike Dataset.')
    st.write('Dataset source: [click here](https://www.kaggle.com/datasets/utkarshsaxenadn/car-vs-bike-classification-dataset/data)')

    # Subheader
    st.subheader("Explanation of EDA")
    # Display 75 images of bike
    bikeFolder = "Car-Bike-Dataset/Bike"
    st.write("Here are 75 images from the bike dataset:")
    st.image("eda1.png")
    st.image("eda2.png")
    st.image("eda3.png")

    # Bike image analysis
    st.write("""
    Based on the source I read ([Understanding 8 Types of Motorcycles](https://www.inews.id/otomotif/motor/mengenal-8-jenis-sepeda-motor-dari-model-skuter-hingga-touring/2)), there are 8 types of motorcycles:  
    1. Cub 
    2. Scooter  
    3. Dual-Sport  
    4. Naked Bike  
    5. Sport Bike  
    6. Retro  
    7. Cruiser  
    8. Touring  

    Based on the 75 images in the bike category displayed above, it was found that the motorcycle images in the dataset are dominated by Dual-Sport, Naked Bike, Sport Bike, Retro, Cruiser, and Touring types. There are no images of motorcycles belonging to the Cub or Scooter types. The model is likely to learn more from images of motorcycle shapes other than Cub and Scooter types.

    In terms of color, many motorcycles in the images are dominated by black, white, red, and blue. It was also found that a motorcycle can contain two colors, such as red and black, blue and black, or white and black.

    Additionally, the angles of the images in the bike category are quite varied, including front views, side views (right and left), front and side views, and rear views of motorcycles. This allows the model to learn the shape of motorcycles from multiple angles. However, some images are taken from a considerable distance from the camera, which may make it difficult for the model to recognize motorcycles.

    From some images in the bike category displayed, the following characteristics were also found:  
    - Some images only show partial parts of motorcycles, such as the front, rear, or side.  
    - Some images in the dataset have no background (only white), while others feature road backgrounds, expansive grassy views, racetrack environments, house yards, or even indoor exhibition settings.  
    - Some images show motorcycles being ridden by people, taken with a model, or only show the motorcycle without people.  
    - Some images appear to be taken for commercial purposes, while others seem to be for documentation.  
    - Some images contain more than one motorcycle.  

    These characteristics allow the model to learn to recognize motorcycle shapes in various backgrounds and conditions. However, it may also make it challenging for the model to recognize images if only certain parts of the motorcycle are visible in the image.    
    """)

    # Display 75 images of car
    carFolder ="Car-Bike-Dataset/Car"
    st.write("Here are 75 images from the bike dataset car:")
    st.image("eda4.png")
    st.image("eda5.png")
    st.image("eda6.png")

    # Car images analysis
    st.write("""
    Based on the source I read ([Car Types](https://www.caranddriver.com/shopping-advice/g26100588/car-types/)), there are several types of cars, including:  
    1. Sedan  
    2. Coupe  
    3. Sports Car  
    4. Station Wagon  
    5. Hatchback  
    6. Convertible  
    7. Sport-utility Vehicle (SUV)  
    8. Minivan  
    9. Pickup Truck  

    From the 75 images in the car category, it was found that the car images in the dataset fairly represent the mentioned car types, except for the pickup truck type. Thus, the model will learn a lot about the shapes of various car types, but the absence of the pickup truck type may make it difficult for the model to recognize the object.  

    In terms of color, the car images are dominated by red, white, black, blue, and orange. It is very rare to find car images with a combination of two colors (unlike the motorcycle images).  

    In addition, the angles of the images are quite varied, including front views, side views (right and left), rear views, front and side views, and top views. This allows the model to learn to recognize the object from various angles. However, some cars are far from the camera, which may make it difficult for the model to recognize their shapes.  

    From some images in the car category displayed, the following characteristics were found:  
    - Some images have no background (only white or black), while others feature roads, buildings, scenic views, and indoor exhibition settings.  
    - Some images appear to be taken with the car in motion, and some include humans near the car.  
    - Some images seem to have been taken for commercial purposes, while others seem to be for documentation.  

    This supports the model in learning car shapes with various backgrounds.  

    Overall, the dominant difference between the bike and car categories in the dataset is the shape of the objects. Objects in the car category have larger dimensions compared to those in the bike category. This can affect how the computer vision model detects and recognizes objects, as larger objects will have a different visual representation, such as larger pixel sizes in the images.  

    Next, I will perform a color mode analysis on the car and bike datasets. This analysis aims to standardize the image input for the model so that the image data used by the model later will have a consistent format and prevent errors.""")

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
    st.write("Types of color modes present in bike dataset bike: RGB, P, RGBA")
    st.write("Types of color modes present in car dataset: RGB, P, RGBA")
    
    # Dataframe bike and car
    st.write("Here is a table of several images with labels and descriptions of their color modes:")
    bikesDF = pd.DataFrame({'images':sorted(os.listdir(bikeFolder)), 'label':'bikes', 'colorModes':bikeModeList})
    carsDF = pd.DataFrame({'images':sorted(os.listdir(carFolder)), 'label': 'cars', 'colorModes':carModeList})
    df = pd.concat([bikesDF, carsDF]).reset_index(drop=True)
    df = df.sample(len(df), random_state = 26).reset_index(drop=True)
    st.dataframe(df)

    # The number of color modes
    st.write('Total number of each color modes:')
    colorModes =["RGB", "RGBA", "P"]  
    count = [1982, 14, 4]
    dfColor = {"Color Modes": colorModes,
               "Count": count}
    st.dataframe(dfColor)
    st.write("""
    From the calculations above, it was found that there are a total of 16 images with color mode RGBA, which accounts for 0.4% of the total data, and 7 images with color mode P, which accounts for 0.175% of the total data. Therefore, 99.425% of the images have the RGB color mode.

    Based on a literature review I conducted, one journal on Color Spaces states that the qualitative results of the architecture creation suggest that loss calculation should be done in the RGB color space.  

    Journal link: [Influence of Color Spaces for Deep Learning Image Colorization](https://arxiv.org/abs/2204.02850).

    Since the available RGB data is quite abundant (99.425%), in the feature engineering process, images with P and RGBA color modes will be removed. This will ensure that the model only learns from images that have the RGB color mode.

    Next, I will analyze the file sizes of the images in the dataset.
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

    # To DataFrame
    dfBikeSize = pd.DataFrame(list(bikeSizes), columns=["Width", "Height"])
    st.write("Several types of image sizes in the bike dataset:")
    st.dataframe(dfBikeSize)
    st.write("The number of unique sizes found in the bike dataset is 307.")

    # To DataFrame
    dfCarSize = pd.DataFrame(list(carSizes), columns=["Width", "Height"])
    st.write("")
    st.write("Several types of image sizes in the car dataset:")
    st.dataframe(dfCarSize)
    st.write("The number of unique sizes found in the car dataset is 231.")
    st.write("""
    From the calculations above, it was found that the images in the dataset have different sizes. 
    For the Bike dataset, there are 307 different sizes, and for the Car dataset, there are 231 different sizes. 
    Therefore, in the feature engineering process, resizing will be performed to standardize the image sizes. 
    This is necessary to ensure consistent image input, reduce computational load, simplify the images, and prepare for augmentation.
    """)

    # Subheader
    st.subheader("EDA Conclusion")
    st.write("""
    Based on the results of the EDA, the following information was obtained:
    - The bike dataset is dominated by motorbike types other than scooters and underbones, while the car dataset sufficiently represents various car types and shapes, except for pickup trucks.
    - The image angles for cars and motorcycles are quite varied, although some are too far away, making it difficult for the model to recognize the objects.
    - The object colors are sufficiently varied for the model to recognize different object colors.
    - The backgrounds in the images are also highly varied, helping the model learn to recognize objects in various backgrounds.
    - The image sizes in the dataset are very diverse, requiring resizing during data preprocessing.
    - The dataset contains 3 types of color modes, so it needs to be standardized by cleaning the dataset of images with color modes other than RGB.
    """)

if __name__ =='__main__':
    run()