# Team 4 from DeepLearning540 course notebook: 

# Day 1 :grinning:
Mar 1 - 3, 2021 @ 2nd Terascale School for Machine Learning, https://indico.desy.de/event/28296/

## House Keeping
Some important links to not get lost:

- zoom link team 4: https://cern.zoom.us/j/69653268222?pwd=UXI2NlpkblJwVG82QURCbWZmcHFiZz09
- the main mattermost channel: https://mattermost.web.cern.ch/signup_user_complete/?id=j93uppzm6ff9zg5brdeuqobfgw
- team 4 mattermost channel: https://mattermost.web.cern.ch/terascale-ml/channels/group-4

## Say Hello
- good morning!
- Moin!
- Привіт!
- Oi!
- Moin Moin!
- Hello!
- Bom dia!
- HI
- :wave: 

## Time Frames lesson 1 :timer_clock: 
- ~~9:30-10:10 Watch the lesson 1 video and start the exercise~~
- ~~10:10-10:20 Check-your-learning question~~
- ~~10:20-10:30 Discussion and completion of the exercise~~ 
- 10:00 - 10:40 Watch the lesson 1 video and start the exercise
- 10:40 Meeting at zoom and discussion


## Course working materials:
https://deeplearning540.github.io/lesson01/content.html


---

## Lesson 1:
- Download the video :cinema:: [link]( https://indico.desy.de/event/28296/contributions/99576/attachments/64395/79079/deeplearning540-lesson01-2021-02-19_17.59.48.mkv)
- Link to the jupyter notebook: [link](https://github.com/deeplearning540/lesson01/blob/main/lesson.ipynb)

:question: Instructors help with show stoppers like syntax errors where they can.
:computer: if you like to conduct the exercises, or code along during the videos, we suggest to use google colab. Note, you may need a google account for this.

Each lesson has a jupyter notebook, that is half filled. The video lectures start from this notebook and provide content to fill in.

### Lesson 1 notes:

- If you want to execute linux commands in colab you can write them with `!` directly in the cell, e.g:  !ls, !pwd, !lscpu ... you can pip install something if needed
- to reference the column in the dataframe use `df.iloc[:,2]` where `:` means to take all the rows and 2 means the second column. (alternative: `df.loc[:, 'Jan']`)
- `pd.to_numeric` converts to numeric representation
- .fillna(method='ffill') to use build-in method to fill NaNs
- to do "Least squares" fit for one month:
```
from sklearn import linear_model
ytrain = df[["Mar"]].values
xtrain = df[["year"]].values
model = linear_model.LinearRegression()
model = model.fit(xtrain, ytrain)
print("y = w*x + b = {:2.5f}*x + {:2.5f}".format(model.coef_[0][0],
                                                 model.intercept_[0]))

```



### Lesson 1 check-your-learning:
Exercise 1

In the following, the order of steps was confused, please rearrange:

- collect training data, compute accuracy, predict new data, fit training data
- compute accuracy, collect training data, predict new data, fit training data
- collect training data, fit training data, compute accuracy, predict new data 
+1
+1
+1
+1
+1
+1
+1
+1
- collect training data, predict new data, fit training data, compute accuracy

Exercise 2

The least squares method for an input data pair `x` and `y` derives it’s name as it …

- Minimizes the sum of the product of x*y
- Minimizes the sum of the absolute difference between y and the predicted y_hat
- Minimizes the sum of the squared difference between y and the predicted y_hat 
+1+1+1+1+1+1+1+1
- Minimizes the sum of $y^2$ and $x^2$

Exercise 3

NaN stands for not-a-number. When loading a dataset with `pandas`, NaN values occur in the loaded data because …

- Input files contain string values in a column
- Computational Problems occurred, like computing the square root of a negative number
- Data could not be parsed correctly when reading input files into memory 
+1+1+1+1+1+1+1+1
- there was no internet connection

### Technical problems:
- Fine
+1+1+1+1+1+1+1+1
- Problems


---

### Time Frames lesson 2 :timer_clock: 
- 11:00-**11:45** Watch the lesson 2 video and start the exercise
- **11:45**-11:50 Check-your-learning question
- 11:50-12:00 Discussion and completion of the exercise

### Write +1 if you are present at the second lesson:
+1+1+1+1+1+1+1+1+1


## Lesson 2:

- Link to the video: [link](https://indico.desy.de/event/28296/contributions/97975/attachments/64396/79084/deeplearning540_lesson02-2021-02-22_23.30.44.mkv)
- Link to the jupyter notebook: [link](https://github.com/deeplearning540/lesson02/blob/main/lesson.ipynb)

### Have you finished the video? :cinema: 
:+1: 
+1
+1
+1
+1
+1
+1
+1
### Questions from the video lessons

- from another group: Is the forward fill the correct method for preprocessing NaNs for linear regression? Shouldn't we use e.g. ".dropna()" to drop the rows containing NaNs? 

`ffill` effectively doubles the weight of one measurement, which may not be what you want to do

## BTW: what is your field of research/study ?
- Particle physics at CMS
- Particle physics at LHCb
- Experimental Particle Physics at ATLAS, SM Higgs boson stuff
- Experimental Particle physics at ATLAS
- Theoretical Particle Physics, Flavor
- Particle physics at ATLAS
- particle physics
- Particle Phy at ATLAS
- Experimental Physics at ATLAS, detector development

### Lesson 2 notes:

- to do scatter plot
```
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import seaborn as sns
sns.scatterplot(x=df.bill_length_mm, y=df.flipper_length_mm, palette="husl")
plt.show()

```
- to do KMean clustering
```
import sklearn.cluster as skl_cluster
import numpy as np
kmeans = skl_cluster.KMeans(n_clusters=3, init='random')
data = np.stack((df.bill_length_mm, df.flipper_length_mm), axis=-1)
kmeans = kmeans.fit(data)
```

- DBScan https://en.wikipedia.org/wiki/DBSCAN

### Lesson 2 check-your-learning:

Exercise 1

You are provided a table of measurements from a weather station. Each measurements comes with values for temperature, precipation, cloud structure, date, humidity, and a quality ID. The latter tells you if the instrument was performing OK. You’d like to learn an algorithm that is able to predict the quality ID (5 possible integer values from 0 to 4) for any new data coming in. This falls into …

- Supervised Learning
+1+1+1+1+1+1+1+1+1
- Unsupervised Learning
- Reinforcement Learning

Exercise 2

You are given a dataset of iris flowers. The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Which of the following feature combinations lend themselves for clustering? See this overview [plot](https://en.wikipedia.org/wiki/Iris_flower_data_set#/media/File:Iris_dataset_scatterplot.svg) for help.


- Sepal.Length versus Sepal.Width
- Sepal.Length versus Petal.Width
- Petal.Length versus Petal.Width
+1+1+1+1+1
- Sepal.Width versus Petal.Width
+1

Exercise 3

You are helping to organize a conference of more than 1000 attendants. All participants have already paid and are expecting to pick up their conference t-shirt on the first day. Your team is in shock as it discovers that t-shirt sizes have not been recorded during online registration. However, all participants were asked to provide their age, gender, body height and weight. To help out, you sit down to write a python script that predicts the t-shirt size for each participant using a clustering algorithm. You know that you can only get 7 t-shirt sizes (XS, S, M, L, XL, XXL). This falls into:

- Supervised Learning
- Unsupervised Learning
+1+1+1+1+1+1+1+1
- Reinforcement Learning

## Technical problems:
- Fine +1
:+1:+1+1+1+1+1:+1:1
- Problems

# Day 2 :hamster: 

## Time Frames Day 2 :timer_clock: 
- 9:00 - 9:55 Watch video 3 part1 & 3 part2 and work with the notebook
- 9:55 - 10:10 Short coffee break (we can meet at zoom also)
- 10:10 - 10:20 Meeting at zoom and discussion
- ~~10:20 - 11:00 Watch video 4~~
- ~~11:00 - 11:10 Short coffee break (we can meet at zoom also)~~
- ~~11:10 - 11:50 **Watch video 5** (NNs are here already!)~~
- ~~11:50 - 12:00 Meeting at zoom and discussion~~

## Alternative Time Frames Day 2 :timer_clock:
- 11:30-11:45 Meeting at zoom and discussion
- 11:45-12:15 Coffee break
- 12:15-12:45 Feedback session
- 13:00-13:40 Video 5
- 13:40-13:55 Discussion

## Lesson 3
- Link to the video part 1 (27 min): [link](https://indico.desy.de/event/28296/contributions/97976/attachments/64398/79089/deeplearning540_lesson03-2021-02-23_23.14.33_part1.mkv)
- Link to the video part 2 (24 min): [link](https://indico.desy.de/event/28296/contributions/97976/attachments/64398/79097/deeplearning540_lesson03_part2-2021-02-26_22.37.04.mkv)
- Link to the jupyter notebook: [link](https://github.com/deeplearning540/lesson03/blob/main/lesson.ipynb)
- Link to the jupyter notebook with solutions: [link](https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson03/script.ipynb)

## General remark:
After the course it is recommended to do the exercises to the lesson:
https://deeplearning540.github.io/lesson03/content.html

### Type +1 after both videos are done:
+1+1+1+1 :+1:+1+1+1

### votes for canceling lesson 5 (moving to Wednesday):
:+1: :+1::-1:-1

### votes for meeting after 13:00:
:+1: :+1:+1+1:+1:+1 +1

### Lesson 3 notes:
![](https://i.imgur.com/DqCJZ6C.png)

- Four important evaluation metrics:
-- accuracy = (tp + tn) / total
-- true positive rate (recall) = tp / (tp + fn)
-- precision = tp / (tp + fp)
-- F1 score = 2 * precision * recall / ( precision+recall )

### Check your Learning

The following questions serve as a help for learners to reflect on the content of the videos. Answer at least one question. At best you want to answer these questions as a team.

#### Exercise 1

   When using the k-Nearest-Neighbor (kNN) algorithm for classifying a query point `x_q`, the `k` stands for:

   1. the number of neighbors that must have a given label for the query point to get this label assigned
   
   2. the number of classes occurring in the data set
   
   3. the number of observations that define a neighborhood
   +1+1+1+1+1+1:+1:

   
   4. the number of clusters in the dataset
 
 
#### Exercise 2

   When going through tutorials and exercises that discuss the k-Nearest-Neighbor (kNN) method, you observe that `k` is typically chosen to be an odd number. Checking the code, `sklearn` also access even numbers for `k`. Why do people tend to choose odd numbers?

   1. tradition that often works best in practice
   
   2. odd numbers prevent ties from happening with the majority vote +1+1+1+1
   
   3. this way, the total number of samples in the neighborhood is always even as one has to add the query sample
   
   4. odd numbers prevent ties from happening with the plurarity vote
    +1:+1::+1:+1
   
   
#### Exercise 3

   What is the majority vote and the plurality vote if the 8 nearest neighbors to your unknown data point are of the following classes:

   a)
   
   - class 1: 3
   - class 2: 2
   - class 3: 2
   - class 4: 1

   majority vote: `____`
   plurality vote: `____`

   b)
   
   - class 1: 5
   - class 2: 2
   - class 3: 1

   majority vote: `____`
   plurality vote: `____`


#### Exercise 4

   Find the four hidden bug(s)!
   
   **We can do one bug by the person.**

   .. code-block:: python

      from sklearn.neighbors import KNeighborsClassifier as knn
      from sklearn.model_selection import train_test_split
      from sklearn.metrics import confusion_matrix

      # ... load dataset ...

      X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    -> test_size = 1.5,
                                                    random_state = 42)
      kmeans = knn(n_neighbors=5)
      kmeans = kmeans.fit(X_train, y_train)
      -> y_test_hat = kmeans.predict(X_train)

      -> cm = confusion_matrix(y_train, y_test_hat)

      -> accuracy = (cm[0,0]+cm[0,1]) / cm.sum()
      

## Lesson 4
- Link to the video (40 min): [link](https://indico.desy.de/event/28296/contributions/97977/attachments/64400/79098/deeplearning540_lesson04-2021-02-24_18.09.02.mkv)
- Link to the jupyter notebook: [link](https://github.com/deeplearning540/lesson04/blob/main/lesson.ipynb)
- Link to the jupyter notebook with solutions: [link](https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson04/script.ipynb)

### Type +1 when you finish the video 4:
+1+1:+1:+1:+1: :+1:+1

### Lesson 3 notes:
![](https://i.imgur.com/r9eS7Jv.png)
- $TPR = \frac{TP}{TP+FN}$ also known as `recall`, always within $[0,1]$
- $FPR = \frac{FP}{FP+TN}$ also known as `fall-out`, always within $[0,1]$

### Check your Learning

The following questions serve as a help for learners to reflect on the content of the videos. Answer at least one question. At best you want to answer these questions as a team.

#### Exercise 1

   The `ROC` acronym stands for

   1. Receiver Operator Curve

   2. Receiving Operates Curves

   3. Receiver Operating Characteristic
:+1:+1:+1:+1+1
   4. Reception Occlusion Characteristic


####  Exercise 2

   Fill in the blanks!

   A k-Nearest-Neighbor (kNN) classifier can produce a probability when predicting the class label of an unseen sample `x_q`. This can be achieved by counting class `members/labels` in the training set neighborhood of this query point.

   For a `k=7` neighborhood, the threshold to decide for any given class in this neighborhood is calculated as `4/7`. In the same setting (`k=7`), let's assume we find `5` labels for class `1` and `2` labels for class `0`. This means, that we get two probabilities, which are `5/7` for class `1` and `2/7` for class `0`. 


## Lesson 5
- Link to the video part (40 min): [link](https://indico.desy.de/event/28296/contributions/97977/attachments/64400/79101/deeplearning540_lesson05-2021-02-25_17.48.08.mkv)
- Link to the jupyter notebook: [link](https://github.com/deeplearning540/lesson05/blob/main/lesson.ipynb)
- Link to the jupyter notebook with solutions: [link](https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson05/script.ipynb)

## are you familiar with NN already?
+1 +1 +1+1+1
(but only with the theory part, not in practice) +1

### Check your Learning

The following questions serve as a help for learners to reflect on the content of the videos. Answer at least one question. At best you want to answer these questions as a team.

#### Notes:
```
df_iris = sns.load_dataset('iris') 
X = df_iris[["sepal_length","sepal_width","petal_length","petal_width"]].values
y = df_iris["species"].values
```
- https://playground.tensorflow.org/

#### Exercise 1

   A hidden layer of an artificial neural network consists a fixed set of parts. These are ...

   1. weights $W$ and a bias term $\vec{b}$
   2. weights $W$ and a non-linear activation function $F$
   3. a bias term $\vec{b}$ and a non-linear activation function $F$
   4. weights $W$, a bias term $\vec{b}$ and a non-linear activation function $F$ +1+1+1+1 :+1:

#### Exercise 2

   Unlike `scikit-learn`, `keras` is a machine learning framework that ...

   1. offers one-stop-shop prepared networks that are already published 
   2. offers building blocks to construct neural networks on CPU or GPU architectures
   3. offers an API to either wrap around backends (keras library) or represents the high-level API for `tensorflow` +1+1
   4. all of the above

# Day 3 :

## Time Frames Day 2 :timer_clock: 
- 9:20 - 10:00 Work with lesson 6
- 10:00 - 10:20 Short dis.
- ~~10:20 - 11:00 Work with lesson 7~~
- ~~11:10 Start looking into the project~~
- 10:40 - 11:30 Work with lesson 7 :triangular_ruler: 
- 11:30 - 11:40 Meeting in zoom and further plan :airplane: 

## Did you finish lesson 5 (+1)?:
+1+1+1+1+1

## Your progress with the homework (from 1 to 3):
+2+2+1+1+3

## Vote for exercises :angel: vs. capstone project :japanese_ogre: ("ex" vs "cp")
cp, cp, cp
cp
cp
no preference
### Lesson 6
- Link to the video 6: [link](https://indico.desy.de/event/28296/contributions/98225/attachments/64451/79196/deeplearning540_lesson06-2021-01-03_233847.mkv)
- slides: [link](https://indico.desy.de/event/28296/contributions/98225/attachments/64451/79197/deeplearning540-lesson06-slides.pdf)

### Did you finish video 6:

+1+1+1+1
- 

#### Exercise 1
The advantage of mini-batched based optimisation is …

1. a mini-batch represents the entire data set and hence is enough to optimize on 
 
2. the optimisation converges faster +1+1+1+1+1

3. the optimisation can be performed in memory independent of the data set size

4. the optimisation will converge always into a global optimum


#### Exercise 2
Categorical Cross-Entropy is part of a well-known divergence in statistics. A divergence is a method to compare two probability density functions. It provides a large value if two distributions are different and a small value if they are similar. This well-known divergance that spurrs the Categorical Cross-Entropy is …

1. Mean-Squared-Error divergence

2. Negative-Log-Likelihood divergence

3. Kullback-Leibler divergence +1+1+1+1+1+1

4. Maximum-Mean-Discreptancy divergence


#### Exercise 3
The gradient that is required for gradient descent is the gradient …

1. of the loss function L with respect to the testset input data, df/dx, given the network parameters theta

2. of the network f with respect to the input data, df/dx, given the network parameters theta

3. of the network f with respect to the network parameters, df/dtheta, given the training data x

4. of the loss function L with respect to the network parameters, df/dtheta, given the training data x  +1+1+1



### Lesson 7
- Link to the video part 1: [link](https://indico.desy.de/event/28296/contributions/98226/attachments/64470/79239/deeplearning540_lesson07_part1-2021-03-02_17.11.15.mkv)
- Link to the video part 2: [link](https://indico.desy.de/event/28296/contributions/98226/attachments/64470/79240/deeplearning540_lesson07_part2-2021-03-02_17.39.37.mkv)
- full notebook: [link](https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson07/script.ipynb)

### Did you finish the video(+1)?
+1+1:+1: +1+1


#### Exercise 1
Fill in the blanks to produce a CNN for classification!

```python 
from tensorflow import keras from keras.layers import Input,
Dense, Dropout, Flatten, Conv2D, MaxPooling2D

#load the data

# define the network
# padding = same
conv1 = Conv2D(16, kernel_size=(3,3), activation=’relu’, input_shape=X_train.shape[1:]) 
conv2 = Conv2D(32, kernel_size=(3,3), activation=’relu’) 
mpool = MaxPooling2D(pool_size=(2,2)) -> 3D tensor

## MLP layers 
flat = Flatten() # 3D structure -> 1D array
dense1 = Dense(128, activation='anything') 
dense2 = Dense(num_classes, activation='softmax')

#compile and train

x_inputs = Input(shape=X_train.shape[1:])
x1 = conv1(x_input) 
x2 = conv2(x1) 
x3 = mpool(x2)
x4 = flat(x3) 
x5 = dense1(x4) 
output_yhat = dense2(x5)

model = keras.Model(inputs = x_input, outputs = output_yhat, name=”hello-world-cnn”)
```


#### Exercise 2
The Flatten operation rearranges an input image (or feature map) into a sequence of numbers. How does it perform this?

1. ~~the pixel intensities are averaged per row and concatenated~~

2. ~~all rows of the input are added and provided as a result~~

3. all columns of the input are concatenated (from top to bottom)

4. all rows of the input are concatenated (from top to bottom)+1


#### Exercise 3
For an input image shape of 28x28 what is the shape of the feature map after running the image through a single 5x5 convolutional filter?

1. 24x28

2. 20x28

3. 26x26 +1+1+1

4. **24x24** +1


0000000
0111110
0011100
0011100
0011100
0000000
0000000

#### Exercise 4
28x28

(3*3 + 1)*16 = 160

tensor (26*26*16) = 10816

dense -> 16*10816 + 16

For an MNIST input image, how many parameters does a Conv2D layer require when being defined to produce 16 feature maps as output and a 3x3 neighborhood. How many parameters does a Dense layer with 16 outputs have? Compute the two parameter counts!
 
Parameters of Conv2D: 

Parameters of Dense layer: 


# Capstone Project :trident: :trophy: 

https://deeplearning540.github.io/lesson08/content.html#physics

# To download data
```
!wget https://desycloud.desy.de/index.php/s/xip274LKzzypRba/download -O data_train_40k.h5 -c
```
```
!wget https://desycloud.desy.de/index.php/s/xip274LKzzypRba/download -O train_img.h5 -c
```