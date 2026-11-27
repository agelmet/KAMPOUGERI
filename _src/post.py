import re,sys
p=sys.argv[1]+'/privacy.html';s=open(p).read()
s=s.replace('24 Σεπτεμβρίου 2026','27 Νοεμβρίου 2026').replace('24 September 2026','27 November 2026')
el='''<h2>4. Φόρμα παραγγελίας και δήλωση ενδιαφέροντος</h2><p>Όταν στέλνετε παραγγελία από το eshop, τα στοιχεία που συμπληρώνετε (ονοματεπώνυμο, τηλέφωνο, e-mail, διεύθυνση αποστολής, επιλογές παράδοσης και πληρωμής, σημειώσεις) και τα προϊόντα του καλαθιού αποστέλλονται, μέσω υπηρεσίας αποστολής e-mail, στο e-mail του υπευθύνου, αποκλειστικά για την εκτέλεση της παραγγελίας. Η ιστοσελίδα δεν δέχεται πληρωμές με κάρτα και δεν αποθηκεύει τα στοιχεία σας. Νομική βάση: η εκτέλεση της σύμβασης πώλησης (άρθρο 6 παρ. 1 β΄ ΓΚΠΔ) και οι φορολογικές υποχρεώσεις για το παραστατικό (άρθρο 6 παρ. 1 γ΄). Το καλάθι κρατιέται μόνο στο πρόγραμμα περιήγησής σας. Η δήλωση ενδιαφέροντος για την εκπαίδευση δεν περνά από την ιστοσελίδα: ανοίγει το δικό σας e-mail ή το WhatsApp με το μήνυμα έτοιμο.</p>'''
en='''<h2>4. Order form and expression of interest</h2><p>When you send an order from the eshop, the details you enter (name, phone, e-mail, delivery address, delivery and payment choices, notes) and the products in your basket are sent through an e-mail delivery service to the controller's e-mail, only to fulfil the order. The website accepts no card payments and does not store your details. Legal basis: performance of the sales contract (Art. 6(1)(b) GDPR) and tax obligations for the receipt (Art. 6(1)(c)). The basket is kept only in your browser. The expression of interest for the training does not go through the website: it opens your own e-mail or WhatsApp with the message ready.</p>'''
n1=len(re.findall(r'<h2>4\.',s))
s=re.sub(r'<h2>4\. Φόρμα επικοινωνίας</h2>.*?(?=<h2>5\.)',el,s,count=1,flags=re.S)
s=re.sub(r'<h2>4\. Contact form</h2>.*?(?=<h2>5\.)',en,s,count=1,flags=re.S)
assert 'Φόρμα παραγγελίας' in s and 'Order form' in s, 'patch failed'
s=s.replace('Google Maps, κοινωνικά δίκτυα','WhatsApp, κοινωνικά δίκτυα').replace('Google Maps, social networks','WhatsApp, social networks')
open(p,'w').write(s);print('privacy patched',n1)
