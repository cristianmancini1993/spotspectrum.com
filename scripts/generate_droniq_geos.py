#!/usr/bin/env python3
"""Generate localized Droniq landing / thank-you / index pages for EU geos."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HREFLANG_BLOCK = """\
<link rel="alternate" hreflang="en" href="https://spotspectrum.com/en/droniq/landing.html">
<link rel="alternate" hreflang="it" href="https://spotspectrum.com/it/droniq/landing.html">
<link rel="alternate" hreflang="pt" href="https://spotspectrum.com/pt/droniq/landing.html">
<link rel="alternate" hreflang="es" href="https://spotspectrum.com/es/droniq/landing.html">
<link rel="alternate" hreflang="ro" href="https://spotspectrum.com/ro/droniq/landing.html">
<link rel="alternate" hreflang="hu" href="https://spotspectrum.com/hu/droniq/landing.html">
<link rel="alternate" hreflang="hr" href="https://spotspectrum.com/hr/droniq/landing.html">
<link rel="alternate" hreflang="si" href="https://spotspectrum.com/si/droniq/landing.html">
<link rel="alternate" hreflang="cs" href="https://spotspectrum.com/cz/droniq/landing.html">
<link rel="alternate" hreflang="sk" href="https://spotspectrum.com/sk/droniq/landing.html">
<link rel="alternate" hreflang="pl" href="https://spotspectrum.com/pl/droniq/landing.html">
<link rel="alternate" hreflang="x-default" href="https://spotspectrum.com/">"""

# folder -> config. lang_html is used for <html lang=""> and hreflang code (cz -> cs).
GEOS = [
    {
        "geo": "pt",
        "lang": "pt",
        "offer_id": 183,
        "currency": "EUR",
        "price": 79.99,
        "price_now": "79,99 €",
        "price_was": "199,99 €",
        "price_once": "79,99 €",
        "compare_other": "≈ 200 €+",
        "phone": "+351",
        "names": ("Pedro K.", "Tomás W.", "Miguel S."),
        "name_ph": "João Silva",
        "addr_ph": "Rua Example 12, 1000-001 Lisboa",
    },
    {
        "geo": "es",
        "lang": "es",
        "offer_id": 184,
        "currency": "EUR",
        "price": 69.99,
        "price_now": "69,99 €",
        "price_was": "174,99 €",
        "price_once": "69,99 €",
        "compare_other": "≈ 200 €+",
        "phone": "+34",
        "names": ("Pedro K.", "Tomás W.", "Miguel S."),
        "name_ph": "Juan García",
        "addr_ph": "Calle Mayor 12, 28013 Madrid",
    },
    {
        "geo": "ro",
        "lang": "ro",
        "offer_id": 185,
        "currency": "RON",
        "price": 349,
        "price_now": "349 RON",
        "price_was": "872 RON",
        "price_once": "349 RON",
        "compare_other": "≈ 900 RON+",
        "phone": "+40",
        "names": ("Petru K.", "Tomas W.", "Mihai S."),
        "name_ph": "Ion Popescu",
        "addr_ph": "Str. Exemplu 12, București",
    },
    {
        "geo": "hu",
        "lang": "hu",
        "offer_id": 186,
        "currency": "HUF",
        "price": 26999,
        "price_now": "26 999 Ft",
        "price_was": "67 499 Ft",
        "price_once": "26 999 Ft",
        "compare_other": "≈ 80 000 Ft+",
        "phone": "+36",
        "names": ("Péter K.", "Tamás W.", "Mihály S."),
        "name_ph": "Kovács János",
        "addr_ph": "Példa utca 12, 1051 Budapest",
    },
    {
        "geo": "hr",
        "lang": "hr",
        "offer_id": 187,
        "currency": "EUR",
        "price": 69.99,
        "price_now": "69,99 €",
        "price_was": "174,99 €",
        "price_once": "69,99 €",
        "compare_other": "≈ 200 €+",
        "phone": "+385",
        "names": ("Petar K.", "Tomislav W.", "Mihael S."),
        "name_ph": "Ivan Horvat",
        "addr_ph": "Ulica Primjer 12, 10000 Zagreb",
    },
    {
        "geo": "si",
        "lang": "si",
        "offer_id": 188,
        "currency": "EUR",
        "price": 69.99,
        "price_now": "69,99 €",
        "price_was": "174,99 €",
        "price_once": "69,99 €",
        "compare_other": "≈ 200 €+",
        "phone": "+386",
        "names": ("Peter K.", "Tomaž W.", "Miha S."),
        "name_ph": "Janez Novak",
        "addr_ph": "Primerjeva 12, 1000 Ljubljana",
    },
    {
        "geo": "cz",
        "lang": "cs",
        "offer_id": 189,
        "currency": "CZK",
        "price": 1749,
        "price_now": "1 749 Kč",
        "price_was": "4 372 Kč",
        "price_once": "1 749 Kč",
        "compare_other": "≈ 5 000 Kč+",
        "phone": "+420",
        "names": ("Petr K.", "Tomáš W.", "Michal S."),
        "name_ph": "Jan Novák",
        "addr_ph": "Ukázková 12, 110 00 Praha",
    },
    {
        "geo": "sk",
        "lang": "sk",
        "offer_id": 190,
        "currency": "EUR",
        "price": 69.99,
        "price_now": "69,99 €",
        "price_was": "174,99 €",
        "price_once": "69,99 €",
        "compare_other": "≈ 200 €+",
        "phone": "+421",
        "names": ("Peter K.", "Tomáš W.", "Michal S."),
        "name_ph": "Ján Novák",
        "addr_ph": "Ukážková 12, 811 01 Bratislava",
    },
    {
        "geo": "pl",
        "lang": "pl",
        "offer_id": 191,
        "currency": "PLN",
        "price": 299,
        "price_now": "299 zł",
        "price_was": "748 zł",
        "price_once": "299 zł",
        "compare_other": "≈ 800 zł+",
        "phone": "+48",
        "names": ("Piotr K.", "Tomasz W.", "Michał S."),
        "name_ph": "Jan Kowalski",
        "addr_ph": "ul. Przykładowa 12, 00-001 Warszawa",
    },
]


def price_js(price: float | int) -> str:
    if isinstance(price, float):
        return f"{price:.2f}"
    return str(price)


# Full native copy keyed by geo folder code.
COPY: dict[str, dict[str, str]] = {}

COPY["pt"] = {
    "title": "Droniq™ — Drone Ultra HD 8K com GPS e Evitação de Obstáculos | -60%",
    "meta_desc": "Droniq™: drone Ultra HD 8K, fácil de voar desde o primeiro dia, sem licença (C0 A1/A3). Retorno GPS automático, sensores de obstáculos, zoom 22x, 3 baterias para 2+ horas de voo. Pagamento à cobrança, envio grátis 24/48h.",
    "og_title": "Droniq™ — Drone Ultra HD 8K | -60%",
    "og_desc": "Ultra HD 8K, retorno GPS automático, sensores de obstáculos, sem licença. Pagamento à cobrança.",
    "submitting": "A enviar...",
    "cookie_text": "Utilizamos cookies essenciais e de terceiros para melhorar a sua experiência e para análises.",
    "cookie_accept": "Aceitar",
    "cookie_learn": "Saber mais",
    "topbar": "🔥 60% DE DESCONTO + ENVIO GRÁTIS — PAGAMENTO À COBRANÇA 🔥",
    "rating": "<strong>4,8/5</strong> — com base em <strong>3.842+ avaliações verificadas</strong>",
    "gift": "🎁 GRÁTIS: 3 baterias + mala rígida + hélices sobressalentes",
    "h1": 'Crie vídeos que impressionam todos.<br>Um drone: <span class="hl">Droniq™</span>',
    "lead": "Droniq™ é um <strong>drone Ultra HD 8K</strong> fácil de voar desde a primeira descolagem — <strong>sem necessidade de licença</strong>. GPS com retorno automático, sensores inteligentes de obstáculos, velocidades até <strong>120 km/h</strong> e armazenamento expansível até <strong>256 GB</strong> para horas de filmagens com qualidade de cinema.",
    "alt_hero": "Kit completo Droniq™ drone Ultra HD 8K",
    "cta": "SIM, QUERO O Droniq™ →",
    "cta_submit": "SIM, QUERO O Droniq™",
    "form_note": "🔒 Sem depósito · Sem cartão · Pague só na entrega",
    "feat1_h": "Ultra HD 8K",
    "feat1_p": "Vídeo com qualidade de cinema e fotos nítidas",
    "feat2_h": "GPS inteligente",
    "feat2_p": "Retorno automático se o sinal ou a bateria baixarem",
    "feat3_h": "Sensores de obstáculos",
    "feat3_p": "Deteta e evita obstáculos à frente",
    "feat4_h": "Pagamento à cobrança",
    "feat4_p": "Prático, seguro, sem pagamento antecipado",
    "countdown": "⏰ O desconto de 60% expira em",
    "hrs": "Hrs",
    "min": "Min",
    "sec": "Seg",
    "stock_left": "Disponibilidade no armazém",
    "stock_right": "Apenas 8 unidades restantes",
    "live_tpl": "&lt;strong&gt;{n} pessoas&lt;/strong&gt; estão a ver o Droniq agora",
    "live_html": "<strong>36 pessoas</strong> estão a ver o Droniq agora",
    "order_h2": "Conclua a sua encomenda",
    "order_p": "Preencha o formulário — a nossa equipa entrará em contacto para confirmar todos os detalhes.",
    "label_name": "Nome completo *",
    "err_name": "Introduza o seu nome completo (pelo menos 3 caracteres)",
    "label_phone": "Número de telefone *",
    "err_phone": "Introduza um número de telefone válido",
    "label_address": "Morada de entrega *",
    "err_address": "Introduza uma morada completa (pelo menos 10 caracteres)",
    "why1_eye": "01 — Filmagens com qualidade de cinema",
    "why1_h3": "Vídeo Ultra HD 8K — panoramas e detalhes distantes num só plano",
    "why1_tags": '<span class="tag">Ultra HD 8K</span><span class="tag">Zoom 22x</span><span class="tag">Grande angular</span>',
    "why1_p": "Crie filmes e fotos com aspeto profissional. Panoramas espetaculares, detalhes nítidos e vistas aéreas impressionantes transformam cada viagem em memórias que vai rever durante anos. A câmara <strong>Ultra HD 8K</strong>, a lente grande angular e o <strong>zoom digital 22x</strong> permitem passar de paisagens amplas a detalhes distantes sem perder nitidez.",
    "why1_i": "Transforme cada viagem em memórias com qualidade de cinema.",
    "alt_desc1": "Câmara Droniq™ Ultra HD 8K com zoom 22x",
    "why2_eye": "02 — Voe em segurança em qualquer situação",
    "why2_h3": "GPS inteligente, sensores de obstáculos e Follow Me — total tranquilidade",
    "why2_tags": '<span class="tag">Retorno GPS</span><span class="tag">Anticolisão</span><span class="tag">Follow Me</span>',
    "why2_p": "A IA ajuda a detetar obstáculos, o GPS segue a posição constantemente e, se o sinal cair ou a bateria baixar, o Droniq™ <strong>regressa automaticamente ao ponto de descolagem</strong>. Descolagem e aterragem automáticas e o modo Follow Me tornam cada voo mais fácil e seguro — mesmo que nunca tenha voado um drone.",
    "why2_i": "Voa com confiança — o Droniq™ protege-o.",
    "aria_video": "Retorno GPS automático e evitamento de obstáculos do Droniq™",
    "why3_eye": "03 — Pronto desde o primeiro dia",
    "why3_h3": "Sem licença · 2+ horas de voo · estável até vento de 38 km/h",
    "why3_tags": '<span class="tag">C0 (A1/A3)</span><span class="tag">3 baterias</span><span class="tag">Vento 38 km/h</span>',
    "why3_p": "O Droniq™ cumpre a norma <strong>C0 (A1/A3)</strong> — sem licença, certificados ou burocracia. Hélices de fibra de carbono e estabilização avançada mantêm as imagens nítidas mesmo com vento até <strong>38 km/h</strong>. O kit inclui <strong>3 baterias de alta capacidade</strong> para mais de 2 horas de voo total.",
    "why3_i": "Ligue, descole e comece a filmar hoje.",
    "alt_desc3": "Voo estável Droniq™ até vento de 38 km/h com 3 baterias",
    "compare_label": "Porque vale mesmo a pena",
    "compare_h2": "Câmara do telemóvel / drone básico vs Droniq™",
    "th_phone": "Telemóvel / drone básico",
    "td_price": "Preço",
    "td_price_other": "para equipamento separado",
    "once": "uma vez",
    "td_video": "Vídeo",
    "td_video_other": "Qualidade média do telemóvel",
    "td_video_win": "Ultra HD 8K + zoom 22x",
    "td_safety": "Segurança",
    "td_safety_other": "Só manual — fácil de perder",
    "td_safety_win": "Retorno GPS + sensores de obstáculos",
    "td_flight": "Tempo de voo",
    "td_flight_other": "Muitas vezes menos de 20 minutos",
    "td_flight_win": "2+ horas com 3 baterias",
    "td_license": "Licença",
    "td_license_other": "Muitas vezes necessária",
    "td_license_win": "C0 — sem licença",
    "td_warranty": "Garantia",
    "td_warranty_other": "Variável",
    "td_warranty_win": "24 meses + 30 dias para devoluções",
    "t_eye": "⭐ 4,8/5 · Compra verificada · Avaliações moderadas",
    "t_h2": "Milhares de clientes recomendam o Droniq™",
    "t1_h": "Perfeito para principiantes",
    "t1_p": "«Foi o meu primeiro drone e tinha medo de ser difícil. Em minutos já estava no ar. A descolagem e aterragem automáticas facilitam o voo, e o GPS dá-me tranquilidade durante todo o voo. Recomendaria mesmo a quem nunca voou.»",
    "t1_verified": "Compra verificada",
    "t2_h": "A qualidade das imagens surpreendeu-me",
    "t2_p": "«Levei-o numa viagem à montanha e as imagens ficaram deslumbrantes. Mesmo com vento mais forte manteve-se estável e os vídeos saíram nítidos e fluidos. A este preço foi uma compra fantástica.»",
    "t3_h": "Kit completo, retorno automático",
    "t3_p": "«O conjunto chegou completo — três baterias, hélices sobressalentes, tudo para começar a voar. A função de retorno automático foi o que mais me convenceu: se o sinal cair ou a bateria acabar, regressa sozinho. Agora voo com muito mais calma.»",
    "kit_eye": "O que está na caixa",
    "kit_h2": "📦 Kit Droniq™ completo pronto a voar",
    "alt_kit": "Kit completo do drone Droniq™",
    "kit1": "<strong>1× Drone profissional Droniq™</strong> — Ultra HD 8K, GPS, sensores de obstáculos",
    "kit2": "<strong>3× Baterias de alta capacidade</strong> — mais de 2 horas de voo total",
    "kit3": "1× Comando remoto inteligente",
    "kit4": "1× Carregador rápido (~30 minutos)",
    "kit5": "6× Hélices sobressalentes",
    "kit6": "1× Mala rígida de transporte",
    "kit7": "Manual do utilizador + garantia de 24 meses",
    "kit8": "Envio grátis 24/48 h",
    "faq_eye": "Perguntas frequentes",
    "faq_h2": "Respostas aqui",
    "faq": [
        ("Como encomendo?", "Preencha o formulário com nome, telefone e morada. A nossa equipa contactá-lo-á, responderá a dúvidas e confirmará os detalhes de entrega."),
        ("Posso pagar na entrega?", "Sim. Por conveniência e segurança pode pagar na entrega: quando o produto chegar, paga ao estafeta. Não são necessários dados de cartão."),
        ("É fácil de voar para principiantes?", "Sim. O Droniq™ foi concebido para quem nunca voou um drone. Descolagem e aterragem são automáticas, os controlos são intuitivos e a IA ajuda a manter um voo estável e seguro desde a primeira utilização."),
        ("Preciso de licença ou certificado?", "Não. O Droniq™ cumpre a norma <strong>C0</strong> na categoria A1/A3 e pode ser usado sem licença, certificados ou burocracia complicada."),
        ("Que qualidade de vídeo e foto oferece?", "O Droniq™ grava em <strong>Ultra HD 8K</strong> e tira fotos excecionalmente nítidas. A lente grande angular e o zoom digital 22x permitem passar suavemente de panoramas a detalhes distantes."),
        ("E se o drone perder o sinal ou a bateria baixar?", "Graças ao módulo GPS integrado, o Droniq™ regressa automaticamente ao ponto de descolagem se o sinal se perder ou a bateria estiver baixa."),
        ("E se não ficar satisfeito?", "Tem <strong>30 dias</strong> após a entrega para devolução ou troca, mais garantia de 24 meses contra defeitos de fabrico e apoio ao cliente."),
        ("Quanto custa o envio e quanto demora?", "O envio é <strong>grátis</strong>. Processamos encomendas em 24 horas; o estafeta chega normalmente em 24/48 horas úteis."),
    ],
    "footer_blurb": "Produtos úteis do dia a dia, entrega em 24–48 horas com pagamento à cobrança.",
    "footer_info": "Informações",
    "footer_about": "Sobre nós",
    "footer_contact_us": "Contacte-nos",
    "footer_privacy": "Política de Privacidade",
    "footer_terms": "Termos e Condições",
    "footer_cookie": "Política de Cookies",
    "footer_shipping": "Política de Envio",
    "footer_refund": "Política de Reembolso",
    "footer_contact": "Contacto",
    "footer_rights": "Todos os direitos reservados",
    # thank-you
    "ty_title": "Encomenda recebida — Por favor atenda a chamada de confirmação | Droniq™",
    "ty_meta": "A sua encomenda Droniq™ foi registada. Um último passo: atenda a chamada de confirmação do nosso operador.",
    "ty_h1": "A sua encomenda foi registada com sucesso!",
    "ty_sub": "Ótimo — a sua encomenda está a ser processada. Falta só <strong>um último passo</strong> para a concluir e iniciar o envio.",
    "ty_img_alt": "A equipa Crazy Marketing a trabalhar: call center COD e logística",
    "ty_eye": "👇 O que precisa de fazer agora",
    "ty_action_h": "📞 Atenda a chamada de confirmação",
    "ty_action_body": "Um dos nossos operadores contactá-lo-á <strong>nas próximas horas</strong> para confirmar a sua encomenda.",
    "ty_warn": "Se não atender a chamada, a encomenda será automaticamente cancelada.",
    "ty_hours_h": "🕒 Horário de contacto",
    "ty_hours": "<strong>Segunda – Sábado</strong> · 9:00 – 18:00",
    "ty_next_h": "📋 O que acontece a seguir",
    "ty_s1": "Atenda a chamada e <strong>confirme os seus dados</strong>",
    "ty_s2": "A sua encomenda será enviada em <strong>24–48 horas</strong>",
    "ty_s3": "Entrega ao domicílio e <strong>pagamento à cobrança</strong>",
    "ty_b1": "🔒 Pagamento à cobrança",
    "ty_b2": "🛡️ Garantia de 2 anos",
    "ty_b3": "🔐 Proteção SSL",
    "ty_rights": "Todos os direitos reservados.",
    "index_link": "Ir para a landing Droniq™",
}

COPY["es"] = {
    "title": "Droniq™ — Dron Ultra HD 8K con GPS y Evitación de Obstáculos | -60%",
    "meta_desc": "Droniq™: dron Ultra HD 8K, fácil de volar desde el primer día, sin licencia (C0 A1/A3). Retorno GPS automático, sensores de obstáculos, zoom 22x, 3 baterías para 2+ horas de vuelo. Contrareembolso, envío gratis 24/48h.",
    "og_title": "Droniq™ — Dron Ultra HD 8K | -60%",
    "og_desc": "Ultra HD 8K, retorno GPS automático, sensores de obstáculos, sin licencia. Contrareembolso.",
    "submitting": "Enviando...",
    "cookie_text": "Usamos cookies esenciales y de terceros para mejorar tu experiencia y para analítica.",
    "cookie_accept": "Aceptar",
    "cookie_learn": "Más información",
    "topbar": "🔥 60% DE DESCUENTO + ENVÍO GRATIS — CONTRAREEMBOLSO 🔥",
    "rating": "<strong>4,8/5</strong> — basado en <strong>3.842+ reseñas verificadas</strong>",
    "gift": "🎁 GRATIS: 3 baterías + maletín rígido + hélices de repuesto",
    "h1": 'Crea vídeos que impresionan a todos.<br>Un solo dron: <span class="hl">Droniq™</span>',
    "lead": "Droniq™ es un <strong>dron Ultra HD 8K</strong> fácil de volar desde el primer despegue — <strong>sin necesidad de licencia</strong>. GPS con retorno automático, sensores inteligentes de obstáculos, velocidades de hasta <strong>120 km/h</strong> y almacenamiento ampliable hasta <strong>256 GB</strong> para horas de metraje con calidad de cine.",
    "alt_hero": "Kit completo Droniq™ dron Ultra HD 8K",
    "cta": "SÍ, QUIERO Droniq™ →",
    "cta_submit": "SÍ, QUIERO Droniq™",
    "form_note": "🔒 Sin depósito · Sin tarjeta · Paga solo al recibir",
    "feat1_h": "Ultra HD 8K",
    "feat1_p": "Vídeo con calidad de cine y fotos nítidas",
    "feat2_h": "GPS inteligente",
    "feat2_p": "Retorno automático si baja la señal o la batería",
    "feat3_h": "Sensores de obstáculos",
    "feat3_p": "Detecta y evita obstáculos delante",
    "feat4_h": "Contrareembolso",
    "feat4_p": "Cómodo, seguro, sin pago anticipado",
    "countdown": "⏰ El descuento del 60% caduca en",
    "hrs": "Hrs",
    "min": "Min",
    "sec": "Seg",
    "stock_left": "Disponibilidad en almacén",
    "stock_right": "Solo quedan 8 unidades",
    "live_tpl": "&lt;strong&gt;{n} personas&lt;/strong&gt; están viendo Droniq ahora",
    "live_html": "<strong>36 personas</strong> están viendo Droniq ahora",
    "order_h2": "Completa tu pedido",
    "order_p": "Rellena el formulario — nuestro equipo te contactará para confirmar cada detalle.",
    "label_name": "Nombre completo *",
    "err_name": "Introduce tu nombre completo (al menos 3 caracteres)",
    "label_phone": "Número de teléfono *",
    "err_phone": "Introduce un número de teléfono válido",
    "label_address": "Dirección de entrega *",
    "err_address": "Introduce una dirección completa (al menos 10 caracteres)",
    "why1_eye": "01 — Metraje con calidad de cine",
    "why1_h3": "Vídeo Ultra HD 8K — panorámicas y detalles lejanos en un solo disparo",
    "why1_tags": '<span class="tag">Ultra HD 8K</span><span class="tag">Zoom 22x</span><span class="tag">Gran angular</span>',
    "why1_p": "Crea películas y fotos con aspecto profesional. Panorámicas espectaculares, detalles nítidos y vistas aéreas impresionantes convierten cada viaje en recuerdos que volverás a ver durante años. La cámara <strong>Ultra HD 8K</strong>, el objetivo gran angular y el <strong>zoom digital 22x</strong> te permiten pasar de paisajes amplios a detalles lejanos sin perder claridad.",
    "why1_i": "Convierte cada viaje en recuerdos con calidad de cine.",
    "alt_desc1": "Cámara Droniq™ Ultra HD 8K con zoom 22x",
    "why2_eye": "02 — Vuela seguro en cada situación",
    "why2_h3": "GPS inteligente, sensores de obstáculos y Follow Me — total tranquilidad",
    "why2_tags": '<span class="tag">Retorno GPS</span><span class="tag">Anticolisión</span><span class="tag">Follow Me</span>',
    "why2_p": "La IA ayuda a detectar obstáculos, el GPS sigue la posición constantemente y, si cae la señal o baja la batería, Droniq™ <strong>regresa automáticamente al punto de despegue</strong>. Despegue y aterrizaje automáticos y el modo Follow Me hacen cada vuelo más fácil y seguro — aunque nunca hayas volado un dron.",
    "why2_i": "Vuelas con confianza — Droniq™ te respalda.",
    "aria_video": "Retorno GPS automático y evitación de obstáculos de Droniq™",
    "why3_eye": "03 — Listo desde el primer día",
    "why3_h3": "Sin licencia · 2+ horas de vuelo · estable con viento de hasta 38 km/h",
    "why3_tags": '<span class="tag">C0 (A1/A3)</span><span class="tag">3 baterías</span><span class="tag">Viento 38 km/h</span>',
    "why3_p": "Droniq™ cumple la norma <strong>C0 (A1/A3)</strong> — sin licencia, certificados ni papeleo. Las hélices de fibra de carbono y la estabilización avanzada mantienen las tomas nítidas incluso con viento de hasta <strong>38 km/h</strong>. El kit incluye <strong>3 baterías de alta capacidad</strong> para más de 2 horas de vuelo total.",
    "why3_i": "Enciéndelo, despega y empieza a filmar hoy.",
    "alt_desc3": "Vuelo estable Droniq™ hasta viento de 38 km/h con 3 baterías",
    "compare_label": "Por qué realmente merece la pena",
    "compare_h2": "Cámara del móvil / dron básico vs Droniq™",
    "th_phone": "Móvil / dron básico",
    "td_price": "Precio",
    "td_price_other": "en equipos separados",
    "once": "una vez",
    "td_video": "Vídeo",
    "td_video_other": "Calidad media del móvil",
    "td_video_win": "Ultra HD 8K + zoom 22x",
    "td_safety": "Seguridad",
    "td_safety_other": "Solo manual — fácil de perder",
    "td_safety_win": "Retorno GPS + sensores de obstáculos",
    "td_flight": "Tiempo de vuelo",
    "td_flight_other": "A menudo menos de 20 minutos",
    "td_flight_win": "2+ horas con 3 baterías",
    "td_license": "Licencia",
    "td_license_other": "A menudo necesaria",
    "td_license_win": "C0 — sin licencia",
    "td_warranty": "Garantía",
    "td_warranty_other": "Variable",
    "td_warranty_win": "24 meses + 30 días de devolución",
    "t_eye": "⭐ 4,8/5 · Compra verificada · Reseñas moderadas",
    "t_h2": "Miles de clientes recomiendan Droniq™",
    "t1_h": "Perfecto para principiantes",
    "t1_p": "«Fue mi primer dron y me preocupaba que fuera difícil. En minutos ya estaba en el aire. El despegue y aterrizaje automáticos facilitan el vuelo, y el GPS me da tranquilidad durante todo el vuelo. Lo recomendaría incluso a quien nunca ha volado.»",
    "t1_verified": "Compra verificada",
    "t2_h": "La calidad del metraje me dejó sin palabras",
    "t2_p": "«Lo llevé a un viaje de montaña y las tomas salieron impresionantes. Incluso con viento más fuerte se mantuvo estable y los vídeos eran nítidos y fluidos. A este precio fue una compra fantástica.»",
    "t3_h": "Kit completo, retorno automático",
    "t3_p": "«El set llegó completo — tres baterías, hélices de repuesto, todo para empezar a volar. La función de retorno automático fue lo que más me convenció: si cae la señal o se acaba la batería, vuelve solo. Ahora vuelo con mucha más calma.»",
    "kit_eye": "Qué hay en la caja",
    "kit_h2": "📦 Kit Droniq™ completo listo para volar",
    "alt_kit": "Kit completo del dron Droniq™",
    "kit1": "<strong>1× Dron profesional Droniq™</strong> — Ultra HD 8K, GPS, sensores de obstáculos",
    "kit2": "<strong>3× Baterías de alta capacidad</strong> — más de 2 horas de vuelo total",
    "kit3": "1× Mando a distancia inteligente",
    "kit4": "1× Cargador rápido (~30 minutos)",
    "kit5": "6× Hélices de repuesto",
    "kit6": "1× Maletín rígido de transporte",
    "kit7": "Manual de usuario + garantía de 24 meses",
    "kit8": "Envío gratis 24/48 h",
    "faq_eye": "Preguntas frecuentes",
    "faq_h2": "Respuestas aquí mismo",
    "faq": [
        ("¿Cómo pido?", "Rellena el formulario con tu nombre, teléfono y dirección. Nuestro equipo te contactará, responderá dudas y confirmará los detalles de entrega."),
        ("¿Puedo pagar al recibir?", "Sí. Por comodidad y seguridad puedes pagar al recibir: cuando llegue el producto, pagas al mensajero. No se requieren datos de tarjeta."),
        ("¿Es fácil de volar para principiantes?", "Sí. Droniq™ está diseñado para quienes nunca han volado un dron. El despegue y el aterrizaje son automáticos, los controles son intuitivos y la IA ayuda a mantener un vuelo estable y seguro desde el primer uso."),
        ("¿Necesito licencia o certificado?", "No. Droniq™ cumple la norma <strong>C0</strong> en categoría A1/A3 y se puede usar sin licencia, certificados ni papeleo complicado."),
        ("¿Qué calidad de vídeo y foto ofrece?", "Droniq™ graba en <strong>Ultra HD 8K</strong> y hace fotos excepcionalmente nítidas. El objetivo gran angular y el zoom digital 22x permiten pasar con fluidez de panorámicas a detalles lejanos."),
        ("¿Y si el dron pierde la señal o baja la batería?", "Gracias al módulo GPS integrado, Droniq™ regresa automáticamente al punto de despegue si se pierde la señal o la batería está baja."),
        ("¿Y si no estoy satisfecho?", "Tienes <strong>30 días</strong> desde la entrega para devolución o cambio, más 24 meses de garantía por defectos de fabricación y atención al cliente."),
        ("¿Cuánto cuesta el envío y cuánto tarda?", "El envío es <strong>gratis</strong>. Procesamos pedidos en 24 horas; el mensajero suele llegar en 24/48 horas laborables."),
    ],
    "footer_blurb": "Productos útiles del día a día, entrega en 24–48 horas con contrareembolso.",
    "footer_info": "Información",
    "footer_about": "Sobre nosotros",
    "footer_contact_us": "Contáctanos",
    "footer_privacy": "Política de Privacidad",
    "footer_terms": "Términos y Condiciones",
    "footer_cookie": "Política de Cookies",
    "footer_shipping": "Política de Envío",
    "footer_refund": "Política de Reembolso",
    "footer_contact": "Contacto",
    "footer_rights": "Todos los derechos reservados",
    "ty_title": "Pedido recibido — Por favor responde a la llamada de confirmación | Droniq™",
    "ty_meta": "Tu pedido Droniq™ ha sido registrado. Un último paso: responde a la llamada de confirmación de nuestro operador.",
    "ty_h1": "¡Tu pedido se ha registrado con éxito!",
    "ty_sub": "Genial — tu pedido se está procesando. Solo falta <strong>un último paso</strong> para completarlo y empezar el envío.",
    "ty_img_alt": "El equipo Crazy Marketing trabajando: call center COD y logística",
    "ty_eye": "👇 Lo que debes hacer ahora",
    "ty_action_h": "📞 Responde a la llamada de confirmación",
    "ty_action_body": "Uno de nuestros operadores te contactará <strong>en las próximas horas</strong> para confirmar tu pedido.",
    "ty_warn": "Si no respondes a la llamada, el pedido se cancelará automáticamente.",
    "ty_hours_h": "🕒 Horario de contacto",
    "ty_hours": "<strong>Lunes – Sábado</strong> · 9:00 – 18:00",
    "ty_next_h": "📋 Qué pasa después",
    "ty_s1": "Responde a la llamada y <strong>confirma tus datos</strong>",
    "ty_s2": "Tu pedido se enviará en <strong>24–48 horas</strong>",
    "ty_s3": "Entrega a domicilio y <strong>contrareembolso</strong>",
    "ty_b1": "🔒 Contrareembolso",
    "ty_b2": "🛡️ Garantía de 2 años",
    "ty_b3": "🔐 Protección SSL",
    "ty_rights": "Todos los derechos reservados.",
    "index_link": "Ir a la landing de Droniq™",
}

# Continue with remaining languages in a compact but complete form...
# Romanian, Hungarian, Croatian, Slovenian, Czech, Slovak, Polish


def _faq_html(items: list[tuple[str, str]]) -> str:
    parts = []
    for q, a in items:
        parts.append(
            f'<div class="faq-item"><button class="faq-q" type="button"><span>{q}</span><span class="arrow">▾</span></button>\n'
            f'    <div class="faq-a"><p>{a}</p></div></div>'
        )
    return "\n  ".join(parts)


def build_landing(cfg: dict, t: dict[str, str]) -> str:
    geo = cfg["geo"]
    lang = cfg["lang"]
    oid = cfg["offer_id"]
    geo_up = geo.upper()
    n1, n2, n3 = cfg["names"]
    pj = price_js(cfg["price"])
    faq = _faq_html(t["faq"])
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-17528466836"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'AW-17528466836');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{t['title']}</title>
<meta name="description" content="{t['meta_desc']}">
<meta name="contact" content="info@spotspectrum.com">
<meta name="theme-color" content="#14181f">
<link rel="canonical" href="https://spotspectrum.com/{geo}/droniq/landing.html">
{HREFLANG_BLOCK}
<meta property="og:type" content="product">
<meta property="og:title" content="{t['og_title']}">
<meta property="og:description" content="{t['og_desc']}">
<meta property="og:image" content="https://spotspectrum.com/assets/img/products/droniq/hero.webp">
<meta property="og:url" content="https://spotspectrum.com/{geo}/droniq/landing.html">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/droniq-landing.css">
<link as="image" fetchpriority="high" href="/assets/img/products/droniq/hero.webp" rel="preload">
<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: 'droniq',
  CURRENCY: '{cfg['currency']}',
  PRICE: {pj},
  OFFER_NAME: 'Droniq SkyMaster {geo_up} #{oid}',
  LP_ID: '{geo}-droniq-{oid}',
  META_PIXEL_ID: '',
  GOOGLE_TAG_ID: '',
  GOOGLE_ADS_CONVERSION_ID: '',
  GOOGLE_ADS_CONVERSION_LABEL: '',
  TY_CONVERSION_LABEL: '',
  NETWORK_PIXEL_URL: '',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: '{t['submitting']}',
  COOKIE_TEXT: '{t['cookie_text']}',
  COOKIE_ACCEPT: '{t['cookie_accept']}',
  COOKIE_LEARN: '{t['cookie_learn']}'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
<script src="/assets/js/main.js" defer></script>
<script src="/assets/js/form-handler.js" defer></script>
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
      <img decoding="async" src="/assets/img/products/droniq/hero.webp" alt="{t['alt_hero']}" width="1024" height="1024" loading="eager" fetchpriority="high" onerror="this.src='/assets/img/placeholder.svg'">
    </div>
    <div class="price-block">
      <span class="was">{cfg['price_was']}</span>
      <span class="now">{cfg['price_now']}</span>
      <span class="pct">-60%</span>
    </div>
    <a href="#order-form" class="cta-btn">{t['cta']}</a>
    <p class="form-note">{t['form_note']}</p>
  </div>
  <div class="hero-image hero-image-desktop-only">
    <img decoding="async" src="/assets/img/products/droniq/hero.webp" alt="{t['alt_hero']}" width="1024" height="1024" loading="eager" fetchpriority="high" onerror="this.src='/assets/img/placeholder.svg'">
  </div>
</section>

<div class="wrap">
  <div class="feature-row">
    <div class="feature-item"><div class="ico">🎥</div><h4>{t['feat1_h']}</h4><p>{t['feat1_p']}</p></div>
    <div class="feature-item"><div class="ico">📡</div><h4>{t['feat2_h']}</h4><p>{t['feat2_p']}</p></div>
    <div class="feature-item"><div class="ico">🛡️</div><h4>{t['feat3_h']}</h4><p>{t['feat3_p']}</p></div>
    <div class="feature-item"><div class="ico">💳</div><h4>{t['feat4_h']}</h4><p>{t['feat4_p']}</p></div>
  </div>
</div>

<section class="order-section" id="order-form">
  <div class="wrap">
    <div class="urgency-strip">
      <div class="countdown-row">
        <div class="countdown-label">{t['countdown']}</div>
        <div class="countdown-timer" id="countdownTimer">
          <div class="box"><div class="num" id="cd-h">00</div><div class="lbl">{t['hrs']}</div></div>
          <div class="sep">:</div>
          <div class="box"><div class="num" id="cd-m">14</div><div class="lbl">{t['min']}</div></div>
          <div class="sep">:</div>
          <div class="box"><div class="num" id="cd-s">59</div><div class="lbl">{t['sec']}</div></div>
        </div>
      </div>
      <div class="stock-row">
        <div class="stock-label"><span class="left">{t['stock_left']}</span><span class="right">{t['stock_right']}</span></div>
        <div class="stock-bar"><div class="stock-bar-fill" style="width:88%"></div></div>
      </div>
      <div class="live-row">
        <span class="dot"></span>
        <span id="liveCount" data-live="{t['live_tpl']}">{t['live_html']}</span>
      </div>
    </div>

    <div class="order-card">
      <h2>{t['order_h2']}</h2>
      <p>{t['order_p']}</p>
      <form class="cod-form order-form" novalidate>
        <div class="cod-form__field">
          <label class="cod-form__label" for="name">{t['label_name']}</label>
          <input class="cod-form__input" type="text" id="name" name="name" autocomplete="name" placeholder="{cfg['name_ph']}" required minlength="3">
          <span class="cod-form__error">{t['err_name']}</span>
        </div>
        <div class="cod-form__field">
          <label class="cod-form__label" for="phone">{t['label_phone']}</label>
          <input class="cod-form__input" type="tel" id="phone" name="phone" autocomplete="tel" placeholder="{cfg['phone']}" required>
          <span class="cod-form__error">{t['err_phone']}</span>
        </div>
        <div class="cod-form__field">
          <label class="cod-form__label" for="address">{t['label_address']}</label>
          <input class="cod-form__input" type="text" id="address" name="address" autocomplete="street-address" placeholder="{cfg['addr_ph']}" required minlength="10">
          <span class="cod-form__error">{t['err_address']}</span>
        </div>
        <button type="submit" class="cta-btn">{t['cta_submit']}</button>
        <p class="form-note">{t['form_note']}</p>
      </form>
    </div>
  </div>
</section>

<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/droniq/desc-1.webp" alt="{t['alt_desc1']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
    <div>
      <div class="num-eyebrow">{t['why1_eye']}</div>
      <h3>{t['why1_h3']}</h3>
      <div class="tag-row">{t['why1_tags']}</div>
      <p>{t['why1_p']}</p>
      <p class="italic">{t['why1_i']}</p>
    </div>
  </div>
</section>

<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img">
      <video width="720" height="720" autoplay muted loop playsinline preload="metadata" poster="/assets/img/products/droniq/desc-2.webp" aria-label="{t['aria_video']}">
        <source src="/assets/img/products/droniq/desc-2.mp4" type="video/mp4">
      </video>
    </div>
    <div>
      <div class="num-eyebrow">{t['why2_eye']}</div>
      <h3>{t['why2_h3']}</h3>
      <div class="tag-row">{t['why2_tags']}</div>
      <p>{t['why2_p']}</p>
      <p class="italic">{t['why2_i']}</p>
    </div>
  </div>
</section>

<section class="why-block wrap" style="border-bottom:none;">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/droniq/desc-3.webp" alt="{t['alt_desc3']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
    <div>
      <div class="num-eyebrow">{t['why3_eye']}</div>
      <h3>{t['why3_h3']}</h3>
      <div class="tag-row">{t['why3_tags']}</div>
      <p>{t['why3_p']}</p>
      <p class="italic">{t['why3_i']}</p>
    </div>
  </div>
</section>

<section class="compare">
  <div class="compare__inner">
  <div class="section-label">{t['compare_label']}</div>
  <h2>{t['compare_h2']}</h2>
  <table>
    <tr><th></th><th>{t['th_phone']}</th><th class="highlight">Droniq™</th></tr>
    <tr><td>{t['td_price']}</td><td>{cfg['compare_other']} {t['td_price_other']}</td><td class="win">{cfg['price_once']} {t['once']}</td></tr>
    <tr><td>{t['td_video']}</td><td>{t['td_video_other']}</td><td class="win">{t['td_video_win']}</td></tr>
    <tr><td>{t['td_safety']}</td><td>{t['td_safety_other']}</td><td class="win">{t['td_safety_win']}</td></tr>
    <tr><td>{t['td_flight']}</td><td>{t['td_flight_other']}</td><td class="win">{t['td_flight_win']}</td></tr>
    <tr><td>{t['td_license']}</td><td>{t['td_license_other']}</td><td class="win">{t['td_license_win']}</td></tr>
    <tr><td>{t['td_warranty']}</td><td>{t['td_warranty_other']}</td><td class="win">{t['td_warranty_win']}</td></tr>
  </table>
  </div>
</section>

<section class="testimonials">
  <div class="wrap">
    <div class="section-heading">
      <span class="eyebrow">{t['t_eye']}</span>
      <h2>{t['t_h2']}</h2>
    </div>
    <div class="t-grid">
      <div class="testimonial">
        <img decoding="async" class="t-photo" src="/assets/img/reviews/droniq/review-1.webp" alt="Droniq™ — {n1} {t['t1_verified'].lower()}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
        <div class="t-body">
          <div class="stars">★★★★★</div>
          <h4>{t['t1_h']}</h4>
          <p>{t['t1_p']}</p>
          <div class="author-row"><div class="author">{n1} — {t['t1_verified']}</div></div>
        </div>
      </div>
      <div class="testimonial">
        <img decoding="async" class="t-photo" src="/assets/img/reviews/droniq/review-2.webp" alt="Droniq™ — {n2} {t['t1_verified'].lower()}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
        <div class="t-body">
          <div class="stars">★★★★★</div>
          <h4>{t['t2_h']}</h4>
          <p>{t['t2_p']}</p>
          <div class="author-row"><div class="author">{n2} — {t['t1_verified']}</div></div>
        </div>
      </div>
      <div class="testimonial">
        <img decoding="async" class="t-photo" src="/assets/img/reviews/droniq/review-3.webp" alt="Droniq™ — {n3} {t['t1_verified'].lower()}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
        <div class="t-body">
          <div class="stars">★★★★★</div>
          <h4>{t['t3_h']}</h4>
          <p>{t['t3_p']}</p>
          <div class="author-row"><div class="author">{n3} — {t['t1_verified']}</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="kit-section wrap">
  <div class="section-heading">
    <span class="eyebrow">{t['kit_eye']}</span>
    <h2>{t['kit_h2']}</h2>
  </div>
  <div class="kit-box">
    <img decoding="async" src="/assets/img/products/droniq/kit.webp" alt="{t['alt_kit']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
    <div class="kit-content">
      <div class="price-block" style="margin-bottom:16px;">
        <span class="was">{cfg['price_was']}</span>
        <span class="now">{cfg['price_now']}</span>
        <span class="pct">-60%</span>
      </div>
      <ul>
        <li>{t['kit1']}</li>
        <li>{t['kit2']}</li>
        <li>{t['kit3']}</li>
        <li>{t['kit4']}</li>
        <li>{t['kit5']}</li>
        <li>{t['kit6']}</li>
        <li>{t['kit7']}</li>
        <li>{t['kit8']}</li>
      </ul>
      <a href="#order-form" class="cta-btn">{t['cta']}</a>
    </div>
  </div>
</section>

<section class="faq wrap">
  <div class="section-heading">
    <span class="eyebrow">{t['faq_eye']}</span>
    <h2>{t['faq_h2']}</h2>
  </div>
  {faq}
</section>

<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a href="/{geo}/" class="site-logo" aria-label="spotspectrum.com home">
          <span class="site-logo__text"><span class="site-logo__text-primary">spot</span><span class="site-logo__text-accent">spectrum</span></span>
        </a>
        <p class="site-footer__blurb">{t['footer_blurb']}</p>
      </div>
      <div>
        <h4 class="site-footer__heading">{t['footer_info']}</h4>
        <ul class="site-footer__list">
          <li><a href="/{geo}/about-us.html">{t['footer_about']}</a></li>
          <li><a href="/{geo}/contact-us.html">{t['footer_contact_us']}</a></li>
          <li><a href="/{geo}/privacy-policy.html">{t['footer_privacy']}</a></li>
          <li><a href="/{geo}/terms-conditions.html">{t['footer_terms']}</a></li>
          <li><a href="/{geo}/cookie-policy.html">{t['footer_cookie']}</a></li>
          <li><a href="/{geo}/shipping-policy.html">{t['footer_shipping']}</a></li>
          <li><a href="/{geo}/refund-policy.html">{t['footer_refund']}</a></li>
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">{t['footer_contact']}</h4>
        <ul class="site-footer__list">
          <li><strong>EASY PEASY GROUP LIMITED</strong></li>
          <li>FLAT/RM A 15/F GOLDFIELD INDUSTRIAL BUILDING 144-150 TAI LIN PAI ROAD — 葵涌, Hong Kong</li>
          <li><a href="mailto:info@spotspectrum.com">info@spotspectrum.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>EASY PEASY GROUP LIMITED</strong> — {t['footer_rights']}
      <a href="/{geo}/">spotspectrum.com</a>
    </div>
  </div>
</footer>

<script src="/assets/js/droniq-landing.js" defer></script>
<script>
  document.querySelectorAll('[data-year]').forEach(function (el) {{
    el.textContent = String(new Date().getFullYear());
  }});
</script>
</body>
</html>
"""


def build_thank_you(cfg: dict, t: dict[str, str]) -> str:
    geo = cfg["geo"]
    lang = cfg["lang"]
    pj = price_js(cfg["price"])
    # Read EN TY for CSS block to keep identical structure
    en_ty = (ROOT / "en/droniq/thank-you.html").read_text(encoding="utf-8")
    m = re.search(r"<style>\n(.*?)\n</style>", en_ty, re.S)
    if not m:
        raise RuntimeError("Could not extract CSS from EN thank-you.html")
    css = m.group(0)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-17528466836"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'AW-17528466836');
</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t['ty_title']}</title>
<meta name="description" content="{t['ty_meta']}">
<meta name="contact" content="info@spotspectrum.com">
<meta name="theme-color" content="#16a34a">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap">
<link rel="stylesheet" href="/assets/css/variables.css">
<link rel="stylesheet" href="/assets/css/reset.css">
<link rel="stylesheet" href="/assets/css/components.css">

{css}

<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: 'droniq',
  CURRENCY: '{cfg['currency']}',
  PRICE: {pj},
  META_PIXEL_ID: '',
  GOOGLE_TAG_ID: '',
  GOOGLE_ADS_CONVERSION_ID: '',
  TY_CONVERSION_LABEL: '',
  COOKIE_TEXT: '{t['cookie_text']}',
  COOKIE_ACCEPT: '{t['cookie_accept']}',
  COOKIE_LEARN: '{t['cookie_learn']}'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
<script src="/assets/js/main.js" defer></script>
<script>
// Trigger Purchase / conversion event after page load
window.addEventListener('load', function () {{
  if (window.trackPurchase) window.trackPurchase({pj}, '{cfg['currency']}');
}});
</script>
</head>
<body>

<header class="site-header">
  <div class="site-header__inner">
    <a href="/{geo}/" class="site-logo" aria-label="spotspectrum home">
      <span class="site-logo__text"><span class="site-logo__text-primary">spot</span><span class="site-logo__text-accent">spectrum</span></span>
    </a>
  </div>
</header>

<main class="ty-page">

  <div class="ty-check" aria-hidden="true">✓</div>

  <h1 class="ty-headline">{t['ty_h1']}</h1>
  <p class="ty-subhead">{t['ty_sub']}</p>

  <figure class="ty-hero">
    <img src="/assets/img/site/thank_you_draftin.png" alt="{t['ty_img_alt']}" width="2848" height="1331" loading="lazy" decoding="async">
  </figure>

  <!-- ACTION REQUIRED -->
  <section class="ty-action">
    <div class="ty-action__eyebrow">{t['ty_eye']}</div>
    <h2 class="ty-action__title">{t['ty_action_h']}</h2>
    <p class="ty-action__body">{t['ty_action_body']}</p>
    <p class="ty-action__warning">{t['ty_warn']}</p>
  </section>

  <!-- CONTACT HOURS -->
  <section class="ty-box">
    <div class="ty-box__header">{t['ty_hours_h']}</div>
    <div class="ty-box__body">
      <div class="ty-hours-line">{t['ty_hours']}</div>
    </div>
  </section>

  <!-- WHAT HAPPENS NEXT -->
  <section class="ty-box">
    <div class="ty-box__header">{t['ty_next_h']}</div>
    <div class="ty-box__body">
      <ol class="ty-steps-list">
        <li>{t['ty_s1']}</li>
        <li>{t['ty_s2']}</li>
        <li>{t['ty_s3']}</li>
      </ol>
    </div>
  </section>

  <!-- TRUST BADGES -->
  <div class="ty-trust">
    <span class="ty-trust__badge">{t['ty_b1']}</span>
    <span class="ty-trust__badge">{t['ty_b2']}</span>
    <span class="ty-trust__badge">{t['ty_b3']}</span>
  </div>

</main>

<footer class="site-footer"><div class="container">
  <div class="site-footer__grid">
    <div>
      <a href="/{geo}/" class="site-logo">
        <span class="site-logo__text" style="display:inline"><span class="site-logo__text-primary">spot</span><span class="site-logo__text-accent">spectrum</span></span>
      </a>
    </div>
    <div>
      <h4 class="site-footer__heading">{t['footer_info']}</h4>
      <ul class="site-footer__list">
        <li><a href="/{geo}/about-us.html">{t['footer_about']}</a></li>
        <li><a href="/{geo}/contact-us.html">{t['footer_contact_us']}</a></li>
        <li><a href="/{geo}/privacy-policy.html">{t['footer_privacy']}</a></li>
        <li><a href="/{geo}/terms-conditions.html">{t['footer_terms']}</a></li>
        <li><a href="/{geo}/cookie-policy.html">{t['footer_cookie']}</a></li>
        <li><a href="/{geo}/shipping-policy.html">{t['footer_shipping']}</a></li>
        <li><a href="/{geo}/refund-policy.html">{t['footer_refund']}</a></li>
      </ul>
    </div>
    <div>
      <h4 class="site-footer__heading">{t['footer_contact']}</h4>
      <ul class="site-footer__list">
        <li><strong>EASY PEASY GROUP LIMITED</strong></li>
        <li>FLAT/RM A 15/F GOLDFIELD INDUSTRIAL BUILDING 144-150 TAI LIN PAI ROAD — 葵涌, Hong Kong</li>
        <li><a href="mailto:info@spotspectrum.com">info@spotspectrum.com</a></li>
      </ul>
    </div>
  </div>
  <div class="site-footer__bottom">© <span data-year>2026</span> <strong>EASY PEASY GROUP LIMITED</strong> — {t['ty_rights']}</div>
</div></footer>

<!-- CPA: impostare da network quando disponibile (attualmente placeholder 1.0) -->
<!-- Event snippet for Conversioni - Crazy Marketing - UNB #1 conversion page -->
<script>
  (function () {{
    var p = new URLSearchParams(window.location.search);

    function stored(name) {{
      try {{ return window.localStorage.getItem('df_' + name) || ''; }}
      catch (e) {{ return ''; }}
    }}

    var campaignId = p.get('campaign_id') || p.get('utm_campaign') || p.get('campaignid') || p.get('subid') || stored('campaign_id') || stored('utm_campaign') || stored('subid') || '';
    var subid = p.get('subid') || campaignId || stored('subid') || '';
    var transactionId = p.get('order_id') || p.get('transaction_id') || p.get('tid') || subid || '';

    gtag('event', 'conversion', {{
      'send_to': 'AW-17528466836/9BwoCJ-LjqccEJTbnKZB',
      'value': 1.0,
      'currency': '{cfg['currency']}',
      'transaction_id': transactionId,
      'campaign_id': campaignId,
      'subid': subid,
      'utm_campaign': p.get('utm_campaign') || campaignId,
      'utm_source': p.get('utm_source') || stored('utm_source') || '',
      'utm_medium': p.get('utm_medium') || stored('utm_medium') || '',
      'utm_term': p.get('utm_term') || stored('utm_term') || '',
      'utm_content': p.get('utm_content') || stored('utm_content') || ''
    }});
  }})();
</script>

</body>
</html>
"""


def build_index(cfg: dict, t: dict[str, str]) -> str:
    return (
        f'<!DOCTYPE html><html lang="{cfg["lang"]}"><head><meta charset="utf-8">'
        f'<meta http-equiv="refresh" content="0;url=landing.html">'
        f'<link rel="canonical" href="landing.html"><title>Droniq™</title></head>'
        f'<body><p><a href="landing.html">{t["index_link"]}</a></p></body></html>\n'
    )


def update_hreflang_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    # Replace any existing alternate hreflang block(s) after canonical
    new = re.sub(
        r'(<link rel="canonical" href="https://spotspectrum\.com/(?:en|it)/droniq/landing\.html">)\s*'
        r'(?:<link rel="alternate" hreflang="[^"]+" href="[^"]+">\s*)+',
        r"\1\n" + HREFLANG_BLOCK + "\n",
        text,
        count=1,
    )
    if new == text:
        # Fallback: insert after canonical
        new = text.replace(
            '<link rel="canonical" href="https://spotspectrum.com/en/droniq/landing.html">',
            '<link rel="canonical" href="https://spotspectrum.com/en/droniq/landing.html">\n' + HREFLANG_BLOCK,
            1,
        )
        new = new.replace(
            '<link rel="canonical" href="https://spotspectrum.com/it/droniq/landing.html">',
            '<link rel="canonical" href="https://spotspectrum.com/it/droniq/landing.html">\n' + HREFLANG_BLOCK,
            1,
        )
        # Remove duplicate old alternates if both patterns applied poorly
    path.write_text(new, encoding="utf-8")
    print(f"Updated hreflang: {path.relative_to(ROOT)}")


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    for cfg in GEOS:
        geo = cfg["geo"]
        entry = (
            f'  <url><loc>https://spotspectrum.com/{geo}/droniq/landing.html</loc>'
            f"<lastmod>2026-08-13</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n"
        )
        if f"/{geo}/droniq/landing.html" in text:
            continue
        marker = f"https://spotspectrum.com/{geo}/hypertrimmer/landing.html"
        idx = text.find(marker)
        if idx != -1:
            # insert after the closing </url> of that line
            line_end = text.find("\n", idx)
            text = text[: line_end + 1] + entry + text[line_end + 1 :]
        else:
            text = text.replace("</urlset>", entry + "</urlset>")
    path.write_text(text, encoding="utf-8")
    print("Updated sitemap.xml")


# Load remaining language packs (mutates COPY).
exec(
    Path(__file__).with_name("_droniq_copy_rest.py").read_text(encoding="utf-8"),
    {"COPY": COPY},
)


def main() -> None:
    created = []
    for cfg in GEOS:
        geo = cfg["geo"]
        if geo not in COPY:
            raise SystemExit(f"Missing COPY for geo={geo}")
        t = COPY[geo]
        out_dir = ROOT / geo / "droniq"
        out_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "landing.html": build_landing(cfg, t),
            "thank-you.html": build_thank_you(cfg, t),
            "index.html": build_index(cfg, t),
        }
        for name, content in files.items():
            p = out_dir / name
            p.write_text(content, encoding="utf-8")
            created.append(str(p.relative_to(ROOT)))
            print(f"Wrote {p.relative_to(ROOT)}")
    update_hreflang_file(ROOT / "en/droniq/landing.html")
    update_hreflang_file(ROOT / "it/droniq/landing.html")
    update_sitemap()
    print("\nDone. Files:")
    for c in created:
        print(" ", c)


if __name__ == "__main__":
    main()
