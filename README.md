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
Sometimes it is difficult to collect such a large amount of data to correctly identify a feature. There are functions that deform data in Python, which from the original input can generate a lot examples of fake data, which has a characteristic feature so visible that the network can do it catch, but at the same time they are so different from the original that they do not "spoil" the performance of this network.

```
def resize_data(path1):
    images = [Image.open(file) for file in glob.glob(path1)]
    i = 0
    for pic in images:
        i = i + 1
        image = pic.resize((int(200), int(200)))
        image.save(out_path + name + str(i) + '.jpg')

```
