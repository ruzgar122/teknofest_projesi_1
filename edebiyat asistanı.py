from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser

r = sr.Recognizer()

#MİKROFONU TANIMLAMA KISMI VE HATA KOMUTLARI ↓↓↓↓↓↓↓↓↓↓

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
        return voice


#BU KISIM SORULARI EKLİÇEMİZ KISIM ↓↓↓↓↓↓↓↓↓↓↓↓

def response(voice):
    
    if "merhaba" in voice:
        speak("Sanada merhaba")
    
    if "günün nasıl geçti" in voice or "bugun nasıl geçti" in voice:
        speak("iyi senin nasıl geçti")
    
    if "s a" in voice or "selamünaleyküm" in voice:
        speak("aleykümselam")
    
    if "teşekkürler" in voice or "teşekkür ederim" in voice:
        speak("rica ederim")
    
    if "eyvallah" in voice or "gardaşım eyvallah" in voice or "helal olsun" in voice:
        speak("eyvallah gardaş")
    
    if "nasılsın" in voice or "iyi misin" in voice:
        speak("iyim Allah'a şükür")
    
    if "seni yapan kim" in voice or "seni kim programladı" in voice:
        selection = ["rüzgar tarafından programlandım: ", "rüzgarla ilyas saulsun yaptı beni: "]
        selection = random.choice(selection)
        speak(selection)

    if "görüşürüz" in voice or "baybay" in voice:
        speak("baybay canım")
        exit()
    
    if "hangi gündeyiz" in voice or "bugün günlerden ney" in voice or "günlerden ney" in voice:
        today = time.strftime("%A")
        if today == "Monday":
                today = "Pazartesi"

        elif today == "Tuesday":
                today = "Salı"

        elif today == "Wednesday":
                today = "Çarşamba"

        elif today == "Thursday":
                today = "Perşembe"

        elif today == "Friday":
                today = "Cuma"

        elif today == "Saturday":
                today = "Cumartesi"

        elif today == "Sunday":
                today = "Pazar"

        speak(today)
        
    if "saat kaç" in voice or "saati söyler misin" in voice or "saate bakar mısın" in voice:
        selection = ["bir dakkika bakıyorum: ", "hemen bakıyorum: ", "bir dakka canım ", "sen iste yeterki"]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

    if "google'da ara" in voice:
        speak("ne aramamı istersin?")
        search = record()
        url = "https://www.google.com.tr/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} için googlede bulabildiklerimi listeliyorum.".format(search))

    if "beni ne kadar seviyorsun" in voice:
        selection = ["bunu bir düşünmem lazım: ", "şuan bunu söyleyecek bir tabir bulamadım: "]
        selection = random.choice(selection)
        speak(selection)

    if "akşam yemek yiyelim mi" in voice:
        speak("tabi seninle yemek yemek hoş olur")

    if "benimle evlenir misin" in voice:
        selection = ["bunu bir düşünmem lazım: ", "kalbimi aşkın kapılarına kapattım: "]
        selection = random.choice(selection)
        
    
    if "en sevdiğim hoca kim" in voice:
        speak("büşra hoca tabiki")
    
    if "tekerleme söyler misin" in voice:
        selection = ["Gagavuz kuşunun gagası gerdandan sarkar, ger ger gerilen gergefin gültası Galata’dan galat gergedana gül atar: ", " Kara kızın kısa kayışını kasışına kızmayışına şaşmamışsın da, kuru kazın kızıp kayısı kazışına şaşmış kalmışsın: ", "Kapıyı kıcır gattırıcılardan mısın, ocağı kıvılcımlattırıcılardan mısın? Ne kapıyı kıcırdattırıcılardanım ne ocağı kıvılcımlattırıcılardanım: "]
        selection = random.choice(selection)
        speak(selection)

    if "benim için şarkı söyler misin" in voice or "beni şaşırt" in voice:
        speak("Ben yoruldum hayat, gelme üstüme Diz çöktüm dünyanın namert yüzüne")

    if "edebiyat nedir" in voice:
        speak("Olay, düşünce, duygu ve hayallerin dil aracılığıyla sözlü veya yazılı olarak biçimlendirilme sanatıdır, Diğer bir tanımla edebiyat dille gerçekleştirilen güzel sanat etkinliğidir,")
    
    if "edebiyat kelime anlamı" in voice:
        speak("Arapça edeb kökünden gelen edebiyat aslında ilm-i edeb’in bütün anlamlarını toplayan çoğul bir kelimedir. Tanzimat’tan sonra Türkçede tekil olarak bugünkü anlamında kullanılmıştır.")
    
    if "edebiyat nelerle ilişkilidir" in voice:
        speak("tarih, din, coğrafya, sosyoloji, psikoloji, felsefe, bilim ve teknik")

    if "edebiyat ile tarih ilişkisi" in voice or "edebiyat tarih ilişkisi" in voice:
        speak("Son derece geniş bir konu alanına sahip olan tarih, edebiyat açısından bulunmaz bir nimet olarak karşımıza çıkmaktadır. Bundan dolayı da edebiyat ile tarih iç içe geçmiş bilimler olup edebiyat tarihi anlayışını da ortaya çıkarmıştır.")

    if "edebiyat din ilişkisi" in voice or "edebiyat ile din ilişkisi" in voice:
        speak("Dinin etkisi her dönemde edebiyatta önemli bir yer tutmuştur. Örneğin Türk edebiyatı İslamiyet öncesi ve İslamiyet sonrası olarak ayrılmasının nedeni de din değişiminden kaynaklanmaktadır. ")

    if "edebiyat coğrafya ilişkisi" in voice or "edebiyat ile coğrafya ilişkisi" in voice:
        speak("Özellikle belli bir olayı anlatan edebi eserlerde mekân (yer) kavramı vardır. Olaylar belli mekânlarda cereyan eder ve o mekânın (coğrafyanın) eserdeki kahramanlar üzerinde yarattığı etkiye yer verilir. Böylece edebiyat, coğrafya biliminden yararlanmış olur")
    
    if "edebiyat sosyoloji ilişkisi" in voice or "edebiyat ile sosyoloji ilişkisi" in voice:
        speak("Edebi eserlerin bir kısmı, topluma öncülük etmek, onu değiştirip geliştirmek amacını taşır, bu yönüyle de edebiyat sosyoloji bilimine katkıda bulunur, kaynaklık eder.")

    if "edebiyat psikoloji ilişkisi" in voice or "edebiyat ile psikoloji ilişkisi" in voice:
        speak("Geniş ruh çözümlemeleri yapar, insanın iç dünyasını, duygu ve hayallerini anlatır. Böylece okurun “insan” denen varlığı çok yönlü olarak tanımasına yardımcı olur. Bireyin iç dünyasını konu alan bu eserler, hem psikolojiden yararlanmış hem de psikoloji bilimine katkı sağlamış olur. ")

    if "edebiyat felsefe ilişkisi" in voice or "edebiyat ile felsefe ilişkisi" in voice:
        speak("edebiyat doğrudan felsefeden, felsefi düşünce sisteminden yararlanmış olur. Kimi edebi eserlerde yer alan fikirler ve bakış açısı felsefede yeni bir düşünce sisteminin oluşmasına katkı sağlar.")

    if "edebiyat bilim ve teknik ilişkisi" in voice or "edebiyat ile bilim ve teknik ilişkisi" in voice:
        speak("Bilimsel gelişmelerin bir kısmı edebiyatı doğrudan etkilemiştir. Örneğin matbaanın icat edilmesi, kitapların çoğaltılmasını kolaylaştırmış ve kitap daha çok insana ulaşmıştır, böylece teknoloji edebiyata katkı sağlamıştır. Edebi eserler de bilimsel çalışmalarda kullanılabilir ve bilim için ilham kaynağı olabilir. Edebi eserler yeni buluşlara ilham verebilir.")

    if "redif nedir" in voice:
        speak("şiirde, genellikle kimi ikilikte ya da dörtlükte uyaktan sonra yer alan, yinelenen sözcük ya da ek.")

    if "roman nedir" in voice:
        speak("Olmuş ya da olabilir nitelikteki olayları ve konuları ele alan edebî türlere Roman denir. Diğer türlerden ayrılan en önemli özelliği, uzunluğudur. Romanlarda, toplumsal olaylar ve ilişkiler gerçeklere uygun bir tarzda ele alınır.")

    if "hikaye nedir" in voice or "öykü nedir" in voice:
        speak("Hikâye ya da öykü, gerçek ya da gerçeğe yakın bir olayı aktaran kısa, düzyazı şeklindeki anlatıdır. Kısa oluşu, yalın bir olay örgüsüne sahip olması, genellikle önemli bir olay ya da sahne aracılığıyla tek ve yoğun bir etki uyandırması ve az sayıda karaktere yer vermesiyle roman ve diğer anlatı türlerinden ayrılır.")

    if "bağlaç nedir" in voice:
        speak("anlamca ilgili tümceleri, kavramları, önermeleri ya da görevdeş sözcükleri birbirine bağlayan sözcük türü.")

    if "edat nedir" in voice or "ilgeç nedir" in voice:
        speak("bellibaşlı bir anlamı olmayan, bir tümcede, önünde yer aldığı sözcükle ardından geldiği sözcükler ya da öteki öğeler arasında anlam ilgisi kuran ve anlamı bunlarla belirginleşen sözcük türü.")

    if "olay nedir" in voice:
        speak("ortaya çıkan, oluşan durum, ilgiyi çeken ya da çekebilecek nitelikte olan hertürlü eylem, hadise, vaka.")

    if "mekan nedir" in voice:
        speak("bir olayın gerçekleştiği yer")

    if "zaman nedir" in voice:
        speak("Zaman herhangi bir dönemi ifade eder. Buna karşın roman ve hikâyede zaman unsuru, belirleyici bir işlev görür. Çünkü zaman, kurgulanış aktarımında önemlidir. Olaylar, zaman unsurundan bağımsız düşünülemez.")

    if "romanda zaman kaça ayrılır" in voice:
        speak("Romanlarda temel olarak şimdiki zaman, gelecek zaman, geniş zaman kullanılır. Ancak bunlar daha karmaşık bir şekilde de kullanılabilir. Olmuş veya gelecekteki bir vakayı, bu üç zamanla aktarabilir yazar.")

    if "lehçe nedir" in voice:
        speak("bir anadilin tarihsel, toplumsal, bölgesel ve kültürel nedenlerle ses, yapı ve sözdizimi yönlerinden oldukça büyük farklılıklar gösteren kolu.")

    if "şive nedir" in voice:
        speak("bir dilin, konuşulduğu sınırlar içinde, bölgelere ve değişik kültür düzeylerine göre söyleyiş özelliği.")

    if "jargon nedir" in voice:
        speak("küçük bir toplulukça kullanılan bozuk dil, argo.")

    if "argo nedir" in voice:
        speak("aynı uğraş alanındaki insanların, kullanılan ortak, genel dilden ayrı olarak, benimseyip kullandıkları, herkesçe anlaşılamayan, kendilerine özgü sözcük ve deyimlerin yer aldığı özel dil ve bu dili oluşturan sözcüklerin tümü.")

    if "kanal nedir" in voice:
        speak("Edebiyatta kanal, iletinin göndericiden alıcıya aktarılması olarak tanımlanır.")

    if "dönüt nedir" in voice:
        speak("letişim sürecinde gönderilen iletinin alıcıya ulaşıp ulaşmadığını alıcıya bildiren ileti/cevaptır. Diğer adıyla geribildirimdir.")

    if "bağlam nedir" in voice:
        speak("Bağlam veya kontekst; kelime ve cümle gibi anlatım unsurlarının, kullanıldıkları yere ve zamana göre, kendinden önce ve sonra gelen unsurlar nedeniyle kazandığı farklı anlam ve değerler bütünü.")

    if "belirti nedir" in voice:
        speak("kendi dışında başka bir şeyi gösteren düşündüren onun yerini alabilen kelime nesne görünüş ve olgulara gösterge denir.")

    if "belirtke nedir" in voice:
        speak("İletişim kurma, bir ileti aktarma, bir bilgi verme amacı içeren göstergelerdir. Gösteren ve gösterilen arasındaki ilişki nedensiz ve uzlaşımsaldır.")

    if "ikon nedir" in voice:
        speak("Dili kullanmadan bilgi ve iletileri aktaran en basit araçlardır. Temelde benzerlik ilişkisi vardır. Örneğin, bir kişinin fotoğrafları, resim, heykel")

    if "simge nedir" in voice:
        speak("Genel anlamda, toplumsal anlaşmaya dayanan, anlamı önceden karalaştırılmış, belirli işaret, sembol.")

    if "durum hikayesi nedir" in voice:
        speak("bir olayı değil günlük yaşamın herhangi bir kesitini ele alıp anlatan öykülerdir")

    if "olay hikayesi nedir" in voice:
        speak("bu tarz öykülere klasik vaka öyküsüde denir bu tür öykülerde oalylar zinciri kişi yer ve zaman öğesine bağlıdır")

    if "betimleme nedir" in voice:
        speak("Betimleme, sözcüklerle resim çizme işidir. Görme, dokunma, işitme, tatma ve koklama duyularımız aracılığıyla varlıkların niteliklerini, bu varlıkların duyularımız üzerinde uyandırdıkları izlenimleri belirtmektir. Betimleme, varlıkların belirgin özelliklerini tanıtıp göz önünde canlandırmaktır.")

    if "soyut isim nedir" in voice:
        speak("Soyut isim, soyut ad veya mana ismi; varlığı düşünce yoluyla kabul edilen, söylendiğinde zihinde belli bir görüntü veya tasavvur uyandırmayan bir kavramdır")

    if "somut isim nedir" in voice:
        speak("Somut isim, duyu organları ile tespit edilebilecek varlıklara verilen isimdir")

    if "tekil isim nedir" in voice:
        speak("Bir varlığın sadece bir tane olduğunu bildiren kelimelere tekil ad denir. Çoğul isimler -ler ya da -lar eki alırken, tekil isimler ek almazlar.")

    if "çoğul isim nedir" in voice:
        speak("Çoğul isim:Yapısında, anlamında birden çok varlığı barındıran, çokluk eki almış isimlerdir. Cins isimlerinin çoğulu yapılır")

    if "sözcük nedir" in voice or "kelime nedir" in voice:
        speak("Cümlenin anlamlı en küçük birimlerine ya da tek başına anlamı olmadığı hâlde cümle içinde anlam kazanan anlatım birimlerine kelime denir.")

    if "sıfat nedir" in voice:
        speak("Sıfat ya da ön ad; isimlerin ya da diğer sıfatların önüne gelerek onları miktar, sıra, konum, renk, biçim, bıraktığı izlenim gibi çeşitli yönlerden tanımlayan, tarif eden kelime türü.")

    if "tamlama nedir" in voice:
        speak("Bir ismin benzerlerinden ayırt edilebilmesi için başka bir isim, zamir veya sıfatla anlam ilişkisi kurarak oluşturduğu söz öbeğine tamlama denir.")

    if "tamlanan nedir" in voice:
        speak("bir tamlamada belirtilen, açıklanan ad; örneğin okulun bahçesi tamlamasında bahçe tamlanandır.")

    if "çekim eki nedir" in voice:
        speak("ad ve eylemlerin kök ya da gövdelerine kişi kavramı vermek için getirilen ek")

    if "nazım birimi nedir" in voice:
        speak("Nazım birimi, nazım şekillerinde ölçü olarak kullanılan parçaya denir. Şiir mısralardan oluşur. Mısraların kuruluşu, kümelenişi nazım birimini meydana getirir.")

    if "divan edebiyatı nedir" in voice:
        speak("Klasik türk Edebiyatı olarak da tanımlanan Divan edebiyatı, Türklerin İslam kültüründen etkilenmeleri sonucu oluşturdukları bir edebiyattır")

    if "serbest ölçü nedir" in voice:
        speak("Serbest ölçü, hece, aruz gibi herhangi bir ölçüye bağlı kalınmayan ölçüdür.")

    if "aruz nedir" in voice:
        speak("Aruz kelime anlamı olarak Arapça bir kelime olup sözlük anlamı çadırın ortasına dikilen direk anlamına gelmektedir. Edebiyat teriminde aruzun anlamı ise mısralarda hecelerin uzunluk ve kısalıkları temeline dayanmış nazım veya şiir ölçüsüdür")

    if "kafiye nedir" in voice or "uyak nedir" in voice:
        speak("Kafiye ya da uyak, şiirde mısra sonlarında bulunan sözcüklerin son heceleri arasındaki ses benzerliğidir.")

    if "lirik şiir nedir" in voice:
        speak("Lirik şiir, duyguların coşkun bir dille anlatıldığı edebiyat eserlerinin genel adıdır.")

    if "eglog nedir" in voice:
        speak("pastoral şiirde çobanın karşılıklı konuşmalarıdır")

    if "idil nedir" in voice:
        speak("ozanın azğında kır güzelliklerinin anlatılmasıdır")

    if "pastoral şiir nedir" in voice:
        speak("Pastoral şiir doğa güzelliklerini anlatan şiirlerdir.")

    if "didaktif şiir nedir" in voice:
        speak("Didaktik (öğretici) şiir, belli bir düşünceyi aşılamak veya belli bir konuda öğüt, bilgi vermek, bir ahlak dersi çıkarmak amacıyla öğretici nitelikte yazılan, duygu yönü az olan şiir türüdür.")

    if "satirik şiir nedir" in voice:
        speak("Satirik şiir eleştirici bir anlatımı olan şiirlerdir.")

    if "dramatik şiir nedir" in voice:
        speak("Dramatik şiir, dram türü konuları içeren bir şiir türüdür. Acıklı ya da korkunç bir olayı konu alır. Konuyu okuyucunun gözünde canlandırabilen, harekete dönüşebilen bir şiir türüdür.")

    if "imge nedir" in voice:
        speak("İmge kelime anlamı olarak hayal demektir. Şiirin özünü oluşturan ve şiiri şiir haline getiren en önemli unsurlardan biri imgedir")

    if "mazmun nedir" in voice:
        speak("Mazmun kelime anlamı olarak anlam, kavram demektir. Edebiyatta, bazı düşüncelerin ifadesinde kullanılan klişileşmiş söz ve anlatımlara denir.")

    if "şiir nedir" in voice:
        speak("Şiir, düz kelime anlamına ek olmak üzere ya da yerine anlamlar oluşturmak için dilin ses estetiği veya ses sembolizmi ve ölçü gibi estetik ve ritmik özelliklerini kullanan bir edebiyat türüdür.")

    if "teşbih nedir" in voice or "benzetme nedir" in voice:
        speak("Teşbih, benzetmek manasına gelir. İfadeyi kuvvetlendirmek için aralarında benzerlik bulunan iki kavramdan zayıf olanın güçlüye benzetilmesidir.")

    if "teşbih i beliğ nedir" in voice:
        speak("Teşbihi beliğ sanatı benzetme sanatı olan teşbih sanatından türemiş ve güzel benzetme olarak açıklanmış bir söz sanatıdır.")

    if "istiare nedir" in voice or "eğretileme nedir" in voice:
        speak("İstiare, Türk Edebiyatında, bir sözcüğü kendi anlamı dışında kullanarak, bir şeyi benzediği başka varlığının adıyla anma sanatı. Diğer adı eğretilemedir.")

    if "teşhis nedir" in voice or "kişileştirme nedir" in voice:
        speak("insana ait özelliklerin insan dışı varlıklara mal etme sanatıdır")

    if "intak nedir" in voice or "konuşturma nedir" in voice:
        speak("İntak bir edebi sanattır. Kişileştirilen bir varlığın konuşturulmasına denir.")

    if "mezazı mürsel nedir" in voice or "ad aktarması nedir" in voice:
        speak("Ad aktarması ya da mecâz-ı mürsel şiirlerde sıkça kullanılan bir söz sanatı türüdür Ad aktarması yapılırken anlatılmak istenilen herhangi bir nesne ya da varlık, doğrudan söylenilmek yerine bir parçası ya da özelliği söylenilerek aktarılır.")

    if "tenasüp nedir" in voice or "uygunluk nedir" in voice:
        speak("Tenasüp, şiirde birbiriyle ilgili, birbirine uygun sözleri birlikte kullanma sanatıdır. Anlamca birbiri ile ilgili kelimeleri bir arada kullanmaktır.")

    if "tezat nedir" in voice or "zıtlık nedir" in voice:
        speak("Edebiyatta tezat, birbirinin zıddı olan duygu, düşünce ve durumları; aralarında bir ilgi kurarak aynı cümlede, mısrada veya beyitte dile getirme sanatıdır.")

    if "telmih nedir" in voice or "anımsatma nedir" in voice:
        speak("Telmih, bir edebi sanat türüdür. Hatırlatma sanatı olarak da geçer.")

    if "hüsnütatil nedir" in voice:
        speak("Hüsn-i ta'lil, nedeni bilinen bir olay, olgu ya da durumun gerçek nedenini bir yana bırakıp; onu hoşa gidecek hayalî bir nedenle açıklama ve anlamlandırma sanatıdır.")

    if "tecahüliarif nedir" in voice:
        speak("Tecahül-i arif, şiir ve nesirde bilinen bir hususun bir nükteye bağlı olarak bilinmiyormuş gibi ifade edilmesidir")   

    if "kinaye nedir" in voice:
        speak("Kinâye veya alegori, bir fikri kapalı, dolaylı olarak anlatan üstü örtülü söz. Edebiyatta bir maksattan dolayı sözü hem hakiki, hem mecazi anlamlara uygun olarak kullanmaktır.")

    if "tevriye nedir" in voice:
        speak("Tevriye, anlamla ilgili edebî sanatlardan biri. Sesteş bir kelimenin bir dizede, beyitte, dörtlükte iki gerçek anlama gelecek biçimde kullanılmasına ve bir sözcüğün yakın anlamını söyleyip uzak anlamını kastetmeye tevriye sanatı denir.")

    if "tariz nedir" in voice:
        speak("Tariz veya Dokundurma, sözün ya da kavramın gerçek ve mecazlı anlamı dışında büsbütün tersini kastetmektir.")

    if "irsalimesel nedir" in voice:
        speak("İrsal-ı mesel, atasözlerini kullanarak yapılan bir söz sanatıdır.")

    if "yunus emre" in voice or "yusuf emre kimdir" in voice:
        speak("Anadolu'da Türkçe şiirin öncüsü olan ünlü tasavvuf ve halk şairidir. Yunus Emre, Anadolu Selçuklu Devleti'nin yavaşça dağılmaya ve Anadolu'nun çeşitli bölgelerinde büyüklü küçüklü Türk beyliklerinin kurulmaya başlandığı 13. yüzyıl ortalarından 14. yüzyılın birinci çeyreğine kadar Orta Anadolu havzasında, Eskişehir'in Sivrihisar ilçesinde yer alan Sarıköy'de yetişmiş ve Ankara'nın Nallıhan ilçesindeki Tapduk Emre'nin dergâhında yaşamıştır.")

    if "yunus emrenin eserleri" in voice or "yunus emrenin şiiri" in voice or "yunus emrenin kitapları" in voice:
        speak("Yunus Emre'nin şiirlerinin yer aldığı iki farklı eser bulunmaktadır. Bunlar; Divan ve Risaletü'n Nushiye'dir. Divan'da Yunus Emre'nin; Fatih, Nuruosmaniye, Yahya Efendi, Karaman, Bursa nüshaları kullanılmıştır. Risaletü'n Nushiye ise mesnevi tarzında yazılmış ve toplam 573 beyitten oluşan öğüt kitabıdır.")

    if "mevlana nedir" in voice or "mevlana kimdir" in voice:
        speak("Muhammed Celâleddîn-i Rumi, veya kısaca bilinen adıyla Mevlânâ, 13. yüzyılda yaşamış Fars Sünni Müslüman şair, fâkih, âlim, ilahiyatçı ve Sûfi mutasavvıftır. Kendisinin etkisi yalnızca bir ulusla veya etnik kimlikle sınırlı kalmayarak pek çok farklı millete ulaşmıştır.")

    if "mevlana eserleri" in voice or "mevlana kitapları" in voice:
        speak("esrlerinin ismi Mektuplar, Mevlana'nın 7 vaazı, Ne varsa İçindedir, mesnevi, Divan-ı Kebir yani Büyük Divan eserleri vardır.")
    
    if "halk hikayesi nedir" in voice:
        speak("Halk hikâyesi veya halk öyküsü, toplumsal iz bırakmış bir olaydan veya bir yazınsal ürünün sözlü kültürde bıraktığı derin etkiden kaynaklanarak ortaya çıkan halk edebiyatı ürünlerine verilen ad.")

    if "koşuk nedir" in voice:
        speak("Türkler islamiyet öncesi belli dönemlerde, sığır töreni adı verilen av törenlerinde, Toy / Şölen adı verilen kurban törenlerinde ziyafetler ve kazanılan savaşlar sonunda, tüm boyların erkekleri bir araya gelerek eğlenirdi. Bu eğlencelerde söylenen çoklukla aşk, doğa ve yiğitlik konularını işleyen ve kopuz adı verilen sazla birlikte söylenen şiirlere koşuk adı verilir.")

    if "fiilimsi nedir" in voice:
        speak("Fiilden (eylemden) türeyen ancak tam olarak eylem bildirmeyen, fiillerin aldıkları zaman kip ve kişi eklerini alamayan yalnızca “-ma, -me” gibi olumsuzluk eklerini alabilen sözcüklere “fiilimsiler ya da eylemsi” denir.")

    if "fiilimsiler kaça ayrılır" in voice:
        speak("Üç tür fiilimsi vardır: İsim-fiil, sıfat-fiil, zarf-fiil.")

    if "isim fiil nedir" in voice:
        speak("İsim-fiil, mastar veya eylemlik, fiillerin cümlede isim görevinde kullanılan hâli. Türkçedeki üç fiilimsi grubundan biridir. Fiil kök veya gövdelerine -me, -mek veya -iş mastar eklerinin getirilmesiyle oluşturulur. Bu eklerde ses uyumlarına göre gerekli değişiklikler yapılır.")

    if "sıfat fiil nedir" in voice:
        speak("Sıfat-fiil, ortaç veya partisip; bir fiilin cümlede sıfat görevinde kullanılan hâli. Türkçedeki üç fiilimsi grubundan biridir. Fiillerin sonuna sıfat-fiil ekleri olan -en, -esi, -mez, -ar, -di, -di, -ecek ve -miş getirilerek oluşturulur ve kısaca anası mezar dikecekmiş şeklinde formülize edilir.")

    if "zarf fiil nedir" in voice:
        speak("Zarf-fiiller, fiil kök ve gövdelerine getirilen eklerle geçici olarak zarf oluşturur ve çekim eki almaz. Çoğunlukla yükleme yöneltilen nasıl veya ne zaman sorularının yanıtıdır.")

    if "gazel nedir" in voice:
        speak("Gazel, Türkçe Divan edebiyatında kullanılan ve en yaygın görülen nazım şeklidir. Arapça edebiyatında ise kasidelerin başında yer alan ve aşktan söz edilen kısımdır. Kaidelere göre daha içten ve etkileyici kabul edilmektedirler.")

    if "kaide nedir" in voice:
        speak("Kaide, kural olarak ifade edilirken aynı zamanda herhangi bir şeyin bir yere dayanan bir bölümünü ya da üzerine oturulan bir nesneyi anlatmaktadır.")

    if "sagu nedir" in voice:
        speak("Sagu, ölen bir kişinin ardından söylenen bir tür ağıt şiiridir. Genelde ölen kişinin erdemlerini ve yiğitliklerini konu alır. Yedili hece ölçüsü ile, nazım şeklinde söylenir. Edebi sanatlara yer verilir. Dörtlük esasına dayanır.")

    if "kutatgu bilig özellikleri nelerdir" in voice:
        speak("Didaktik (öğretici) bir eserdir. Mesnevi şeklinde ve aruz vezniyle 6645 beyit olarak yazılmıştır. Eserde 173 de dörtlük vardır. Eserde, toplum hayatındaki bozuklukları düzeltecek, insanı mutlu edecek yolların neler olduğu belirtilmiş; bunun yolları, devrin hükümdarına öğütler halinde gösterilmiştir.")

    if "atabetül hakayık özellikleri nelerdir" in voice:
        speak("Gerçeklerin eşiği anlamına gelir.Konusu din ve ahlaktır.Didaktik (öğretici) bir eserdir.Mesnevi tarzında yazılmıştır.Nazım birimi olarak beyit ve dörtlük kullanılmıştır.Aruz ölçüsüyle yazılmıştır.Arapça ve Farsça kelimeler vardır.Telmih (hatırlatma) sanatı kullanılmıştır.Eserin Konusu: Eser 14 bölümden oluşur.Baştaki 5 bölüm giriş, şairin adını verdiği 8 bölüm asıl konu, sondaki 1 bölüm de bitiriş bölümüdür.")

    if "divanı lügatit türk ve özellikleri nelerdir" in voice:
        speak("Türkçenin ilk sözlüğü ve dilbilgisi kitabıdır. - 7500 Türkçe kelimenin Arapça karşılığı verilmiştir. - Türk dilini Araplara öğretmek amacıyla ve Arapça olarak yazılmıştır.  Yazar Türkçe kelimelerin karşılıklarını göstermiş ve bunu halk dilinden derlediği örneklerle açıklamıştır.")

    if "divanı hikmet özellikleri nelerdir" in voice:
        speak("Kitapta Allah aşkı Peygamber sevgisi işlenmiştir.Hikmet: Hoş, hayırlı anlamlarına gelir.Sade ve yalın bir dil kullanılmıştır.Aruz ve hece ölçüsü bir arada kullanılmıştır.Dörtlük ve beyitle yazılmıştır.144 hikmet ve 1 münacaattan oluşur. (2009 yılında bulunan yeni hikmetlerle bilinen hikmet sayısı 217 olmuştur. Dr. Hayatı Bice tarafından hazırlanan 5. baskıda yeni hikmetler günümüz Türkçesi ile de yayınlanmıştır.)Eser Karahanlı Türkçesinin Hakaniye lehçesiyle yazılmıştır.İstifham (soru sorma) ve Tecahül-i Arif (bilip de bilmezlikten gelme) sanatları kullanılmıştır.Ahmed Yesevi hikmetlerinin birleşmesiyle olmuştur ve Karahanlı Türkçesiyle söylemiştir.Hikmetler dini tasavvufi şiirlerdir.Peygamber Muhammed'in vefât yaşı olan 63 (Hicrî) yaşından sonra toprağın altında yaşamayı seçmiştir.Allah'a yakın olma isteği vardır.Şiirlerde ulusal ögeler (ölçü, nazım biçimi, yarım uyak) ile İslamlıktan gelme yabancı ögeler (din ve tasavvuf konuları, yabancı sözcükler) bir arada kullanılmıştır.Eserin uyaklanışı abcd dddb eeeb şeklindedir. Dördüncü dizelerin birbiriyle uyaklı oluşu hatta zaman zaman aynen tekrarlanışı bu şiirlerin musiki ile okunmak için söylendiğini gösterir.Divan-ı Hikmet'i Ahmed Yesevi yazmamıştır. Ahmet Yesevi'nin kurduğu tarikattaki Şaban Durmuş, Ahmed Yesevi'nin görüşlerini ve düşüncelerini kitap haline getirmiştir. Eser 12.yüzyıla aittir ve manzum bir eserdir.")

    if "dede kotkut hikayeleri ve özellikleri" in voice:
        speak("Eser, bir önsöz ile 12 hikâyeden oluşur. Olağanüstü olaylarla gerçeğe uygun olaylar eserde iç içedir. Türklerin eski yaşam tarzları ile ilgili ayrıntılar yanında İslam dini ile ilgili özellikler de vardır. Eserde geçen “Dede Korkut” meçhul bir halk ozanıdır.")

    if "kuvayı milliye destanı nedir" in voice:
        speak("Kuvayi Milliye Destanı, Nâzım Hikmet'in Türk Kurtuluş Savaşı'nı bölümler halinde anlattığı destandır. Nâzım Hikmet, Kuvayi Milliye'yi 1939'da yazmaya başlar, 1941'de bitirir. Yapıtın sonunda 939 İstanbul Tevkifhanesi, 940 Çankırı Hapisanesi, 941 Bursa Hapisanesi diye bir not bulunmaktadır.")

    if "kurtuluş savaşı destanı nedir" in voice:
        speak("Kurtuluş Savaşı Destanı ilk basımı 1965'te yapılan Nâzım Hikmet Ran kitabıdır. 1968'de Kuvâyi Milliye adıyla yeniden basılmıştır.")

    if "sakarya meydan savaşı nedir" in voice:
        speak("Yunan Ordusu 7 Eylül'den itibaren sol kanattan kuvvetlerini çekmeye başladı daha sonra 12 -13 Eylül gecesi Sakarya doğusundaki arazi Yunanlılardan geri alındı. Sakarya Savaşı 22 gün 22 gece sürmüş 23 Ağustos 1921 tarihinde başlamış ve 13 Eylül 1921 tarihinde sona ermiştir.")

    if "çanakkale destanı nedir" in voice:
        speak("Çanakkale Destanı, 1915-1916 yılları arasında, Çanakkale Boğazını geçerek İstanbul'u ele geçirmek isteyen İtilaf Devletleri'ne karşı verilmiş bir destandır. Tarihin akışını değiştiren bu savaşta düşman kuvvetleri insanlık suçları da işledi.")

    if "serveti fünun zamanında yazılan romanlar nelerdir" in voice:
        speak("Servet-i Fünûn Dönemi'nde yazılan bazı romanlar: Halit Ziya Uşaklıgil: Aşk-ı Memnu, Mai ve Siyah, Kırık Hayatlar, Nemide. Mehmet Rauf: Eylül, Bir Aşkın Tarihi, Ferdâ-yı Gâram. Hüseyin Cahit Yalçın: Nadide, Hayal İçinde.")

    if "milli edebiyat döneminde roman nedir" in voice:
        speak("1911-1923 yılları arasına denk gelen “Milli Edebiyat Dönemi'nde Roman” sanatçıları, toplumun içinde bulunduğu duruma kayıtsız kalmamış, bu çalkantılı ve sıkıntılı günleri gerçekçi ve halkın anlayabileceği bir dille eserlerinde anlatmaya çalışmışlardır.")

    if "tiyatro nedir" in voice:
        speak("Tiyatro, bir sahnede, seyirciler önünde oyuncuların sergilemesi amacıyla hazırlanmış gösterilerdir. Farklı bir şekilde duyguların ve olayların hareket ve konuşmalarla anlatılmasıdır. Genel olarak temsil edilen eser anlamında da kullanılır. Tiyatro, bir sahne sanatıdır. Tiyatro eseri, olayları oluş yoluyla gösterir.")

    if "eleştiri nedir" in voice:
        speak("Eleştiri, bir kişi, eser ya da konuyu doğru ve yanlışlarını göstererek anlatmak amacıyla yazılan kısa metinlerdir. Sanat, edebiyat, düşünce eserlerini hem öz hem yapı yönünde açıklayan, başarılı ve başarısız ya da değerli ve değersiz yönlerini gösteren, bunları örneklerle somutlayıp belirten yazıdır.")

    if "mehmet rauf kimdir" in voice:
        speak("İstanbul’da doğan sanatçı asker kökenli sanatçılardandır. Askeri okulda okurken edebiyata ilgi duymuştur. Servetifünun romanının en büyük ikinci sanatçısıdır")

    if "ilk psikolojik roman nedir" in voice:
        speak("Eylül romanı, Türk edebiyatında ilk psikolojik roman olarak kabul edilir. Osmanlıca kaleme alınan roman ilk kez 1901 yılında yayımlandı. Sadakatsizlik temasının işlendiği Eylül kitabı toplam 256 sayfadır.")

    if "realist roman nedir" in voice:
        speak("Olayları, insanları ve toplumları gerçekçi açıdan yansıtan romanlardır. Gözlem ve araştırma esastır. Gerçekler, görülenler ve incelemeler önemlidir.")

    if "terim anlam nedir" in voice:
        speak("Bir bilim veya sanat dalıyla ilgili özel bir kavramı ifade eden sözcüklere terim anlamlı sözcükler denir.")

    if "özel anlam nedir" in voice:
        speak("Bazı sözcükler kavramları veya varlıkları toplu olarak içine alır, yani kapsar. Bu sözcüklere genel anlamlı sözcükler denir.")

    if "ikileme nedir" in voice:
        speak("Anlatıma çekicilik kazandırmak, anlamı güçlendirmek amacıyla çeşitli sözcüklerin art arda kullanılmasıyla oluşan söz öbeklerine ikileme denir")

    if "atasözü nedir" in voice:
        speak("Milletlerin yüzyıllar boyunca geçirdikleri denemelerden ve bunlara dayanan düşüncelerden doğmuş olan sözlere atasözü denir. Milletlerin ortak düşünce, yaşayış, inanış ve gelenekleri atasözüne yansır.")

    if "deyim nedir" in voice:
        speak("Kavramları, olayları mecaz yoluyla belirten kalıplaşmış söz gruplarına deyim denir.")

    if "vecize nedir" in voice:
        speak("Ünlü kişilerce söylenmiş özlü sözlere vecize denir.")

    if "koşul cümlesi nedir" in voice or "şart cümlesi nedir" in voice:
        speak("Bir olayın gerçekleşebilmesi için başka bir olayın varlığının gerektiğini bildiren cümlelere şart cümlesi denir. “-se, -sa; -ınca, -ince; -dıkça, -dikçe gibi eklerle; mı, mi edatıyla ve üzere sözcüğüyle yapılır.”")

    if "neden sonuç cümlesi nedir" in voice:
        speak("Eylemin niçin yapıldığını gerekçesini ve sonucunda ne olduğunu bildiren cümlelere neden  sonuçcümlesi denir. için; -dan, -den; diye ile yapılır. Niçin sorusuyla bulunabilir.")

    if "karşılaştırma cümlesi nedir" in voice:
        speak("Birden fazla nesneyi benzer veya farklı yönlerden kıyaslayan cümleye karşılaştırma cümlesi denir. en, daha sözcükleri kullanılır.")

    if "nesnet cümle nedir" in voice or "objektif cümle nedir" in voice:
        speak("Doğruluğu ya da yanlışlığı ispatlanabilen, kişiden kişiye değişmeyen tarafsız yargı bildiren cümlelere nesnel yargılı cümle denir. Gözlem ve deneye dayalı olduğu için herkesçe aynıdır.")

    if "öznel cümle nedir" in voice or "subjektif cümle nedir" in voice:
        speak("Doğruluğu ya da yanlışlığı ispatlanamayan, kişiden kişiye değişen yargı bildiren cümlelere öznel yargılı cümle denir.")

    if "benzetme cümlesi nedir" in voice:
        speak("Bir varlığın başka bir varlığın özellikleriyle anlatıldığı cümlelere benzetme cümlesi denir.")

    if "dolaylı anlatım nedir" in voice:
        speak("Bir kişiye ait sözlerin, yazıların ikinci kişinin ağzından yeniden ifade edilmesini dolaylı anlatım denir.")

    if "paragrafın yapısı kaça ayrılır" in voice:
        speak("paragrafın yapısı üçe ayrılır bunlar giriş bölümü gelişme bölümü ve sonuç bölümüdür") 

    if "paragrafta konu nedir" in voice or "paragrafta içerik nedir" in voice:
        speak("Üzerinde durulan, hakkında yazı yazılan, söz söylenen, her türlü kavramdır. Her yazının bir konusuvardır. Her şey konu olabilir. Yaşam sevinci, köyden kente göç, dil yanlışları, ölüm, yalnızlık, dostluk, vatansevgisi, hasret en çok işlenen konulardır. Bir paragrafın konusu, o paragrafta en genel anlamda üzerinde durulanolay, olgu, durum ve kavramdır.")

    if "paragrafta ana düşünce nedir" in voice or "paragrafta ana fikir nedir" in voice:
        speak("Bir yazının yazılmasına neden olan ve yazının özünü oluşturan düşünce ana düşüncedir. Bunasanatçının okuyucuya vermek istediği mesaj da denebilir. Ana düşünce paragrafta bir cümle halindeverilebileceği gibi parçanın bütününe de serpiştirilebilir. Şiirlerde ana düşünce yerini tema denir.")

    if "paragrafta yardımcı düşünce nedir" in voice:
        speak("Her paragraf bir ana düşünce üzerine kurulur. Bu düşüncenin anlaşılır ve inandırıcı kılınması için deyardımcı düşüncelere ihtiyaç vardır. Yardımcı düşünceler ana düşünceyi örnekler, açıklar ve destekler. Böyleceverilmek istenen mesaj okuyucunun zihninde somutlaştırılmış olur. Bir paragrafta birden fazla yardımcı düşünce vardır. Genellikle gelişme bölümünde bulunur.")

    if "paragrafta başlık nedir" in voice:
        speak("Bir yazının başlığı, o yazıda anlatılan konunun, vurgulanmak istenen ana düşüncenin en kısa, yalın veaçık biçimidir. Bir paragrafın başlığı bulunurken öncelikle o yazının ne anlattığı belirlenmelidir.")

    if "paragrafta tamamlama nedir" in voice:
        speak("Paragraf tamamlama, giriş cümlesini ve sonuç cümlesini bulma ile ilgilidir.")

    if "duyulara seslenme nedir" in voice:
        speak("İnsanın beş duyusu vardır görme, tatma, duyma, dokunma, koklama. Cümlelerde bu beş duyu organından herhangi birisiyle algılanan bir ayrıntıya yer verilebilir.")

    if "duygulara seslenme nedir" in voice:
        speak("Duygu kalben algılanan hislerdir. örneğin sitem, ümit, ümitsizlik, coşku, sevinç, korku, merak, endişe, yalnızlık")

    if "açıklayıcı anlatım nedir" in voice:
        speak("Okuyucuyu herhangi bir konuda eğitmek ve ona bilgi vermek amacıyla başvurulan anlatım tekniğine açıklayıcı anlatım denir. Sade ve sanatsız bir dil kullanılır. Tanımlarla, örneklerle konunun en iyi biçimde anlaşılması sağlanır.")

    if "öyküleyici anlatım nedir" in voice:
        speak("Bir duygunun, düşüncenin bir olay etrafında veya olaya bağlı olarak anlatılmasıyla oluşan anlatımtekniğine öyküleyici anlatım denir. Öykülemede yer, zaman ve kişi gibi unsurlara rastlanır. Genellikle geçmişzaman kullanılır.")

    if "tartışmacı anlatım nedir" in voice:
        speak("Herhangi bir konunun farklı bir bakış açısıyla değerlendirilmesinden kaynaklanan anlatım tekniğinetartışmacı anlatım denir. Amaç karşı tarafın düşüncesini çürütmektir. Düşüncenin kanıtlanması için örneklerverir, tanıklar gösterilir, karşılaştırmalar yapılır. Soru cümleleriyle yazıya akıcılık kazandırılır. Konuşma havasısezilir.")

    if "tanımlama nedir" in voice or "tarif etme nedir" in voice:
        speak("Bir kavrama ait belirleyici özelliklerin anlatılmasıyla oluşan yönteme tanımlama denir. Tanımlamadanedir? sorusunun cevabı bulunur ve tanım cümleleri genellikle -dır, -dir; -tır, -tir ekleriyle veya denir ile biter.")

    if "mukayese etme nedir" in voice:
        speak("Birden fazla düşünce, olay, kavram ya da durumun birbiriyle kıyaslanmasıyla oluşan yönteme karşılaştırma denir.")

    if "tanık gösterme nedir" in voice:
        speak("Yazarın, düşüncelerini inandırıcı kılabilmek için ele aldığı konuda yetkili ve ünlü bir kimseninsözlerinden alıntı yapmasıyla oluşan yönteme tanık gösterme denir. Kişinin sadece adı yetmez. Sözünaktarılmadığı yerde tanık gösterme söz konusu olmaz.")

    if "ulama nedir" in voice:
        speak("Ünsüz harfle bitten sözcükten sonra ünlü ile başlayan bir sözcük geldiği zaman ulama yapılır. Iki sözcük arasında noktalama işareti varsa ulama yapılmaz.") 

    if "vurgu nedir" in voice:
        speak(" Kurallı fiil cümlesinde vurgu yüklemden önceki sözcüktedir. Devrik fiil cümlelerinde vurgu yuklemdedir. ve İsim cümlelerinde vurgu yüklemdedir.")

    if "sertleşme nedir" in voice or "sessiz benzeşmeis nedir" in voice:
        speak("Türkçe sözcüklerde sert sessizden sonra yine sert sessiz gelmelidir.")

    if "sert sessiz yumuşası nedir" in voice:
        speak("Süreksiz sessizlerle bitten bir kelime sesliyle başlayan bir ek aldığında sondaki sert sessizler yumuşar.")

    if "ses türemesi nedir" in voice:
        speak("Tek heceli bazı sözcüklere küçültme eki getirildiğinde sesli türemesi olur.")

    if "geniş ünlü daralması nedir" in voice: 
        speak("Son hecesi geniş seslilerle (a-e) bitten sözcüklere -yor eki getirildiğinde geniş sesliler daralarak ı, i, u, ü olur.")

    if "ses düşmesi nedir" in voice:
        speak("Sonu k ile bitten sözcüklere küçültme eki geldiğinde k ünsüzü düşer.")

    if "kaynaştırma harfi nedir" in voice:
        speak("Türkçe bir sözcükte iki ünlü harf yan yana gelmez. Sesli ile bir sözcükten sonra sesli ile başlayan ek getirildiğinde araya Y, Ş, S, N ünsüzlerinden biri gelir. Bu harflere kaynaştırma harfleri denir.")

    if "küçük ünlü uyumu nedir" in voice:
        speak("Düzlük yuvarlaklık uyumudur. İki kuralı vardır. Sözcüğün ilk hecesindeki ünlü harf düz ise diğer hecedeki ünlüler de düz olmalıdır.")

    if "sayısal verilerden yararlanma nedir" in voice:
        speak("Bir düşünceyi kanıtlayabilmek için anlatılanlarla ilgili istatistiksel bilgileri, anketleri, araştırmaları, sayısal verileri yazı içinde aktarmaktır.")

    if "tanık gösterme nedir" in voice or "alıntılama denir" in voice:
        speak("Yazarın, düşüncelerini inandırıcı kılabilmek için ele aldığı konuda yetkili ve ünlü bir kimsenin sözlerinden alıntı yapmasıyla oluşan yönteme tanık gösterme denir. Kişinin sadece adı yetmez. Sözün aktarılmadığı yerde tanık gösterme söz konusu olmaz.")

    if "örnekleme nedir" in voice:
        speak("Anlatılan konuyla ilgili değişik örneklerin verilmesiyle oluşan yönteme örnekleme denir. Amaç konunun, okuyucunun zihninde daha da belirginleşmesini sağlamaktır.")

    if "tanımlama nedir" in voice or "tarif etme nedir" in voice:
        speak("Bir kavrama ait belirleyici özelliklerin anlatılmasıyla oluşan yönteme tanımlama denir. Tanımlamada nedir sorusunun cevabı bulunur ve tanım cümleleri genellikle -dır, dir, tır, tir ekleriyle veya denir ile biter.")

    if "duyulara seslenme nedir" in voice:
        speak("İnsanın beş duyusu vardır görme, tatma, duyma, dokunma, koklama. Cümlelerde bu beş duyu organından herhangi birisiyle algılanan bir ayrıntıya yer verilebilir.")

    if "ikileme nedir" in voice:
        speak("Anlatıma çekicilik kazandırmak, anlamı güçlendirmek amacıyla çeşitli sözcüklerin art arda kullanılmasıyla oluşan söz öbeklerine ikileme denir.")

    if "ad tamlamaları kaça ayrılır" in voice:
        speak("Takısız ad tamlaması, Belirtisiz ad tamlaması , Belirtili ad tamlaması , Zincirleme ad tamlaması diye dörde ayrılır.")

    if "zincirleme ad tamlaması" in voice:
        speak("En az üç adın (zamir de kullanılabilir) tamlayan ve tamlanan ekleriyle birbirine bağlanmasıyla oluşan söz grubudur.")

    if "ilgi ekleri nelerdir" in voice:
        speak("Ben im , Sen in , O nun , Biz im , Siz in , Onlar ın")

    if "nikolay vasilyeviç gogol kimdir" in voice:
        speak("Realist edebiyatın önde gelen sanatçıları arasında yer alan Gogol, Ukrayna’da doğmuştur. Eserlerinde Puşkinin etkisinde kalan yazar, ilk hikâyelerini Dilanka Yakınlarındaki Çiftlikte Akşam Toplantıları adlı eserde toplamıştır. Halk hikâyeleri geleneğinden, günlük yaşamdan ve sıradan kişilerden etkilenerek oluşturduğu Mirgorod ve Arabeski adlı eserleriyle hızla tanınmaya başlamıştır. Yazarın en önemli eserleri zaman zaman mizahi bir anlatıma da yer verdiği ve döneminin yoksulluğunu, yozlaşmış siyasi yapısını anlatmaya çalıştığı Ölü Canlar ve Taras Bulba adlı romanlarıdır")

    if "mektup türkleri kaça ayrılır" in voice:
        speak("özel mektuplar, edebi mektuplar, resmi mektuplar, iş mektupları diye dörde ayrılır")

    if "özel mektup nedir" in voice:
        speak("Özel mektuplar birbirini çok yakından tanıyan kişilerin, birbirlerine yazdığı mektuplardır. Özel mektuplarda gönderici ile alıcının birbirine karşı özel durumu yanında, ele alınan konu da metnin üslubunu belirler. Özel mektuplar Edebi Nitelik Taşıyan Özel Mektup ve Edebi Nitelik Taşımayan Özel Mektup ikiye ayrılır")

    if "edebi nitelik taşıyan özel mektup nedir" in voice:
        speak("Sanatçı ve edebiyatçıların, daha çok genel konular üzerinde yazdıkları mektuplardır. Belli bir konuya bağlı kalmadan bütün hayatı içine alabilen bir anlatım aracıdır. Gönderenin iç dünyasından veya çevresinden seçilen haberler, çeşitli gözlemler, bir toplumun ve çevrenin özellikleri mektubun konusu olabilir. Mektubu yazan kişi yaşadığı çevreyi ve hayatı da anlatır.")

    if "edebi nitelik taşımayan özel mektup nedir" in voice:
        speak("Birbirini çok yakından tanıyan kişilerin karşılıklı yazdıkları mektuplardır. Bunların belirleyici özelliği kişiden kişiye yazılmış olması, içten ve senli benli bir dille oluşturulmalarıdır.")

    if "edebi mektup nedir" in voice:
        speak("Edebî mektuplar; yazarları, içerikleri ve ifade şekilleri ile özel mektuplar içinde ayrı yer tutar ve ayrı şekilde ele alınırlar. Edebî mektuplarda, mektubun yazıldığı dönemin edebiyat ve düşünce olayları yer alır. Yazar, karşısındakine öğüt verir, yol gösterir.")

    if "resmi mektup nedir" in voice:
        speak("Resmî dairelerin ve tüzel kişilik taşıyan kuruluşların birbirlerine yazdıkları resmî yazılarla; bunların, vatandaşların başvurularına verdikleri yazılı cevaplara denir. İş mektuplarına benzerler.")

    if "iş mektupları nedir" in voice:
        speak("Özel kişilerle iş kurumları ve iş kurumlarının kendi arasında, işle ilgili olarak yazılan mektuplara denir. Bu mektuplarda konusu ne olursa olsun bir iş ya da hizmet söz konusudur. Bu bir sipariş, satış, şikâyet, borç alıp verme isteği, tavsiye ya da bilgi isteme olabilir.")

    if "ahmet hamdi tanpınar kimdir" in voice:
        speak("Ahmet Hamdi Tanpınar Türk şair, romancı, deneme yazarı, edebiyat tarihçisi, siyasetçi ve akademisyendir. Cumhuriyet neslinin ilk öğretmenlerinden olan Ahmet Hamdi Tanpınar; Bursa'da Zaman şiiri ile geniş bir okuyucu kitlesi tarafından tanınmış bir şairdir.")

    if "fuzûlî kimdir" in voice:
        speak("Azerbaycan Türkçesinde eser veren Türk divan şâiridir. Asıl adı Mehmed bin Süleyman'dır. Oğuzlar'ın Bayat boyuna mensuptur. Arapça ve Farsça eserleri de bulunmakla birlikte Azerbaycan Türkçesinin en önemli lirik şairi olarak kabul görmüştür.")

    if "namık kemal kimdir" in voice:
        speak("Namık KemalTürk milliyetçiliğine ilham kaynağı olmuş, Genç Osmanlı hareketi mensubu yazar, gazeteci, devlet adamı ve şairdir. Yurtseverlik, hürriyet, millet kavramlarına bağlı bir Tanzimat Devri aydınıdır.")

    if "basit fiiller nedir" in voice:
        speak("Yapılarına göre fiiller üçe ayrılır. Bir ya da daha fazla yapım eki almış olan fiillere türemiş fiil denir. Birleşik fiiller iki fiilin birleşmesiyle oluşur. Aynı zamanda, etmek  olmak gibi yardımcı eylemlerle oluşturulan fiiller de birleşik fiiller arasında yer alır")

    if "türemiş fiiller nedir" in voice:
        speak("Türemiş kelime veya türemiş sözcük, isim ve fiil köklerine veya diğer türemiş kelimelere yapım ekleri getirilerek türetilen kelime. Yalın hâldeki türemiş kelimeler gövde olarak da bilinir. Türetilen kelime, genellikle türediği kelimeyle ilişkili olmakla birlikte, tamamen yeni bir anlama sahiptir")

    if "birleşik filler nedir" in voice:
        speak("Birleşik fiiller ya da bileşik fiiller, bir eylemi karşılamak üzere birden fazla sözcüğün bir araya gelmesi ile oluşturulmuş fiiller. Bazı birleşik fiiller bir arada, bazıları iki ayrı sözcük halinde yazılır. Birleşik fiiller yapılarına göre üçe ayrılır")

    if "dilekçe nedir" in voice:
        speak("Dilekçe bir dileği bildirmek için resmî makamlara sunulan, imzalı ve adresli, pullu veya pulsuz yazı. Osmanlı İmparatorluğu'nda istida ve arzuhâl adıyla bilinmekte olup memuriyet, maaş, rütbe, vb. istekler için kullanılmıştır. Elkab yazılır; mühür ve imza konulması ise serbesttir.")

    if "tutanak nedir" in voice:
        speak("Belgelenmesi gereken bir durumu tespit edenler tarafından hazırlanıp imzalanan belgeye tutanak veya zabıt denir. Tutanaklar, yalın ve açık bir üslupla, kişisel görüş ve yorumlara yer verilmeden aynen yazılır.")

    if "açık oturum nedir" in voice:
        speak("Açık oturum, bir sözlü anlatım türüdür. Toplumun her kesimini ilgilendirdiği gibi, belli bir konuda da düzenlenebilir. Uzman kişiler bir başkan yönetiminde topluluk karşısında tartışır. Açık oturumlar kalabalık izleyici kitleleri karşısında yapılabileceği gibi radyo veya televizyon ile yayımlanabilir")

    if "günlük nedir" in voice or "günce nedir" in voice:
        speak("Bir kişinin yaşadıklarını, duygu ve izlenimlerini, tarih belirterek günü gününe anlatmasıyla oluşan yazı türüne günlük denir. Günlükler her gün yazıldığı için kısadır. Bu yazılar yazarın yaşamından izler taşır. Eski edebiyattaki adı ruznamedir.")

    if "ilhan berk kimdir" in voice:
        speak("İlhan Berk Kendini şiir ve yazılarına verdi. Manisa Halkevi Dergisi'nde yayınlanan ilk şiirleriyle bu şiirlerden oluşan Güneşi Yakanların Selamında 1935 görülen Nâzım Hikmet etkisi sonraki şiirlerinde kayboldu.")

    if "blog nedir" in voice:
        speak("Blog veya Weblog teknik bilgi gerektirmeden, kendi istedikleri şeyleri, kendi istedikleri şekilde yazan insanların oluşturabildikleri, günlüğe benzeyen web siteleridir. Genellikle güncelden eskiye doğru sıralanmış yazı ve yorumların yayınlandığı, web tabanlı bir yayını belirtir.")






    if "not et" in voice:
        speak ("Dosya ismi ne olsun?")
        txtFile = record() + ".txt"
        speak ("Ne kaydetmek istiyorsun?")
        theText = record()
        f = open(txtFile, "w", encoding="utf-8")
        f.writelines (theText)
        f.close()


def speak(string):
    tts = gTTS(text=string, lang="tr")
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("selam ben edebiyat assistanı")


while True:
    voice = record()
    if voice !='':
        voice = voice.lower()
        print(voice)
        response(voice)


