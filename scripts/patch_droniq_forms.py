#!/usr/bin/env python3
"""Replace local COD forms with Unbreakable Offers tm-order-form on Droniq geos."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

FORMS = {
    "pl": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Imię i nazwisko:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Imię i nazwisko:" required><br>
        <label for="tel">Telefon (najlepiej komórkowy):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefon (najlepiej komórkowy):" required><br>
        <label for="street-address">Pełny adres:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Pełny adres:" required><br>
        <label for="postal-code">Kod Pocztowy:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="Kod Pocztowy:"><br>
        <input name="uid" type="hidden" value="019f60bd-7f67-709f-a69c-8041b92c05ba">
        <input name="offer" type="hidden" value="191">
        <input name="lp" type="hidden" value="191">
        <input name="thankyoupage" type="hidden" value="https://spotspectrum.com/pl/droniq/thank-you.html">
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/nirpd72vokb2m0x5wsd6x3d68hbgn8ae">
        <input name="_key" type="hidden" value="603c90212948915cec39b4c5f3682d7f79920011">
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit">Kup Teraz i Zapłać Przy Odbiorze!</button>
        </div>
        <p class="form-note">🔒 Bez zaliczki · Bez karty · Płacisz tylko przy odbiorze</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "sk": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Meno a priezvisko:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Meno a priezvisko:" required><br>
        <label for="tel">Telefón (najlepšie mobilný):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefón (najlepšie mobilný):" required><br>
        <label for="street-address">Úplná adresa:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Úplná adresa:" required><br>
        <label for="postal-code">PSČ:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="PSČ:"><br>
        <input name="uid" type="hidden" value="019f60bd-7f67-709f-a69c-8041b92c05ba">
        <input name="offer" type="hidden" value="190">
        <input name="lp" type="hidden" value="190">
        <input name="thankyoupage" type="hidden" value="https://spotspectrum.com/sk/droniq/thank-you.html">
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/nirpd72vokb2m0x5wsd6x3d68hbgn8ae">
        <input name="_key" type="hidden" value="cb0f3d7d4d068bfa2e06a7d5386ded7e322969ca">
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit">Kúpte Teraz A Plaťte Pri Dobierke!</button>
        </div>
        <p class="form-note">🔒 Bez zálohy · Bez karty · Platíte až pri doručení</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "cz": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Jméno A Příjmení:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Jméno A Příjmení:" required><br>
        <label for="tel">Telefon (Nejlépe Mobilní):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefon (Nejlépe Mobilní):" required><br>
        <label for="street-address">Úplná Adresa:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Úplná Adresa:" required><br>
        <label for="postal-code">PSČ:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="PSČ:"><br>
        <input name="uid" type="hidden" value="019f60bd-7f67-709f-a69c-8041b92c05ba">
        <input name="offer" type="hidden" value="189">
        <input name="lp" type="hidden" value="189">
        <input name="thankyoupage" type="hidden" value="https://spotspectrum.com/cz/droniq/thank-you.html">
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/nirpd72vokb2m0x5wsd6x3d68hbgn8ae">
        <input name="_key" type="hidden" value="71698b891d7fafa8e3892438ef072d33d937b3ad">
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit">Kupte Nyní A Plaťte Při Doručení</button>
        </div>
        <p class="form-note">🔒 Bez zálohy · Bez karty · Platíte až při doručení</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "si": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Ime in priimek:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Ime in priimek:" required><br>
        <label for="tel">Telefon (po možnosti mobilni):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefon (po možnosti mobilni):" required><br>
        <label for="street-address">Celoten naslov:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Celoten naslov:" required><br>
        <label for="postal-code">Poštna številka:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="Poštna številka:"><br>
        <input name="uid" type="hidden" value="019f60bd-7f67-709f-a69c-8041b92c05ba">
        <input name="offer" type="hidden" value="188">
        <input name="lp" type="hidden" value="188">
        <input name="thankyoupage" type="hidden" value="https://spotspectrum.com/si/droniq/thank-you.html">
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/nirpd72vokb2m0x5wsd6x3d68hbgn8ae">
        <input name="_key" type="hidden" value="81a49ceaab1dca40bfbbdc99e4c6a92803919e3a">
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit">Kupite zdaj in plačajte ob prevzemu!</button>
        </div>
        <p class="form-note">🔒 Brez predplačila · Brez kartice · Plačate šele ob dostavi</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "hr": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Ime i prezime:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Ime i prezime:" required><br>
        <label for="tel">Telefon (najbolje mobitel):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefon (najbolje mobitel):" required><br>
        <label for="street-address">Puna adresa:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Puna adresa:" required><br>
        <label for="postal-code">Poštanski broj:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="Poštanski broj:"><br>
        <input name="uid" type="hidden" value="019f60bd-7f67-709f-a69c-8041b92c05ba">
        <input name="offer" type="hidden" value="187">
        <input name="lp" type="hidden" value="187">
        <input name="thankyoupage" type="hidden" value="https://spotspectrum.com/hr/droniq/thank-you.html">
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/nirpd72vokb2m0x5wsd6x3d68hbgn8ae">
        <input name="_key" type="hidden" value="2281cefd5f3417a8d445076b873d6edaadcb4900">
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit">Kupi sada i plati pouzećem!</button>
        </div>
        <p class="form-note">🔒 Bez predujma · Bez kartice · Plaćate tek pri dostavi</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "hu": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Teljes név:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Teljes név:" required><br>
        <label for="tel">Telefonszám (lehetőleg mobil):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefonszám (lehetőleg mobil):" required><br>
        <label for="street-address">Teljes cím:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Teljes cím:" required><br>
        <label for="postal-code">Irányítószám:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="Irányítószám:"><br>
        <input name="uid" type="hidden" value="019f60bd-7f67-709f-a69c-8041b92c05ba">
        <input name="offer" type="hidden" value="186">
        <input name="lp" type="hidden" value="186">
        <input name="thankyoupage" type="hidden" value="https://spotspectrum.com/hu/droniq/thank-you.html">
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/nirpd72vokb2m0x5wsd6x3d68hbgn8ae">
        <input name="_key" type="hidden" value="2e7df757105042c1405bccd2077cc6b478179d90">
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit">Vásároljon most és fizessen utánvéttel!</button>
        </div>
        <p class="form-note">🔒 Nincs előleg · Nincs kártya · Csak átvételkor fizet</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "ro": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Nume si Prenume:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Nume si Prenume:" required><br>
        <label for="tel">Telefon (de preferință mobil):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefon (de preferință mobil):" required><br>
        <label for="street-address">Adresa completă:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Adresa completă:" required><br>
        <label for="postal-code">Cod poștal:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="Cod poștal:"><br>
        <input name="uid" type="hidden" value="019f60bd-7f67-709f-a69c-8041b92c05ba">
        <input name="offer" type="hidden" value="185">
        <input name="lp" type="hidden" value="185">
        <input name="thankyoupage" type="hidden" value="https://spotspectrum.com/ro/droniq/thank-you.html">
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/nirpd72vokb2m0x5wsd6x3d68hbgn8ae">
        <input name="_key" type="hidden" value="e237f816785b3757173c5ed62f8507bcf7c36eb7">
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit">Cumpărați Acum Și Plătiți La Livrare!</button>
        </div>
        <p class="form-note">🔒 Fără avans · Fără card · Plătiți doar la livrare</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "es": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Nombre y apellido:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Nombre y apellido:" required><br>
        <label for="tel">Teléfono (preferiblemente móvil):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Teléfono (preferiblemente móvil):" required><br>
        <label for="street-address">Dirección completa:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Dirección completa:" required><br>
        <label for="postal-code">Código postal:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="Código postal:"><br>
        <input name="uid" type="hidden" value="019f60bd-7f67-709f-a69c-8041b92c05ba">
        <input name="offer" type="hidden" value="184">
        <input name="lp" type="hidden" value="184">
        <input name="thankyoupage" type="hidden" value="https://spotspectrum.com/es/droniq/thank-you.html">
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/nirpd72vokb2m0x5wsd6x3d68hbgn8ae">
        <input name="_key" type="hidden" value="86f783152f017fefcd6d149e300903de4b7e4088">
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit">¡Compra ahora y paga al recibir el pedido!</button>
        </div>
        <p class="form-note">🔒 Sin depósito · Sin tarjeta · Pagas solo al recibir</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "pt": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Nome e apelido:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Nome e apelido:" required><br>
        <label for="tel">Telefone (de preferência telemóvel):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefone (de preferência telemóvel):" required><br>
        <label for="street-address">Endereço completo:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Endereço completo:" required><br>
        <label for="postal-code">CEP:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="CEP:"><br>
        <input name="uid" type="hidden" value="019f60bd-7f67-709f-a69c-8041b92c05ba">
        <input name="offer" type="hidden" value="183">
        <input name="lp" type="hidden" value="183">
        <input name="thankyoupage" type="hidden" value="https://spotspectrum.com/pt/droniq/thank-you.html">
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/nirpd72vokb2m0x5wsd6x3d68hbgn8ae">
        <input name="_key" type="hidden" value="d7757541deb6d8375a020d1f101cb42de6dfa66c">
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit">Compre agora e pague na entrega!</button>
        </div>
        <p class="form-note">🔒 Sem adiantamento · Sem cartão · Paga só na entrega</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
}

form_re = re.compile(r'<form class="cod-form order-form" novalidate>.*?</form>', re.DOTALL)


def main() -> None:
    for geo, form_html in FORMS.items():
        path = ROOT / geo / "droniq" / "landing.html"
        text = path.read_text(encoding="utf-8")
        if not form_re.search(text):
            print(f"NO FORM MATCH: {geo}")
            continue
        text = form_re.sub(form_html, text, count=1)
        text = text.replace('<script src="/assets/js/form-handler.js" defer></script>\n', "")
        path.write_text(text, encoding="utf-8")
        offer = re.search(r'name="offer"[^>]*value="(\d+)"', form_html).group(1)
        key = re.search(r'name="_key"[^>]*value="([^"]+)"', form_html).group(1)
        print(f"OK {geo} offer={offer} key={key[:8]}...")
    print("DONE")


if __name__ == "__main__":
    main()
