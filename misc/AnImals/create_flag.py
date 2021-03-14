from predictor import Predict

model_path = 'DogCat.h5'
flag = '7MQ}YD"Ka#Q"k(8;/cC*Vc6IBtS-CTF{EsOr7_f3Vb3CCV_1guV9R_OLUHYb1}xZA[nd1hg7Ii*uBa@&l[3'
images='images'
flag_directory='flag_v2'


if __name__ == '__main__':
    pred = Predict(model_path)
    pred.load_model()

    pred.create_flag_from_model(flag, images, flag_directory)