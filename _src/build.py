# -*- coding: utf-8 -*-
"""KAMPOUGERI — Body Noesis® by Katerina Kampougeri. Builds site/index.html, site/arthro-*.html, site/oroi.html.
Skeleton: split hero (text | beach photo) · proof strip · ACADEMY (who / format / syllabus / route / certificate preview /
trainers / fee / enquiry) · method with scroll-straightened spine (signature) · ticker · sessions · eshop (cart → e-mail
order, no card) · reviews rotation · about with sticky portrait · articles · FAQ + at a glance · contact band · footer.
Opening «Ευθυγράμμιση»: vertebrae line up, butterfly appears, the page opens in seven bands."""
import json, os, re, html, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import SYL, TICK, PRODUCTS, REVIEWS, ARTS, ICONS, FAQ
S = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(S, '..', 'site')
DOMAIN = 'bodynoesis.com'
J = json.load(open(os.path.join(S, 'img.json')))
BF = open(os.path.join(S, 'butterfly.d')).read(); BFVB = open(os.path.join(S, 'butterfly.vb')).read()
E = lambda s: html.escape(s, quote=True)

def srcset(k):
    v = [x for x in J[k] if os.path.exists(os.path.join(OUT, 'assets/img', x[0]))]
    return v
def IMG(k, sizes, alt, alten, cls='', eager=''):
    v = srcset(k); big = v[-1]; mid = v[min(1, len(v) - 1)] if len(v) > 1 else v[0]
    ss = ', '.join(f'assets/img/{f} {w}w' for f, w, h, b in v)
    a = (f'loading="eager" fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"')
    c = f' class="{cls}"' if cls else ''
    return (f'<img{c} src="assets/img/{mid[0]}" srcset="{ss}" sizes="{sizes}" width="{mid[1]}" height="{mid[2]}" '
            f'alt="{E(alt)}" data-en-alt="{E(alten)}" {a}>')
def imgmacro(m):
    p = m.group(1).split('|') + [''] * 6
    return IMG(p[0].strip(), p[1], p[2], p[3], p[4], p[5])
FLAG_GR = '<svg viewBox="0 0 27 18" preserveAspectRatio="xMidYMid slice"><rect width="27" height="18" fill="#0D5EAF"/><g fill="#fff"><rect y="2" width="27" height="2"/><rect y="6" width="27" height="2"/><rect y="10" width="27" height="2"/><rect y="14" width="27" height="2"/></g><rect width="10" height="10" fill="#0D5EAF"/><rect x="4" width="2" height="10" fill="#fff"/><rect y="4" width="10" height="2" fill="#fff"/></svg>'
FLAG_EN = '<svg viewBox="0 0 60 30" preserveAspectRatio="xMidYMid slice"><clipPath id="ukc"><path d="M0 0v30h60V0z"/></clipPath><g clip-path="url(#ukc)"><path d="M0 0v30h60V0z" fill="#012169"/><path d="M0 0l60 30m0-30L0 30" stroke="#fff" stroke-width="6"/><path d="M0 0l60 30m0-30L0 30" stroke="#C8102E" stroke-width="4"/><path d="M30 0v30M0 15h60" stroke="#fff" stroke-width="10"/><path d="M30 0v30M0 15h60" stroke="#C8102E" stroke-width="6"/></g></svg>'
FLAGS = (f'<button type="button" data-l="el" aria-pressed="true" aria-label="Ελληνικά"><span class="fl">{FLAG_GR}</span></button>'
         f'<button type="button" data-l="en" aria-pressed="false" aria-label="English"><span class="fl">{FLAG_EN}</span></button>')

def products():
    out = []; tpl = []
    for n, p in enumerate(PRODUCTS):
        rev = ' flip' if n % 2 else ''
        imgs = ''.join(IMG(k, '(max-width:1000px) 100vw, 50vw', p['name'][0] + f' — φωτογραφία {i+1}', p['name'][1] + f' — photo {i+1}', 'on' if i == 0 else '').replace('<img', f'<img data-big="assets/img/{srcset(k)[-1][0]}"', 1) for i, k in enumerate(p['gal']))
        th = ''.join(f'<button type="button" aria-pressed="{"true" if i == 0 else "false"}" aria-label="Φωτογραφία {i+1}" data-en-aria="Photo {i+1}"><img src="assets/img/{J[k+'_th'][0][0]}" alt="" aria-hidden="true" width="64" height="64" loading="lazy"></button>' for i, k in enumerate(p['gal']))
        price = f'<b class="num">{p["price"]}€</b>' + (f'<s class="num">{p["old"]}€</s>' if p['old'] else '') + '<small data-en="incl. VAT · shipping extra">με ΦΠΑ · + μεταφορικά</small>'
        pts = ''.join(f'<li data-en="{E(b)}">{a}</li>' for a, b in p['pts'])
        out.append(f'''<article class="prod{rev}" data-id="{p['id']}" id="p-{p['id']}">
 <div class="pgal rv"><div class="pmain">{imgs}<button type="button" aria-label="Μεγέθυνση" data-en-aria="Enlarge"></button></div><div class="pthumbs">{th}</div></div>
 <div class="pinfo rv"><span class="pat"><svg viewBox="{BFVB}" width="16" height="16" aria-hidden="true"><use href="#bf"/></svg><span data-en="Patent · OBI">Ευρεσιτεχνία · ΟΒΙ</span></span>
  <h3 data-en="{E(p['name'][1])}">{p['name'][0]}</h3><div class="pp">{price}</div>
  <p class="lead" data-en="{E(p['lead'][1])}">{p['lead'][0]}</p><ul class="pts">{pts}</ul>
  <p class="dims" data-en="{E(p['dims'][1])}">{p['dims'][0]}</p>
  <div class="buy"><span class="qty" role="group" aria-label="Ποσότητα" data-en-aria="Quantity"><button type="button" data-v="-1" aria-label="Λιγότερα" data-en-aria="Fewer">−</button><output>1</output><button type="button" data-v="1" aria-label="Περισσότερα" data-en-aria="More">+</button></span>
  <button class="btn rasp" type="button" data-add data-en="Add to basket">Στο καλάθι</button><button class="more" type="button" data-more data-en="Full description">Πλήρης περιγραφή</button></div>
 </div>
</article>''')
        gal = ''.join(f'<button type="button" aria-label="Φωτογραφία" data-s="assets/img/{srcset(k)[-1][0]}" aria-pressed="{"true" if i == 0 else "false"}"><img src="assets/img/{J[k+'_th'][0][0]}" alt="" aria-hidden="true" width="58" height="58" loading="lazy"></button>' for i, k in enumerate(p['gal']))
        desc = ''.join(f'<p data-en="{E(b)}">{a}</p>' for a, b in p['desc'])
        tpl.append(f'''<template id="pd-{p['id']}"><h3 id="pmT" data-en="{E(p['name'][1])}">{p['name'][0]}</h3><div class="pmg"><div><img src="assets/img/{srcset(p['gal'][0])[-1][0]}" alt="{E(p['name'][0])}" width="700" height="700"><div class="pmt">{gal}</div></div>
<div class="desc"><div class="pp" style="display:flex;gap:12px;align-items:baseline;margin-bottom:12px"><b class="num" style="font:500 40px/1 var(--fd);color:var(--rasp)">{p['price']}€</b>{f'<s class="num">{p["old"]}€</s>' if p['old'] else ''}</div>{desc}<p class="dims" style="color:var(--mut);font-size:14px" data-en="{E(p['dims'][1])}">{p['dims'][0]}</p>
<p style="font-size:14px;color:var(--mut)" data-en="Registered patent with the Hellenic Industrial Property Organisation — copying is prohibited.">Καταχωρημένη ευρεσιτεχνία στον ΟΒΙ — η αντιγραφή απαγορεύεται.</p>
<button class="btn rasp" type="button" data-add data-en="Add to basket">Στο καλάθι</button></div></div></template>''')
    data = [dict(id=p['id'], el=p['name'][0], en=p['name'][1], price=p['price'], thumb='assets/img/' + J[p['gal'][0]+'_th'][0][0]) for p in PRODUCTS]
    return '\n'.join(out) + '\n' + '\n'.join(tpl) + f'\n<script type="application/json" id="bn-products">{json.dumps(data, ensure_ascii=False)}</script>'

def reviews():
    names = ''; qs = ''
    for i, (n, pro, el, en) in enumerate(REVIEWS):
        tag = ('<small data-en="Physiotherapist">Φυσικοθεραπεύτρια</small>' if pro else '')
        names += f'<li role="presentation"><button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="rq{i}" id="rt{i}">{n}{tag}<i class="pb"></i></button></li>'
        star = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2.5l2.9 6.2 6.8.8-5 4.6 1.3 6.7L12 17.5l-6 3.3 1.3-6.7-5-4.6 6.8-.8z"/></svg>'
        protag = '<span class="pro" data-en="Health professional">Επαγγελματίας υγείας</span>' if pro else ''
        qs += f'<figure id="rq{i}" role="tabpanel" aria-labelledby="rt{i}" class="{"on" if i == 0 else ""}"><div class="stars" aria-label="5/5">{star*5}</div><blockquote data-en="{E(en)}">{el}</blockquote><figcaption>{n}{protag}</figcaption></figure>'
    return names, qs

def arts():
    return ''.join(f'<a class="ac" href="arthro-{s}.html"><svg viewBox="0 0 64 64" aria-hidden="true">{ICONS[ic]}</svg><h3>{t}</h3><p>{sh}</p><span class="rd" data-en="Read the article (Greek) →">Διαβάστε το άρθρο →</span></a>' for s, t, sh, dt, ic, ps in ARTS)

def faq():
    return ''.join(f'<details><summary><span data-en="{E(qe)}">{q}</span><i aria-hidden="true"></i></summary><div class="an"><p data-en="{E(ae)}">{a}</p></div></details>' for q, qe, a, ae in FAQ)

def jsonld():
    base = f'https://{DOMAIN}/'
    img = base + 'assets/img/' + J['hero'][1][0]
    org = {"@type": "HealthClub", "@id": base + "#org", "name": "Body Noesis® by Katerina Kampougeri",
           "alternateName": ["Body Noesis", "Κατερίνα Καμπουγέρη Body Noesis", "bodynoesis.com"], "url": base, "image": img,
           "logo": base + "assets/icons/icon-512.png", "telephone": "+30 693 676 3840", "email": "info@bodynoesis.com",
           "description": "Ολιστική μέθοδος θεραπευτικής άσκησης Body Noesis® της Κατερίνας Καμπουγέρη: εκπαίδευση και πιστοποίηση επαγγελματιών υγείας, ατομικά και μίνι γκρουπ μαθήματα online και live, προϊόντα ευρεσιτεχνίας για την ευθυγράμμιση της σπονδυλικής στήλης.",
           "areaServed": [{"@type": "Country", "name": "Ελλάδα"}, "Online"], "availableLanguage": ["el", "en", "es"],
           "founder": {"@id": base + "#katerina"}, "priceRange": "€€",
           "knowsAbout": ["Body Noesis", "θεραπευτική άσκηση", "πυελικό έδαφος", "ευθυγράμμιση σπονδυλικής στήλης", "αποκατάσταση τραυματισμών", "εκπαίδευση γυμναστών", "πιστοποίηση εκπαιδευτών άσκησης", "body mindfulness"],
           "sameAs": ["https://www.facebook.com/katerinakampougeri1", "https://www.instagram.com/callaneticsgreece/"]}
    person = {"@type": "Person", "@id": base + "#katerina", "name": "Κατερίνα Καμπουγέρη", "alternateName": ["Katerina Kampougeri", "Kampougeri Katerina"],
              "jobTitle": "Body Noesis® εκπαιδεύτρια και δημιουργός της μεθόδου, Καθηγήτρια Φυσικής Αγωγής", "image": base + 'assets/img/' + J['selfie'][1][0],
              "worksFor": {"@id": base + "#org"}, "knowsLanguage": ["el", "en"],
              "alumniOf": [{"@type": "CollegeOrUniversity", "name": "ΤΕΦΑΑ Αθηνών (ΕΚΠΑ)"}, {"@type": "CollegeOrUniversity", "name": "University of Essex"}],
              "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": "MSc Management of Musculoskeletal Conditions"}, {"@type": "EducationalOccupationalCredential", "name": "Certificate International Organization Physio Pilates"}],
              "sameAs": ["https://www.facebook.com/katerinakampougeri1"]}
    course = {"@type": "Course", "@id": base + "#course", "name": "Εκπαίδευση & Πιστοποίηση Body Noesis® για επαγγελματίες υγείας",
              "description": "50 ώρες (40 ώρες εκπαίδευσης και 10 ώρες πρακτικής) στη μέθοδο Body Noesis®: θεμελιώδεις αρχές, πλήρες ασκησιολόγιο, πυελικό έδαφος, κινησιολογία, προσαρμογές ανά επίπεδο, αποκατάσταση τραυματισμών, πρακτική διόρθωση με τα χέρια. Πιστοποίηση και δυνατότητα διδασκαλίας της μεθόδου.",
              "provider": {"@id": base + "#org"}, "inLanguage": ["el", "en", "es"], "educationalCredentialAwarded": "Πιστοποίηση εκπαιδευτή Body Noesis®",
              "hasCourseInstance": [{"@type": "CourseInstance", "courseMode": "online", "courseWorkload": "PT50H"}, {"@type": "CourseInstance", "courseMode": "onsite", "courseWorkload": "PT50H"}],
              "offers": {"@type": "Offer", "price": "1000", "priceCurrency": "EUR", "category": "Paid"}}
    prods = [{"@type": "Product", "@id": base + "#p-" + p['id'], "name": p['name'][0], "description": p['lead'][0], "image": base + 'assets/img/' + srcset(p['gal'][0])[-1][0],
              "brand": {"@type": "Brand", "name": "Body Noesis"}, "offers": {"@type": "Offer", "price": str(p['price']), "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": base + "#p-" + p['id'], "seller": {"@id": base + "#org"}}} for p in PRODUCTS]
    site = {"@type": "WebSite", "@id": base + "#website", "url": base, "name": "Body Noesis®", "alternateName": ["Body Noesis by Katerina Kampougeri", "Κατερίνα Καμπουγέρη", "bodynoesis.com"], "inLanguage": ["el", "en"], "publisher": {"@id": base + "#org"}}
    fq = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, qe, a, ae in FAQ]}
    return json.dumps({"@context": "https://schema.org", "@graph": [org, person, course, *prods, site, fq]}, ensure_ascii=False)

FONTS = open(os.path.join(S, 'fonts.css')).read()
CSS = open(os.path.join(S, 'style.css')).read()
def minjs(src):
    t = '/home/claude/tools/node_modules/.bin/terser'
    if os.path.exists(t):
        return subprocess.run([t, '-c', '-m'], input=src, capture_output=True, text=True, check=True).stdout
    return src
JS = minjs(open(os.path.join(S, 'script.js')).read())
SYM = f'<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="bf" viewBox="{BFVB}"><path fill="currentColor" fill-rule="evenodd" d="{BF}"/></symbol></svg>'
TITLE = 'Body Noesis® εκπαίδευση & πιστοποίηση | Κατερίνα Καμπουγέρη'
DESC = 'Body Noesis® της Κατερίνας Καμπουγέρη: εκπαίδευση & πιστοποίηση για γυμναστές, φυσικοθεραπευτές & επαγγελματίες υγείας, μαθήματα online & live, eshop.'
INTRO_JS = "<script>(function(){var h=document.documentElement;h.classList.add('js');try{if(!sessionStorage.getItem('bn-in')&&!matchMedia('(prefers-reduced-motion:reduce)').matches&&!document.hidden)h.classList.add('bn-intro')}catch(e){}})()</script>"

def head(title, desc, canon_path='', extra=''):
    return f'''<!DOCTYPE html>
<html lang="el">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0B2326">
<meta name="color-scheme" content="light only">
<meta property="og:type" content="website"><meta property="og:locale" content="el_GR"><meta property="og:locale:alternate" content="en_GB">
<meta property="og:site_name" content="Body Noesis®">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="assets/img/{J['hero'][1][0]}"><meta property="og:image:width" content="1600"><meta property="og:image:height" content="1200">
<meta name="twitter:card" content="summary_large_image">
{INTRO_JS}
<link rel="preload" href="assets/fonts/eb-garamond-greek-500.woff2" as="font" type="font/woff2" crossorigin>
<style id="advon-fonts">{FONTS}</style>
<style>{CSS}</style>
{extra}
</head>'''

def build_index():
    b = open(os.path.join(S, 'body.html')).read()
    names, qs = reviews()
    tick = ''.join(f'<span data-en="{E(en)}">{el}</span>' for el, en in TICK)
    syl = ''.join(f'<li data-en="{E(en)}">{el}</li>' for el, en in SYL)
    rep = {'{{BFVB}}': BFVB, '{{FLAGS}}': FLAGS, '{{SYL}}': syl, '{{SYLN}}': str(len(SYL)), '{{TICK}}': tick, '{{PRODUCTS}}': products(),
           '{{RNAMES}}': names, '{{RQUOTES}}': qs, '{{ARTS}}': arts(), '{{FAQ}}': faq(), '{{PATENTL}}': 'assets/img/' + J['patent'][-1][0]}
    for k, v in rep.items(): b = b.replace(k, v)
    b = re.sub(r'\{\{IMG ([^}]+)\}\}', imgmacro, b)
    assert '{{' not in b, re.findall(r'\{\{[^}]+\}\}', b)[:3]
    h = head(TITLE, DESC, extra=f'<link rel="preload" as="image" href="assets/img/{J["hero"][1][0]}" imagesrcset="{", ".join(f"assets/img/{f} {w}w" for f, w, hh, bb in J["hero"])}" imagesizes="(max-width:1000px) 100vw, 56vw" fetchpriority="high">\n<script type="application/ld+json">{jsonld()}</script>')
    out = h + '\n<body>\n' + SYM + '\n' + b + f'\n<script>{JS}</script>\n</body>\n</html>\n'
    open(os.path.join(OUT, 'index.html'), 'w').write(out)

ART_CSS = '''.ah{padding:150px 0 64px;background:var(--deep);color:#EDE7DC;position:relative;overflow:clip}.ah .bfw{position:absolute;right:-4%;top:50%;width:min(44vw,620px);transform:translateY(-50%);color:#7CC8CC;opacity:.07;pointer-events:none}
.ah .g2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(32px,5vw,110px);align-items:end;position:relative}
.ah .bc{font-size:13px;color:#9FB3B1}.ah .bc a{text-decoration:none}.ah h1{font:500 clamp(40px,4.6vw,80px)/1.03 var(--fd);margin-top:20px;text-wrap:balance}
.ah .ld{font:400 clamp(19px,1.45vw,24px)/1.5 var(--fd);color:#E3DCCF;max-width:46ch;margin:0}.ah .mt{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:22px;font-size:14px;color:#B9C6C4}.ah .mt span{display:flex;align-items:center;gap:8px}.ah .mt span::before{content:"";width:6px;height:6px;border-radius:50%;background:#7CC8CC}
.ab2{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:clamp(32px,5vw,110px);padding:clamp(56px,6vw,96px) 0 clamp(64px,7vw,110px);align-items:start}
.ab2 .tx p{font-size:19px;line-height:1.75;color:#24383b;max-width:68ch;text-wrap:pretty}.ab2 .tx p:first-child::first-letter{float:left;font:500 82px/.8 var(--fd);color:var(--teal);margin:8px 12px 0 0}
.ab2 .tx .dis{font-size:14px;color:var(--mut);margin-top:30px;padding-top:18px;border-top:1px solid var(--line)}
.ab2 aside{position:sticky;top:100px;display:grid;gap:14px}
.ab2 .au{display:flex;gap:16px;align-items:center;padding:22px;border-radius:24px;border:1px solid var(--line);background:var(--paper)}.ab2 .au svg{width:54px;height:54px;flex:none;color:var(--teal)}.ab2 .au b{display:block;font:500 22px/1.15 var(--fd)}.ab2 .au span{font-size:13.5px;color:var(--mut);line-height:1.45;display:block;margin-top:4px}
.ab2 .cta{padding:28px;border-radius:24px;background:var(--deep);color:#EDE7DC}.ab2 .cta b{display:block;font:500 28px/1.15 var(--fd)}.ab2 .cta p{font-size:15px;color:#B9C6C4;margin:10px 0 20px}.ab2 .cta .tl{color:#EDE7DC}
.ab2 .ol{padding:22px 24px;border-radius:24px;border:1px solid var(--line)}.ab2 .ol h2{font:600 12px/1 var(--fb);letter-spacing:.16em;text-transform:uppercase;color:var(--tealt);margin:0 0 6px}.ab2 .ol a{display:flex;justify-content:space-between;gap:14px;padding:13px 0;border-bottom:1px solid var(--line);text-decoration:none;font:500 19px/1.25 var(--fd)}.ab2 .ol a:last-child{border-bottom:0}.ab2 .ol a i{font-style:normal;color:var(--teal);transition:transform .3s var(--ease)}
@media (hover:hover){.ab2 .ol a:hover i{transform:translateX(4px)}}
@media (max-width:1000px){.ah .g2,.ab2{grid-template-columns:1fr}.ab2 aside{position:static}.ah{padding:120px 0 48px}}
.more2{border-top:1px solid var(--line);padding:60px 0 90px}.more2 .ag{margin-top:24px}.hd{color:var(--ink)}.hd::before{opacity:1}.hd .wm b{color:var(--teal)}'''
def build_articles():
    hdr = f'''<header class="hd solid" id="hd"><div class="wrap"><a href="index.html" class="brand" aria-label="Body Noesis — αρχική"><svg viewBox="{BFVB}" aria-hidden="true"><use href="#bf"/></svg><span class="wm"><b>BODY NOESIS</b><i>MIND YOUR BODY</i></span></a>
<nav class="nav" aria-label="Κύριο μενού"><a href="index.html#akadimia">Εκπαίδευση &amp; Πιστοποίηση</a><a href="index.html#methodos">Η μέθοδος</a><a href="index.html#mathimata">Μαθήματα</a><a href="index.html#eshop">Eshop</a><a href="index.html#katerina">Η Κατερίνα</a><a href="index.html#arthra" class="cur" aria-current="page">Άρθρα</a><a href="index.html#epikoinonia">Επικοινωνία</a></nav>
<div class="hdr"><a class="btn" href="index.html#akadimia" style="min-height:44px;padding:0 18px;font-size:14px">Εκπαίδευση</a></div></div></header>'''
    ftr = f'''<footer class="ft"><div class="wrap"><div class="ft-b" style="margin-top:0"><span>© 2026 Body Noesis® · Κατερίνα Καμπουγέρη · <a href="tel:+306936763840">693 676 3840</a> · <a href="mailto:info@bodynoesis.com">info@bodynoesis.com</a></span><span><a href="https://advonmedia.com" target="_blank" rel="noopener" style="text-decoration:none">Designed by <b class="adv">Advon Media</b></a></span></div></div></footer>'''
    for s, t, sh, dt, ic, ps in ARTS:
        others = [a for a in ARTS if a[0] != s][:3]
        oc = ''.join(f'<a class="ac" href="arthro-{o[0]}.html"><svg viewBox="0 0 64 64" aria-hidden="true">{ICONS[o[4]]}</svg><h3>{o[1]}</h3><p>{o[2]}</p><span class="rd">Διαβάστε →</span></a>' for o in others)
        url = f'https://{DOMAIN}/arthro-{s}.html'
        ld = json.dumps({"@context": "https://schema.org", "@graph": [
            {"@type": "BlogPosting", "headline": t, "description": sh, "datePublished": dt, "dateModified": dt, "inLanguage": "el", "mainEntityOfPage": url,
             "author": {"@type": "Person", "name": "Κατερίνα Καμπουγέρη", "url": f"https://{DOMAIN}/#katerina"}, "publisher": {"@type": "Organization", "name": "Body Noesis®", "url": f"https://{DOMAIN}/"}},
            {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Αρχική", "item": f"https://{DOMAIN}/"}, {"@type": "ListItem", "position": 2, "name": "Άρθρα", "item": f"https://{DOMAIN}/#arthra"}, {"@type": "ListItem", "position": 3, "name": t, "item": url}]}]}, ensure_ascii=False)
        body = ''.join(f'<p>{p}</p>' for p in ps)
        page = head(f'{t} | Κατερίνα Καμπουγέρη', sh[:155], extra=f'<style>{ART_CSS}</style><script type="application/ld+json">{ld}</script>').replace(' preload', ' preload', 1)
        page = page.replace('<html lang="el">', '<html lang="el">')
        mins = max(1, round(sum(len(p.split()) for p in ps)/190))
        ol = ''.join(f'<a href="arthro-{o[0]}.html">{o[1]}<i aria-hidden="true">→</i></a>' for o in [a for a in ARTS if a[0] != s][3:7])
        doc = page + f'\n<body>\n{SYM}\n{hdr}\n<main><section class="ah"><svg class="bfw" viewBox="{BFVB}" aria-hidden="true"><use href="#bf"/></svg><div class="wrap g2"><div><p class="bc"><a href="index.html">Αρχική</a> · <a href="index.html#arthra">Άρθρα</a></p><h1>{t}</h1></div><div><p class="ld">{sh}</p><p class="mt"><span>Κατερίνα Καμπουγέρη</span><span><time datetime="{dt}">13 Δεκεμβρίου 2022</time></span><span>{mins} λεπτ{"ό" if mins==1 else "ά"} ανάγνωσης</span></p></div></div></section>\n<div class="wrap ab2"><article class="tx">{body}<p class="dis">Το άρθρο έχει ενημερωτικό χαρακτήρα και δεν αντικαθιστά τη διάγνωση από ιατρό.</p></article><aside aria-label="Σχετικά"><div class="au"><svg viewBox="{BFVB}" aria-hidden="true"><use href="#bf"/></svg><div><b>Κατερίνα Καμπουγέρη</b><span>Καθηγήτρια Φυσικής Αγωγής, MSc · δημιουργός της μεθόδου Body Noesis®</span></div></div><div class="cta"><b>Θέλετε να το δοκιμάσετε — ή να το διδάξετε;</b><p>Μαθήματα για όλους, online και live· εκπαίδευση και πιστοποίηση για επαγγελματίες υγείας.</p><a class="btn" href="index.html#mathimata">Μαθήματα</a> <a class="tl" href="index.html#akadimia" style="margin-left:16px">Εκπαίδευση &amp; πιστοποίηση <span>→</span></a></div><nav class="ol" aria-label="Περισσότερα άρθρα"><h2>Περισσότερα άρθρα</h2>{ol}</nav></aside></div>\n<section class="more2"><div class="wrap"><span class="kick">Διαβάστε επίσης</span><div class="ag in">{oc}</div></div></section></main>\n{ftr}\n</body>\n</html>\n'
        doc = doc.replace("h.classList.add('bn-intro')", "0")
        open(os.path.join(OUT, f'arthro-{s}.html'), 'w').write(doc)

def build_terms():
    tx = '''<h1>Όροι παραγγελιών</h1><p class="by">Body Noesis® · Κατερίνα Καμπουγέρη · ενημέρωση: Νοέμβριος 2026</p>
<h2>1. Πώς γίνεται η παραγγελία</h2><p>Η παραγγελία από την ιστοσελίδα είναι αίτημα αγοράς: στέλνεται με e-mail στην Κατερίνα Καμπουγέρη, η οποία επικοινωνεί μαζί σας για να επιβεβαιώσει διαθεσιμότητα, κόστος αποστολής και στοιχεία πληρωμής. Η αγορά ολοκληρώνεται μετά την επιβεβαίωση.</p>
<h2>2. Τιμές</h2><p>Οι τιμές των προϊόντων είναι σε ευρώ και περιλαμβάνουν ΦΠΑ. Τα μεταφορικά δεν περιλαμβάνονται και σας γνωστοποιούνται πριν από την πληρωμή.</p>
<h2>3. Πληρωμή</h2><p>Με τραπεζική κατάθεση ή με αντικαταβολή. Στην ιστοσελίδα δεν γίνεται καμία πληρωμή με κάρτα και δεν αποθηκεύονται στοιχεία πληρωμής.</p>
<h2>4. Αποστολή & παραλαβή</h2><p>Με courier σε όλη την Ελλάδα ή παραλαβή κατόπιν συνεννόησης. Ο χρόνος παράδοσης σας γνωστοποιείται με την επιβεβαίωση της παραγγελίας.</p>
<h2>5. Δικαίωμα υπαναχώρησης</h2><p>Ως καταναλωτής έχετε δικαίωμα να υπαναχωρήσετε από την αγορά εντός 14 ημερών από την παραλαβή, χωρίς αιτιολογία (ν. 2251/1994). Ενημερώστε μας με e-mail ή τηλεφωνικά· το προϊόν επιστρέφεται αχρησιμοποίητο, στην αρχική του κατάσταση, και τα έξοδα επιστροφής βαρύνουν τον αγοραστή εκτός αν το προϊόν είναι ελαττωματικό.</p>
<h2>6. Επικοινωνία</h2><p>Τηλέφωνο <a href="tel:+306936763840">693 676 3840</a> · e-mail <a href="mailto:info@bodynoesis.com">info@bodynoesis.com</a>.</p>
<h2 lang="en">Order terms (English summary)</h2><p lang="en">Orders on this website are purchase requests sent by e-mail; we confirm availability, shipping cost and payment details before the sale is completed. Prices include VAT, shipping is extra. Payment by bank transfer or cash on delivery — no card payment on the website. Consumers may withdraw within 14 days of delivery.</p>'''
    css = '.lg{padding:140px 0 90px}.lg .in{max-width:70ch}.lg h1{font:500 clamp(40px,5vw,70px)/1.05 var(--fd)}.lg h2{font:500 26px/1.2 var(--fd);margin:34px 0 10px}.lg p{color:#33484b}.lg .by{color:var(--mut);font-size:14px}.hd{color:var(--ink)}.hd::before{opacity:1}.hd .wm b{color:var(--teal)}'
    page = head('Όροι παραγγελιών | Body Noesis®', 'Όροι παραγγελιών του eshop Body Noesis®: πώς γίνεται η παραγγελία, τιμές, πληρωμή με κατάθεση ή αντικαταβολή, αποστολή και υπαναχώρηση.', extra=f'<style>{css}</style>')
    doc = page + f'\n<body>\n{SYM}\n<header class="hd solid"><div class="wrap"><a href="index.html" class="brand" aria-label="Body Noesis — αρχική"><svg viewBox="{BFVB}" aria-hidden="true"><use href="#bf"/></svg><span class="wm"><b>BODY NOESIS</b><i>MIND YOUR BODY</i></span></a></div></header>\n<main class="lg"><div class="wrap"><div class="in">{tx}</div></div></main>\n<footer class="ft"><div class="wrap"><div class="ft-b" style="margin-top:0"><span>© 2026 Body Noesis®</span><span><a href="https://advonmedia.com" target="_blank" rel="noopener" style="text-decoration:none">Designed by <b class="adv">Advon Media</b></a></span></div></div></footer>\n</body>\n</html>\n'
    doc = doc.replace("h.classList.add('bn-intro')", "0")
    open(os.path.join(OUT, 'oroi.html'), 'w').write(doc)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    build_index(); build_articles(); build_terms()
    open(os.path.join(OUT, '.nojekyll'), 'w').close()
    open(os.path.join(OUT, '_redirects'), 'w').write('\n'.join([
        '/katerina-kampougeri/  /#katerina  301', '/body-noesis/  /#methodos  301', '/programata-bodynoesis/  /#akadimia  301', '/programata-bodynoesis  /#akadimia  301',
        '/body-noesis-articles/  /#arthra  301', '/epikinonia/  /#epikoinonia  301', '/store/  /#eshop  301', '/my-account/  /#eshop  301',
        '/product/body-noesis-pillow/  /#p-pillow  301', '/product/body-noesis-seat/  /#p-seat  301', '/product/body-noesis-sanida/  /#p-sanida  301', '']))
    print('built', os.listdir(OUT))
