from .base import Const


class Language(Const):
    AB = "ab"
    AA = "aa"
    AF = "af"
    AK = "ak"
    SQ = "sq"
    AM = "am"
    AR = "ar"
    AN = "an"
    HY = "hy"
    AS = "as"
    AV = "av"
    AE = "ae"
    AY = "ay"
    AZ = "az"
    BM = "bm"
    BA = "ba"
    EU = "eu"
    BE = "be"
    BN = "bn"
    BI = "bi"
    BS = "bs"
    BR = "br"
    BG = "bg"
    MY = "my"
    CA = "ca"
    CH = "ch"
    CE = "ce"
    NY = "ny"
    ZH = "zh"
    CU = "cu"
    CV = "cv"
    KW = "kw"
    CO = "co"
    CR = "cr"
    HR = "hr"
    CS = "cs"
    DA = "da"
    DV = "dv"
    NL = "nl"
    DZ = "dz"
    EN = "en"
    EO = "eo"
    ET = "et"
    EE = "ee"
    FO = "fo"
    FJ = "fj"
    FI = "fi"
    FR = "fr"
    FY = "fy"
    FF = "ff"
    GD = "gd"
    GL = "gl"
    LG = "lg"
    KA = "ka"
    DE = "de"
    EL = "el"
    KL = "kl"
    GN = "gn"
    GU = "gu"
    HT = "ht"
    HA = "ha"
    HE = "he"
    HZ = "hz"
    HI = "hi"
    HO = "ho"
    HU = "hu"
    IS = "is"
    IO = "io"
    IG = "ig"
    ID = "id"
    IA = "ia"
    IE = "ie"
    IU = "iu"
    IK = "ik"
    GA = "ga"
    IT = "it"
    JA = "ja"
    JV = "jv"
    KN = "kn"
    KR = "kr"
    KS = "ks"
    KK = "kk"
    KM = "km"
    KI = "ki"
    RW = "rw"
    KY = "ky"
    KV = "kv"
    KG = "kg"
    KO = "ko"
    KJ = "kj"
    KU = "ku"
    LO = "lo"
    LA = "la"
    LV = "lv"
    LI = "li"
    LN = "ln"
    LT = "lt"
    LU = "lu"
    LB = "lb"
    MK = "mk"
    MG = "mg"
    MS = "ms"
    ML = "ml"
    MT = "mt"
    GV = "gv"
    MI = "mi"
    MR = "mr"
    MH = "mh"
    MN = "mn"
    NA = "na"
    NV = "nv"
    ND = "nd"
    NR = "nr"
    NG = "ng"
    NE = "ne"
    NO = "no"
    NB = "nb"
    NN = "nn"
    OC = "oc"
    OJ = "oj"
    OR = "or"
    OM = "om"
    OS = "os"
    PI = "pi"
    PS = "ps"
    FA = "fa"
    PL = "pl"
    PT = "pt"
    PA = "pa"
    QU = "qu"
    RO = "ro"
    RM = "rm"
    RN = "rn"
    RU = "ru"
    SE = "se"
    SM = "sm"
    SG = "sg"
    SA = "sa"
    SC = "sc"
    SR = "sr"
    SN = "sn"
    SD = "sd"
    SI = "si"
    SK = "sk"
    SL = "sl"
    SO = "so"
    ST = "st"
    ES = "es"
    SU = "su"
    SW = "sw"
    SS = "ss"
    SV = "sv"
    TL = "tl"
    TY = "ty"
    TG = "tg"
    TA = "ta"
    TT = "tt"
    TE = "te"
    TH = "th"
    BO = "bo"
    TI = "ti"
    TO = "to"
    TS = "ts"
    TN = "tn"
    TR = "tr"
    TK = "tk"
    TW = "tw"
    UG = "ug"
    UK = "uk"
    UR = "ur"
    UZ = "uz"
    VE = "ve"
    VI = "vi"
    VO = "vo"
    WA = "wa"
    CY = "cy"
    WO = "wo"
    XH = "xh"
    II = "ii"
    YI = "yi"
    YO = "yo"
    ZA = "za"
    ZU = "zu"

    CHOICES = (
        (AB, "Аҧсуа (Apsua)"),
        (AA, "Qafar Af"),
        (AF, "Afrikaans"),
        (AK, "Ákán"),
        (SQ, "Shqip"),
        (AM, "አማርኛ (Amarəñña)"),
        (AR, "اَلْعَرَبِيَّةُ(Al-ʿArabiyyah)"),
        (AN, "Aragonés"),
        (HY, "Հայերեն (Hayeren)"),
        (AS, "অসমীয়া (Ôxômiya)"),
        (AV, "Авар Мацӏ; اوار ماض (Avar Maz)"),
        (AE, "Upastawakaēna"),
        (AY, "Aymara"),
        (AZ, "Azərbaycan Dili; آذربایجان دیلی; Азәрбајҹан Дили"),
        (BM, "بَمَنَنكَن ;ߓߡߊߣߊ߲ߞߊ߲ (Bamanankan)"),
        (BA, "Башҡорт Теле; Başqort Tele"),
        (EU, "Euskara"),
        (BE, "Беларуская Мова (Belaruskaâ Mova)"),
        (BN, "বাংলা (Bāŋlā)"),
        (BI, "Bislama"),
        (BS, "Босански (Bosanski)"),
        (BR, "Brezhoneg"),
        (BG, "Български (Bulgarski)"),
        (MY, "မြန်မာစာ (Mrãmācā)"),
        (CA, "Català; Valencià"),
        (CH, "Finu' Chamoru"),
        (CE, "Нохчийн Мотт;(Noxçiyn Mott)"),
        (NY, "Chichewa; Chinyanja"),
        (ZH, "中文 (Zhōngwén)汉语; 漢語 (Hànyǔ)"),
        (CU, "Славе́Нскїй Ѧ҆Зы́Къ"),
        (CV, "Чӑвашла (Çăvaşla)"),
        (KW, "Kernowek"),
        (CO, "Corsu"),
        (CR, "ᓀᐦᐃᔭᐁᐧᐃᐧᐣ (Nehiyawewin)"),
        (HR, "Hrvatski"),
        (CS, "Čeština"),
        (DA, "Dansk"),
        (DV, "ދިވެހި (Dhivehi)"),
        (NL, "Nederlands"),
        (DZ, "རྫོང་ཁ་ (Dzongkha)"),
        (EN, "English"),
        (EO, "Esperanto"),
        (ET, "Eesti Keel"),
        (EE, "Èʋegbe"),
        (FO, "Føroyskt"),
        (FJ, "Na Vosa Vakaviti"),
        (FI, "Suomi"),
        (FR, "Français"),
        (FY, "Frysk"),
        (FF, "𞤊𞤵𞤤𞤬𞤵𞤤𞤣𞤫 ;ࢻُلْࢻُلْدٜ; Fulfulde𞤨𞤵𞤤𞤢𞥄𞤈 ;ݒُلَارْ; Pulaar"),
        (GD, "Gàidhlig"),
        (GL, "Galego"),
        (LG, "Luganda"),
        (KA, "ქართული (Kharthuli)"),
        (DE, "Deutsch"),
        (EL, "Νέα Ελληνικά; (Néa Ellêniká)"),
        (KL, "Kalaallisut"),
        (GN, "Avañe'Ẽ"),
        (GU, "ગુજરાતી (Gujarātī)"),
        (HT, "Kreyòl Ayisyen"),
        (HA, "هَرْشٜن هَوْس (Halshen Hausa)"),
        (HE, "עברית‎ (Ivrit)"),
        (HZ, "Otjiherero"),
        (HI, "हिन्दी (Hindī)"),
        (HO, "Hiri Motu"),
        (HU, "Magyar Nyelv"),
        (IS, "Íslenska"),
        (IO, "Ido"),
        (IG, "Ásụ̀Sụ́ Ìgbò"),
        (ID, "Bahasa Indonesia"),
        (IA, "Interlingua"),
        (IE, "Interlingue; Occidental"),
        (IU, "ᐃᓄᒃᑎᑐᑦ (Inuktitut)"),
        (IK, "Iñupiaq"),
        (GA, "Gaeilge"),
        (IT, "Italiano"),
        (JA, "日本語 (Nihongo)"),
        (JV, "ꦧꦱꦗꦮ; Basa Jawa"),
        (KN, "ಕನ್ನಡ (Kannađa)"),
        (KR, "كَنُرِيِه; Kànùrí"),
        (KS, "कॉशुर; كأشُر (Kosher)"),
        (KK, "Қазақша; Qazaqşa"),
        (KM, "ខេមរភាសា; (Khémôrôphéasa)"),
        (KI, "Gĩgĩkũyũ"),
        (RW, "Ikinyarwanda"),
        (KY, "Кыргызча; Kırgızça"),
        (KV, "Коми Кыв"),
        (KG, "Kikongo"),
        (KO, "한국어 (Hangugeo)조선말 (Chosŏnmal)"),
        (KJ, "Oshikwanyama"),
        (KU, "کوردی; Kurdî"),
        (LO, "ພາສາລາວ (Phasa Lao)"),
        (LA, "Latinum"),
        (LV, "Latviski"),
        (LI, "Lèmburgs"),
        (LN, "Lingála"),
        (LT, "Lietuviškai"),
        (LU, "Kiluba"),
        (LB, "Lëtzebuergesch"),
        (MK, "Македонски (Makedonski)"),
        (MG, "مَلَغَسِ; Malagasy"),
        (MS, "بهاس ملايو (Bahasa Melayu)"),
        (ML, "മലയാളം (Malayāļã)"),
        (MT, "Malti"),
        (GV, "Gaelg; Gailck"),
        (MI, "Reo Māori"),
        (MR, "मराठी (Marāṭhī)"),
        (MH, "Kajin M̧Ajel‌̧"),
        (MN, "ᠮᠣᠩᠭᠣᠯ ᠬᠡᠯᠡ; Монгол Хэл (Mongol Xel)"),
        (NA, "Dorerin Naoe"),
        (NV, "Diné Bizaad; Naabeehó Bizaad"),
        (ND, "Isindebele; Sasenyakatho; Mthwakazi Ndebele"),
        (NR, "Isindebele; Sakwandzundza"),
        (NG, "Ndonga"),
        (NE, "नेपाली भाषा (Nepālī Bhāśā)"),
        (NO, "Norsk"),
        (NB, "Norsk Bokmål"),
        (NN, "Norsk Nynorsk"),
        (OC, "Occitan; Provençal"),
        (OJ, "ᐊᓂᔑᓈᐯᒧᐎᓐ (Anishinaabemowin)"),
        (OR, "ଓଡ଼ିଆ (Odia)"),
        (OM, "Afaan Oromoo"),
        (OS, "Дигорон Ӕвзаг(Digoron Ævzag)"),
        (PI, "Pāli"),
        (PS, "پښتو (Pax̌Tow)"),
        (FA, "فارسی (Fārsiy)"),
        (PL, "Polski"),
        (PT, "Português"),
        (PA, "ਪੰਜਾਬੀ; پنجابی (Pãjābī)"),
        (QU, "Runa Simi; Kichwa Simi; Nuna Shimi"),
        (RO, "Românește"),
        (RM, "Rumantsch; Rumàntsch; Romauntsch; Romontsch"),
        (RN, "Ikirundi"),
        (RU, "Русский Язык (Russkiĭ Âzyk)"),
        (SE, "Davvisámegiella"),
        (SM, "Gagana Sāmoa"),
        (SG, "Yângâ Tî Sängö"),
        (SA, "संस्कृतम् (Saṃskṛtam)"),
        (SC, "Sardu"),
        (SR, "Српски (Srpski)"),
        (SN, "Chishona"),
        (SD, "سنڌي; सिन्धी (Sindhī)"),
        (SI, "සිංහල (Siṁhala)"),
        (SK, "Slovenčina"),
        (SL, "Slovenščina"),
        (SO, "Soomaali; 𐒈𐒝𐒑𐒛𐒐𐒘; سٝومالِ"),
        (ST, "Sesotho"),
        (ES, "Español; Castellano"),
        (SU, "Basa Sunda; بَاسَا سُوْندَا"),
        (SW, "Kiswahili; كِسوَحِيلِ"),
        (SS, "Siswati"),
        (SV, "Svenska"),
        (TL, "Wikang Tagalog"),
        (TY, "Reo Tahiti"),
        (TG, "Тоҷикӣ (Tojikī)"),
        (TA, "தமிழ் (Tamiḻ)"),
        (TT, "Татар Теле;Tatar Tele; تاتار تئلئ‎"),
        (TE, "తెలుగు (Telugu)"),
        (TH, "ภาษาไทย (Phasa Thai)"),
        (BO, "བོད་སྐད་ (Bodskad);ལྷ་སའི་སྐད་ (Lhas'Iskad)"),
        (TI, "ትግርኛ (Təgrəñña)"),
        (TO, "Lea Faka-Tonga"),
        (TS, "Xitsonga"),
        (TN, "Setswana"),
        (TR, "Türkçe"),
        (TK, "Türkmençe;Түркменче; تۆرکمنچه"),
        (TW, "Twi"),
        (UG, "ئۇيغۇر تىلى;Уйғур Тили; Uyƣur Tili"),
        (UK, "Українська (Ukraїnska)"),
        (UR, "اُردُو (Urduw)"),
        (UZ, "Ózbekça;Ўзбекча; ئوزبېچه"),
        (VE, "Tshivenḓa"),
        (VI, "Tiếng Việt"),
        (VO, "Volapük"),
        (WA, "Walon"),
        (CY, "Cymraeg"),
        (WO, "وࣷلࣷفْ"),
        (XH, "Isixhosa"),
        (II, "ꆈꌠꉙ (Nuosuhxop)"),
        (YI, "ייִדיש (Yidiš)"),
        (YO, "Èdè Yorùbá"),
        (ZA, "話僮 (Vahcuengh)"),
        (ZU, "Isizulu"),
    )
