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

> Before you run the above code, you need to know that the learning network needs a lot of computing power. Currently available mid-priced home computers are able to provide such computing power, but only if we transfer the learning process from the default CPU to the GPU. The process of transferring calculations requires a properly compiled TensorFlow library, which is able to use the powerful resources of graphics cards, relieving weaker processors that have a different task in the learning process - they need to properly manage the resources of the GPU. This approach to the learning process provides acceleration of up to 500% relative to the learning process without using a graphics card. This acceleration allows us to achieve satisfactory results earlier, and also saves electricity and equipment that can run shorter.


## Tests


The tests were carried out on a PC with a GTX 970 graphics card, with limited use of VRAM up to 2457MB.

<table style="font-family: arial, sans-serif; border-collapse: collapse; width: 100%; margin: 0 auto;">
  <tr>
  	<th> </th>
    <th>RestNet</th>
    <th>InceptionV3</th>
    <th>DenseNet</th>
  </tr>
  <tr>
    <td>The number of layers</td>
    <td>50</td>
    <td>189</td>
    <td>121</td>
  </tr>
  <tr>
    <td>The average calculation time of one epoch</td>
    <td>541 s</td>
    <td>688 s</td>
    <td>600 s</td>
  </tr>
  <tr>
    <td>The number of parameters</td>
    <td>25 mln</td>
    <td>23 mln</td>
    <td>15,3 mln</td>
  </tr>
  <tr>
  
  </tr>
</table>
