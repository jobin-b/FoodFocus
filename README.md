This project was developed during the SpartaHack9 Hackathon on the weekend of the 27th of January, 2024.
Contributors:
Jobin Babu https://github.com/jobin-b
Ashton Mamou  
NaveenJohn Premkumar  
Ryan Alsobrooks https://github.com/RyanA3

It is designed to be a nutrition tracking web app,

It estimates nutrition content of meals and adds it to a database for long-term tracking.
Nutrition estimation begins with the user uploading a picture of their food to the webapp.
This image is then processed by a pre-trained AI model from google, which identifies what type of dish the food contains.
This dish is then sent to the Edamame api, which estimates the nutrition content of the dish.
The resulting nutrition data is then stored in the database, where the data can be queried and
shown back to the user as either a part of daily nutrition goals, or long-term tracking.
