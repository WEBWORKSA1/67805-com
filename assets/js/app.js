/* 67805.com interactive tools: hero stack, directory, compare, stack builder, ROI estimator, readiness score, prompt library */
(function(){
  'use strict';
  var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
  var C=window.CATS||{},T=window.TOOLS||[];
  function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function money(n){return '$'+Math.round(n).toLocaleString('en-US')}
  function pick(cat,opt){
    opt=opt||{};
    var list=T.filter(function(t){return t.c===cat});
    if(opt.free)list=list.filter(function(t){return t.p!=='Paid'});
    if(opt.lvl!=null)list=list.filter(function(t){return t.l<=opt.lvl});
    list.sort(function(a,b){
      var sa=(opt.biz&&a.b.indexOf(opt.biz)>-1?2:0)+(a.f?1:0),sb=(opt.biz&&b.b.indexOf(opt.biz)>-1?2:0)+(b.f?1:0);
      return sb-sa;
    });
    return list;
  }
  var saved=[];try{saved=JSON.parse(localStorage.getItem('fav805')||'[]')}catch(e){}
  function saveFav(){try{localStorage.setItem('fav805',JSON.stringify(saved))}catch(e){}var el=$('#favCount');if(el)el.textContent=saved.length}

  /* ---------- Hero: build-a-stack ---------- */
  var hero=$('#heroStack');
  if(hero){
    var GOALS={support:'Answer customers faster',sales:'Find and follow up leads',write:'Write content and emails',mkt:'Grow on search and social',fin:'Cut bookkeeping and admin',auto:'Automate busywork',meet:'Run shorter meetings',design:'Make visuals and video'};
    var on={};
    var box=$('#heroGoals');
    Object.keys(GOALS).forEach(function(k){
      var b=document.createElement('button');b.type='button';b.className='goal';b.textContent=GOALS[k];b.setAttribute('aria-pressed','false');b.dataset.k=k;box.appendChild(b);
    });
    function render(){
      var html='<div class="layer base" style="--c:var(--ink)"><span class="tag">Base</span><div><strong>AI assistant</strong><br><small>Claude or ChatGPT for daily drafting and thinking</small></div><span class="hrs">+3 h</span></div>';
      var hrs=3;
      Object.keys(on).forEach(function(k){
        var t=pick(k)[0],c=C[k];hrs+=c.h;
        html+='<div class="layer" style="--c:'+c.c+'"><span class="tag">'+c.code+'</span><div><strong>'+esc(c.n)+'</strong><br><small>Start with '+esc(t.n)+'</small></div><span class="hrs">+'+c.h+' h</span></div>';
      });
      hero.innerHTML=html;
      $('#heroHrs').textContent=hrs;
      $('#heroVal').textContent=money(hrs*4.33*35);
      var link=$('#heroBuild');if(link)link.href='stack-builder.html?goals='+Object.keys(on).join(',');
    }
    box.addEventListener('click',function(e){
      var b=e.target.closest('.goal');if(!b)return;
      var k=b.dataset.k,p=b.getAttribute('aria-pressed')==='true';
      b.setAttribute('aria-pressed',String(!p));
      if(p)delete on[k];else on[k]=1;
      render();
    });
    ['support','auto'].forEach(function(k){on[k]=1;box.querySelector('[data-k="'+k+'"]').setAttribute('aria-pressed','true')});
    render();
  }

  /* ---------- Featured tools on home ---------- */
  var feat=$('#featuredTools');
  if(feat){feat.innerHTML=T.filter(function(t){return t.f}).slice(0,8).map(card).join('')}

  /* ---------- Category drawers ---------- */
  var drawers=$('#drawers');
  if(drawers){
    drawers.innerHTML=Object.keys(C).map(function(k){
      var n=T.filter(function(t){return t.c===k}).length;
      return '<a class="drawer" href="tools.html?cat='+k+'"><span class="code">'+C[k].code+'</span><h3>'+esc(C[k].n)+'</h3><p>'+esc(C[k].d)+'</p><p class="small mt" style="margin-top:8px">'+n+' tools</p></a>';
    }).join('');
  }
  var tc=$$('[data-toolcount]');tc.forEach(function(el){el.textContent=T.length});
  var cc=$$('[data-catcount]');cc.forEach(function(el){el.textContent=Object.keys(C).length});

  function card(t){
    var c=C[t.c],fav=saved.indexOf(t.n)>-1;
    return '<article class="tool'+(t.f?' featured':'')+'"><header><h3>'+esc(t.n)+'</h3><span class="tag">'+c.code+'</span></header>'+
      '<p>'+esc(t.d)+'</p><div class="row"><span class="tag">'+esc(c.n)+'</span><span class="tag mint">'+t.p+'</span>'+(t.f?'<span class="tag sig">Editors’ pick</span>':'')+'</div>'+
      '<div class="acts"><button class="vote" type="button" data-fav="'+esc(t.n)+'" aria-pressed="'+fav+'">'+(fav?'Saved':'Save')+'</button>'+
      '<label class="cmp"><input type="checkbox" data-cmp="'+esc(t.n)+'"> Compare</label>'+
      '<a class="btn sm ghost" href="'+t.u+'" target="_blank" rel="noopener nofollow" aria-label="Visit '+esc(t.n)+' website (opens in new tab)">Visit site</a></div></article>';
  }
  document.addEventListener('click',function(e){
    var b=e.target.closest('[data-fav]');if(!b)return;
    var n=b.getAttribute('data-fav'),i=saved.indexOf(n);
    if(i>-1)saved.splice(i,1);else saved.push(n);
    b.setAttribute('aria-pressed',String(i<0));b.textContent=i<0?'Saved':'Save';saveFav();
    if(window.S805)S805.toast(i<0?n+' added to your shortlist':n+' removed');
  });

  /* ---------- Directory ---------- */
  var dir=$('#directory');
  if(dir){
    var q=$('#fq'),cat=$('#fcat'),pr=$('#fprice'),so=$('#fsort'),cnt=$('#fcount'),cmpBar=$('#cmpBar'),sel=[];
    cat.innerHTML='<option value="">All categories</option>'+Object.keys(C).map(function(k){return '<option value="'+k+'">'+esc(C[k].n)+'</option>'}).join('')+'<option value="_saved">My shortlist</option>';
    var P=new URLSearchParams(location.search);
    if(P.get('q'))q.value=P.get('q');if(P.get('cat'))cat.value=P.get('cat');
    function run(){
      var s=q.value.trim().toLowerCase(),list=T.filter(function(t){
        if(cat.value==='_saved'){if(saved.indexOf(t.n)<0)return false}
        else if(cat.value&&t.c!==cat.value)return false;
        if(pr.value&&t.p!==pr.value)return false;
        if(s&&(t.n+' '+t.d+' '+C[t.c].n).toLowerCase().indexOf(s)<0)return false;
        return true;
      });
      if(so.value==='az')list.sort(function(a,b){return a.n.localeCompare(b.n)});
      else if(so.value==='free')list.sort(function(a,b){return (a.p==='Paid')-(b.p==='Paid')});
      else list.sort(function(a,b){return (b.f||0)-(a.f||0)});
      cnt.textContent=list.length+' of '+T.length+' tools';
      dir.innerHTML=list.length?list.map(card).join(''):'<div class="panel"><h3>No tools match those filters</h3><p>Clear the search box or pick “All categories”. Know a tool we should list? <a href="list-your-tool.html">Submit it here</a>.</p></div>';
      $$('[data-cmp]',dir).forEach(function(c){c.checked=sel.indexOf(c.getAttribute('data-cmp'))>-1});
      var u=new URL(location.href);u.search='';if(q.value)u.searchParams.set('q',q.value);if(cat.value)u.searchParams.set('cat',cat.value);history.replaceState(null,'',u);
    }
    [q,cat,pr,so].forEach(function(el){el.addEventListener('input',run)});
    dir.addEventListener('change',function(e){
      var c=e.target.closest('[data-cmp]');if(!c)return;
      var n=c.getAttribute('data-cmp'),i=sel.indexOf(n);
      if(c.checked&&i<0){if(sel.length>=3){c.checked=false;S805.toast('Compare up to 3 tools at a time');return}sel.push(n)}
      if(!c.checked&&i>-1)sel.splice(i,1);
      cmpBar.classList.toggle('show',sel.length>1);var gs=document.getElementById('sticky');if(gs&&sel.length>1)gs.remove();
      $('#cmpNames').textContent=sel.join(', ');
      $('#cmpGo').href='compare.html?t='+sel.map(encodeURIComponent).join('|');
    });
    run();saveFav();
  }

  /* ---------- Compare ---------- */
  var cmp=$('#compare');
  if(cmp){
    var sels=$$('select',cmp.parentNode).filter(function(s){return s.hasAttribute('data-slot')});
    var opts='<option value="">Choose a tool</option>'+Object.keys(C).map(function(k){
      return '<optgroup label="'+esc(C[k].n)+'">'+T.filter(function(t){return t.c===k}).map(function(t){return '<option>'+esc(t.n)+'</option>'}).join('')+'</optgroup>';
    }).join('');
    sels.forEach(function(s){s.innerHTML=opts});
    var pre=(new URLSearchParams(location.search).get('t')||'ChatGPT|Claude|Gemini').split('|');
    sels.forEach(function(s,i){if(pre[i])s.value=pre[i]});
    function draw(){
      var chosen=sels.map(function(s){return T.filter(function(t){return t.n===s.value})[0]}).filter(Boolean);
      if(!chosen.length){cmp.innerHTML='<p>Pick at least one tool above to see it here.</p>';return}
      var rows=[['Category',function(t){return C[t.c].n}],['Pricing model',function(t){return t.p}],['What it does',function(t){return t.d}],['Best for',function(t){return t.b.map(function(x){return BIZ[x]}).join(', ')}],['Skill needed',function(t){return ['No-code','Some setup','Technical'][t.l]}],['Est. hours saved per person / week',function(t){return C[t.c].h+' h (category average, our estimate)'}],['Website',function(t){return '<a href="'+t.u+'" target="_blank" rel="noopener nofollow">'+esc(t.u.replace(/^https?:\/\//,''))+'</a>'}]];
      cmp.innerHTML='<table><thead><tr><th scope="col">Feature</th>'+chosen.map(function(t){return '<th scope="col">'+esc(t.n)+'</th>'}).join('')+'</tr></thead><tbody>'+
        rows.map(function(r){return '<tr><th scope="row">'+r[0]+'</th>'+chosen.map(function(t){var v=r[1](t);return '<td>'+(r[0]==='Website'?v:esc(v))+'</td>'}).join('')+'</tr>'}).join('')+'</tbody></table>';
    }
    sels.forEach(function(s){s.addEventListener('change',draw)});draw();
  }

  /* ---------- Stack builder ---------- */
  var sb=$('#stackForm');
  if(sb){
    var gp=new URLSearchParams(location.search).get('goals');
    if(gp)gp.split(',').forEach(function(g){var i=sb.querySelector('input[name=goals][value="'+g+'"]');if(i)i.checked=true});
    var out=$('#stackOut'),last=null;
    sb.addEventListener('submit',function(e){
      e.preventDefault();
      var fd=new FormData(sb),goals=fd.getAll('goals');
      if(!goals.length){S805.toast('Pick at least one goal');return}
      var biz=fd.get('biz'),team=fd.get('team'),budget=fd.get('budget'),lvl=+fd.get('lvl'),rate=+fd.get('rate')||40;
      var tf={'1':1,'2-10':3,'11-50':8,'51+':15}[team]||1;
      var rows=[],hrs=3*tf;
      rows.push({cat:'AI assistant (base layer)',tools:'Claude or ChatGPT',why:'Every role uses it daily for drafting, summarizing and thinking out loud.',h:3*tf,p:'Freemium'});
      goals.forEach(function(g){
        var list=pick(g,{free:budget==='free',lvl:lvl,biz:biz}).slice(0,2);
        if(!list.length)list=pick(g).slice(0,1);
        var h=C[g].h*tf;hrs+=h;
        rows.push({cat:C[g].n,tools:list.map(function(t){return t.n}).join(' or '),why:list[0].d,h:h,p:list.map(function(t){return t.p}).filter(function(v,i,a){return a.indexOf(v)===i}).join(' / ')});
      });
      var month=hrs*4.33,val=month*rate;
      var spend={free:'$0',low:'up to $100',mid:'$100–500',high:'$500+'}[budget];
      out.innerHTML='<div class="result"><div class="sec-head" style="margin-bottom:10px"><div><p class="small mb0">Your estimated time back</p><div class="big">'+Math.round(month)+' hours / month</div></div><div><p class="small mb0">Worth at '+money(rate)+'/hour</p><div class="big" style="color:var(--cobalt)">'+money(val)+'</div></div></div>'+
        '<div class="tablewrap"><table><thead><tr><th>Layer</th><th>Start with</th><th>Why</th><th>Pricing</th><th>Hours / week</th></tr></thead><tbody>'+
        rows.map(function(r){return '<tr><td><strong>'+esc(r.cat)+'</strong></td><td>'+esc(r.tools)+'</td><td>'+esc(r.why)+'</td><td>'+esc(r.p)+'</td><td>'+r.h+'</td></tr>'}).join('')+'</tbody></table></div>'+
        '<p class="small">Monthly software budget you chose: '+spend+'. Hours are planning estimates based on category averages and your team size, not guarantees. Start with one layer, measure for 30 days, then add the next.</p>'+
        '<div class="cta" style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="blueprint.html?from=stack">Get this stack set up for me</a><button class="btn ghost" type="button" id="printStack">Print or save as PDF</button></div></div>';
      last={business:BIZ[biz],team:team,budget:spend,goals:goals.map(function(g){return C[g].n}).join(', '),stack:rows.map(function(r){return r.cat+': '+r.tools}).join(' | '),hours_month:Math.round(month)};
      try{sessionStorage.setItem('stack805',JSON.stringify(last))}catch(e){}
      $('#emailStack').classList.remove('hide');
      out.scrollIntoView({behavior:'smooth',block:'start'});
      $('#printStack').addEventListener('click',function(){print()});
    });
    var es=$('#emailStackForm');if(es)es._extra=function(){return last||{}};
  }
  var bp=$('#blueprintForm');
  if(bp){bp._extra=function(){var s=null;try{s=JSON.parse(sessionStorage.getItem('stack805'))}catch(e){}return s?{stack_builder_result:s.stack+' ('+s.hours_month+' h/month)'}:{}}}

  /* ---------- ROI estimator ---------- */
  var roi=$('#roiForm');
  if(roi){
    var P2=new URLSearchParams(location.search);
    $$('input',roi).forEach(function(i){if(P2.get(i.name))i.value=P2.get(i.name)});
    function calc(){
      var v={};$$('input',roi).forEach(function(i){v[i.name]=parseFloat(i.value)||0});
      $('#pctOut').textContent=v.pct+'%';
      var hrsMonth=v.people*v.hours*(v.pct/100)*4.33;
      var gross=hrsMonth*v.rate;
      var net=gross-v.tools;
      var setup=v.setup*v.rate+v.once;
      var payback=net>0?setup/net:Infinity;
      var year=net*12-setup;
      $('#rHours').textContent=Math.round(hrsMonth).toLocaleString();
      $('#rGross').textContent=money(gross);
      $('#rNet').textContent=money(net);
      $('#rPay').textContent=isFinite(payback)?(payback<1?'under 1 month':payback.toFixed(1)+' months'):'not at these numbers';
      $('#rYear').textContent=money(year);
      $('#rRoi').textContent=setup+v.tools*12>0?Math.round(year/(setup+v.tools*12)*100)+'%':'—';
      $('#rWork').textContent=v.people+' people × '+v.hours+' h/week × '+v.pct+'% automated × 4.33 weeks = '+Math.round(hrsMonth)+' h/month. '+Math.round(hrsMonth)+' h × '+money(v.rate)+' = '+money(gross)+' gross, minus '+money(v.tools)+' tools = '+money(net)+' net per month. Setup cost '+money(setup)+' ('+v.setup+' h × '+money(v.rate)+' + '+money(v.once)+' one-off).';
      var u=new URL(location.href);u.search='';$$('input',roi).forEach(function(i){u.searchParams.set(i.name,i.value)});$('#roiLink').value=u.toString();
    }
    roi.addEventListener('input',calc);calc();
  }

  /* ---------- Readiness score ---------- */
  var rs=$('#readyForm');
  if(rs){
    var lastScore=null;
    rs.addEventListener('submit',function(e){
      e.preventDefault();
      var fd=new FormData(rs),tot=0,n=0,weak=[];
      $$('fieldset[data-q]',rs).forEach(function(f){var v=+fd.get(f.getAttribute('data-q'));tot+=v;n++;if(v<=1)weak.push(f.getAttribute('data-area'))});
      if(n!==$$('fieldset[data-q]',rs).filter(function(f){return fd.get(f.getAttribute('data-q'))!==null}).length){S805.toast('Answer every question');return}
      var score=Math.round(tot/(n*3)*100);
      var lvl=score>=75?['Ready to scale','You have the data, habits and buy-in. Your gains now come from connecting tools into automated workflows.']:score>=45?['Ready to pilot','You can run one or two focused pilots now. Fix the weak areas below before rolling AI out team-wide.']:['Lay the groundwork','Start with an assistant for daily drafting and clean up where your data lives. Big automations will stall until then.'];
      lastScore={score:score,level:lvl[0],weak_areas:weak.join(', ')||'none'};
      $('#readyOut').innerHTML='<div class="result"><p class="small mb0">Your AI readiness score</p><div class="big">'+score+' / 100</div><h3 class="mt" style="margin-top:12px">'+lvl[0]+'</h3><p>'+lvl[1]+'</p>'+(weak.length?'<p><strong>Work on first:</strong> '+esc(weak.join(', '))+'.</p>':'<p><strong>No weak areas.</strong> Move to the automation guide.</p>')+'<p><a class="btn" href="blueprint.html?from=readiness">Get a free blueprint for my score</a></p></div>';
      $('#readyEmail').classList.remove('hide');
      $('#readyOut').scrollIntoView({behavior:'smooth',block:'start'});
    });
    var ref=$('#readyEmailForm');if(ref)ref._extra=function(){return lastScore||{}};
  }

  /* ---------- Prompt library ---------- */
  var pl=$('#prompts');
  if(pl&&window.PROMPTS){
    var pf=$('#pfilter'),groups={};
    window.PROMPTS.forEach(function(p){groups[p.g]=1});
    pf.innerHTML='<option value="">All teams</option>'+Object.keys(groups).map(function(g){return '<option>'+esc(g)+'</option>'}).join('');
    function drawP(){
      pl.innerHTML=window.PROMPTS.filter(function(p){return !pf.value||p.g===pf.value}).map(function(p,i){
        var id='pr'+i+p.t.length;
        return '<article class="prompt"><header class="sec-head" style="margin:0"><h3 class="mb0">'+esc(p.t)+'</h3><span class="tag">'+esc(p.g)+'</span></header><pre id="'+id+'">'+esc(p.x)+'</pre><button class="btn sm ghost" type="button" data-copy="'+id+'">Copy prompt</button></article>';
      }).join('');
    }
    pf.addEventListener('input',drawP);drawP();
  }
})();
