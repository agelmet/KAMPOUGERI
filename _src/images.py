from PIL import Image, ImageOps, ImageEnhance
import os
R='/home/claude/kmat/raw/';O='/home/claude/kb/site/assets/img/'
os.makedirs(O,exist_ok=True)
P='katerina-kampougeri-body-noesis-'
def save(src,name,widths,crop=None,q=78,enh=True):
    im=ImageOps.exif_transpose(Image.open(R+src)).convert('RGB')
    if crop: W,H=im.size;im=im.crop((int(crop[0]*W),int(crop[1]*H),int(crop[2]*W),int(crop[3]*H)))
    if enh: im=ImageEnhance.Contrast(im).enhance(1.04)
    out=[]
    for w in widths:
        w2=min(w,im.width);h=round(im.height*w2/im.width);t=im.resize((w2,h),Image.LANCZOS)
        fn=f"{P}{name}-{w2}.webp";t.save(O+fn,'WEBP',quality=q,method=6);out.append((fn,w2,h,os.path.getsize(O+fn)))
    return out
J={}
J['hero']=save('20-DSC01153-1.jpg','paralia-maxilari',[960,1600,2200],q=72)
J['studio']=save('17-katerina-kampougeri.jpg','studio',[600,1000])
J['stretch']=save('15-36200268_10156721246666614_3488034114647359488_n.jpg','diatasi',[600,1000])
J['selfie']=save('16-278608899_498128128324405_5951346031117720567_n.jpg','portraito',[500,900])
J['abs']=save('10-katerina-kampogeri-with-pillow.jpg','koiliakoi-maxilari',[700,1080])
J['patent']=save('00-.webp','pistopoiisi-eyresitexnias-obi',[700,1400],q=80,enh=False)
J['sylvia']=save('06-Sylvia-small-e1673593802595.webp','sylvia-lampe',[503],enh=False)
J['olga']=save('04-olga-lazara.jpg','olga-lazara',[280],enh=False)
# products
for key,src in [('board0','29-bodynoesis-sanida_700.webp'),('board1','30-bodynoesis-sanida-1_700.webp'),('board2','31-bodynoesis-sanida-2_700.webp'),('board3','32-bodynoesis-sanida-3_700.webp'),('board4','33-bodynoesis-sanida-4_700.webp'),('board5','34-bodynoesis-sanida-5_700.webp'),('board6','35-bodynoesis-sanida-6_700.webp'),('board7','36-bodynoesis-sanida-7_700.webp'),
 ('seatmain','21-seat.jpg'),('seat1','38-bodynoesis-seat-1_700.webp'),('seat2','39-bodynoesis-seat-2_700.webp'),('seat3','40-bodynoesis-seat-3_700.webp'),
 ('pillowmain','22-pillow.jpg'),('pillow0','41-bodynoesis-pillow_700.webp'),('pillow1','42-bodynoesis-pillow-1_700.webp'),('pillow4','44-bodynoesis-pillow-4_700.webp'),('pillow5','45-bodynoesis-pillow-5_700.webp'),('pillow2','43-bodynoesis-pillow-2_700.webp')]:
    nm={'board':'sanida-eythygrammisis','seat':'kathisma-seat','pillow':'maxilari-pillow'}[ [k for k in ('board','seat','pillow') if key.startswith(k)][0] ]
    J[key]=save(src,nm+'-'+key[-1] if not key.endswith('main') else nm,[700,1200] if key.endswith('main') else [700],q=76)
import json;json.dump(J,open('/home/claude/kb/src/img.json','w'),indent=0)
tot=0
for k,v in J.items():
    print(k,[(a,b,c,d//1024) for a,b,c,d in v]);tot+=sum(x[3] for x in v)
print('total KB',tot//1024)
