import os
#هاض عباره عن كلاس ايرور جاهز لما نقرا ملف اليامل ويكون فاضي يعطيني ايرو سهل احله وما ينهار النظام بشكل تام 

from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger

import json
import joblib
#هاي اداه متازه بتثبت الانبوت الي رح يدخل للموديل سترينج مثلا بس سترينج 
from ensure import ensure_annotations
#
# فنكشن بتخليني اعرف اقرا كويس الدكشنري #
#config["artifacts_root"]to config.artifacts_root
from box import ConfigBox

from pathlib import Path


#عشان يساعدني بتعريف انواع المتغيرات 
from typing import Any
#لفك وتشفير لصور ورح تلزمنا باmlops 
import base64
#هسا بدنا نكتب فنكشن قراءة صور يامل  
#وظيفتها تفتح اي ملف بصيغى يامل بتخليني اقراه وبترجع نتيجته بشكل ممتاز وسهل  
@ensure_annotations 
#الفنكشن رح يرجع نوع اسمه configbox  وحكينا عنه 

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml, encoding="utf-8") as yaml_file:
            #بقرا النصوص الي جوا الملف وبحولها لداتا مفهومه لبايثون ب امان
            content = yaml.safe_load(yaml_file)

            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    #يعني اذا الغلط مش موجود برميلك الغلط عشان تعرف شو هو 

#هسا بدي ارجع اعمل دالتين وحده ل انشاء مجلدات ووحده لحفظ النتائج ب ملف جسون 

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        #انشا المجلد ولو كان موجود مسبقا بدون ايرور
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
        #هون رح يسجل العمليه ع طول باللوغر 


# هسا الجسون هون بخزن فيه مثلا نتائج التدريب عشان استعملهم لقدام بال ops  
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        #هون رح يخزن البيانات داخل الملف 
        #وبين كل تخزين والثاني في مسافات 
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


"""  
شو بتعمل؟ بتاخذ أي كائن بايثون (سواء كان موديل ذكاء اصطناعي، أو مصفوفة، أو أوزان شبكة عصبية) وبتحفظه على الهاردسك كملف ثنائي (Binary File) مضغوط وسريع باستخدام مكتبة

"""
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

#هاي الداله شو بتعمل بتحسب حجم اي ملف ع الجهاز وبترجع حجمه بالكيلوبايت  كنص مرتب ومقروء للبشر  
#اهميتها تستخدم لما بدي افحص الووغر لفحص الملفات الي بنزلها من النت او المويلز اذا طلع الحجم 0
#يعني الملف تالف قبل ما اضيع وقت 

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

#هون عندي المستخدم لما برفع صوره من الويب  المتصفح ببعثها للسيرفر ك سلسله نصيه طويلة 

def decodeImage(imgstring, fileName):
    #هذا الكودبحول لنص الطويل لبيانات صور حقيقيه 
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        #هون فتحت الملف بوضع القراءه الثنائية 
        #وبكتب الصوره وبخزنها ع الجهاز كملف صورة طبيعي لتفحصخ شبكة الCNNs 
        
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())



