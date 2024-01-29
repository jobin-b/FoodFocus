<h1>FoodFocus</h1>
<p>
  This project was developed during the SpartaHack9 Hackathon on the weekend of the 27th of January, 2024.
  It is designed to be a nutrition tracking web app,
  
  It estimates nutrition content of meals and adds it to a database for long-term tracking.
  Nutrition estimation begins with the user uploading a picture of their food to the webapp.
  This image is then processed by a pre-trained AI model from google, which identifies what type of dish the food contains.
  This dish is then sent to the Edamame api, which estimates the nutrition content of the dish.
  The resulting nutrition data is then stored in the database, where the data can be queried and
  shown back to the user as either a part of daily nutrition goals, or long-term tracking.
</p>

<h1>Pages</h1>
<h2>Landing</h2>
<img src="https://raw.githubusercontent.com/jobin-b/FoodFocus/main/demo/landing.webp">
<h2>Home</h2>
<img src="https://raw.githubusercontent.com/jobin-b/FoodFocus/main/demo/home.webp">
<h2>Goals & Settings</h2>
<img src="https://raw.githubusercontent.com/jobin-b/FoodFocus/main/demo/settings.webp">

<h1>Technologies Used</h1>
<dl>
  <dt>Backend</dt>
  <dd>
    The back-end service was developed as a RESTful api, which responds to requests with json data.
    It queries the database, submits requests to external apis, and runs the image classification model locally.
  </dd>
  <dt>Database</dt>
  <dd>
    This project uses MongoDB as the database, and uses the ORM developed for python to access it.
  </dd>
  <dt>Image Classification</dt>
  <dd>
    This project uses 
    <a href="https://www.kaggle.com/models/google/aiy/frameworks/tensorFlow1/variations/vision-classifier-food-v1">a pre-trained model from Google</a> 
    to classify what meal is in an image. This classification is used to query an external api to get nutrition estimates for it.
    The model is run locally (on the back-end) using tensorflow.
  </dd>
  <dt>Image Nutrition Data</dt>
  <dd>
    Image nutrition data is obtained from the <a href="https://www.edamam.com/">Edamam</a> api. This api returns
    nutrition data estimates given a string which describes a meal/cuisine.
  </dd>
  <dt>Front-End</dt>
  <dd>
    The frontend of this web app uses React to coordinate between the backend and user.
    We decided this framework would be nessecary since we wanted to show the user lots of
    data that would be updated frequently (charts, daily information). TailWindCSS was used to
    style the website.
  </dd>
  <dt>Authentication</dt>
  <dd>
    This project uses Auth0 for user authentication. This was done to both simplify the authentication implementation, 
    and also simplify logging in for the user.
  </dd>
</dl>

<h3>Contributors</h3>
<br>
<ul>
  <li><a href="https://github.com/jobin-b">Jobin Babu </a></li>
  <li><a href="https://github.com/banana2244">Ashton Mamou </a></li>
  <li><a href="https://github.com/NaveenJohnPremkumar">NaveenJohn Premkumar </a></li>
  <li><a href="https://github.com/RyanA3">Ryan Alsobrooks </a></li>
</ul>
