# The rozpoZNAK application - first part

> This is the first part of the application used to recognize road signs using python and java android. 

## Getting Started

 The repository contains two _fake_data.py_ files and the _server_ folder. _fake_data.py_ is designed to convert input images to the gray scale, and rotate them by angles from -11 to 9 degrees. FIle _fake_data_2.py_ resizes all input data to one specified in the size file (e.g 200 x 200 pixels)

### Installing and Using

Python scripts simply download and run in the IDE or console (creating a Python virtual environment). They are helpful when processing large amounts of data in a relatively short time (.jpeg, .png, .jpg, .gif, .txt).

When you run in the console, do it by make virtual environment: 
```
mkvirtualenv fake_data
```
when installation ends go to your virtual environment:
```
workon fake_data
```
and run script by paste: 
```
py fake_data.py
```

## Model training and data processing

The correctness of the obtained model depends to a large extent on the quality of the data provided to it in the teaching process. They must be data uniquely indicating the class in which they are located, properly crafted to fit the network's input assumptions (dimensions, size, number of channels image), and also different enough to teach the network the correct feature or dependence in the class.

Sometimes it is difficult to collect such a large amount of data to correctly identify a feature. There are functions that deform data in Python, which from the original input can generate a lot examples of fake data, which has a characteristic feature so visible that the network can do it catch, but at the same time they are so different from the original that they do not "spoil" the performance of this network, e.g:

```
def resize_data(path1):
    images = [Image.open(file) for file in glob.glob(path1)]
    i = 0
    for pic in images:
        i = i + 1
        image = pic.resize((int(200), int(200)))
        image.save(out_path + name + str(i) + '.jpg')

```

or:

```
for image_path in os.listdir(path):
    input_path = os.path.join(outpath, image_path)
    image_to_gray = ndimage.imread(input_path)

    i = i + 1

    gray = cv2.cvtColor(image_to_gray, cv2.COLOR_BGR2GRAY)
    input_path = os.path.join(outpath, 'gray_' + str(i) + image_path)
    cv2.imwrite(input_path, gray)

```
Based on such transformed data On the basis of such transformed data, you can start to train the network in order to obtain a model by which the application will recognize the class of the road sign in the image. Training the model in the ImageAI library is very simple, because just a few lines of code, the network implemented in this library began to learn and generate models used for character recognition. The code below is used to configure the learning process.

```
from imageai.Prediction.Custom import ModelTraining
    
    model_trainer = ModelTraining()
    model_trainer.setModelTypeAsInceptionV3()
    
    model_trainer.setDataDirectory(
        r"C:\\Users\\makis\Desktop\znaki_drogowe")

    model_trainer.trainModel(num_objects=12,num_experiments=60,
           enhance_data=False, batch_size=4, show_network_summary=False)

```
At the beginning, the necessary module from the ImageAI library is imported. Next, an object is created to which the ModelTraining instance is assigned and the type of network is set. An absolute path is also given to the folder in which the training and test data are located, as well as a folder with the models generated during learning.
At the end, we define the learning parameters in the function model_trainer.trainModel, where we set the number of classes to be recognized by the model, the number of epochs and the size of the data.
