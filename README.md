# my-daily-scripts

------- check_systemd_service.py --------

Bu Python scripti, Linux sistemlerde bir servisin aktif olup olmadığını kontrol etmek için systemctl is-active komutunu çalıştırır. Kullanıcıdan servis adı alır ve servisin durumu hakkında bilgi verir.

Özellikler
Belirtilen servisin aktif (active) veya pasif (inactive) olduğunu kontrol eder.

Servis durumu farklı ise durumu kullanıcıya açıklar.

Servis kontrolü sırasında hata oluşursa hata mesajını gösterir.

Komut satırı hatalarını yakalar ve bildirir.


------- dated_log_backup.py ---------

Bu Python scripti, logs klasöründeki .log uzantılı dosyaları alır ve her bir dosyayı tarih damgası ekleyerek backup_logs klasörüne yedekler. Böylece log dosyalarınız düzenli olarak tarih bazlı arşivlenmiş olur.

Özellikler:

logs klasöründeki tüm .log dosyalarını tarar.

Dosya adlarının sonuna güncel tarihi YYYY-MM-DD formatında ekler.

--------- disk_checker.py -------------

Bu Python scripti, sistemdeki disk boş alanını kontrol eder ve loglama sistemiyle raporlar.

Özellikler:

Konsolda INFO ve üstü loglar görüntülenir.

disk.log dosyasına yalnızca ERROR ve üstü loglar yazılır.

Boş disk alanı durumuna göre farklı seviyelerde loglama yapılır:

> 5 GB → INFO

2–5 GB → WARNING

< 2 GB → ERROR

Yedekleri backup_logs adlı klasöre kopyalar.


-------- folder_checker_and_creator.py ---------

Bu Python scripti, kullanıcıdan bir klasör adı girmesini ister ve mevcut dizinde bu klasörün olup olmadığını kontrol eder.

Eğer klasör bulunmazsa, aynı isimle yeni bir klasör oluşturmak isteyip istemediğinizi sorar.

Kullanıcı “e” cevabını verirse, klasörü oluşturur ve işlem başarılı mesajı gösterir.


-------- folder_inspect_tool.py ---------

Bu Python scripti, kullanıcıdan bir klasör yolu alır ve aşağıdaki işlemleri yapar:

Girilen yolun bir klasör olup olmadığını kontrol eder.

Klasörün içeriğini ls komutuyla listeler.

Sistemde şu anda aktif olan kullanıcı adını whoami komutuyla gösterir.

Sistemin tarih ve saat bilgisini date komutuyla yazdırır.

Herhangi bir hata durumunda kullanıcıya hata mesajı verir.


--------- log_details_fetcher.py ---------

Bu Python scripti, kullanıcıdan bir klasör yolu alır ve o klasörde bulunan .log uzantılı dosyaların detaylı listesini (ls -lh komutu ile) gösterir.

Özellikler:

Girilen klasör yolunun var olup olmadığını kontrol eder.

Klasör içindeki .log dosyalarını bulur.

Her .log dosyası için dosya detaylarını (boyut, izinler, tarih vb.) listeler.

Hata durumunda kullanıcıya bilgilendirici mesaj verir.


-------- log_detector_and_backup.py ---------

Bu Python scripti, çalışma dizininde bazı klasörler oluşturur, mevcut dizini başka bir klasör içine kopyalar ve ardından dosya ile klasörleri listeler. Ayrıca .log uzantılı dosyaları ve dosya boyutlarını gösterir.

İşlevler:

Çalışma dizininde yedeklemeklasoru ve hedefklasor adlı klasörler oluşturur.

Mevcut dizini hedef_klasor adında bir alt klasöre kopyalar.

Dizin içindeki dosya ve klasörleri ayrı ayrı listeler.

.log uzantılı dosyaları tespit edip ekrana yazdırır.


-------- log_error_analyzer.py ----------

Bu Python scripti, kullanıcıdan bir klasör yolu alır ve o klasördeki tüm .log dosyalarında "ERROR" kelimesinin kaç kez geçtiğini sayar ve sonucu ekrana yazdırır.

Özellikler:

Girilen klasörün var olup olmadığını kontrol eder.

Klasördeki tüm .log dosyalarını tarar.

Her dosyada "ERROR" kelimesinin kaç kez geçtiğini sayar.

Eğer dosyada "ERROR" kelimesi bulunmazsa bunu belirtir.

İşlem sırasında oluşabilecek hataları kullanıcıya bildirir.


-------- log_file_mover.py ----------

Bu Python scripti, loglar_klasoru adlı klasörde bulunan .log uzantılı dosyaları alır ve hedef_klasor adlı klasöre taşır. Ardından hedef klasördeki dosyaların detaylı listesini ekrana yazdırır.

Özellikler:

Kaynak klasörde .log dosyalarını bulur.

Dosyaları hedef klasöre taşır.

Taşıma işleminden sonra hedef klasördeki dosyaların detaylı listesini (ls -l) gösterir.

Gerekirse kaynak ve hedef klasörleri otomatik oluşturur.

Dosya isimleri ve boyutlarını (KB cinsinden) gösterir.


---------- log_manager.py ----------

"my_logs" klasörünü oluşturur,

İçine 3 tane boş dosya yaratır,

Her dosyanın sonuna güncel tarihi yazar,

Son olarak klasördeki dosyaları listeler.

---------- log_tmp_bak_cleanup.py ------------

Bu Python scripti, kullanıcıdan bir dizin yolu alır ve aşağıdaki işlemleri gerçekleştirir:

Belirtilen dizin yoksa oluşturur.

Dizin içindeki .log, .tmp ve .bak uzantılı dosyaları siler.

Dizin içeriğini yedekler adlı klasöre zip arşivi olarak yedekler.

Dizin disk kullanım durumunu df -h komutuyla ekrana yazdırır.

---------- module_import_scanner.py -----------

Bu Python scripti, bulunduğu dizindeki .py uzantılı dosyaları tarar ve içinde import veya from ile başlayan modül import satırlarını bulur. Böylece projende hangi Python dosyalarının hangi modülleri kullandığını hızlıca görebilirsin.

Özellikler:

Çalışma dizinindeki tüm .py dosyalarını tarar.

Her dosyada import veya from ile başlayan satırları listeler.

Modül içermeyen dosyaları da belirtir.

--------- service_status_logger.py ----------

Bu Python scripti, kullanıcıdan bir servis adı alır, Linux sistemlerde systemctl komutuyla servisin durumunu kontrol eder. Servis çalışmıyorsa;

logs adlı bir klasör oluşturur,

Servisin çalışmadığına dair zaman damgalı bir bilgi dosyası (servis.txt) yazar,

Örnek bir log dosyası (ornek.log) oluşturur,

Ve bu log dosyasını logs/yedek_klasor klasörüne yedekler.

Özellikler:

Servis durumu sorgulama (systemctl status <service>)

Çalışmayan servis için log kaydı oluşturma

Log dosyasını yedekleme

Klasörlerin varlığını kontrol ederek gerekirse oluşturma

Basit hata yönetimi içerir

--------- timestamped_folder_backup.py -----------

Bu Python scripti, belirtilen bir kaynak klasörü zaman damgası ile isimlendirilmiş yedek klasörüne kopyalar. Böylece klasörün tam bir yedeği alınmış olur.

Özellikler:

kaynakklasor adlı klasörü otomatik oluşturur (varsa atlar).

yedekdizini adında bir yedek klasörü oluşturur (varsa atlar).

Her yedekleme için tarih ve saat içeren benzersiz bir yedek klasörü oluşturur.

Kaynak klasörü yedek klasörüne tüm içeriğiyle birlikte kopyalar.

Hata durumunda kullanıcıyı bilgilendirir.

Yedekleme sırasında her dosya için işlem bilgisi konsola yazdırılır.

Gerekirse logs ve backup_logs klasörlerini otomatik oluşturur.

--------- service_restarter.py -----------

Bu Python scripti, sistemde çalışan belirli servislerin durumunu kontrol eder, eğer servis çalışmıyorsa yeniden başlatmayı dener ve tüm işlemleri log dosyasına kaydeder.

--------- disk_usage.py --------------

Bu Python scripti, sistem disk alanını kontrol eder ve loglar üretir.
Disk alanı durumuna göre farklı log seviyeleri kullanılır:

DEBUG → Toplam, kullanılan ve boş disk alanı (GB cinsinden)

INFO → Sistem normalse

WARNING → Boş alan 2 GB’tan az

ERROR → Boş alan 1 GB’tan az

CRITICAL → Sistem kritik seviyede dolu (1 GB’tan az)

Özellikler:

Loglar disk_monitor.log dosyasına yazılır

Her çalıştırmada disk durumu güncellenir

Log formatı: tarih-saat - seviye - mesaj

DEBUG seviyesinde detaylı disk bilgisi kaydedilir


