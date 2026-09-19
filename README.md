# مشروع ASTLS للتحكم الذكي في الإشارات المرورية

هذا المشروع يستخدم محاكي SUMO للتحكم في الإشارات المرورية بشكل ذكي بناءً على عدد السيارات المنتظرة.

## المتطلبات
- تثبيت [SUMO](https://sumo.dlr.de/docs/Downloads.php)
- Python 3.8 أو أحدث

## طريقة التشغيل
1. قم بتعريف متغير البيئة `SUMO_HOME` في نظامك ليشير إلى مجلد تثبيت SUMO.
2. افتح ملف `python_ASTLS_code.py`.
3. شغل الكود باستخدام: `python python_ASTLS_code.py`

## الملفات
- `python_ASTLS_code.py`: الكود الرئيسي.
- `ASTLS.sumocfg`: ملف التكوين.
- `ASTLS.net.xml`: شبكة الطرق.
- `ASTLS.rou.xml`: مسارات المركبات.

  
