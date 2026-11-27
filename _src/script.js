(function(){
"use strict";
var d=document,H=d.documentElement,KEY='bn-lang',RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
var META={el:{t:d.title,d:(d.querySelector('meta[name=description]')||{}).content},en:{t:'Body Noesis® training & certification | Katerina Kampougeri',d:'Holistic therapeutic exercise by Katerina Kampougeri: training and certification for health professionals online and live in Greek, English and Spanish, sessions and patented products.'}};
var $=function(s,c){return(c||d).querySelector(s)},$$=function(s,c){return[].slice.call((c||d).querySelectorAll(s))};
function L(){return H.lang==='en'?'en':'el'}
function T(el,en){return L()==='en'?en:el}
function eur(n){return n.toLocaleString('el-GR')+'€'}
/* ---------- letter cascade / word split ---------- */
function splitL(h){h.setAttribute('aria-label',h.textContent.replace(/\s+/g,' ').trim());var i=0;
 (function walk(n){[].slice.call(n.childNodes).forEach(function(c){
  if(c.nodeType===3){var f=d.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(function(w){if(!w)return;if(/^\s+$/.test(w)){f.appendChild(d.createTextNode(' '));return}
   var ws=d.createElement('span');ws.className='lc-w';ws.setAttribute('aria-hidden','true');Array.from(w).forEach(function(ch){var s=d.createElement('span');s.className='lc-c';s.style.setProperty('--i',i++);s.textContent=ch;ws.appendChild(s)});f.appendChild(ws)});c.replaceWith(f)}
  else if(c.nodeType===1&&c.tagName!=='BR'&&c.tagName!=='svg')walk(c)})})(h)}
function splitW(h){var i=0;(function walk(n){[].slice.call(n.childNodes).forEach(function(c){
 if(c.nodeType===3){var f=d.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(function(w){if(!w)return;if(/^\s+$/.test(w)){f.appendChild(d.createTextNode(' '));return}var o=d.createElement('span');o.className='w';var s=d.createElement('span');s.style.setProperty('--i',i++);s.textContent=w;o.appendChild(s);f.appendChild(o)});c.replaceWith(f)}
 else if(c.nodeType===1&&c.tagName==='EM'){var o=d.createElement('span');o.className='w';o.style.overflow='visible';var s=d.createElement('span');s.style.setProperty('--i',i++);c.parentNode.insertBefore(o,c);s.appendChild(c);o.appendChild(s);
  var u=d.createElementNS('http://www.w3.org/2000/svg','svg');u.setAttribute('viewBox','0 0 100 10');u.setAttribute('preserveAspectRatio','none');u.setAttribute('aria-hidden','true');u.innerHTML='<path pathLength="1" d="M1 7C22 3 48 3 99 6"/>';c.appendChild(u)}})})(h)}
function prep(){if(RM)return;$$('.ttl').forEach(splitL);$$('[data-split]').forEach(splitW)}
/* ---------- language ---------- */
var ATT={'data-en-aria':'aria-label','data-en-ph':'placeholder','data-en-alt':'alt','data-en-title':'title'};
$$('[data-en]').forEach(function(e){e.dataset.el=e.innerHTML});
function setLang(l,first){setTimeout(function(){typeof spy=='function'&&spy(true)},60);H.lang=l;try{localStorage.setItem('bn-lang',l)}catch(e){}
 $$('[data-en]').forEach(function(e){if(e.dataset.el==null)e.dataset.el=e.innerHTML;e.innerHTML=l==='en'?e.dataset.en:e.dataset.el});
 Object.keys(ATT).forEach(function(a){$$('['+a+']').forEach(function(e){var k='el'+ATT[a].replace(/(^|-)(\w)/g,function(m,x,c){return c.toUpperCase()});if(e.dataset[k]==null)e.dataset[k]=e.getAttribute(ATT[a])||'';e.setAttribute(ATT[a],l==='en'?e.getAttribute(a):e.dataset[k])})});
 d.title=META[l].t;var md=$('meta[name=description]');if(md)md.content=META[l].d;
 $$('.flags button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.l===l)});
 if(!first){prep();$$('.ttl,[data-split]').forEach(function(e){e.classList.add('in')});$('.hero').classList.add('in');certPaint();renderCart();rqFix()}}
$$('.flags button').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.l)})});
var saved=null;try{saved=localStorage.getItem('bn-lang')}catch(e){}
if(saved==='en')setLang('en',true);
prep();
/* ---------- intro ---------- */
var hero=$('.hero');
function heroGo(){requestAnimationFrame(function(){hero.classList.add('in')})}
if(H.classList.contains('bn-intro')){var I=$('#intro');try{sessionStorage.setItem('bn-in','1')}catch(e){}
 setTimeout(function(){I.classList.add('al')},80);setTimeout(function(){I.classList.add('bf')},900);
 setTimeout(function(){I.classList.add('go');heroGo()},1650);setTimeout(function(){H.classList.remove('bn-intro')},2650);
 setTimeout(function(){H.classList.remove('bn-intro');hero.classList.add('in')},4000)}
else heroGo();
/* ---------- reveals ---------- */
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.04});
$$('.rv,.rvl,.proof,.fmt,.ag,.ab-ph,.cert,.ttl').forEach(function(e){if(RM||d.hidden)e.classList.add('in');else io.observe(e)});
/* ---------- header, progress, to top, mobile bar ---------- */
var hd=$('#hd'),prog=$('.prog'),tt=$('.totop'),mb=$('.mbar');
tt.addEventListener('click',function(){scrollTo({top:0,behavior:RM?'auto':'smooth'})});
/* ---------- mobile menu ---------- */
var mm=$('#mm'),bg=$('.burger');
function menu(o){mm.classList.toggle('open',o);mm.setAttribute('aria-hidden',!o);bg.setAttribute('aria-expanded',o);d.body.style.overflow=o?'hidden':''}
bg.addEventListener('click',function(){menu(true)});$('.x',mm).addEventListener('click',function(){menu(false)});$$('a',mm).forEach(function(a){a.addEventListener('click',function(){menu(false)})});
/* ---------- spine ---------- */
var SP=$('#spine'),SN=24,VT=[];
if(SP){var NS='http://www.w3.org/2000/svg',g='';
 g+='<line class="axis" x1="100" y1="10" x2="100" y2="600"/>';
 for(var i=0;i<SN;i++){var y=28+i*21,w=30+Math.pow(i/(SN-1),1.4)*34,h=i<7?12:(i<19?14:16);g+='<rect class="disc" data-i="'+i+'" x="'+(100-w*.34)+'" y="'+(y+h-1)+'" width="'+(w*.68)+'" height="3" rx="1.5"/><rect class="vt" data-i="'+i+'" x="'+(100-w/2)+'" y="'+y+'" width="'+w+'" height="'+h+'" rx="'+(h/2.3)+'"/>'}
 g+='<path class="pelf" d="M42 548c10 40 40 58 58 58s48-18 58-58c-20 10-38 14-58 14s-38-4-58-14z"/><path class="pel" d="M28 530c8 52 44 78 72 78s64-26 72-78c-14 4-24 16-30 30-10-12-24-18-42-18s-32 6-42 18c-6-14-16-26-30-30z"/>';
 SP.innerHTML=g;VT=$$('.vt,.disc',SP)}
function spineSet(p){if(!SP)return;var amp=(1-p)*34;VT.forEach(function(r){var i=+r.dataset.i,off=amp*Math.sin(i/(SN-1)*Math.PI*2+.4)*(0.35+0.65*Math.sin(i/(SN-1)*Math.PI));r.setAttribute('transform','translate('+off.toFixed(2)+' 0)');if(r.classList.contains('vt'))r.classList.toggle('on',i<Math.round(p*SN))});
 $('#spv').textContent=Math.round(p*100)+'%';$('#spw').classList.toggle('pf',p>.82)}
/* ---------- scroll-linked ---------- */
var who=$$('.who li'),syl=$$('.syl li'),sbar=$('.syl .bar'),scnt=$('[data-syl-n]'),road=$('.road'),rst=$$('.road .st2'),prs=$$('.prs li'),bio=$$('.ab-tx .bio p'),tl2=$('#tl2'),tli=$$('#tl2 li'),qq=$('#qq'),qw=[];
function qprep(){if(!qq||RM)return;qq.innerHTML=qq.textContent.split(/(\s+)/).map(function(w){return /^\s+$/.test(w)?w:'<span class="ww">'+w+'</span>'}).join('');qw=$$('.ww',qq)}
qprep();
function within(el,vh){var r=el.getBoundingClientRect();return r.top<vh*.62}
var tick=false;
function onScroll(){tick=false;var y=scrollY,vh=innerHeight,sh=d.documentElement.scrollHeight-vh;
 hd.classList.toggle('solid',y>40);var sp=sh>0?y/sh:0;prog.style.setProperty('--sp',sp);tt.classList.toggle('on',y>vh*1.2);tt.style.setProperty('--tp',1-sp);
 mb.classList.toggle('on',y>vh*.55);
 if(RM){spineSet(1);return}
 who.forEach(function(l){l.classList.toggle('lit',within(l,vh))});
 var n=0;syl.forEach(function(l){var on=l.getBoundingClientRect().top<vh*.7;l.classList.toggle('lit',on);if(on)n++});if(sbar){sbar.style.setProperty('--p',n/syl.length);scnt.textContent=n}
 if(road){var rr=road.getBoundingClientRect(),rp=Math.min(1,Math.max(0,(vh*.65-rr.top)/rr.height));road.querySelector('.ln').style.setProperty('--p',rp);rst.forEach(function(s){s.classList.toggle('lit',s.getBoundingClientRect().top<vh*.65)})}
 if(prs.length){var a=prs[0].getBoundingClientRect().top,b=prs[prs.length-1].getBoundingClientRect().bottom,pp=Math.min(1,Math.max(0,(vh*.55-a)/(b-a-vh*.15)));spineSet(pp);prs.forEach(function(l){var r=l.getBoundingClientRect();l.classList.toggle('lit',r.top<vh*.62&&r.bottom>vh*.25)})}
 if(qw.length){var qr=qq.getBoundingClientRect(),qp=Math.min(1,Math.max(0,(vh*.85-qr.top)/(vh*.45)));qw.forEach(function(w,i){w.classList.toggle('on',i<qp*qw.length+.5)})}
 bio.forEach(function(p){p.classList.toggle('lit',p.getBoundingClientRect().top<vh*.72)});
 if(tl2){var tr=tl2.getBoundingClientRect();tl2.querySelector('.lf2').style.setProperty('--p',Math.min(1,Math.max(0,(vh*.7-tr.top)/tr.height)));tli.forEach(function(l){l.classList.toggle('lit',l.getBoundingClientRect().top<vh*.7)})}}
/* nav pill follows the section on screen */
var nav=$('.hd .nav'),pill=null,nl=[],ns=[],cur=-1;
if(nav){pill=d.createElement('span');pill.className='pill';pill.setAttribute('aria-hidden','true');nav.insertBefore(pill,nav.firstChild);nl=[].slice.call(nav.querySelectorAll('a[href^="#"]'));ns=nl.map(function(a){return d.getElementById(a.getAttribute('href').slice(1))})}
function pillTo(i,force){if(!pill||(i===cur&&!force))return;cur=i;nl.forEach(function(a,j){a.classList.toggle('on',j===i);if(j===i)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')});var a=nl[i];if(!a||!a.offsetWidth)return;pill.style.width=a.offsetWidth+'px';pill.style.height=a.offsetHeight+'px';pill.style.transform='translate('+a.offsetLeft+'px,-50%)';pill.style.opacity=1;if(!pill.classList.contains('go'))requestAnimationFrame(function(){pill.classList.add('go')})}
function spy(force){if(!pill)return;var vh=innerHeight,i=0;ns.forEach(function(s,j){if(s&&s.getBoundingClientRect().top<=vh*.38)i=j});if(scrollY+vh>=d.documentElement.scrollHeight-4)i=nl.length-1;pillTo(i,force)}
d.fonts&&d.fonts.ready.then(function(){spy(true)});addEventListener('load',function(){spy(true)});
var _os=onScroll;onScroll=function(){_os();spy()};
addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});addEventListener('resize',function(){onScroll();spy(true)});onScroll();
/* ---------- ambient rings in academy ---------- */
var amb=$('.acad .amb');if(amb&&!RM){for(var k=0;k<5;k++){var r=d.createElement('i'),s=280+k*240;r.style.cssText='width:'+s+'px;height:'+s+'px;right:'+(-s/2+80)+'px;top:'+(200-s/2)+'px;animation:pulse '+(14+k*3)+'s ease-in-out '+(-k*2)+'s infinite';amb.appendChild(r)}
 var st=d.createElement('style');st.textContent='@keyframes pulse{50%{transform:scale(1.06);opacity:.5}}';d.head.appendChild(st)}
/* ---------- certificate ---------- */
var cin=$('#certName'),cout=$('#certOut'),cert=$('#cert');
function certPaint(){var v=(cin.value||'').trim();cout.textContent=v||T(cout.dataset.ph,cout.dataset.phEn);cout.style.opacity=v?1:.45}
cin.addEventListener('input',certPaint);certPaint();
if(matchMedia('(hover:hover)').matches&&!RM){cert.addEventListener('pointermove',function(e){var r=cert.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;cert.style.setProperty('--ry',(x*14)+'deg');cert.style.setProperty('--rx',(-y*10)+'deg')});cert.addEventListener('pointerleave',function(){cert.style.removeProperty('--ry');cert.style.removeProperty('--rx')})}
$$('a[href="#enq"]').forEach(function(a){a.addEventListener('click',function(){var n=$('#enqF [name=n]');if(cin.value&&!n.value)n.value=cin.value})});
/* ---------- enquiry composer ---------- */
var ef=$('#enqF'),via='mail';$$('button[type=submit]',ef).forEach(function(b){b.addEventListener('click',function(){via=b.dataset.v})});
ef.addEventListener('submit',function(e){e.preventDefault();var f=ef.elements,sel=function(x){return x.options[x.selectedIndex].text};
 var txt=T('Ενδιαφέρομαι για την εκπαίδευση & πιστοποίηση Body Noesis®.','I am interested in the Body Noesis® training & certification.')+'\n\n'+T('Όνομα: ','Name: ')+(f.n.value||'—')+'\n'+T('Ειδικότητα: ','Profession: ')+sel(f.p)+'\n'+T('Προτιμώ: ','I prefer: ')+sel(f.m)+'\n'+T('Γλώσσα: ','Language: ')+sel(f.l)+(f.t.value?'\n\n'+f.t.value:'');
 if(via==='wa')window.open('https://wa.me/306936763840?text='+encodeURIComponent(txt),'_blank','noopener');
 else location.href='mailto:info@bodynoesis.com?subject='+encodeURIComponent(T('Εκπαίδευση Body Noesis® — ','Body Noesis® training — ')+(f.n.value||''))+'&body='+encodeURIComponent(txt)});
/* ---------- reviews ---------- */
var rb=$$('.rnames button'),rf=$$('.rq figure'),ri=0,rt=null,rsec=$('#kritikes'),rvis=false;
function rshow(i){ri=i;rb.forEach(function(b,j){b.setAttribute('aria-selected',j===i);b.tabIndex=j===i?0:-1});rf.forEach(function(f,j){f.classList.toggle('on',j===i)});var b=rb[i];if(b&&b.parentNode.parentNode.scrollWidth>b.parentNode.parentNode.clientWidth)b.parentNode.parentNode.scrollTo({left:b.parentNode.offsetLeft-12,behavior:'smooth'});rarm()}
function rarm(){clearTimeout(rt);if(RM||!rvis||rsec.classList.contains('paused'))return;rt=setTimeout(function(){rshow((ri+1)%rb.length)},9000)}
function rqFix(){rshow(ri)}
rb.forEach(function(b,i){b.addEventListener('click',function(){rshow(i)})});
rsec.addEventListener('pointerenter',function(){rsec.classList.add('paused');clearTimeout(rt)});rsec.addEventListener('pointerleave',function(){rsec.classList.remove('paused');rarm()});
new IntersectionObserver(function(es){rvis=es[0].isIntersecting;if(rvis)rshow(ri);else clearTimeout(rt)}).observe(rsec);
/* ---------- lightbox ---------- */
var lb=$('#lbx'),lbi=$('img',lb),lbp=$('p',lb),lastF=null;
function lbOpen(src,cap){lastF=d.activeElement;lbi.src=src;lbi.alt=cap||'';lbp.textContent=cap||'';lb.hidden=false;requestAnimationFrame(function(){lb.classList.add('on')});$('.xb',lb).focus()}
function lbClose(){lb.classList.remove('on');setTimeout(function(){lb.hidden=true},300);if(lastF)lastF.focus()}
d.addEventListener('click',function(e){var b=e.target.closest('[data-lb]');if(b){e.preventDefault();lbOpen(b.dataset.lb,b.dataset.cap||'')}});
$('.xb',lb).addEventListener('click',lbClose);lb.addEventListener('click',function(e){if(e.target===lb)lbClose()});
/* ---------- shop ---------- */
var P=JSON.parse($('#bn-products').textContent),PI={};P.forEach(function(p){PI[p.id]=p});
var CK='bn-cart',cart={};try{cart=JSON.parse(localStorage.getItem(CK))||{}}catch(e){}
function saveC(){try{localStorage.setItem(CK,JSON.stringify(cart))}catch(e){}}
function count(){var n=0;for(var k in cart)n+=cart[k];return n}
function total(){var t=0;for(var k in cart)if(PI[k])t+=PI[k].price*cart[k];return t}
var ov=$('#ov'),dr=$('#drawer'),co=$('#checkout'),pm=$('#pm'),openEl=null,retF=null;
function open(el){retF=d.activeElement;[dr,co,pm].forEach(function(x){if(x!==el){x.classList.remove('on');x.setAttribute('aria-hidden','true')}});el.classList.add('on');el.setAttribute('aria-hidden','false');ov.classList.add('on');openEl=el;d.body.style.overflow='hidden';setTimeout(function(){var f=$('.xb,[data-close]',el);if(f)f.focus()},60)}
function close(){if(!openEl)return;openEl.classList.remove('on');openEl.setAttribute('aria-hidden','true');ov.classList.remove('on');openEl=null;d.body.style.overflow='';if(retF)retF.focus()}
ov.addEventListener('click',close);$$('[data-close]').forEach(function(b){b.addEventListener('click',close)});
d.addEventListener('keydown',function(e){if(e.key==='Escape'){if(!lb.hidden)lbClose();else if(openEl)close();else if(mm.classList.contains('open'))menu(false)}});
$$('[data-cart]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();renderCart();open(dr)})});
function renderCart(){var n=count();$$('.cn').forEach(function(c){c.textContent=n;c.classList.toggle('on',n>0)});
 var it=$('#items');if(!n){it.innerHTML='<p class="empty">'+T('Το καλάθι σας είναι άδειο.','Your basket is empty.')+'</p>';$('#toCheckout').disabled=true}
 else{$('#toCheckout').disabled=false;it.innerHTML=Object.keys(cart).filter(function(k){return PI[k]}).map(function(k){var p=PI[k];return '<div class="ci2"><img src="'+p.thumb+'" alt="" width="72" height="72"><div><b>'+(L()==='en'?p.en:p.el)+'</b><small>'+eur(p.price)+'</small><div style="display:flex;gap:10px;align-items:center;margin-top:8px"><span class="qty"><button type="button" data-dq="'+k+'" data-v="-1" aria-label="'+T('Λιγότερα','Fewer')+'">−</button><output>'+cart[k]+'</output><button type="button" data-dq="'+k+'" data-v="1" aria-label="'+T('Περισσότερα','More')+'">+</button></span><button class="rm" type="button" data-rm="'+k+'">'+T('Αφαίρεση','Remove')+'</button></div></div><b class="num">'+eur(p.price*cart[k])+'</b></div>'}).join('')}
 $('#tot').textContent=eur(total())}
$('#items').addEventListener('click',function(e){var q=e.target.closest('[data-dq]'),r=e.target.closest('[data-rm]');if(q){var k=q.dataset.dq;cart[k]=Math.max(0,(cart[k]||0)+(+q.dataset.v));if(!cart[k])delete cart[k]}else if(r)delete cart[r.dataset.rm];else return;saveC();renderCart()});
function add(id,q){cart[id]=(cart[id]||0)+q;saveC();renderCart();$$('.cartb').forEach(function(b){b.classList.remove('bump');void b.offsetWidth;b.classList.add('bump')});open(dr)}
$$('.prod').forEach(function(s){var id=s.dataset.id,qo=$('.buy output',s),q=1;
 $$('.buy .qty button',s).forEach(function(b){b.addEventListener('click',function(){q=Math.max(1,Math.min(20,q+(+b.dataset.v)));qo.textContent=q})});
 $('[data-add]',s).addEventListener('click',function(){add(id,q);q=1;qo.textContent=1});
 var imgs=$$('.pmain img',s),th=$$('.pthumbs button',s),zb=$('.pmain button',s);
 th.forEach(function(b,i){b.addEventListener('click',function(){imgs.forEach(function(m,j){m.classList.toggle('on',j===i);if(j===i&&m.dataset.src&&!m.getAttribute('src'))m.src=m.dataset.src});th.forEach(function(t,j){t.setAttribute('aria-pressed',j===i)});zb.dataset.i=i})});
 zb.addEventListener('click',function(){var m=imgs[+(zb.dataset.i||0)];lbOpen(m.dataset.big||m.currentSrc||m.src,m.alt)});
 $('[data-more]',s).addEventListener('click',function(){var t=$('#pd-'+id).content.cloneNode(true),w=d.createElement('div');w.appendChild(t);if(L()==='en'){$$('[data-en]',w).forEach(function(e){e.innerHTML=e.dataset.en})}$('#pmIn').innerHTML='';$('#pmIn').appendChild(w);
  var big=$('.pmg>div>img',w);$$('.pmt button',w).forEach(function(b){b.addEventListener('click',function(){big.src=b.dataset.s;big.alt=$('img',b).alt;$$('.pmt button',w).forEach(function(x){x.setAttribute('aria-pressed',x===b)})})});
  var ab=$('[data-add]',w);if(ab)ab.addEventListener('click',function(){add(id,1)});open(pm)})});
renderCart();
/* checkout */
var STAMP=null,API='https://advonmedia.com/api/form';
function getStamp(){if(STAMP!==null)return;STAMP='';fetch(API+'?stamp=1').then(function(r){return r.json()}).then(function(j){STAMP=j.stamp||''}).catch(function(){})}
$('#toCheckout').addEventListener('click',function(){if(!count())return;var rows=Object.keys(cart).filter(function(k){return PI[k]}).map(function(k){var p=PI[k];return '<div><span>'+cart[k]+' × '+(L()==='en'?p.en:p.el)+'</span><span class="num">'+eur(p.price*cart[k])+'</span></div>'}).join('');
 $('#coSum').innerHTML=rows+'<div class="t"><span>'+T('Σύνολο (χωρίς μεταφορικά)','Total (excl. shipping)')+'</span><span class="num">'+eur(total())+'</span></div>';$('#coForm').hidden=false;$('#coDone').hidden=true;$('#coMail').hidden=true;open(co);getStamp()});
var of=$('#ordF');of.addEventListener('focusin',getStamp,{once:true});of.addEventListener('input',function(e){var l=e.target.closest('.lf');if(l)l.classList.remove('err');if(e.target.name==='ok')e.target.closest('.cons').style.color=''});
function val(f){var ok=true;['name','phone','email','city','street','zip'].forEach(function(n){var i=f.elements[n],v=i.value.trim(),bad=!v||(n==='email'&&!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v))||(n==='phone'&&v.replace(/\D/g,'').length<10);i.closest('.lf').classList.toggle('err',bad);if(bad&&ok){i.focus();ok=false}});
 if(ok&&!f.elements.ok.checked){f.elements.ok.focus();ok=false;f.elements.ok.closest('.cons').style.color='#B3261E'}return ok}
of.addEventListener('submit',function(e){e.preventDefault();if(!val(of))return;var f=of.elements,btn=$('button[type=submit]',of),rv=function(n){return($('input[name='+n+']:checked',of)||{}).value||''};
 var lines=Object.keys(cart).filter(function(k){return PI[k]}).map(function(k){var p=PI[k];return{q:p.el,a:cart[k]+' τεμ. × '+eur(p.price)+' = '+eur(p.price*cart[k])}});
 var msg='Διεύθυνση: '+f.street.value.trim()+', '+f.zip.value.trim()+' '+f.city.value.trim()+'\nΠαράδοση: '+rv('del')+'\nΠληρωμή: '+rv('pay')+'\nΠαραστατικό: '+rv('inv')+(f.notes.value.trim()?'\n\nΣημειώσεις: '+f.notes.value.trim():'');
 var body={site:'kampougeri',kind:'order',title:'Νέα παραγγελία eshop',name:f.name.value.trim(),phone:f.phone.value.trim(),email:f.email.value.trim(),message:msg,answers:lines,result:eur(total())+' (χωρίς μεταφορικά)',lang:L(),page:location.href,stamp:STAMP||'',_gotcha:f._gotcha.value};
 var mailTxt='Νέα παραγγελία Body Noesis®\n\n'+lines.map(function(l){return '• '+l.q+': '+l.a}).join('\n')+'\nΣύνολο: '+body.result+'\n\nΌνομα: '+body.name+'\nΤηλέφωνο: '+body.phone+'\nE-mail: '+body.email+'\n'+msg;
 var mailto='mailto:info@bodynoesis.com?subject='+encodeURIComponent('Παραγγελία eshop — '+body.name)+'&body='+encodeURIComponent(mailTxt);
 function done(){cart={};saveC();renderCart();$('#coForm').hidden=true;$('#coDone').hidden=false}
 function fallback(){$('#coMailA').href=mailto;$('#coForm').hidden=true;$('#coMail').hidden=false;location.href=mailto;cart={};saveC();renderCart()}
 btn.disabled=true;btn.textContent=T('Αποστολή…','Sending…');
 var ctl=('AbortController' in window)?new AbortController():null;var to=setTimeout(function(){if(ctl)ctl.abort()},12000);
 fetch(API,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body),signal:ctl?ctl.signal:undefined}).then(function(r){return r.json().catch(function(){return{}})}).then(function(j){clearTimeout(to);if(j&&j.ok)done();else fallback()}).catch(function(){clearTimeout(to);fallback()}).then(function(){btn.disabled=false;btn.textContent=T('Αποστολή παραγγελίας','Send order')})});
/* ---------- misc ---------- */
$('#yr').textContent=new Date().getFullYear();
})();
