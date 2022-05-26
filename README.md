# MS-Engage Content-Based-Movie-Recommender-System
The project was built as a part of the Microsoft Engage '22 Program. Contributors were required to Demonstrate through their app the different kinds of algorithms that a web-streaming app (like Netflix) or an audio-streaming app (like Spotify) may use for their Recommendation Engine within a span of 4 weeks.
Content Based Recommender System recommends movies similar to the movie user likes and analyses the sentiments on the reviews given by the user for that movie.

Check out the live demo:

# Features Implemented
1. Top 10 recommended movie
2. Overview genre title etc of the movie
3. Top cast of the movie
4. Role the different cast played in the movie
5. About top cast of the movie 
6. User Reviews
7. About page to help the user know more about the website
8. Authentication and login
9. Updating Profile
10. The site is completely responsive

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API, I did web scraping to get the reviews given by the user in the IMDB site using `beautifulsoup4` and performed sentiment analysis on those reviews.

# Tech Stack
<p align ="center">
  <code><img src="http://api.buttercms.com/static/images/tech_banners/Flask.716baf905d79.png" width="10%" /></code>
  <code><img src="https://www.digitaldesignjournal.com/wp-content/uploads/2018/07/Python-Programming-Wallpaper_1.jpg" width="10%" /></code>
  <code><img src="https://www.sqlalchemy.org/img/sqla_logo.png" width="10%" /></code>
  <code><img src="https://img.icons8.com/color/64/000000/git.png" width="10%"/></code>
  <code><img src="https://img.icons8.com/color/64/000000/github.png" width="10%"/></code>

# Major Learnings
1. **Perseverance and debugging skills**: Having faced numerous bugs that seemed *impossible* to solve at first to actually overcoming them felt like victory. It improved my problem solving skills and faith in hardwork.
2. **New Technologies**: The project was a fun introduction to flask, content based recommendation and databases for me and I thoroughly enjoyed learning the new technologies. With the help of my friends and mentors as well as self study I was able to grow my knowledge.
3. **Growth mindset**: The sessions as well as the project taught me that our skills can be improved and having a growth mindset helps one and their organization in the long run.


# Similarity Score : 
  How does it decide which item is most similar to the item user likes? Here we use the similarity scores.
   
  It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
   
# How Cosine Similarity works?
  Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
  
  ![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)

More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

# Snapshots of the project
<h4>Recommendation system</h4>
<img src="https://i.imgur.com/hNwkzRm.png" width=600 height=400>
<img src="https://i.imgur.com/diIPLCl.png" width=600 height=400>
<br />
<h4>Reviews and cast</h4>
<p float="left">
  <img src="https://i.imgur.com/1lwj7i4.png" width=400 height=300 />
  <img src="https://i.imgur.com/XOz4yKx.png" width=400 height=300/>
</p>
<br />
<h4>About and Update profile </h4>
<p float="left">
  <img src="https://i.imgur.com/6AWGa5P.png" width=280 height=300 />
  <img src="https://i.imgur.com/jP5U4j7.png" width=280 height=300/>
</p>
<br />
<h4>Authentication</h4>
<p float="left">
  <img src="https://i.imgur.com/dSmbSDP.png" width=280 height=300 />
  <img src="https://i.imgur.com/ACeZCM0.png"width=280 height=300/>
</p>

# How to get the API key?
Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved.

# How to run the project?
1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the [requirements.txt] file with the command `pip install -r requirements.txt`
3. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
3. Replace YOUR_API_KEY in both the places (line no. 15 and 29) of `temp/static/recommend.js` file and hit save.
4. Open your terminal/command prompt from your project directory and run the file `run.py` by executing the command `python run.py`.
5. Go to your browser and type `http://127.0.0.1:5000/` in the address bar.
6. Hurray! That's it.

# Sources of the datasets 
1. [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
2. [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
3. [List of movies in 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)
4. [List of movies in 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
5. [List of movies in 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)
