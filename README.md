# EmpONada

## Authors
[Adam Rinehouse](https://github.com/arinehouse) and [Ijemma Onwuzulike](https://github.com/ijemmao)

### What Did We Attempt to Build
In this app, we attempted to build a mobile app capable of answering the question, "Is this thing in front of me a spicy jamaican beef patty?"

Unfortunately, we had to expand the classification to be beyond a jamaican beef patty. Instead, our classifier determines whether the object in question is an empanada of any kind. Thus, we have named the app, "EmpONada".

The app is an android app built in java, with a flask backend running TensorfFlow.keras (for deep learning), and hosted on Heroku.

### Who Did What

#### Adam
TensorFlow (though we both did the tutorial), Flask setup, Heroku deployment, image processing with PIL/Pillow

#### Ijemma

TensorFlow tutorial, Android app from scratch, photo upload using multipart/formdata

### What We Learned

#### Adam

I got some basic exposure to TensorFlow but it was at a very high level. The real trick was struggling with PIL and numpy to get them to work well together, as well as deploying a flask application to Heroku, which I hadn't done before.

#### Ijemma
I wanted to learn more about Android development outside of class. I worked with a Mutlipart data object constructor and the Android AsyncHttpClient. I also got to use the `googleimagedownloads` Python library to scrape images from Google Images. I realized that this package was able to be used to such a large scale because it's not repeatedly query Google for images in a short amount of time.

### How does this relate to possible project ideas?

#### Adam
I was really excited about the idea of using a big deep learning framework, and especially deploying it remotely instead of just hosting on a local machine. It's also important to understand how to submit requests to a server from mobile, which is something I actually have not dealt with before.

#### Ijemma
In order for projects to have a wider reach to more users, mobile development has to be considered. A large portion of the global population uses Android, so it makes sense to consider creating a native Android application instead of using React Native or iOS.

### What Didn't Work

#### Adam
A lot didn't work, actually. The backend code is fairly messy but I tried to make it as clean as possible. Originally it was designed as a bunch of functions for testing, but then I had to reformat a bunch of the code flow and ultimately ended up making the neural network a class so that I could persist it in the server. Unfortunately, instead of caching, I just left it as a global, which is a terrible idea, but since we were short on time I just hacked together what works. Flask was also a big issue, trying to get functions to run on startup etc. The simplest way to do this was to manually call a function on a specific setup GET request, but again this is an extremely hacky way of doing things and is not fit for production.

#### Ijemma
MULTITHREADING IN JAVA. It was surprisingly difficult to get the Android app to handle multiple threads when dealing with async requests. Because this was such a issue with the completion of the project, I decided to look for a package that would handle multiple threads internally. 