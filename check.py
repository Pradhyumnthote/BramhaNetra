import tensorflow as tf
import numpy as np
from keras.preprocessing.image import img_to_array, load_img
from keras.applications.inception_resnet_v2 import preprocess_input
from indic_transliteration import sanscript


# Load an image from file and preprocess it
img_path = 'templates/assets/uploads/'

def image_mod(image):
    # read an image 
    image = load_img(img_path+image)
    model = tf.keras.models.load_model('InceptionResNetV2_max.h5')
    resized_image = image.resize((124,  124))
    img_array = img_to_array(resized_image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    labels = ['a', 'aa', 'ba', 'baa', 'bai', 'bam', 'be', 'bee', 'bha', 'bhaa', 'bhai', 'bham', 'bhe', 'bhee', 'bhi', 'bho', 'bhoo', 'bhu', 'bi', 'bo', 'boo', 'bu', 'cha', 'chaa', 'chai', 'cham', 'che', 'chee', 'chha', 'chhaa', 'chhai', 'chham', 'chhe', 'chhee', 'chhi', 'chho', 'chhoo', 'chhu', 'chi', 'cho', 'choo', 'chu', 'da', 'daa', 'dai', 'dam', 'dda', 'ddaa', 'ddai', 'ddam', 'dde', 'ddee', 'ddha', 'ddhaa', 'ddhai', 'ddham', 'ddhe', 'ddhee', 'ddhi', 'ddho', 'ddhoo', 'ddhu', 'ddi', 'ddo', 'ddoo', 'ddu', 'de', 'dee', 'dha', 'dhaa', 'dhai', 'dham', 'dhe', 'dhee', 'dhi', 'dho', 'dhoo', 'dhu', 'di', 'do', 'doo', 'du', 'e', 'ga', 'gaa', 'gai', 'gam', 'ge', 'gee', 'gha', 'ghaa', 'ghai', 'gham', 'ghe', 'ghee', 'ghi', 'gho', 'ghoo', 'ghu', 'gi', 'go', 'goo', 'gu', 'ha', 'haa', 'hai', 'ham', 'he', 'hee', 'hi', 'ho', 'hoo', 'hu', 'i', 'ja', 'jaa', 'jai', 'jam', 'je', 'jee', 'jha', 'jhaa', 'jhai', 'jham', 'jhe', 'jhee', 'jhi', 'jho', 'jhoo', 'jhu', 'ji', 'jo', 'joo', 'ju', 'ka', 'kaa', 'kai', 'kam', 'ke', 'kee', 'kha', 'khaa', 'khai', 'kham', 'khe', 'khee', 'khi', 'kho', 'khoo', 'khu', 'ki', 'ko', 'koo', 'ku', 'la', 'laa', 'lai', 'lam', 'le', 'lee', 'li', 'lo', 'loo', 'lu', 'ma', 'maa', 'mai', 'mam', 'me', 'mee', 'mi', 'mo', 'moo', 'mu', 'na', 'naa', 'nai', 'nam', 'ne', 'nee', 'ni', 'nna', 'nnaa', 'nnai', 'nnam', 'nne', 'nnee', 'nni', 'nno', 'nnoo', 'nnu', 'no', 'noo', 'nu', 'o', 'pa', 'paa', 'pai', 'pam', 'pe', 'pee', 'pha', 'phaa', 'phai', 'pham', 'phe', 'phee', 'phi', 'pho', 'phoo', 'phu', 'pi', 'po', 'poo', 'pu', 'ra', 'raa', 'rai', 'ram', 're', 'ree', 'ri', 'ro', 'roo', 'ru', 'sa', 'saa', 'sai', 'sam', 'se', 'see', 'sha', 'shaa', 'shai', 'sham', 'she', 'shee', 'shha', 'shhaa', 'shhai', 'shham', 'shhe', 'shhee', 'shhi', 'shho', 'shhoo', 'shhu', 'shi', 'sho', 'shoo', 'shu', 'si', 'so', 'soo', 'su', 'ta', 'taa', 'tai', 'tam', 'te', 'tee', 'tha', 'thaa', 'thai', 'tham', 'the', 'thee', 'thi', 'tho', 'thoo', 'thu', 'ti', 'to', 'too', 'tta', 'ttaa', 'ttai', 'ttam', 'tte', 'ttee', 'ttha', 'tthaa', 'tthai', 'ttham', 'tthe', 'tthee', 'tthi', 'ttho', 'tthoo', 'tthu', 'tti', 'tto', 'ttoo', 'ttu', 'tu', 'va', 'vaa', 'vai', 'vam', 've', 'vee', 'vi', 'vo', 'voo', 'vu', 'ya', 'yaa', 'yai', 'yam', 'ye', 'yee', 'yi', 'yo', 'yoo', 'yu']

    predictions = model.predict(img_array)

    name = labels[np.argmax(predictions)]

    from indic_transliteration import sanscript

    # Define a function to convert transliteration to Devanagari script
    def transliteration_to_devanagari(transliteration):
        # Specify the source script as IAST (International Alphabet of Sanskrit Transliteration)
        # and target script as Devanagari
        devanagari = sanscript.transliterate(transliteration, sanscript.ITRANS, sanscript.DEVANAGARI)
        return devanagari

    # Test the function
    transliteration = name
    devanagari = transliteration_to_devanagari(transliteration)
    return devanagari