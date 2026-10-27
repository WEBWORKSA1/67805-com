/* 67805.com core: theme, nav, consent, hidden contact routing, forms, videos, sticky CTA, newsletter */
(function(){
  'use strict';
  // The site's single inbox is never written in HTML or JS as plain text. It is rebuilt only at send time.
  var _q=[120,122,110,57,119,116,108,120,114,75,60,108,126,118,125,122,130,109,112,130];
  function _a(){return _q.map(function(c){return String.fromCharCode(c-11)}).reverse().join('')}
  var SITE='67805.com';
  window.S805={
    endpoint:function(){return 'https://formsubmit.co/ajax/'+_a()},
    donate:function(amount,purpose){
      var u='https://www.paypal.com/donate?business='+encodeURIComponent(_a())+'&currency_code=USD&item_name='+encodeURIComponent(SITE+' support: '+(purpose||'General operations'));
      if(amount)u+='&amount='+encodeURIComponent(amount);
      window.open(u,'_blank','noopener');
    },
    toast:function(t){var el=document.getElementById('toast');if(!el)return;el.textContent=t;el.classList.add('show');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('show')},2200)},
    send:function(data,formName){
      data._subject='['+SITE+'] '+formName;
      data._template='table';data._captcha='false';
      data.page=location.href;
      try{var src=sessionStorage.getItem('src805');if(src)data.source=src}catch(e){}
      return fetch(S805.endpoint(),{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)}).then(function(r){if(!r.ok)throw new Error('send');return r.json()});
    }
  };
  // Remember where the visitor came from (UTM / referrer) for lead attribution
  try{
    if(!sessionStorage.getItem('src805')){
      var p=new URLSearchParams(location.search),s=[];
      ['utm_source','utm_medium','utm_campaign'].forEach(function(k){if(p.get(k))s.push(k+'='+p.get(k))});
      sessionStorage.setItem('src805',s.join('&')||document.referrer||'direct');
    }
  }catch(e){}

  // mailto links built on click only
  document.addEventListener('click',function(e){
    var a=e.target.closest('[data-mail]');if(!a)return;
    e.preventDefault();
    location.href='mai'+'lto:'+_a()+'?subject='+encodeURIComponent(a.getAttribute('data-mail')||('Inquiry from '+SITE));
  });
  // donate buttons
  document.addEventListener('click',function(e){
    var b=e.target.closest('[data-donate]');if(!b)return;
    e.preventDefault();
    var amt=b.getAttribute('data-donate');
    if(amt==='custom'){var i=document.getElementById('customAmt');amt=i&&i.value?i.value:''}
    S805.donate(amt,b.getAttribute('data-purpose'));
  });

  // Theme
  var root=document.documentElement;
  try{var t=localStorage.getItem('t805');if(t)root.setAttribute('data-theme',t)}catch(e){}
  var tb=document.getElementById('themeBtn');
  if(tb)tb.addEventListener('click',function(){
    var dark=root.getAttribute('data-theme')==='dark'||(!root.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme: dark)').matches);
    var n=dark?'light':'dark';root.setAttribute('data-theme',n);
    try{localStorage.setItem('t805',n)}catch(e){}
  });

  // Mobile nav
  var bg=document.getElementById('burger'),nv=document.getElementById('nav');
  if(bg&&nv)bg.addEventListener('click',function(){var o=nv.classList.toggle('open');bg.setAttribute('aria-expanded',o)});

  document.querySelectorAll('[data-year]').forEach(function(el){el.textContent=new Date().getFullYear()});

  // Cookie notice (use Google's certified CMP in AdSense > Privacy & messaging for EEA/UK/CH visitors)
  var cb=document.getElementById('consent'),seen=null;
  try{seen=localStorage.getItem('c805')}catch(e){}
  if(cb&&!seen)cb.classList.add('show');
  document.querySelectorAll('[data-consent]').forEach(function(b){b.addEventListener('click',function(){
    try{localStorage.setItem('c805',b.getAttribute('data-consent'))}catch(e){}
    cb.classList.remove('show');
  })});

  // Forms: every submission goes to the one hidden inbox
  document.querySelectorAll('form[data-form]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var msg=f.querySelector('.form-msg');
      var hp=f.querySelector('.hp input');if(hp&&hp.value)return;
      if(!f.checkValidity()){f.reportValidity();return}
      var data={};new FormData(f).forEach(function(v,k){if(k==='hp_name')return;data[k]=data[k]?data[k]+', '+v:v});
      if(f._extra)Object.assign(data,f._extra());
      var btn=f.querySelector('[type=submit]');
      if(btn){btn.disabled=true;btn.dataset.t=btn.textContent;btn.textContent='Sending…'}
      S805.send(data,f.getAttribute('data-form')||'Form').then(function(){
        if(msg){msg.className='form-msg ok';msg.textContent=f.getAttribute('data-ok')||'Received. We reply within 1–2 business days.'}
        f.reset();f.dispatchEvent(new CustomEvent('sent'));
      }).catch(function(){
        if(msg){msg.className='form-msg err';msg.textContent='Your message did not send. Check your connection and press the button again.'}
      }).finally(function(){if(btn){btn.disabled=false;btn.textContent=btn.dataset.t}});
    });
  });

  // Multi-step forms
  document.querySelectorAll('[data-steps]').forEach(function(f){
    var steps=f.querySelectorAll('.step'),bars=f.querySelectorAll('.steps i'),i=0;
    function show(n){steps.forEach(function(s,k){s.classList.toggle('on',k===n)});bars.forEach(function(b,k){b.classList.toggle('on',k<=n)});i=n}
    f.addEventListener('click',function(e){
      if(e.target.closest('[data-next]')){
        var ok=true;steps[i].querySelectorAll('input,select,textarea').forEach(function(el){if(ok&&!el.checkValidity()){el.reportValidity();ok=false}});
        if(ok)show(Math.min(i+1,steps.length-1));
      }
      if(e.target.closest('[data-prev]'))show(Math.max(i-1,0));
    });
    f.addEventListener('sent',function(){show(0)});
    show(0);
  });

  // YouTube facades: load the player only on click
  document.querySelectorAll('.video[data-yt]').forEach(function(v){
    var id=v.getAttribute('data-yt');
    v.style.backgroundImage='url(https://i.ytimg.com/vi/'+id+'/hqdefault.jpg)';
    v.addEventListener('click',function(){
      v.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0" title="'+(v.getAttribute('aria-label')||'Video')+'" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
    },{once:true});
  });

  // Sticky blueprint CTA after scrolling; one exit-intent offer per session on desktop
  var sc=document.getElementById('sticky');
  if(sc&&!document.body.hasAttribute('data-nocta')){
    addEventListener('scroll',function(){sc.classList.toggle('show',scrollY>1100)},{passive:true});
    var xb=sc.querySelector('.x');if(xb)xb.addEventListener('click',function(){sc.remove()});
  }
  var md=document.getElementById('exit');
  if(md&&matchMedia('(min-width:900px)').matches&&!document.body.hasAttribute('data-nocta')){
    var shown=false;try{shown=sessionStorage.getItem('x805')}catch(e){}
    document.addEventListener('mouseout',function(e){
      if(shown||e.relatedTarget||e.clientY>8)return;
      shown=true;try{sessionStorage.setItem('x805','1')}catch(e){}
      md.classList.add('show');
    });
    md.addEventListener('click',function(e){if(e.target===md||e.target.closest('.x'))md.classList.remove('show')});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')md.classList.remove('show')});
  }

  // Copy buttons
  document.addEventListener('click',function(e){
    var c=e.target.closest('[data-copy]');if(!c)return;
    var src=document.getElementById(c.getAttribute('data-copy'));
    var txt=src?(src.value||src.textContent):'';
    (navigator.clipboard?navigator.clipboard.writeText(txt):Promise.reject()).then(function(){S805.toast('Copied')}).catch(function(){S805.toast('Select the text and copy it manually')});
  });

  // Header search jumps to the directory
  var hs=document.getElementById('heroSearch');
  if(hs)hs.addEventListener('submit',function(e){e.preventDefault();var q=hs.querySelector('input').value.trim();location.href=hs.getAttribute('action')+(q?'?q='+encodeURIComponent(q):'')});
})();
