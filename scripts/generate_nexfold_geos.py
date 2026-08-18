#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HREFLANG = """<link rel="alternate" hreflang="en" href="https://spotspectrum.com/en/nexfold/landing.html">
<link rel="alternate" hreflang="it" href="https://spotspectrum.com/it/nexfold/landing.html">
<link rel="alternate" hreflang="cs" href="https://spotspectrum.com/cz/nexfold/282/landing.html">
<link rel="alternate" hreflang="sl" href="https://spotspectrum.com/si/nexfold/283/landing.html">
<link rel="alternate" hreflang="hu" href="https://spotspectrum.com/hu/nexfold/284/landing.html">
<link rel="alternate" hreflang="sk" href="https://spotspectrum.com/sk/nexfold/285/landing.html">
<link rel="alternate" hreflang="pl" href="https://spotspectrum.com/pl/nexfold/286/landing.html">
<link rel="alternate" hreflang="x-default" href="https://spotspectrum.com/en/nexfold/landing.html">"""

GEOS = {
  "cz": {
    "lang": "cs", "offer": "282", "cpa": "20", "currency": "CZK", "price": "2449",
    "was": "8.163 Kč", "now": "2.449 Kč", "now_plain": "2.449 Kč",
    "phone_ph": "+420 777 123 456", "name_ph": "Jan Novák",
    "addr_ph": "Hlavní 12, 110 00 Praha",
    "reviewers": [
      "Jan N. — Praha, ověřený zákazník",
      "Marie K. — Brno, ověřená zákaznice",
      "Tomáš S. — Ostrava, ověřený zákazník",
    ],
    "t": {
      "title": "NexFold™ — Skládací smartphone se 3 obrazovkami | -70%",
      "desc": "NexFold™: skládací smartphone se 3 obrazovkami, 5G, Dual SIM, fotoaparátem 48 MP a baterií 6800 mAh. Dobírka a doprava zdarma.",
      "og_title": "NexFold™ — Skládací smartphone se 3 obrazovkami | -70%",
      "og_desc": "Tři skládací obrazovky, 5G, Dual SIM, fotoaparát 48 MP a baterie 6800 mAh. Platba na dobírku.",
      "ld_desc": "Skládací smartphone se třemi obrazovkami, 5G, Dual SIM, fotoaparátem 48 MP a baterií 6800 mAh.",
      "submit": "Odesílání...",
      "cookie": "Používáme nezbytné a cookies třetích stran pro lepší zkušenost a analytiku.",
      "cookie_ok": "Přijmout", "cookie_more": "Zjistit více",
      "topbar": "JEN DNES: -70 % + DOPRAVA ZDARMA — PLATBA NA DOBÍRKU",
      "rating": "<strong>4,9/5</strong> — Více než <strong>1 824</strong> spokojených zákazníků",
      "gift": "🚚 Doprava zdarma + 2roční záruka v ceně",
      "h1": "Tři skládací obrazovky, výkon 5G a výdrž na celý den — v jednom smartphonu.",
      "lead": "<strong>NexFold™</strong> spojuje skládací design se 3 obrazovkami, fotoaparát <strong>48 MP</strong>, připojení <strong>5G</strong>, funkce AI a baterii <strong>6800 mAh</strong>. Více prostoru na práci, sledování obsahu a spojení kdekoli.",
      "cta": "ANO, CHCI NEXFOLD™ →",
      "note": "🔒 Žádná záloha · Žádná karta · Platíte až při doručení",
      "f1t": "Doprava zdarma", "f1p": "Rychlé doručení po celé ČR",
      "f2t": "Platba na dobírku", "f2p": "Karta není potřeba",
      "f3t": "Záruka 2 roky", "f3p": "Oficiální krytí v ceně",
      "f4t": "Vrácení do 30 dnů", "f4p": "Jednoduché a bezplatné",
      "cd": "⏰ Cena -70 % platí ještě", "h": "Hod", "m": "Min", "s": "Sek",
      "stock_l": "Dostupnost skladu", "stock_r": "Zbývají jen 4 kusy",
      "live": "<strong>{n} lidí</strong> si právě prohlíží NexFold™",
      "live0": "<strong>38 lidí</strong> si právě prohlíží NexFold™",
      "order_h": "Rezervujte NexFold™ za 2.449 Kč",
      "order_p": "Vyplňte 3 pole. Do 24 hodin vám zavoláme a potvrdíme doručení — předem nic neplatíte.",
      "lab_name": "Jméno a příjmení *", "err_name": "Zadejte jméno a příjmení",
      "lab_phone": "Telefon *", "err_phone": "Zadejte platné telefonní číslo",
      "lab_addr": "Kompletní adresa *", "err_addr": "Zadejte kompletní adresu",
      "confirm": "POTVRDIT OBJEDNÁVKU",
      "b1e": "01 — Multitasking nové generace",
      "b1h": "Tři skládací obrazovky: pracujte, sledujte a komunikujte bez změny zařízení",
      "b1t1": "3 obrazovky", "b1t2": "Skládací design", "b1t3": "Široký displej",
      "b1p": "Z kompaktního telefonu uděláte velké pracovní plátno během vteřiny. Díky <strong>třem skládacím obrazovkám</strong> můžete číst dokumenty, odpovídat na zprávy a sledovat video najednou — bez neustálého přepínání aplikací.",
      "b1i": "Víc prostoru, když ho potřebujete, kompaktní rozměry na cestách.",
      "b2e": "02 — Energie a rychlost bez čekání",
      "b2h": "Baterie 6800 mAh a rychlé nabíjení 66W: zůstaňte produktivní celý den",
      "b2t1": "6800 mAh", "b2t2": "Nabíjení 66W", "b2t3": "Asi 25 min",
      "b2p": "Vysokokapacitní baterie zvládne hodiny práce, streamování i hovorů. Když potřebujete energii, <strong>rychlé nabíjení 66W</strong> zkrátí čekání a NexFold™ se nabije zhruba za 25 minut.",
      "b2i": "Víc výdrže, méně času u zásuvky.",
      "b3e": "03 — Vždy online, se dvěma čísly",
      "b3h": "5G, Dual SIM a fotoaparát 48 MP: vše, co potřebujete, v jednom zařízení",
      "b3t1": "5G", "b3t2": "Dual SIM", "b3t3": "48 MP",
      "b3p": "Oddělte práci a soukromí díky <strong>Dual SIM</strong>, surfujte rychle na 5G a foťte ostře duálním fotoaparátem <strong>48 MP</strong>. NexFold™ je připraven na práci, sítě i cestování.",
      "b3i": "Dvě čísla, rychlé připojení a detailní fotky vždy s sebou.",
      "cmp_l": "Přímé srovnání", "cmp_h": "Klasický smartphone vs NexFold™",
      "cmp_trad": "Klasický",
      "r1": "Formát", "r1a": "Pevný displej", "r1b": "Kompaktní skládací design",
      "r2": "Displej", "r2a": "Jedna obrazovka", "r2b": "3 skládací obrazovky",
      "r3": "Baterie", "r3a": "Rychle se vybije", "r3b": "6800 mAh s vysokou výdrží",
      "r4": "Nabíjení", "r4a": "Pomalé", "r4b": "66W, plné za cca 25 min",
      "r5": "Konektivita", "r5a": "4G / jedna SIM", "r5b": "5G + Dual SIM",
      "r6": "Navíc", "r6a": "Základní funkce", "r6b": "AI + fotoaparát 48 MP",
      "rev_h": "Více než 1 800 spokojených zákazníků. Proto volí NexFold™.",
      "rev1h": "Baterie a tři obrazovky opravdu pomáhají.",
      "rev1p": "«Pracuji celý den a baterie vydrží. Tři obrazovky jsou skutečná výhoda, když potřebuji zvládat víc věcí najednou.»",
      "rev2h": "Pohodlné ovládání, 5G vždy rychlé.",
      "rev2p": "«Je praktický na psaní i práci cestou. 5G je rychlé a skládací formát zabere málo místa.»",
      "rev3h": "Na třech obrazovkách je hraní úžasné.",
      "rev3p": "«Hry jsou na širokém displeji mnohem strhujícíjší. Akci i ovládání vidím jasně a vše běží plynule i při delších sezeních.»",
      "kit_e": "V balení", "kit_h": "Kompletní sada NexFold™, připravená k použití",
      "k1": "1× skládací smartphone NexFold™ se 3 obrazovkami",
      "k2": "1× rychlá nabíječka 66W", "k3": "1× kabel USB-C",
      "k4": "Baterie 6800 mAh s vysokou výdrží", "k5": "Ochranné pouzdro jako dárek",
      "k6": "Stručný návod k použití", "k7": "Oficiální záruka 2 roky",
      "faq_h": "Často kladené otázky",
      "q1": "Jak dlouho trvá doručení?", "a1": "Doručení obvykle trvá 1–2 pracovní dny. Do 24 hodin vám zavoláme a potvrdíme objednávku i čas doručení.",
      "q2": "Musím platit předem?", "a2": "Ne. Kurýrovi zaplatíte 2.449 Kč, až NexFold™ dorazí k vám domů.",
      "q3": "Podporuje NexFold™ 5G a Dual SIM?", "a3": "Ano. Podporuje připojení 5G a dvě SIM karty pro oddělení práce a soukromí.",
      "q4": "Jak dlouho trvá nabíjení?", "a4": "S přiloženou rychlou nabíječkou 66W trvá plné nabití asi 25 minut.",
      "q5": "Co když nebudu spokojený?", "a5": "Máte 30 dní od doručení na vrácení a 2roční záruku na výrobní vady.",
      "q6": "Jak objednám?", "a6": "Vyplňte formulář se jménem, telefonem a adresou. Zavoláme vám kvůli potvrzení a platíte až při doručení.",
      "foot_b": "Užitečné produkty pro každodenní život, doručení do 24–48 hodin na dobírku.",
      "foot_h": "Informace", "about": "O nás", "contact": "Kontaktujte nás",
      "privacy": "Zásady ochrany osobních údajů", "terms": "Obchodní podmínky",
      "cookie_l": "Zásady cookies", "ship": "Doprava", "refund": "Vrácení zboží",
      "contact_h": "Kontakt", "rights": "Všechna práva vyhrazena",
      "ty_title": "Objednávka přijata | NexFold™",
      "ty_h": "Vaše objednávka NexFold™ byla zaregistrována!",
      "ty_p": "Zbývá jen poslední krok, než objednávku dokončíme a odešleme.",
      "ty_n": "📞 Zvedněte potvrzovací hovor",
      "ty_b": "Operátor vás v následujících hodinách kontaktuje a ověří údaje. Pokud hovor nezvednete, objednávku nelze odeslat.",
      "ty_h2": "Pondělí–sobota · 9:00–18:00",
      "ty_b1": "🔒 Platba na dobírku", "ty_b2": "🛡️ Záruka 2 roky", "ty_b3": "🚚 Doručení 24–48 h",
      "ty_back": "Zpět na web",
    },
  },
  "si": {
    "lang": "sl", "offer": "283", "cpa": "19", "currency": "EUR", "price": "99.99",
    "was": "333,30 €", "now": "99,99 €", "now_plain": "99,99 €",
    "phone_ph": "+386 41 123 456", "name_ph": "Janez Novak",
    "addr_ph": "Slovenska cesta 12, 1000 Ljubljana",
    "reviewers": [
      "Janez N. — Ljubljana, preverjeni kupec",
      "Marija K. — Maribor, preverjena stranka",
      "Luka S. — Celje, preverjeni kupec",
    ],
    "t": {
      "title": "NexFold™ — Zložljiv pametni telefon s 3 zasloni | -70%",
      "desc": "NexFold™: zložljiv pametni telefon s 3 zasloni, 5G, Dual SIM, 48 MP kamero in baterijo 6800 mAh. Plačilo po povzetju in brezplačna dostava.",
      "og_title": "NexFold™ — Zložljiv pametni telefon s 3 zasloni | -70%",
      "og_desc": "Trije zložljivi zasloni, 5G, Dual SIM, 48 MP kamera in baterija 6800 mAh. Plačilo po povzetju.",
      "ld_desc": "Zložljiv pametni telefon s tremi zasloni, 5G, Dual SIM, 48 MP kamero in baterijo 6800 mAh.",
      "submit": "Pošiljanje...",
      "cookie": "Uporabljamo nujne in piškotke tretjih oseb za boljšo izkušnjo in analitiko.",
      "cookie_ok": "Sprejmem", "cookie_more": "Več informacij",
      "topbar": "SAMO DANES: -70 % + BREZPLAČNA DOSTAVA — PLAČILO PO POVZETJU",
      "rating": "<strong>4,9/5</strong> — Več kot <strong>1.824</strong> zadovoljnih strank",
      "gift": "🚚 Brezplačna dostava + 2-letna garancija vključena",
      "h1": "Trije zložljivi zasloni, zmogljivost 5G in energija za ves dan — v enem telefonu.",
      "lead": "<strong>NexFold™</strong> združuje zložljivo zasnovo s 3 zasloni, kamero <strong>48 MP</strong>, povezavo <strong>5G</strong>, funkcije AI in baterijo <strong>6800 mAh</strong>. Več prostora za delo, gledanje in povezavo kjerkoli.",
      "cta": "DA, ŽELIM NEXFOLD™ →",
      "note": "🔒 Brez predplačila · Brez kartice · Plačate šele ob dostavi",
      "f1t": "Brezplačna dostava", "f1p": "Hitra dostava po vsej Sloveniji",
      "f2t": "Plačilo po povzetju", "f2p": "Kartica ni potrebna",
      "f3t": "2 leti garancije", "f3p": "Uradno kritje vključeno",
      "f4t": "Vračilo v 30 dneh", "f4p": "Enostavno in brezplačno",
      "cd": "⏰ Cena -70 % velja še", "h": "Ur", "m": "Min", "s": "Sek",
      "stock_l": "Zaloga", "stock_r": "Ostali so samo 4 kosi",
      "live": "<strong>{n} oseb</strong> si trenutno ogleduje NexFold™",
      "live0": "<strong>38 oseb</strong> si trenutno ogleduje NexFold™",
      "order_h": "Rezervirajte NexFold™ za 99,99 €",
      "order_p": "Izpolnite 3 polja. V 24 urah vas pokličemo in potrdimo dostavo — vnaprej ne plačate ničesar.",
      "lab_name": "Ime in priimek *", "err_name": "Vnesite ime in priimek",
      "lab_phone": "Telefon *", "err_phone": "Vnesite veljavno telefonsko številko",
      "lab_addr": "Celoten naslov *", "err_addr": "Vnesite celoten naslov",
      "confirm": "POTRDI NAROČILO",
      "b1e": "01 — Večopravilnost nove generacije",
      "b1h": "Trije zložljivi zasloni: delajte, glejte in komunicirajte brez menjave naprave",
      "b1t1": "3 zasloni", "b1t2": "Zložljiva zasnova", "b1t3": "Širok zaslon",
      "b1p": "Iz kompaktnega telefona v sekundi naredite veliko delovno površino. S <strong>tremi zložljivimi zasloni</strong> berete dokumente, odgovarjate na sporočila in gledate video hkrati — brez nenehnega preklapljanja aplikacij.",
      "b1i": "Več prostora, ko ga potrebujete, kompaktne mere na poti.",
      "b2e": "02 — Energija in hitrost brez čakanja",
      "b2h": "Baterija 6800 mAh in hitro polnjenje 66W: ostanite produktivni ves dan",
      "b2t1": "6800 mAh", "b2t2": "Polnjenje 66W", "b2t3": "Približno 25 min",
      "b2p": "Zmogljiva baterija zdrži ure dela, pretakanja in klicev. Ko potrebujete energijo, <strong>hitro polnjenje 66W</strong> skrajša čakanje in NexFold™ napolni v približno 25 minutah.",
      "b2i": "Več avtonomije, manj časa ob vtičnici.",
      "b3e": "03 — Vedno povezani, z dvema številkama",
      "b3h": "5G, Dual SIM in kamera 48 MP: vse, kar potrebujete, v eni napravi",
      "b3t1": "5G", "b3t2": "Dual SIM", "b3t3": "48 MP",
      "b3p": "Ločite delo in zasebno življenje z <strong>Dual SIM</strong>, brskajte hitro po 5G in fotografirajte ostro z dvojno kamero <strong>48 MP</strong>. NexFold™ je pripravljen na delo, družabna omrežja in potovanja.",
      "b3i": "Dve številki, hitra povezava in podrobne slike vedno s seboj.",
      "cmp_l": "Neposredna primerjava", "cmp_h": "Klasični pametni telefon vs NexFold™",
      "cmp_trad": "Klasični",
      "r1": "Oblika", "r1a": "Fiksni zaslon", "r1b": "Kompaktna zložljiva zasnova",
      "r2": "Zaslon", "r2a": "En zaslon", "r2b": "3 zložljivi zasloni",
      "r3": "Baterija", "r3a": "Hitro se izprazni", "r3b": "6800 mAh z dolgo avtonomijo",
      "r4": "Polnjenje", "r4a": "Počasno", "r4b": "66W, polno v cca 25 min",
      "r5": "Povezljivost", "r5a": "4G / ena SIM", "r5b": "5G + Dual SIM",
      "r6": "Dodatno", "r6a": "Osnovne funkcije", "r6b": "AI + kamera 48 MP",
      "rev_h": "Več kot 1.800 zadovoljnih strank. Zato izberejo NexFold™.",
      "rev1h": "Baterija in trije zasloni res pomagajo.",
      "rev1p": "«Delam ves dan in baterija zdrži. Trije zasloni so prava prednost, ko moram upravljati več nalog.»",
      "rev2h": "Udobna uporaba, 5G vedno hiter.",
      "rev2p": "«Praktičen je za pisanje in delo na poti. 5G je hiter, zložljiva oblika pa zavzame malo prostora.»",
      "rev3h": "Na treh zaslonih je igranje neverjetno.",
      "rev3p": "«Igre so na širokem zaslonu veliko bolj privlačne. Akcijo in ukaze vidim jasno, vse pa teče tekoče tudi pri daljših sejah.»",
      "kit_e": "V paketu", "kit_h": "Kompletni komplet NexFold™, pripravljen za uporabo",
      "k1": "1× zložljivi pametni telefon NexFold™ s 3 zasloni",
      "k2": "1× hitri polnilec 66W", "k3": "1× kabel USB-C",
      "k4": "Baterija 6800 mAh z visoko avtonomijo", "k5": "Zaščitna torbica darilo",
      "k6": "Kratek priročnik za uporabo", "k7": "Uradna 2-letna garancija",
      "faq_h": "Pogosta vprašanja",
      "q1": "Kako dolgo traja dostava?", "a1": "Dostava običajno traja 1–2 delovna dneva. V 24 urah vas pokličemo in potrdimo naročilo ter čas dostave.",
      "q2": "Ali moram plačati vnaprej?", "a2": "Ne. Kurirju plačate 99,99 €, ko NexFold™ prispe na vaš dom.",
      "q3": "Ali NexFold™ podpira 5G in Dual SIM?", "a3": "Da. Podpira povezavo 5G in dve kartici SIM za ločitev službe in zasebnosti.",
      "q4": "Kako dolgo traja polnjenje?", "a4": "S priloženim hitrim polnilcem 66W traja polno polnjenje približno 25 minut.",
      "q5": "Kaj, če nisem zadovoljen?", "a5": "Imate 30 dni od dostave za vračilo in 2-letno garancijo za tovarniške napake.",
      "q6": "Kako naročim?", "a6": "Izpolnite obrazec z imenom, telefonom in naslovom. Pokličemo vas za potrditev in plačate šele ob dostavi.",
      "foot_b": "Uporabni vsakodnevni izdelki, dostava v 24–48 urah s plačilom po povzetju.",
      "foot_h": "Informacije", "about": "O nas", "contact": "Kontaktirajte nas",
      "privacy": "Pravilnik o zasebnosti", "terms": "Pogoji uporabe",
      "cookie_l": "Pravilnik o piškotkih", "ship": "Pravilnik o dostavi", "refund": "Pravilnik o vračilih",
      "contact_h": "Kontakt", "rights": "Vse pravice pridržane",
      "ty_title": "Naročilo prejeto | NexFold™",
      "ty_h": "Vaše naročilo NexFold™ je bilo zabeleženo!",
      "ty_p": "Ostaja še zadnji korak, preden naročilo zaključimo in odpošljemo.",
      "ty_n": "📞 Sprejmite potrditveni klic",
      "ty_b": "Operater vas bo v naslednjih urah kontaktiral in potrdil podatke. Če klica ne sprejmete, naročila ni mogoče odposlati.",
      "ty_h2": "Ponedeljek–sobota · 9:00–18:00",
      "ty_b1": "🔒 Plačilo po povzetju", "ty_b2": "🛡️ 2 leti garancije", "ty_b3": "🚚 Dostava 24–48 h",
      "ty_back": "Nazaj na spletno mesto",
    },
  },
  "hu": {
    "lang": "hu", "offer": "284", "cpa": "20", "currency": "HUF", "price": "36499",
    "was": "121.663 Ft", "now": "36.499 Ft", "now_plain": "36.499 Ft",
    "phone_ph": "+36 30 123 4567", "name_ph": "Nagy János",
    "addr_ph": "Fő utca 12, 1051 Budapest",
    "reviewers": [
      "János N. — Budapest, ellenőrzött vásárló",
      "Mária K. — Debrecen, ellenőrzött vásárló",
      "Dávid S. — Szeged, ellenőrzött vásárló",
    ],
    "t": {
      "title": "NexFold™ — Összecsukható okostelefon 3 kijelzővel | -70%",
      "desc": "NexFold™: összecsukható okostelefon 3 kijelzővel, 5G, Dual SIM, 48 MP kamera és 6800 mAh akkumulátor. Utánvét és ingyenes szállítás.",
      "og_title": "NexFold™ — Összecsukható okostelefon 3 kijelzővel | -70%",
      "og_desc": "Három összecsukható kijelző, 5G, Dual SIM, 48 MP kamera és 6800 mAh akkumulátor. Utánvét.",
      "ld_desc": "Összecsukható okostelefon három kijelzővel, 5G, Dual SIM, 48 MP kamerával és 6800 mAh akkumulátorral.",
      "submit": "Küldés...",
      "cookie": "Szükséges és harmadik féltől származó cookie-kat használunk a jobb élmény és az elemzés érdekében.",
      "cookie_ok": "Elfogadom", "cookie_more": "További információ",
      "topbar": "CSAK MA: -70% + INGYENES SZÁLLÍTÁS — UTÁNVÉT",
      "rating": "<strong>4,9/5</strong> — Több mint <strong>1 824</strong> elégedett vásárló",
      "gift": "🚚 Ingyenes szállítás + 2 év garancia a csomagban",
      "h1": "Három összecsukható kijelző, 5G teljesítmény és egész napos energia — egyetlen telefonban.",
      "lead": "A <strong>NexFold™</strong> 3 kijelzős összecsukható dizájnt, <strong>48 MP</strong> kamerát, <strong>5G</strong> kapcsolatot, AI funkciókat és <strong>6800 mAh</strong> akkumulátort egyesít. Több hely a munkához, nézéshez és kapcsolattartáshoz bárhol.",
      "cta": "IGEN, KÉREM A NEXFOLD™-OT →",
      "note": "🔒 Nincs előleg · Nincs kártya · Csak átvételkor fizet",
      "f1t": "Ingyenes szállítás", "f1p": "Gyors kiszállítás egész Magyarországon",
      "f2t": "Utánvét", "f2p": "Kártya nem szükséges",
      "f3t": "2 év garancia", "f3p": "Hivatalos fedezet a csomagban",
      "f4t": "30 napos visszaküldés", "f4p": "Egyszerű és ingyenes",
      "cd": "⏰ A -70% ár még ennyi ideig él", "h": "Óra", "m": "Perc", "s": "Mp",
      "stock_l": "Készlet", "stock_r": "Csak 4 darab maradt",
      "live": "<strong>{n} ember</strong> nézi most a NexFold™-ot",
      "live0": "<strong>38 ember</strong> nézi most a NexFold™-ot",
      "order_h": "Foglalja le a NexFold™-ot 36.499 Ft-ért",
      "order_p": "Töltse ki a 3 mezőt. 24 órán belül felhívjuk, és megerősítjük a szállítást — előre semmit sem fizet.",
      "lab_name": "Teljes név *", "err_name": "Adja meg a teljes nevét",
      "lab_phone": "Telefonszám *", "err_phone": "Adjon meg érvényes telefonszámot",
      "lab_addr": "Teljes cím *", "err_addr": "Adja meg a teljes címet",
      "confirm": "RENDELÉS MEGERŐSÍTÉSE",
      "b1e": "01 — Új generációs többfeladatos munka",
      "b1h": "Három összecsukható kijelző: dolgozzon, nézzen és kommunikáljon eszközváltás nélkül",
      "b1t1": "3 kijelző", "b1t2": "Összecsukható dizájn", "b1t3": "Széles kijelző",
      "b1p": "Kompakt telefonból másodpercek alatt nagy munkafelület lesz. A <strong>három összecsukható kijelzővel</strong> egyszerre olvashat dokumentumokat, válaszolhat üzenetekre és nézhet videót — alkalmazásváltás nélkül.",
      "b1i": "Több hely, ha kell, kompakt méret útközben.",
      "b2e": "02 — Energia és sebesség várakozás nélkül",
      "b2h": "6800 mAh akkumulátor és 66W gyorstöltés: maradjon produktív egész nap",
      "b2t1": "6800 mAh", "b2t2": "66W töltés", "b2t3": "Kb. 25 perc",
      "b2p": "A nagy kapacitású akkumulátor órákon át bírja a munkát, a streaminget és a hívásokat. Ha energiára van szüksége, a <strong>66W gyorstöltés</strong> rövidíti a várakozást, és a NexFold™ körülbelül 25 perc alatt feltöltődik.",
      "b2i": "Több üzemidő, kevesebb idő a konnektornál.",
      "b3e": "03 — Mindig kapcsolatban, két számmal",
      "b3h": "5G, Dual SIM és 48 MP kamera: minden, amire szüksége van, egy készülékben",
      "b3t1": "5G", "b3t2": "Dual SIM", "b3t3": "48 MP",
      "b3p": "Válassza szét a munkát és a magánéletet <strong>Dual SIM</strong>-mel, böngésszen gyorsan 5G-n, és fotózzon élesen a <strong>48 MP</strong> duál kamerával. A NexFold™ készen áll munkára, közösségi médiára és utazásra.",
      "b3i": "Két szám, gyors kapcsolat és részletes képek mindig önnel.",
      "cmp_l": "Közvetlen összehasonlítás", "cmp_h": "Hagyományos okostelefon vs NexFold™",
      "cmp_trad": "Hagyományos",
      "r1": "Formátum", "r1a": "Fix kijelző", "r1b": "Kompakt összecsukható dizájn",
      "r2": "Kijelző", "r2a": "Egy kijelző", "r2b": "3 összecsukható kijelző",
      "r3": "Akkumulátor", "r3a": "Gyorsan lemerül", "r3b": "6800 mAh, hosszú üzemidő",
      "r4": "Töltés", "r4a": "Lassú", "r4b": "66W, tele kb. 25 perc",
      "r5": "Kapcsolat", "r5a": "4G / egy SIM", "r5b": "5G + Dual SIM",
      "r6": "Extrák", "r6a": "Alapfunkciók", "r6b": "AI + 48 MP kamera",
      "rev_h": "Több mint 1 800 elégedett vásárló. Ezért választják a NexFold™-ot.",
      "rev1h": "Az akkumulátor és a három kijelző tényleg segít.",
      "rev1p": "«Egész nap dolgozom, és az akkumulátor bírja. A három kijelző valódi előny, ha több feladatot kezelek.»",
      "rev2h": "Kényelmes használat, az 5G mindig gyors.",
      "rev2p": "«Gyakorlatias íráshoz és útközbeni munkához. Az 5G gyors, az összecsukható forma kevés helyet foglal.»",
      "rev3h": "Három kijelzőn a játék hihetetlen.",
      "rev3p": "«A játékok a széles kijelzőn sokkal magával ragadóbbak. Az akciót és a vezérlést tisztán látom, és hosszabb köröknél is gördülékeny.»",
      "kit_e": "A csomagban", "kit_h": "Teljes NexFold™ készlet, használatra kész",
      "k1": "1× NexFold™ összecsukható okostelefon 3 kijelzővel",
      "k2": "1× 66W gyorstöltő", "k3": "1× USB-C kábel",
      "k4": "6800 mAh akkumulátor, hosszú üzemidő", "k5": "Védőtok ajándékba",
      "k6": "Rövid használati útmutató", "k7": "Hivatalos 2 év garancia",
      "faq_h": "Gyakori kérdések",
      "q1": "Mennyi ideig tart a szállítás?", "a1": "A szállítás általában 1–2 munkanap. 24 órán belül felhívjuk, és megerősítjük a rendelést és a szállítási időt.",
      "q2": "Előre kell fizetnem?", "a2": "Nem. 36.499 Ft-ot a futárnak fizet, amikor a NexFold™ megérkezik.",
      "q3": "Támogatja a NexFold™ az 5G-t és a Dual SIM-et?", "a3": "Igen. Támogatja az 5G kapcsolatot és két SIM-kártyát a munka és a magánélet szétválasztásához.",
      "q4": "Mennyi ideig tart a töltés?", "a4": "A mellékelt 66W gyorstöltővel a teljes töltés körülbelül 25 perc.",
      "q5": "Mi van, ha nem vagyok elégedett?", "a5": "A kézhezvételtől 30 napja van a visszaküldésre, plusz 2 év garancia a gyártási hibákra.",
      "q6": "Hogyan rendelhetek?", "a6": "Töltse ki az űrlapot névvel, telefonnal és címmel. Felhívjuk a megerősítéshez, és csak átvételkor fizet.",
      "foot_b": "Hasznos mindennapi termékek, szállítás 24–48 óra alatt utánvéttel.",
      "foot_h": "Információ", "about": "Rólunk", "contact": "Kapcsolat",
      "privacy": "Adatvédelmi szabályzat", "terms": "Általános szerződési feltételek",
      "cookie_l": "Cookie szabályzat", "ship": "Szállítási feltételek", "refund": "Visszaküldési szabályzat",
      "contact_h": "Kapcsolat", "rights": "Minden jog fenntartva",
      "ty_title": "Rendelés rögzítve | NexFold™",
      "ty_h": "A NexFold™ rendelését rögzítettük!",
      "ty_p": "Már csak egy utolsó lépés van hátra a rendelés lezárásához és a szállítás indításához.",
      "ty_n": "📞 Vegye fel a megerősítő hívást",
      "ty_b": "Operátorunk a következő órákban felhívja, hogy megerősítse az adatokat. Ha nem veszi fel, a rendelést nem tudjuk elküldeni.",
      "ty_h2": "Hétfő–szombat · 9:00–18:00",
      "ty_b1": "🔒 Utánvét", "ty_b2": "🛡️ 2 év garancia", "ty_b3": "🚚 Szállítás 24–48 óra",
      "ty_back": "Vissza a weboldalra",
    },
  },
  "sk": {
    "lang": "sk", "offer": "285", "cpa": "20", "currency": "EUR", "price": "99.99",
    "was": "333,30 €", "now": "99,99 €", "now_plain": "99,99 €",
    "phone_ph": "+421 905 123 456", "name_ph": "Ján Novák",
    "addr_ph": "Hlavná 12, 811 01 Bratislava",
    "reviewers": [
      "Ján N. — Bratislava, overený zákazník",
      "Mária K. — Košice, overená zákazníčka",
      "Tomáš S. — Žilina, overený zákazník",
    ],
    "t": {
      "title": "NexFold™ — Skladací smartfón s 3 obrazovkami | -70%",
      "desc": "NexFold™: skladací smartfón s 3 obrazovkami, 5G, Dual SIM, fotoaparátom 48 MP a batériou 6800 mAh. Dobierka a doprava zadarmo.",
      "og_title": "NexFold™ — Skladací smartfón s 3 obrazovkami | -70%",
      "og_desc": "Tri skladacie obrazovky, 5G, Dual SIM, fotoaparát 48 MP a batéria 6800 mAh. Platba na dobierku.",
      "ld_desc": "Skladací smartfón s troma obrazovkami, 5G, Dual SIM, fotoaparátom 48 MP a batériou 6800 mAh.",
      "submit": "Odosielanie...",
      "cookie": "Používame nevyhnutné cookies a cookies tretích strán na lepší zážitok a analytiku.",
      "cookie_ok": "Prijať", "cookie_more": "Zistiť viac",
      "topbar": "LEN DNES: -70 % + DOPRAVA ZADARMO — PLATBA NA DOBIERKU",
      "rating": "<strong>4,9/5</strong> — Viac ako <strong>1 824</strong> spokojných zákazníkov",
      "gift": "🚚 Doprava zadarmo + 2-ročná záruka v cene",
      "h1": "Tri skladacie obrazovky, výkon 5G a výdrž na celý deň — v jednom smartfóne.",
      "lead": "<strong>NexFold™</strong> spája skladací dizajn s 3 obrazovkami, fotoaparát <strong>48 MP</strong>, pripojenie <strong>5G</strong>, funkcie AI a batériu <strong>6800 mAh</strong>. Viac priestoru na prácu, sledovanie a spojenie kdekoľvek.",
      "cta": "ÁNO, CHCEM NEXFOLD™ →",
      "note": "🔒 Žiadna záloha · Žiadna karta · Platíte až pri doručení",
      "f1t": "Doprava zadarmo", "f1p": "Rýchle doručenie po celom Slovensku",
      "f2t": "Platba na dobierku", "f2p": "Karta nie je potrebná",
      "f3t": "Záruka 2 roky", "f3p": "Oficiálne krytie v cene",
      "f4t": "Vrátenie do 30 dní", "f4p": "Jednoduché a bezplatné",
      "cd": "⏰ Cena -70 % platí ešte", "h": "Hod", "m": "Min", "s": "Sek",
      "stock_l": "Dostupnosť skladu", "stock_r": "Zostávajú len 4 kusy",
      "live": "<strong>{n} ľudí</strong> si práve prezerá NexFold™",
      "live0": "<strong>38 ľudí</strong> si práve prezerá NexFold™",
      "order_h": "Rezervujte NexFold™ za 99,99 €",
      "order_p": "Vyplňte 3 polia. Do 24 hodín vám zavoláme a potvrdíme doručenie — vopred nič neplatíte.",
      "lab_name": "Meno a priezvisko *", "err_name": "Zadajte meno a priezvisko",
      "lab_phone": "Telefón *", "err_phone": "Zadajte platné telefónne číslo",
      "lab_addr": "Kompletná adresa *", "err_addr": "Zadajte kompletnú adresu",
      "confirm": "POTVRDIŤ OBJEDNÁVKU",
      "b1e": "01 — Multitasking novej generácie",
      "b1h": "Tri skladacie obrazovky: pracujte, sledujte a komunikujte bez zmeny zariadenia",
      "b1t1": "3 obrazovky", "b1t2": "Skladací dizajn", "b1t3": "Široký displej",
      "b1p": "Z kompaktného telefónu spravíte veľkú pracovnú plochu za sekundu. Vďaka <strong>trom skladacím obrazovkám</strong> môžete čítať dokumenty, odpovedať na správy a sledovať video naraz — bez neustáleho prepínania aplikácií.",
      "b1i": "Viac priestoru, keď ho potrebujete, kompaktné rozmery na cestách.",
      "b2e": "02 — Energia a rýchlosť bez čakania",
      "b2h": "Batéria 6800 mAh a rýchle nabíjanie 66W: zostaňte produktívni celý deň",
      "b2t1": "6800 mAh", "b2t2": "Nabíjanie 66W", "b2t3": "Asi 25 min",
      "b2p": "Vysokokapacitná batéria zvládne hodiny práce, streamovania aj hovorov. Keď potrebujete energiu, <strong>rýchle nabíjanie 66W</strong> skráti čakanie a NexFold™ sa nabije približne za 25 minút.",
      "b2i": "Viac výdrže, menej času pri zásuvke.",
      "b3e": "03 — Vždy online, s dvoma číslami",
      "b3h": "5G, Dual SIM a fotoaparát 48 MP: všetko, čo potrebujete, v jednom zariadení",
      "b3t1": "5G", "b3t2": "Dual SIM", "b3t3": "48 MP",
      "b3p": "Oddeľte prácu a súkromie vďaka <strong>Dual SIM</strong>, surfujte rýchlo na 5G a foťte ostro duálnym fotoaparátom <strong>48 MP</strong>. NexFold™ je pripravený na prácu, siete aj cestovanie.",
      "b3i": "Dve čísla, rýchle pripojenie a detailné fotky vždy so sebou.",
      "cmp_l": "Priame porovnanie", "cmp_h": "Klasický smartfón vs NexFold™",
      "cmp_trad": "Klasický",
      "r1": "Formát", "r1a": "Pevný displej", "r1b": "Kompaktný skladací dizajn",
      "r2": "Displej", "r2a": "Jedna obrazovka", "r2b": "3 skladacie obrazovky",
      "r3": "Batéria", "r3a": "Rýchlo sa vybíja", "r3b": "6800 mAh s vysokou výdržou",
      "r4": "Nabíjanie", "r4a": "Pomalé", "r4b": "66W, plné za cca 25 min",
      "r5": "Konektivita", "r5a": "4G / jedna SIM", "r5b": "5G + Dual SIM",
      "r6": "Navyše", "r6a": "Základné funkcie", "r6b": "AI + fotoaparát 48 MP",
      "rev_h": "Viac ako 1 800 spokojných zákazníkov. Preto volia NexFold™.",
      "rev1h": "Batéria a tri obrazovky naozaj pomáhajú.",
      "rev1p": "«Pracujem celý deň a batéria vydrží. Tri obrazovky sú skutočná výhoda, keď potrebujem zvládnuť viac vecí naraz.»",
      "rev2h": "Pohodlné ovládanie, 5G vždy rýchle.",
      "rev2p": "«Je praktický na písanie aj prácu cestou. 5G je rýchle a skladací formát zaberie málo miesta.»",
      "rev3h": "Na troch obrazovkách je hranie úžasné.",
      "rev3p": "«Hry sú na širokom displeji oveľa pohlcujúcejšie. Akciu aj ovládanie vidím jasne a všetko beží plynulo aj pri dlhších sedeniach.»",
      "kit_e": "V balení", "kit_h": "Kompletná sada NexFold™, pripravená na použitie",
      "k1": "1× skladací smartfón NexFold™ s 3 obrazovkami",
      "k2": "1× rýchla nabíjačka 66W", "k3": "1× kábel USB-C",
      "k4": "Batéria 6800 mAh s vysokou výdržou", "k5": "Ochranné puzdro ako darček",
      "k6": "Stručný návod na použitie", "k7": "Oficiálna záruka 2 roky",
      "faq_h": "Často kladené otázky",
      "q1": "Ako dlho trvá doručenie?", "a1": "Doručenie zvyčajne trvá 1–2 pracovné dni. Do 24 hodín vám zavoláme a potvrdíme objednávku aj čas doručenia.",
      "q2": "Musím platiť vopred?", "a2": "Nie. Kuriérovi zaplatíte 99,99 €, keď NexFold™ dorazí k vám domov.",
      "q3": "Podporuje NexFold™ 5G a Dual SIM?", "a3": "Áno. Podporuje pripojenie 5G a dve SIM karty na oddelenie práce a súkromia.",
      "q4": "Ako dlho trvá nabíjanie?", "a4": "S priloženou rýchlou nabíjačkou 66W trvá plné nabitie približne 25 minút.",
      "q5": "Čo ak nebudem spokojný?", "a5": "Máte 30 dní od doručenia na vrátenie a 2-ročnú záruku na výrobné chyby.",
      "q6": "Ako objednám?", "a6": "Vyplňte formulár s menom, telefónom a adresou. Zavoláme vám kvôli potvrdeniu a platíte až pri doručení.",
      "foot_b": "Užitočné produkty na každý deň, doručenie do 24–48 hodín na dobierku.",
      "foot_h": "Informácie", "about": "O nás", "contact": "Kontaktujte nás",
      "privacy": "Zásady ochrany osobných údajov", "terms": "Obchodné podmienky",
      "cookie_l": "Zásady cookies", "ship": "Doprava", "refund": "Vrátenie tovaru",
      "contact_h": "Kontakt", "rights": "Všetky práva vyhradené",
      "ty_title": "Objednávka prijatá | NexFold™",
      "ty_h": "Vaša objednávka NexFold™ bola zaregistrovaná!",
      "ty_p": "Zostáva už len posledný krok, kým objednávku dokončíme a odošleme.",
      "ty_n": "📞 Zdvihnite potvrdzovací hovor",
      "ty_b": "Operátor vás v nasledujúcich hodinách kontaktuje a overí údaje. Ak hovor nezdvihnete, objednávku nemožno odoslať.",
      "ty_h2": "Pondelok–sobota · 9:00–18:00",
      "ty_b1": "🔒 Platba na dobierku", "ty_b2": "🛡️ Záruka 2 roky", "ty_b3": "🚚 Doručenie 24–48 h",
      "ty_back": "Späť na web",
    },
  },
  "pl": {
    "lang": "pl", "offer": "286", "cpa": "19", "currency": "PLN", "price": "429",
    "was": "1 430 zł", "now": "429 zł", "now_plain": "429 zł",
    "phone_ph": "+48 600 123 456", "name_ph": "Jan Kowalski",
    "addr_ph": "ul. Główna 12, 00-001 Warszawa",
    "reviewers": [
      "Jan N. — Warszawa, zweryfikowany klient",
      "Maria K. — Kraków, zweryfikowana klientka",
      "Dawid S. — Gdańsk, zweryfikowany klient",
    ],
    "t": {
      "title": "NexFold™ — Składany smartfon z 3 ekranami | -70%",
      "desc": "NexFold™: składany smartfon z 3 ekranami, 5G, Dual SIM, aparatem 48 MP i baterią 6800 mAh. Płatność przy odbiorze i darmowa dostawa.",
      "og_title": "NexFold™ — Składany smartfon z 3 ekranami | -70%",
      "og_desc": "Trzy składane ekrany, 5G, Dual SIM, aparat 48 MP i bateria 6800 mAh. Płatność przy odbiorze.",
      "ld_desc": "Składany smartfon z trzema ekranami, 5G, Dual SIM, aparatem 48 MP i baterią 6800 mAh.",
      "submit": "Wysyłanie...",
      "cookie": "Używamy niezbędnych i zewnętrznych plików cookie, aby poprawić doświadczenie i analitykę.",
      "cookie_ok": "Akceptuję", "cookie_more": "Dowiedz się więcej",
      "topbar": "TYLKO DZIŚ: -70% + DARMOWA DOSTAWA — PŁATNOŚĆ PRZY ODBIORZE",
      "rating": "<strong>4,9/5</strong> — Ponad <strong>1 824</strong> zadowolonych klientów",
      "gift": "🚚 Darmowa dostawa + 2 lata gwarancji w zestawie",
      "h1": "Trzy składane ekrany, wydajność 5G i energia na cały dzień — w jednym smartfonie.",
      "lead": "<strong>NexFold™</strong> łączy składaną konstrukcję z 3 ekranami, aparat <strong>48 MP</strong>, łączność <strong>5G</strong>, funkcje AI i baterię <strong>6800 mAh</strong>. Więcej miejsca do pracy, oglądania i bycia w kontakcie wszędzie.",
      "cta": "TAK, CHCĘ NEXFOLD™ →",
      "note": "🔒 Bez zaliczki · Bez karty · Płacisz dopiero przy odbiorze",
      "f1t": "Darmowa dostawa", "f1p": "Szybka dostawa w całej Polsce",
      "f2t": "Płatność przy odbiorze", "f2p": "Karta nie jest potrzebna",
      "f3t": "2 lata gwarancji", "f3p": "Oficjalne pokrycie w cenie",
      "f4t": "Zwrot w 30 dni", "f4p": "Prosty i bezpłatny",
      "cd": "⏰ Cena -70% obowiązuje jeszcze", "h": "Godz", "m": "Min", "s": "Sek",
      "stock_l": "Dostępność magazynowa", "stock_r": "Zostały tylko 4 sztuki",
      "live": "<strong>{n} osób</strong> ogląda teraz NexFold™",
      "live0": "<strong>38 osób</strong> ogląda teraz NexFold™",
      "order_h": "Zarezerwuj NexFold™ za 429 zł",
      "order_p": "Wypełnij 3 pola. Zadzwonimy w 24 godziny, aby potwierdzić dostawę — z góry nic nie płacisz.",
      "lab_name": "Imię i nazwisko *", "err_name": "Podaj imię i nazwisko",
      "lab_phone": "Telefon *", "err_phone": "Podaj prawidłowy numer telefonu",
      "lab_addr": "Pełny adres *", "err_addr": "Podaj pełny adres",
      "confirm": "POTWIERDŹ ZAMÓWIENIE",
      "b1e": "01 — Wielozadaniowość nowej generacji",
      "b1h": "Trzy składane ekrany: pracuj, oglądaj i komunikuj się bez zmiany urządzenia",
      "b1t1": "3 ekrany", "b1t2": "Składana konstrukcja", "b1t3": "Szeroki wyświetlacz",
      "b1p": "Z kompaktowego telefonu w sekundę zrobisz dużą przestrzeń roboczą. Dzięki <strong>trzem składanym ekranom</strong> możesz czytać dokumenty, odpowiadać na wiadomości i oglądać wideo naraz — bez ciągłego przełączania aplikacji.",
      "b1i": "Więcej miejsca, gdy go potrzebujesz, kompaktowe wymiary w drodze.",
      "b2e": "02 — Energia i szybkość bez czekania",
      "b2h": "Bateria 6800 mAh i szybkie ładowanie 66W: zostań produktywny cały dzień",
      "b2t1": "6800 mAh", "b2t2": "Ładowanie 66W", "b2t3": "Około 25 min",
      "b2p": "Pojemna bateria wytrzymuje godziny pracy, streamingu i rozmów. Gdy potrzebujesz energii, <strong>szybkie ładowanie 66W</strong> skraca oczekiwanie, a NexFold™ ładuje się w około 25 minut.",
      "b2i": "Więcej czasu pracy, mniej czasu przy gniazdku.",
      "b3e": "03 — Zawsze w sieci, z dwoma numerami",
      "b3h": "5G, Dual SIM i aparat 48 MP: wszystko, czego potrzebujesz, w jednym urządzeniu",
      "b3t1": "5G", "b3t2": "Dual SIM", "b3t3": "48 MP",
      "b3p": "Oddziel pracę i życie prywatne dzięki <strong>Dual SIM</strong>, surfuj szybko na 5G i rób ostre zdjęcia podwójnym aparatem <strong>48 MP</strong>. NexFold™ jest gotowy do pracy, social mediów i podróży.",
      "b3i": "Dwa numery, szybkie połączenie i szczegółowe zdjęcia zawsze przy sobie.",
      "cmp_l": "Bezpośrednie porównanie", "cmp_h": "Tradycyjny smartfon vs NexFold™",
      "cmp_trad": "Tradycyjny",
      "r1": "Format", "r1a": "Sztywny ekran", "r1b": "Kompaktowa składana konstrukcja",
      "r2": "Wyświetlacz", "r2a": "Jeden ekran", "r2b": "3 składane ekrany",
      "r3": "Bateria", "r3a": "Szybko się rozładowuje", "r3b": "6800 mAh z dużą żywotnością",
      "r4": "Ładowanie", "r4a": "Wolne", "r4b": "66W, pełne w ok. 25 min",
      "r5": "Łączność", "r5a": "4G / jedna SIM", "r5b": "5G + Dual SIM",
      "r6": "Dodatki", "r6a": "Podstawowe funkcje", "r6b": "AI + aparat 48 MP",
      "rev_h": "Ponad 1 800 zadowolonych klientów. Dlatego wybierają NexFold™.",
      "rev1h": "Bateria i trzy ekrany naprawdę pomagają.",
      "rev1p": "«Pracuję cały dzień i bateria daje radę. Trzy ekrany to realna przewaga, gdy ogarniam kilka zadań.»",
      "rev2h": "Wygodne w użyciu, 5G zawsze szybkie.",
      "rev2p": "«Praktyczny do pisania i pracy w drodze. 5G jest szybkie, a składany format zajmuje mało miejsca.»",
      "rev3h": "Na trzech ekranach granie jest niesamowite.",
      "rev3p": "«Gry na szerokim wyświetlaczu są dużo bardziej wciągające. Widzę akcję i sterowanie wyraźnie, a wszystko działa płynnie nawet podczas dłuższych sesji.»",
      "kit_e": "W zestawie", "kit_h": "Kompletny zestaw NexFold™, gotowy do użycia",
      "k1": "1× składany smartfon NexFold™ z 3 ekranami",
      "k2": "1× szybka ładowarka 66W", "k3": "1× kabel USB-C",
      "k4": "Bateria 6800 mAh o dużej żywotności", "k5": "Etui ochronne w prezencie",
      "k6": "Krótka instrukcja obsługi", "k7": "Oficjalna 2-letnia gwarancja",
      "faq_h": "Często zadawane pytania",
      "q1": "Jak długo trwa dostawa?", "a1": "Dostawa zwykle trwa 1–2 dni robocze. Zadzwonimy w 24 godziny, aby potwierdzić zamówienie i czas dostawy.",
      "q2": "Czy muszę płacić z góry?", "a2": "Nie. Kurierowi płacisz 429 zł, gdy NexFold™ dotrze do domu.",
      "q3": "Czy NexFold™ obsługuje 5G i Dual SIM?", "a3": "Tak. Obsługuje łączność 5G i dwie karty SIM, aby oddzielić pracę od życia prywatnego.",
      "q4": "Ile trwa ładowanie?", "a4": "Z dołączoną szybką ładowarką 66W pełne naładowanie trwa około 25 minut.",
      "q5": "Co jeśli nie będę zadowolony?", "a5": "Masz 30 dni od dostawy na zwrot oraz 2 lata gwarancji na wady fabryczne.",
      "q6": "Jak zamówić?", "a6": "Wypełnij formularz z imieniem, telefonem i adresem. Zadzwonimy, aby potwierdzić, a płacisz dopiero przy odbiorze.",
      "foot_b": "Przydatne produkty codziennego użytku, dostawa w 24–48 godzin z płatnością przy odbiorze.",
      "foot_h": "Informacje", "about": "O nas", "contact": "Kontakt",
      "privacy": "Polityka prywatności", "terms": "Regulamin",
      "cookie_l": "Polityka cookies", "ship": "Polityka dostawy", "refund": "Polityka zwrotów",
      "contact_h": "Kontakt", "rights": "Wszelkie prawa zastrzeżone",
      "ty_title": "Zamówienie przyjęte | NexFold™",
      "ty_h": "Twoje zamówienie NexFold™ zostało zarejestrowane!",
      "ty_p": "Został tylko ostatni krok, zanim dokończymy zamówienie i wyślemy przesyłkę.",
      "ty_n": "📞 Odbierz telefon potwierdzający",
      "ty_b": "Operator skontaktuje się z Tobą w ciągu kilku godzin, aby potwierdzić dane. Jeśli nie odbierzesz, zamówienia nie będzie można wysłać.",
      "ty_h2": "Poniedziałek–sobota · 9:00–18:00",
      "ty_b1": "🔒 Płatność przy odbiorze", "ty_b2": "🛡️ 2 lata gwarancji", "ty_b3": "🚚 Dostawa 24–48 h",
      "ty_back": "Wróć na stronę",
    },
  },
}


def landing(geo, d):
    t = d["t"]
    url = f"https://spotspectrum.com/{geo}/nexfold/{d['offer']}/landing.html"
    asset = "../../../assets"
    fav = "../../../favicon.svg"
    home = "../../"
    r1, r2, r3 = d["reviewers"]
    return f"""<!DOCTYPE html>
<html lang="{d['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<meta name="contact" content="info@spotspectrum.com">
<meta name="theme-color" content="#14181f">
<link rel="canonical" href="{url}">
{HREFLANG}
<meta property="og:type" content="product">
<meta property="og:title" content="{t['og_title']}">
<meta property="og:description" content="{t['og_desc']}">
<meta property="og:image" content="https://spotspectrum.com/assets/img/products/nexfold/hero.png">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="{fav}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="image" href="{asset}/img/products/nexfold/hero.png" fetchpriority="high">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{asset}/css/nexfold-landing.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Product","name":"NexFold™","image":"https://spotspectrum.com/assets/img/products/nexfold/hero.png","description":"{t['ld_desc']}","brand":{{"@type":"Brand","name":"NexFold"}},"offers":{{"@type":"Offer","price":"{d['price']}","priceCurrency":"{d['currency']}","availability":"https://schema.org/InStock","url":"{url}"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"1824"}}}}
</script>
<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: 'nexfold',
  OFFER_ID: '{d['offer']}',
  CPA: '{d['cpa']}',
  CURRENCY: '{d['currency']}',
  PRICE: {d['price']},
  OFFER_NAME: 'FlexiPocket Phone {geo.upper()} #{d['offer']}',
  LP_ID: '{geo}-nexfold-{d['offer']}',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: {t['submit']!r},
  COOKIE_TEXT: {t['cookie']!r},
  COOKIE_ACCEPT: {t['cookie_ok']!r},
  COOKIE_LEARN: {t['cookie_more']!r}
}};
</script>
<script src="{asset}/js/tracking.js" defer></script>
<script src="{asset}/js/main.js" defer></script>
<script src="{asset}/js/form-handler.js" defer></script>
</head>
<body>

<div class="topbar">{t['topbar']}</div>

<div class="rating-strip wrap">
  <div class="stars">★★★★★</div>
  <div class="rating-text">{t['rating']}</div>
</div>

<section class="hero wrap">
  <div class="hero-copy">
    <span class="gift-strip">{t['gift']}</span>
    <h1>{t['h1']}</h1>
    <p class="lead">{t['lead']}</p>
    <div class="hero-image hero-image-mobile-only">
      <img decoding="async" src="{asset}/img/products/nexfold/hero.png" alt="NexFold" width="1024" height="1024" loading="eager" fetchpriority="high">
    </div>
    <div class="price-block"><span class="was">{d['was']}</span><span class="now">{d['now']}</span><span class="pct">-70%</span></div>
    <a href="#order-form" class="cta-btn">{t['cta']}</a>
    <p class="form-note">{t['note']}</p>
  </div>
  <div class="hero-image hero-image-desktop-only">
    <img decoding="async" src="{asset}/img/products/nexfold/hero.png" alt="NexFold" width="1024" height="1024" loading="eager" fetchpriority="high">
  </div>
</section>

<div class="wrap">
  <div class="feature-row">
    <div class="feature-item"><div class="ico">🚚</div><h4>{t['f1t']}</h4><p>{t['f1p']}</p></div>
    <div class="feature-item"><div class="ico">💳</div><h4>{t['f2t']}</h4><p>{t['f2p']}</p></div>
    <div class="feature-item"><div class="ico">🛡️</div><h4>{t['f3t']}</h4><p>{t['f3p']}</p></div>
    <div class="feature-item"><div class="ico">↩️</div><h4>{t['f4t']}</h4><p>{t['f4p']}</p></div>
  </div>
</div>

<section class="order-section" id="order-form">
  <div class="wrap">
    <div class="urgency-strip">
      <div class="countdown-row">
        <div class="countdown-label">{t['cd']}</div>
        <div class="countdown-timer" id="countdownTimer">
          <div class="box"><div class="num" id="cd-h">00</div><div class="lbl">{t['h']}</div></div><div class="sep">:</div>
          <div class="box"><div class="num" id="cd-m">14</div><div class="lbl">{t['m']}</div></div><div class="sep">:</div>
          <div class="box"><div class="num" id="cd-s">59</div><div class="lbl">{t['s']}</div></div>
        </div>
      </div>
      <div class="stock-row"><div class="stock-label"><span class="left">{t['stock_l']}</span><span class="right">{t['stock_r']}</span></div><div class="stock-bar"><div class="stock-bar-fill"></div></div></div>
      <div class="live-row"><span class="dot"></span><span id="liveCount" data-live="{t['live']}">{t['live0']}</span></div>
    </div>
    <div class="order-card">
      <h2>{t['order_h']}</h2>
      <p>{t['order_p']}</p>
      <form class="cod-form order-form" novalidate>
        <div class="cod-form__field"><label class="cod-form__label" for="name">{t['lab_name']}</label><input class="cod-form__input" id="name" type="text" name="name" autocomplete="name" placeholder="{d['name_ph']}" required minlength="3"><span class="cod-form__error">{t['err_name']}</span></div>
        <div class="cod-form__field"><label class="cod-form__label" for="phone">{t['lab_phone']}</label><input class="cod-form__input" id="phone" type="tel" name="phone" autocomplete="tel" placeholder="{d['phone_ph']}" required><span class="cod-form__error">{t['err_phone']}</span></div>
        <div class="cod-form__field"><label class="cod-form__label" for="address">{t['lab_addr']}</label><input class="cod-form__input" id="address" type="text" name="address" autocomplete="street-address" placeholder="{d['addr_ph']}" required minlength="10"><span class="cod-form__error">{t['err_addr']}</span></div>
        <button type="submit" class="cta-btn">{t['confirm']}</button>
        <p class="form-note">{t['note']}</p>
      </form>
    </div>
  </div>
</section>

<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="{asset}/img/products/nexfold/feature-1.png" alt="NexFold" width="1024" height="1024" loading="lazy"></div>
    <div><div class="num-eyebrow">{t['b1e']}</div><h3>{t['b1h']}</h3><div class="tag-row"><span class="tag">{t['b1t1']}</span><span class="tag">{t['b1t2']}</span><span class="tag">{t['b1t3']}</span></div><p>{t['b1p']}</p><p class="italic">{t['b1i']}</p></div>
  </div>
</section>
<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="{asset}/img/products/nexfold/feature-2.png" alt="NexFold" width="1024" height="1024" loading="lazy"></div>
    <div><div class="num-eyebrow">{t['b2e']}</div><h3>{t['b2h']}</h3><div class="tag-row"><span class="tag">{t['b2t1']}</span><span class="tag">{t['b2t2']}</span><span class="tag">{t['b2t3']}</span></div><p>{t['b2p']}</p><p class="italic">{t['b2i']}</p></div>
  </div>
</section>
<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="{asset}/img/products/nexfold/feature-3.png" alt="NexFold" width="1024" height="1024" loading="lazy"></div>
    <div><div class="num-eyebrow">{t['b3e']}</div><h3>{t['b3h']}</h3><div class="tag-row"><span class="tag">{t['b3t1']}</span><span class="tag">{t['b3t2']}</span><span class="tag">{t['b3t3']}</span></div><p>{t['b3p']}</p><p class="italic">{t['b3i']}</p></div>
  </div>
</section>

<section class="compare wrap">
  <div class="section-label">{t['cmp_l']}</div><h2>{t['cmp_h']}</h2>
  <table>
    <tr><th></th><th>{t['cmp_trad']}</th><th class="highlight">NexFold™</th></tr>
    <tr><td>{t['r1']}</td><td>{t['r1a']}</td><td class="win">{t['r1b']}</td></tr>
    <tr><td>{t['r2']}</td><td>{t['r2a']}</td><td class="win">{t['r2b']}</td></tr>
    <tr><td>{t['r3']}</td><td>{t['r3a']}</td><td class="win">{t['r3b']}</td></tr>
    <tr><td>{t['r4']}</td><td>{t['r4a']}</td><td class="win">{t['r4b']}</td></tr>
    <tr><td>{t['r5']}</td><td>{t['r5a']}</td><td class="win">{t['r5b']}</td></tr>
    <tr><td>{t['r6']}</td><td>{t['r6a']}</td><td class="win">{t['r6b']}</td></tr>
  </table>
</section>

<section class="testimonials">
  <div class="wrap">
    <div class="section-heading"><h2>{t['rev_h']}</h2></div>
    <div class="t-grid">
      <div class="testimonial"><img decoding="async" class="t-photo" src="{asset}/img/reviews/nexfold/review-1.png" alt="NexFold" width="1024" height="1024" loading="lazy"><div class="t-body"><div class="stars">★★★★★</div><h4>{t['rev1h']}</h4><p>{t['rev1p']}</p><div class="author-row"><div class="author">{r1}</div></div></div></div>
      <div class="testimonial"><img decoding="async" class="t-photo" src="{asset}/img/reviews/nexfold/review-2.png" alt="NexFold" width="1024" height="1024" loading="lazy"><div class="t-body"><div class="stars">★★★★★</div><h4>{t['rev2h']}</h4><p>{t['rev2p']}</p><div class="author-row"><div class="author">{r2}</div></div></div></div>
      <div class="testimonial"><img decoding="async" class="t-photo" src="{asset}/img/reviews/nexfold/review-3.png" alt="NexFold" width="1024" height="1024" loading="lazy"><div class="t-body"><div class="stars">★★★★★</div><h4>{t['rev3h']}</h4><p>{t['rev3p']}</p><div class="author-row"><div class="author">{r3}</div></div></div></div>
    </div>
  </div>
</section>

<section class="kit-section wrap">
  <div class="section-heading"><span class="eyebrow">{t['kit_e']}</span><h2>{t['kit_h']}</h2></div>
  <div class="kit-box">
    <img decoding="async" src="{asset}/img/products/nexfold/kit.png" alt="NexFold" width="1024" height="1024" loading="lazy">
    <div class="kit-content">
      <div class="price-block" style="margin-bottom:16px;"><span class="was">{d['was']}</span><span class="now">{d['now']}</span><span class="pct">-70%</span></div>
      <ul><li>{t['k1']}</li><li>{t['k2']}</li><li>{t['k3']}</li><li>{t['k4']}</li><li>{t['k5']}</li><li>{t['k6']}</li><li>{t['k7']}</li></ul>
      <a href="#order-form" class="cta-btn">{t['cta']}</a>
    </div>
  </div>
</section>

<section class="faq wrap">
  <div class="section-heading"><h2>{t['faq_h']}</h2></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{t['q1']}</span><span class="arrow">▾</span></button><div class="faq-a"><p>{t['a1']}</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{t['q2']}</span><span class="arrow">▾</span></button><div class="faq-a"><p>{t['a2']}</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{t['q3']}</span><span class="arrow">▾</span></button><div class="faq-a"><p>{t['a3']}</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{t['q4']}</span><span class="arrow">▾</span></button><div class="faq-a"><p>{t['a4']}</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{t['q5']}</span><span class="arrow">▾</span></button><div class="faq-a"><p>{t['a5']}</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{t['q6']}</span><span class="arrow">▾</span></button><div class="faq-a"><p>{t['a6']}</p></div></div>
</section>

<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div><a href="{home}" class="site-logo" aria-label="spotspectrum home"><span class="site-logo__text"><span class="site-logo__text-primary">spot</span><span class="site-logo__text-accent">spectrum</span></span></a><p class="site-footer__blurb">{t['foot_b']}</p></div>
      <div><h4 class="site-footer__heading">{t['foot_h']}</h4><ul class="site-footer__list"><li><a href="{home}about-us.html">{t['about']}</a></li><li><a href="{home}contact-us.html">{t['contact']}</a></li><li><a href="{home}privacy-policy.html">{t['privacy']}</a></li><li><a href="{home}terms-conditions.html">{t['terms']}</a></li><li><a href="{home}cookie-policy.html">{t['cookie_l']}</a></li><li><a href="{home}shipping-policy.html">{t['ship']}</a></li><li><a href="{home}refund-policy.html">{t['refund']}</a></li></ul></div>
      <div><h4 class="site-footer__heading">{t['contact_h']}</h4><ul class="site-footer__list"><li><strong>EASY PEASY GROUP LIMITED</strong></li><li>FLAT/RM A 15/F GOLDFIELD INDUSTRIAL BUILDING 144-150 TAI LIN PAI ROAD — 葵涌, Hong Kong</li><li><a href="mailto:info@spotspectrum.com">info@spotspectrum.com</a></li></ul></div>
    </div>
    <div class="site-footer__bottom">© <span data-year>2026</span> <strong>EASY PEASY GROUP LIMITED</strong> — {t['rights']}. <a href="{home}">spotspectrum.com</a></div>
  </div>
</footer>

<script src="{asset}/js/droniq-landing.js" defer></script>
<script>document.querySelectorAll('[data-year]').forEach(function(el){{el.textContent=String(new Date().getFullYear());}});</script>
</body>
</html>
"""


def thank_you(geo, d):
    t = d["t"]
    return f"""<!DOCTYPE html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{t['ty_title']}</title>
<link rel="icon" href="../../../favicon.svg">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#f7f9fb;color:#14181f;font-family:Poppins,sans-serif}}.card{{max-width:560px;margin:48px auto;padding:34px 24px;background:#fff;border-radius:18px;box-shadow:0 8px 28px #14181f12;text-align:center}}.check{{width:70px;height:70px;margin:auto;border-radius:50%;display:grid;place-items:center;background:#dcfce7;color:#15803d;font-size:36px;font-weight:800}}h1{{font-size:28px;line-height:1.25}}.notice{{margin:24px 0;padding:20px;background:#fff7ed;border:1px solid #fed7aa;border-radius:12px}}.badges{{display:flex;flex-wrap:wrap;justify-content:center;gap:8px}}.badges span{{padding:8px 12px;background:#f1f5f9;border-radius:999px;font-size:12px;font-weight:600}}a{{color:#1e9be0}}
</style>
<script>window.SITE_CONFIG={{GEO:'{geo}',PRODUCT_SLUG:'nexfold',OFFER_ID:'{d['offer']}',CURRENCY:'{d['currency']}',PRICE:{d['price']}}};</script>
<script src="../../../assets/js/tracking.js" defer></script>
</head>
<body>
<main class="card">
  <div class="check">✓</div>
  <h1>{t['ty_h']}</h1>
  <p>{t['ty_p']}</p>
  <section class="notice"><h2>{t['ty_n']}</h2><p>{t['ty_b']}</p></section>
  <p><strong>{t['ty_h2']}</strong></p>
  <div class="badges"><span>{t['ty_b1']}</span><span>{t['ty_b2']}</span><span>{t['ty_b3']}</span></div>
  <p><a href="../../">{t['ty_back']}</a></p>
</main>
<script>window.addEventListener('load',function(){{if(window.trackPurchase)window.trackPurchase({d['price']},'{d['currency']}');}});</script>
</body>
</html>
"""


def index_redirect(geo, offer, lang, label):
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0;url=landing.html">
<link rel="canonical" href="landing.html">
<title>NexFold™</title>
</head>
<body><p><a href="landing.html">{label}</a></p></body>
</html>
"""


def main():
    labels = {
        "cz": "Přejít na NexFold™",
        "si": "Pojdi na NexFold™",
        "hu": "Ugrás a NexFold™ oldalra",
        "sk": "Prejsť na NexFold™",
        "pl": "Przejdź do NexFold™",
    }
    for geo, d in GEOS.items():
        dest = ROOT / geo / "nexfold" / d["offer"]
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "landing.html").write_text(landing(geo, d), encoding="utf-8")
        (dest / "thank-you.html").write_text(thank_you(geo, d), encoding="utf-8")
        (dest / "index.html").write_text(index_redirect(geo, d["offer"], d["lang"], labels[geo]), encoding="utf-8")
        parent = ROOT / geo / "nexfold"
        parent.mkdir(parents=True, exist_ok=True)
        (parent / "index.html").write_text(
            f"""<!DOCTYPE html><html lang="{d['lang']}"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={d['offer']}/landing.html"><link rel="canonical" href="{d['offer']}/landing.html"><title>NexFold™</title></head><body><p><a href="{d['offer']}/landing.html">{labels[geo]}</a></p></body></html>\n""",
            encoding="utf-8",
        )
        print(f"wrote {dest}")


if __name__ == "__main__":
    main()
