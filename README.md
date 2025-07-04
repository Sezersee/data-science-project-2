# Data Science SQL Project - JOINS 

### Proje Kurulumu
Projeyi öncelikle forklayın ve clone edin.
Proje sayımız ilerledikçe proje yönetimimizi kolaylaştırmak adına projelerimizi belli klasör kalıplarında saklamak işimizi kolaylaştırmak adına iyi bir alışkanlıktır.
Örnek bir Lokasyon: Code2Work/DataScience/data-projects

### Proje Kurulumu Komutlar
Aşağıdaki komutları sıtrayla çalıştırınız.
* python -m venv venv
* venv\Scripts\activate
* pip install -r requirements.txt => Install all dependencies
* python watch.py => Python run all tests

## Bonus
* Eğer daha detaylı bir şekilde testlerin içerisine bakmak isterseniz
* pytest .\tests\test_question.py -s -v 

### Projeye Başlamadan Önce
* Belirtilen sql querylerini yazabilmek için scripts klasörü altındaki bulunan init_db.py dosyası içerisindeki tüm queryleri 
sırasıyla kendi local veritabanınızda çalıştırınız. 
* Veritabanınızın hazır olduğundan emin olmak için tüm tablolara birer SELECT sorgusu atıp sonuçların doğru olduğundan emin olunuz.
* Çalışırken sadece data klasörü altında bulunan questions.py dosyasında çalışacağız. Bunun klasör dışındaki kodları değiştirmeyiniz !
* connect_db fonksiyonu içerisinde veritabanına bağlanma bilgileri var. Projenizi kendi localinizde test ederken burada bilgileri kendi local veritabanı bilgilerinizle değiştirerek test ediniz. Ancak kodunuzu <b>pushlarken bu veritabanı bilgilerini ilk bulduğunuz şekilde bırakınız.</b> Çünkü kodlarınız Cloud bir ortamda bu bilgilerle bir veritabanına bağlancaklardır.

### Hedeflerimiz:

### Görev 1

* question_1_query fonksiyonun içerisinde `Yaşı 22’den büyük öğrencileri listele.` işlemini gerçekleştirecek sql querysini yazınız.
query tüm kolonları dönmelidir.
* question_2_query fonksiyonun içerisinde `Kurs kategorisi 'Veritabanı' olanları getir.` işlemini gerçekleştirecek sql querysini yazınız.
query tüm kolonları dönmelidir.
* question_3_query fonksiyonun içerisinde `İsmi ‘A’ harfi ile başlayan öğrencileri bul.` işlemini gerçekleştirecek sql querysini yazınız.
query tüm kolonları dönmelidir.
* question_4_query fonksiyonun içerisinde `Kurs ismi içinde ‘SQL’ geçenleri listele.` işlemini gerçekleştirecek sql querysini yazınız.
query tüm kolonları dönmelidir.
* question_5_query fonksiyonun içerisinde `Yaşı 22 ile 24 arasında olan öğrencileri getir.` işlemini gerçekleştirecek sql querysini yazınız.
query tüm kolonları dönmelidir.
* question_6_query fonksiyonun içerisinde `Kursa kayıtlı olan öğrencilerin isimlerini listele.` işlemini gerçekleştirecek sql querysini yazınız.
query first_name ve last_name kolonlarını dönmelidir.
* question_7_query fonksiyonun içerisinde `SQL kategorisindeki kurslara kayıtlı öğrenci sayısını bul.` işlemini gerçekleştirecek sql querysini yazınız.
query course_name ve enrollment sayısını dönmelidir. enrollemnt sayısını student_count ismiyle dğitiriniz.
* question_8_query fonksiyonun içerisinde `Her kursun adını ve bu kursu veren öğretmenin adını getir.` işlemini gerçekleştirecek sql querysini yazınız.
query course_name ve instructor name kolonunu instructor_name şeklinde dönmelidir.
* question_9_query fonksiyonun içerisinde `Kayıtlı olmayan öğrencileri listele.` işlemini gerçekleştirecek sql querysini yazınız.
query tüm kolonları dönmelidir.
* question_10_query fonksiyonun içerisinde `Kurslara göre ortalama öğrenci yaşı nedir?` işlemini gerçekleştirecek sql querysini yazınız.
query course_name ve yaşların ortalamasını avg_age ismiyle dönmelidir.
* question_11_query fonksiyonu içerisinde `Öğrenci başına toplam kaç kursa kayıtlı olduklarını listele.` işlemini gerçekleştirecek sql querysini yazınız. 
query first_name, last_name ve toplam kurs sayısını total_courses ismiyle dönmelidir.
* question_12_query fonksiyonu içerisinde `Birden fazla kurs veren öğretmenleri listele.` işlemini gerçekleştirecek sql querysini yazınız.
query instructor_name, ve toplam kurs sayısını total_courses ismiyle dönmelidir.
* question_13_query fonksiyonu içerisinde `Kurslara göre kaç farklı öğrenci kayıtlı?` işlemini gerçekleştirecek sql querysini yazınız.
query course_name ve farklı öğrenci sayısını unique_students ismiyle dönmelidir.
* question_14_query  fonksiyonu içerisinde `Hem ‘SQL Temelleri’ hem de ‘İleri SQL’ kursuna kayıtlı öğrencileri bul.` işlemini gerçekleştirecek sql querysini yazınız. 
query öğrenciye ait first_name ve last_name kolonlarını dönmelidir.
* question_15_query  fonksiyonu içerisinde `Kurs, öğretmen ve öğrenciyi birleştirerek kayıt tarihlerini listele.` işlemini gerçekleştirecek sql querysini yazınız. 
query öğrenciye ait first_name, last_name, course_name, instructor_name ve enrollment_date kolonlarını dönmelidir.
