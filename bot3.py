import sys




class telefon:
    def __init__(self, name,marka, yaddas,ram, color, yeni, mekan,qiymet,sim_kart,catdirilma,zemanet,batareya_tutumu):
        self.name = name
        self.marka = marka
        self.yaddas = yaddas
        self.ram = ram
        self.color = color
        self.yeni = yeni
        self.mekan = mekan
        self.qiymet = qiymet
        self.sim_kart = sim_kart
        self.catdirilma = catdirilma
        self.zemanet = zemanet
        self.batareya_tutumu = batareya_tutumu
    
    def get_info(self):
        print(f"Adı: {self.name}")
        print(f"Növü: {self.marka}")
        print(f"Yaddaşı: {self.yaddas}")
        print(f"Ram: {self.ram} ")
        print(f"Color: {self.color} ")
        print(f"Telefon yenidi?: {self.yeni}")
        print(f"Məkan: {self.mekan}")
        print(f"Qiymət: {self.qiymet} Azn")        
        print(f"Sim-kart sayı: {self.sim_kart}")
        print(f"Catdırılma: {self.catdirilma}")        
        print(f"Zəmanət verilir rəsmi: {self.zemanet}")  
        print(f"Batareya tutumu: {self.batareya_tutumu} ")    
    
    def get_sale (self):
        if self.qiymet > 500:
           print(f"Telefonun qiyməti {self.qiymet}AZN.Nəğd alışda endirimli qiyməti: {self.qiymet - 150} AZN")

iphone = telefon("	Apple" , "14 Pro Max" , "512GB" , "6GB" , "Gold" , "2022ci ilindi" , "Baki" ,3500 , "Dual SIM" , " 7/24 Günün istənilən vaxtı çatdırılma" , "1.5 il" , "5000 mAh" )
Samsung = telefon("	Samsung" , "Galaxy A31" , "64GB" , "4GB" , "Black" , "2020ci ilindi" , "Baki" , 700 , "Dual SIM" , " 7/24 Günün istənilən vaxtı çatdırılma" , "1 il","4500 mAh")
Huawei = telefon("	Xiaomi " , " Redmi Note 11 Pro" , "128GB" , "8GB" , "Crystal Blue" , "2021-ci ilindi" , "Baki" , 555 , "Dual SIM" , " 7/24 Günün istənilən vaxtı çatdırılma" , "1 il","4500 mAh")

 # finiş



class  komputer:
    def __init__(self,name,brend  ,ram  , yaddas ,ekran  , color , ceki,seher ,zemanet  ,odənis_növü):
        self.name = name
        self.brend = brend
        self.ram = ram
        self.yaddas = yaddas
        self.ekran = ekran
        self.color = color
        self.ceki = ceki
        self.seher = seher
        self.zemanet = zemanet
        self.odənis_növü = odənis_növü

    def get_info(self):
        print(f"Kompüter  adı: {self.name}")
        print(f"Kompüterin  brendi: {self.brend}")
        print(f"Kompüterin  ramı: {self.ram}")
        print(f"Kompüterin  yaddaşi: {self.yaddas}")
        print(f"Kompüterin  ekran ölçüsü: {self.ekran}")
        print(f"Kompüterin  rəngi: {self.color}")
        print(f"Kompüterin  çəkisi: {self.ceki}")
        print(f"Kompüterin satış məkanaı: {self.seher}")
        print(f"Kompüterin  zəmanəti var?: {self.zemanet}")
        print(f"Ödəniş növü: {self.odənis_növü}")

Noutbuk  = komputer("Noutbuk ","ACER A515-56-50RS " , " 8GB " , "256GB " , "15.6 ", "Pure Silver ", "1.9 Kq ","Bakı","2 il","Nağd və Rəsmi elektron qaimə ilə satış ( Bank köçürməsi ilə ) \n             Köçürmə satış zamanı qiymət ƏDV daxil olaraq hesablanır")
Apple  = komputer("Apple","Macbook Pro 16 " , "32 GB " , "1 TB " , "3072x1080 ", " Boz kosmos ","1.6 кq  ","Xırdalan "," 1il ","Nağd və Rəsmi elektron qaimə ilə satış ( Bank köçürməsi ilə ) \n             Köçürmə satış zamanı qiymət ƏDV daxil olaraq hesablanır" )

 # finiş

 

class komputer_aksesuarlari:
    def __init__(self,name,color,model,isiqlandirma,ceki,qosulma,qiymet,mekan):
        self.name = name
        self.color = color
        self.model = model
        self.isiqlandirma = isiqlandirma
        self.ceki = ceki
        self.qosulma = qosulma
        self.qiymet = qiymet
        self.mekan = mekan

    def get_info(self):
        print(f"Aksesuarın adı: {self.name}")
        print(f"Aksesuarın rəngı: {self.color}")
        print(f"Aksesuarın modeli: {self.model}")
        print(f"Aksesuarın işıqlandırma: {self.isiqlandirma}")
        print(f"Aksesuarın çəki: {self.ceki}")
        print(f"Aksesuarın qoşulma: {self.qosulma}")
        print(f"Aksesuarın qiymət: {self.qiymet} AZN")
        print(f"Aksesuarın satış məkanı: {self.mekan}")
        print("Birkart ilə 6,12,18 aya qədər kredit imkanı var qadasıı .")

Mouse = komputer_aksesuarlari("Razer ","red","Deathadder V2 Pro","RGB","88qr","Wireless","250"," AF Mall ")
Klaviatura = komputer_aksesuarlari("Razer","blue","BlackWidow V3","RGB","1.02 kg","USB","360","AF Mall ")

# finiş



class  meiset_texnikasi :
    def __init__(self,name,brend , color ,qiymet , ceki ,zemanet ,istehsalcı_olke,):
        self.name =  name
        self.brend = brend
        self.color = color
        self.qiymet = qiymet
        self.ceki = ceki
        self.zemanet = zemanet 
        self.istehsalcı_olke = istehsalcı_olke
  
    def get_info(self):
        print(f"Məişət texnikasının adı: {self.name}")
        print(f"Məişət texnikasının brendi: {self.brend}")
        print(f"Məişət texnikasının rəngi: {self.color}")
        print(f"Məişət texnikasının qiyməti: {self.qiymet}")
        print(f"Məişət texnikasının çəkisi: {self.ceki}")
        print(f"Məişət texnikasının zəmanətlidi? : {self.zemanet}")
        print(f"Məişət texnikasının istehsalçı ölkəsi: {self.istehsalcı_olke}")
        print("MÖHTƏŞƏM TƏKLİF!!!")
        print("Bu məhsulu nağd aldıqda Kiçik məişət texnikası HƏDİYYƏ 🎁")

Paltaryuyan  = meiset_texnikasi("Hoffmann"," Bosch" , "Silver gümüşü " ,799, " 68 kq" , "1il ", "Türkiyə ")
Soba  = meiset_texnikasi("Soba ","Bosch" , "Antrasit " , 205  , "30kq", "Zəmanətsiz","Cin")
Soyuducu = meiset_texnikasi("Soyuducu","Samsung","Qara",2399,"101 kq", "2il","Türkiyə")


# finiş
class heyvan:
    def __init__(self, name,color,yas,boy,ceki,cinsi,qiymet,mekan):
        self.name = name
        self.color = color
        self.yas =  yas
        self.boy = boy 
        self.ceki = ceki 
        self.cinsi = cinsi
        self.qiymet = qiymet
        self.mekan = mekan
        
    def get_info(self):
        print(f"Heyvanın adı: {self.name}")
        print(f"Heyvanın rəngi: {self.color}")
        print(f"Heyvanın yaşı: {self.yas}")
        print(f"Heyvanın boyu: {self.boy}")
        print(f"Heyvanın çəkisi: {self.ceki}")
        print(f"Heyvanın cinsi: {self.cinsi}")
        print(f"Heyvanın qiyməti: {self.qiymet} AZN ")
        print("Saglam heyvandi)")
        print("Real alicilara endirim olunacaq.")
    
Alabay = heyvan("Alabay","black","1","80sm","85kq","erkek",400,"Baki")
Britan = heyvan("Britan","white","0.8","75sm","3kq","disi",100,"Xirdalan")
At = heyvan("Qirat","white","5","1.5m","555kq","erkek",600,"Cebrayıl")

# finiş

if sys.argv[1] == "telefona" and sys.argv[2] == "bax":   
    iphone.get_info()
    iphone.get_sale()
    # Samsung.get_info()
    # Samsung.get_sale()
    # Huawei.get_info()
    # Huawei.get_sale()


elif sys.argv[1] == "komputere" and sys.argv[2] == "bax" :
    # Noutbuk.get_info()
    Apple.get_info()


elif sys.argv[1] == "komputer" and sys.argv[2] == "aksesuarlarina" and sys.argv[3] == "bax":
    Mouse.get_info()
    # Klaviatura.get_info()


elif sys.argv[1] == "meiset" and sys.argv[2] == "texnikasina"  and sys.argv[3] == "bax":
    Paltaryuyan .get_info()
    # Soba .get_info()
    # Soyuducu .get_info()


elif sys.argv[1] == "heyvanlara" and sys.argv[2] == "bax":
    Alabay.get_info()

# not)



class elan:
    def __init__(self,marka, model,color,buraxılıs_ili,ban_novu,muherrik,yurus,seher,veziyyeti,oturucu,suretler_qutusu,qiymet):
        self.marka = marka
        self.model = model
        self.color =  color
        self.buraxılıs_ili = buraxılıs_ili 
        self.ban_novu = ban_novu
        self.muherrik = muherrik
        self.yurus = yurus
        self.seher = seher
        self.oturucu = oturucu
        self.veziyyeti = veziyyeti
        self.suretler_qutusu = suretler_qutusu
        self.qiymet = qiymet
    def get_qovluq(self):
        with open (input() , "w") as yaz:        
            yaz.write(f"Marka: {self.marka} \nNovu: {self.color} \nModeli: {self.model} \nBuraxilish ili: {self.buraxılıs_ili} \nBan novu: {self.ban_novu} \nMuherrik: {self.muherrik} \nYurusu: {self.yurus} \nSeher: {self.seher} \nVeziyyeti: {self.veziyyeti} \nSuretler qutusu: {self.suretler_qutusu}  \nQiymeti: {self.qiymet} AZN  ")
    def get_qaqa(self):
        open (input() , "w").close()

Geely = elan("Geely","Coolray","Qirmizi","2023","Offroader / SUV","1.5 L/177 a.g./Benzin","0 km","Baku","On","Vuruğu yoxdur","Avtomat",39900 )
Honda = elan("Honda","CR-V","Gumush","2004","Offroader / SUV"," 2.4 L/162 a.g./Benzin", "135000km","Baku","Tam","Vuruğu yoxdur","Avtomat",15000)




if sys.argv[1] == "elan" and sys.argv[2] == "yarat":
    Geely.get_qovluq()
    # Honda.get_qovluq()

elif sys.argv[1] == "elan" and sys.argv[2] == "sil":
    Honda.get_qaqa()
