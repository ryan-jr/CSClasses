# Fast AI lecture 2: Convolutional Neural Networks


* One of the most common ways to structure things is to have a 'train' folder and a 'valid' folder, and within each of those folders is a X folder and a Y folder.  

```
Numbers from our image classifier:

[Epoch number, loss on the training set, loss on the validation set, accuracy]
[0. ]


```

* The key numbers: Epoch(How many times through the data set), Loss on the training set(images we're looking at), loss on the validation set, learning rate.

* We primarily care about the learning rate and the accuracy

* Learning rate: How quickly do we hone in on the solution?  Usually we pick a random point and decide the gradient (up or down), and we see what the error rate is at that point.  

* Be comfortable with scientific notations (10^-1 is .1(1e-1) and 10^-2 is .01(1e-2, 10^0 is 1, etc...)

* The trick for the learning rate is to find on the plot (learn.sched.plot) the lowest point, and the go back about one magnitude.  This is because at the lowest point, the learning rate isn't getting any better, so you want to find the point where it is getting better the most.  

* Also the learn.sched.plot is downward sloping/negative because we want the losss rate to DECREASE.

* Generally the best thing you can do is give your model more data, but sometimes the model will overfit(if not given enough data), which means that the model is learning to recognize specific images in the dataset rather than generalizing in such a way that we get good results on the validation set as well.  

* One way that we can avoid overfitting is through data augmentation, which is changing the test images in a variety of ways.  With fast.ai we can do this by passing aug_tfms to tfms_from_model, and what type of image transforms we want to do.  (architecture, from side on, max_zoom)

*  The data tranforms/augmentations are not entirely new images, but allow the Convolutional Neural Net(CNN) to recognize the image in different ways.

* In order to use the data augmentations we also have to pass in learn.precompute = False so that the model does not use precompiled areas/activations.

* One thing to watch out for, is that if your model is doing much better on the training set than on the validation set, it indicates that your model is not generalizing(AKA: Overfitting)

* There is another paramater that we can pass into the function that is learn.fit() that paramater is cycle length, which would look like learn.fit(cycle_len = 1).  

* The cycle length is part of a technique called stochastic gradient descent with restarts(SGDR), which itself is a variant of learning rate annealing.  (Cycle length basically means reset/change/update the learning rate every epoch, if cycle_len were 2, the learning rate would update every 2 epochs)

* Learning rate annealing is gradually decreasing the learning rate as training progresses, which is because as we get closer to the optimal learning rate, we want to take smaller steps.  

* There are some different approaches/curves to learning rate annealing, one approach is using just a linear learning rate, another is a stepwise learning rate(Find a rate that works for a while, then when it stops working, drop by 10x, repeat (NOTE: This is very manual/hacky/time consuming)), one good form is 1/2 of a cosine curve(cosine anealing). 

* We use 1/2 cosine annealing because it has a higher learning rate to start out with, and then drops down, and flattens out.  

*  Before SGDR researchers would restart a model 10x in the hope that the learning rate would be better.  

* SGDR finds an optimal learning rate for that session/epcoch and then continues on until it finds a better one

* A useful thing to remember here is that a batch is the number of training examples used in one epoch/iteration.

* A layer is a portion/part of the image that the CNN is attuned to/pays attention to.  The CNN might pay attention to multiple things, so those attributes are saved into different layers.  

* Earlier layers are more general purpose features, and usually don't need much fine tuning/don't need a higher learning rate.  

* Unfreezing is where we get the layer out of a predetermined learning rate and specify our own.  

* We can specify the learning rates for different layers(AKA: Differential learning rates) through using numpy arrays, and by UNFREEZING all the layers:

* Later on we can specify the learning rate for specific layers, but keep in mind we cannot unfreeze specific layers we can only unfreeze from layer N onward/downward to the last layer.  


```
learn.unfreeze()
lr = np.array([1e-4, 1e-3, 1e-2])
learn.fit(lr, 3, cycle_len = 1, cycle_mult = 2) # learning rate(s), cycles/epochs, cycle length for a new learing rate, double the length of the cycle after each cycle
```

* Cycle_mult = 2 is doubling the length of the cycle after each cycle

* A spiky bit on a graph is where the model stops learning effectively. 

* learn.fit(lr, 3, cycle_len = 1, cycle_mult = 2) This line should get you a solid learning rate/model.   

* Cycle multiplier means that it is increasing/doubling the learning rate annealing each after each time/epoch.  

* One of the final tools in our toolbox to get better results is to use Test Time Augmentation(TTA), which makes preductions on images in the validation set as well as making predictions on a number of randomly asugmented versions of them(by default it uses the original image along with 4 randomly augmented versions)

* One idiosyncracy of image recognition is that for simplicity the images have to be square/rectangular dimensions, this is because the GPU slows down if the dimensions are different, so to keep things uniform/quick we use squares/rectangles.

* The above point can be an issue of the model takes a square portion of the image that cuts off recognizable features of an image (say a dog photographed from the side, but the cropped/square part of the image only has the body, which isn't particularly unique)

* The fast.ai library is built on pytorch which simplifies/magicifies away a lot of the complexity that pytorch, keras, or tensorflow has.  

* Steps to create a world class image classifier:

```
1.  Enable data augmentation and precompute = True
2.  Use lr_find() to find the highest learning rate while the loss rate is improving(decreasing)
3.  Train the first layer from precomputer activations for 1-2 epochs
4.  Train the last layer with data augmentation(e.g. precompute = False) for 2-3 epochs with cycle_len = 1
5.  Unfreeze all layers
6.  Se earlier layers w/ a 3x =10x (e.g. 1e-1 to 1e-2 is 10x)lower learning rate than the next higher layer
7.  Use lr_find() again
8.  Train full network with cycle_mult = 2 until over fitting

```

