import os

srcDirPath = os.path.abspath('.')

def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class Members(object):
    @constant
    def CEOS():
        return 2

    @constant
    def EMPLOYEE():
        return 1

    # members
    @constant
    def NOUTOMI():
        return 23

    @constant
    def HAMASAKI():
        return 24

    @constant
    def YASUMOTO():
        return 25

    @constant
    def SAKURAGAWA():
        return 28

    @constant
    def SUGIMOTO():
        return 34

    @constant
    def SHIMADA():
        return 35

    @constant
    def YAMAMOTO():
        return 36

    @constant
    def HAGIWARA():
        return 37

    @constant
    def MIHO():
        return 38
        
    @constant
    def ITO():
        return 41

    @constant
    def HAYASAKI():
        return 83

    @constant
    def NAMBU():
        return 103

    @constant
    def MOURI():
        return 183

    @constant
    def KAI():
        return 243

    @constant
    def FUNAKOSHI():
        return 283

    @constant
    def YOKOTA():
        return 303

    @constant
    def UCHIDA():
        return 343

    @constant
    def HIROSAWA():
        return 383

    @constant
    def LEE():
        return 403

    @constant
    def SHINOHARA():
        return 443

    @constant
    def NAKAMURA():
        return 483

    @constant
    def TAKASE():
        return 503

    @constant
    def YOSHINO():
        return 563

    @constant
    def OKABE():
        return 603

    @constant
    def ARAKAWA():
        return 623

    @constant
    def HAMANO():
        return 663

    @constant
    def JAEYOON():
        return 683

    @constant
    def SHIMAO():
        return 703

    @constant
    def SEIKE():
        return 783

    @constant
    def Y_NAKAMURA():
        return 843

    @constant
    def URATA():
        return 923

    @constant
    def TOKUNAGA():
        return 983

    @constant
    def MASATANI():
        return 1023

    @constant
    def WATANABE():
        return 1063

    @constant
    def KOBARU():
        return 1083

    @constant
    def JUSEUNG():
        return 1163

    @constant
    def KANEKO():
        return 1183

    @constant
    def OKAZAKI():
        return 1223

    @constant
    def SHINKAWA():
        return 1243

    @constant
    def KAWANO():
        return 1283

    @constant
    def JIHO():
        return 1303

    @constant
    def YOSHITAKE():
        return 1323

    @constant
    def TAKEDA():
        return 1383

    @constant
    def SAE():
        return 1403

    @constant
    def LIST():
        return [
            [Members().NOUTOMI,'noutomi','納富'],
            [Members().HAMASAKI,'hamasaki','浜崎'],	
            [Members().YASUMOTO,'yasumoto','安元'],	
            [Members().SAKURAGAWA,'sakuragawa','櫻川'],
            [Members().SUGIMOTO,'sugimoto','杉本'],
            [Members().SHIMADA,'shimada','島田'],
            [Members().YAMAMOTO,'yamamoto','山本'],
            [Members().HAGIWARA,'hagiwara','萩原'],
            [Members().MIHO,'miho','美穂 '],
            [Members().ITO,'ito','伊藤潤樹'],
            [Members().HAYASAKI,'hayasaki','早﨑'],
            [Members().NAMBU,'nambu','南部'],
            [Members().MOURI,'mouri','毛利'],
            [Members().KAI,'kai','甲斐'],
            [Members().FUNAKOSHI,'funakoshi','船越'],
            [Members().YOKOTA,'yokota','横田'],
            [Members().UCHIDA,'uchida','内田'],
            [Members().HIROSAWA,'hirosawa','広沢'],
            [Members().LEE,'lee','イ'],
            [Members().SHINOHARA,'shinohara','篠原'],
            [Members().NAKAMURA,'yu-ki','ゆっきー'],
            [Members().TAKASE,'takase','高瀬'],
            [Members().YOSHINO,'yoshino','吉野'],
            [Members().OKABE,'okabe','岡部'],
            [Members().ARAKAWA,'arakawa','荒川'],
            [Members().HAMANO,'hamano','濱野'],
            [Members().JAEYOON,'jeayoon','ジョン'],
            [Members().SHIMAO,'shimao','嶋生'],
            [Members().SEIKE,'seike','清家'],
            [Members().Y_NAKAMURA,'nakamu','なかむ'],
            [Members().URATA,'urata','浦田'],
            [Members().TOKUNAGA,'tokunaga','徳永'],
            [Members().MASATANI,'masatani','政谷'],
            [Members().WATANABE,'watanabe','渡辺'],
            [Members().KOBARU,'kobaru','小原'],
            [Members().JUSEUNG,'juseung','ジュスン'],
            [Members().KANEKO,'kaneko','金子'],
            [Members().OKAZAKI,'okazaki','岡嵜'],
            [Members().SHINKAWA,'shinkawa','新川'],
            [Members().KAWANO,'kawano','川野'],
            [Members().JIHO,'jiho','ジホ'],
            [Members().YOSHITAKE,'yoshitake','吉武'],
            [Members().TAKEDA,'takeda','竹田'],
            [Members().SAE,'sae','紗慧']
        ]





# 1	'noutomi'
# 2	'hamasaki'
# 3	'yasumoto'
# 5	'sakuragawa'
# 6	'sugimoto'
# 7	'shimada'
# 8	'yamamoto'
# 9	'hagiwara'
# 10	'miho'
# 11	'ito'
# 13	'hayasaki'
# 14	'nambu'
# 15	'mouri'
# 16	'kai'
# 17	'funakoshi'
# 18	'yokota'
# 19	'uchida'
# 20	'hirosawa'
# 21	'lee'
# 22	'shinohara'
# 23	'yu-ki'
# 24	'takase'
# 25	'yoshino'
# 26	'okabe'
# 27	'arakawa'
# 28	'hamano'
# 29	'jeayoon'
# 30	'shimao'
# 31	'seike'
# 32	'nakamu'
# 33	'urata'
# 34	'tokunaga'
# 35	'masatani'
# 36	'watanabe'
# 37	'kobaru'
# 38	'juseung'
# 39	'kaneko'
# 40	'okazaki'
# 41	'shinkawa'
# 42	'kawano'
# 43	'jiho'
# 44	'yoshitake'
# 45	'takeda'
# 46	'sae'