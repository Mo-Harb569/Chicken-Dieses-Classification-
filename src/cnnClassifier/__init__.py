#عشان اقدر انشئ مجلد جديد اسمه لوغز 
import os
#بحتاجه حتى اتحكم بمخرج الشاشه حتى اطبع السجلات ع التيرمنال 
import sys

import logging



#%(module)s: اسم الملف الي طلع منه هذا السجل 
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
#هون حددت اسم المجلد الي رح تتجمع فيه هاي الملفات 
log_dir = "logs"

log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)
#هون حكيتله انشئ مجلد جديد للوغز واذا كان فيه قبل لا تضرب عادي 


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    #هون المستقبلات 
    #رح السجل يروح لمكانين همه بنفس اللحظه الاول يكتب الرساله ويخزنها بملف للوغ
    #الثاني يطبع نفس الرساله على شاشه التيرمنال قدامك وانتا شغال 
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("cnnClassifierLogger")
#هون عملت الكائن تبعه عشان من هون وطالع عشان بس بدي استدعيه ب اي مكان بعمل هيك  بس 
#from cnnClassifier import logger
#وبتبلش تكتب 
#logger.info("Welcome to our custom log") 
