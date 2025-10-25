
كيفية استخدام السكريبت:
تحميل السكريبت: تأكد من أن السكريبت موجود في مجلدك الحالي أو قم بتحديد مسار السكريبت بشكل صحيح.

تحميل قوائم الكلمات السرية: تأكد من أن لديك قوائم كلمات السرية للمستخدمين وكلمات المرور. يجب أن تكون هذه القوائم ملفات نصية (username.txt و password.txt).

استخدام السكريبت من السطر الأوامر: استخدم السطر الأوامر لتشغيل السكريبت مع تحديد مسار قوائم الكلمات السرية. مثال على ذلك:

sh
python ELI5-WPS-BF-ar.py -u username.txt -p password.txt
إدخال URL الموقع: بعد تشغيل السكريبت، سيطلب منك إدخال URL موقع ووردبريس الذي تريد قسر كلمة المرور له. مثال على ذلك:

أدخل URL موقع ووردبريس (مثال: https://example.com): https://www.noguchi.org
مثال كامل:
تحميل السكريبت:

sh
git clone https://github.com/sigmakader/ELI5-WPS-BF.git
cd ELI5-WPS-BF
تحميل قوائم الكلمات السرية:

تأكد من أن لديك ملفين نصيين username.txt و password.txt في نفس المجلد.

تشغيل السكريبت:

sh
python ELI5-WPS-BF-ar.py -u username.txt -p password.txt
إدخال URL الموقع:

أدخل URL موقع ووردبريس (مثال: https://example.com): https://www.noguchi.org
