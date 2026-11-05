import os  
from pathlib import Path
# عشان اتعامل مع مسارات الملفات بطريقه امنه ومتوافقه مع كل انظمة التشغيل 
# إعداد نظام التسجيل (Logging Configuration): 
import logging  

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') 
# هون رح يطبع الوقت ب جانب رسالة الحددث الي عندي 

# هسا بدي احدد اسم المشروع الاساسي  
project_name = "cnnClassifier"
# هذا ال ver الي رح احط بداخله اكواد ال ML + DL 

# هسا بدي ابني ال Architichurer الاساسيه ل اي مشروع MLOPS احترافي  
list_of_files = [
    # GitHub Actions 
    # يستعمل لاحقا لللأتمته CI/CD
    ".github/workflows/.gitkeep",
    
    # هذا انا بعمله عشان احوله رسميا ل بكج عشان اقدر استدعي ملفاته ب سهوله بين بعضها البعض 
    f"src/{project_name}/__init__.py", 
    
    # مجلد المكونات 
    # هذا المجلد رح يجتوي على خطوات بناء الموديل ب شكل منفصل سحب بيانات معالجه تدريب 
    f"src/{project_name}/components/__init__.py",
    
    # مجلد الادوات المساعده 
    # مخصص للاكواد المتكرره الي تستخدم في اماكن متعدده بالمشروع 
    f"src/{project_name}/utils/__init__.py",
    
    # مجلد الاعدادات الخاصه بالمشروع
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    
    # ملفات ال YAML هي عباره عن 
    # نوع من انواع الملفات 
    # يستخدم ل تخزين الاعدادات والمتغيرات الخاصه بالمشروع مثل روابط مسارات ارقام اعداداات 
    
    # مجدل ال Pipeline 
    # لترتيب وتسلسل خطوات تدريب الموديل والتنبو بشكل متتابع 
    f"src/{project_name}/pipeline/__init__.py",
    
    # مجلد الكيانات هسا 
    # يستخدم ل تخزين الكلاسات الي رح اعملها عشان اعبر عن البيانات الي رح استخدمها بالمشروع
    f"src/{project_name}/entity/__init__.py",
    
    # مجلد ال Constants 
    # بخزن هون الشغلات الي مستحيل تتغير بالمشروع 
    f"src/{project_name}/constants/__init__.py",

    # ملفات التكوين الخارجيه والبيانات 
    # يحتوي مسارات البيانات وروابط التحميل  
    "config/config.yaml",
    
    # هون بكون فيه متغيرات التدريب مثل ايبوكس ليرنينغ ريت هاي القصص  
    "params.yaml",
    
    # لإدارة وتتبع خطوات خط أنابيب البيانات باستخدام أداة DVC (Data Version Control).
    "dvc.yaml",
    "requirements.txt",
    "setup.py", 
    "research/trials.ipynb",
    "templet/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    # بفصل المسار ل جزئين 
    # اسم المجلد ثم اسم الملف 
    filedir, filename = os.path.split(filepath) 

    #هون تاكد انه مسار الملف فعلا موجود اذا عمله ع القرص الصلب 
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")

