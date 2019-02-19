from imageai.Prediction.Custom import CustomImagePrediction
import os


def prediction_custom(image):
    pred = ""
    execution_path = os.getcwd()

    prediction = CustomImagePrediction()
    prediction.setModelTypeAsInceptionV3()
    prediction.setModelPath(os.path.join(execution_path, "model_ex-006_acc-0.836483.h5"))
    prediction.setJsonPath(os.path.join(execution_path, "model_class.json"))
    prediction.loadModel(num_objects=12, prediction_speed="fast")

    predictions, probabilities = prediction.predictImage(os.path.join(execution_path, image), result_count=1)
    # print(str(prediction + " " + probabilities))

    for eachPrediction, eachProbability in zip(predictions, probabilities):
        class1 = eachPrediction
        pred = eachProbability

    return class1, pred


#print(str(prediction_custom("stop.jpg")))
