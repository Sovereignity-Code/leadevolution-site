// Mobile nav
document.addEventListener('DOMContentLoaded',()=>{
  const hb=document.getElementById('hamburger');
  const mm=document.getElementById('mobile-menu');
  if(hb&&mm){hb.addEventListener('click',()=>mm.classList.toggle('open'))}

  // FAQ toggles
  document.querySelectorAll('.faq-q').forEach(q=>{
    q.addEventListener('click',()=>{
      const item=q.parentElement;
      const isOpen=item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i=>i.classList.remove('open'));
      if(!isOpen)item.classList.add('open');
    });
  });

  // Counter animation
  function animCount(id,target,suffix,duration){
    const el=document.getElementById(id);
    if(!el)return;
    let s=0;const step=target/(duration/16);
    const t=setInterval(()=>{s+=step;if(s>=target){s=target;clearInterval(t)}el.textContent=Math.floor(s).toLocaleString()+(suffix||'');},16);
  }
  setTimeout(()=>{
    animCount('c1',4200,'+',1400);
    animCount('c2',6,'',700);
    animCount('c3',2400,'+',1200);
    animCount('c4',94,'%',1000);
  },300);

  // Live ticker
  const ticker=document.getElementById('ticker-n');
  if(ticker)ticker.textContent=47+Math.floor(Math.random()*30);

  // ROI Calc
  const dealMap={mortgage:2400,financial:1800,solar:850,insurance:960,energy:400,commercial:8500};
  const cplMap={mortgage:150,financial:200,solar:100,insurance:140,energy:90,commercial:250};
  function calcROI(){
    const ind=document.getElementById('ci')?.value||'mortgage';
    const leads=parseInt(document.getElementById('cl')?.value)||0;
    const cpl=parseFloat(document.getElementById('cc')?.value)||0;
    const deal=parseFloat(document.getElementById('cd')?.value)||dealMap[ind];
    const le=65;
    const curr=leads*cpl;const leS=leads*le;const rev=leads*deal;
    const roi=leS>0?(((rev-leS)/leS)*100).toFixed(0):0;
    const save=Math.max(0,curr-leS);
    const set=(id,v)=>{const el=document.getElementById(id);if(el)el.textContent=v};
    set('rc','$'+curr.toLocaleString());
    set('rl','$'+leS.toLocaleString());
    set('rr','$'+rev.toLocaleString());
    set('roi',Number(roi).toLocaleString()+'%');
    set('rs','$'+save.toLocaleString());
  }
  document.getElementById('ci')?.addEventListener('change',function(){
    const i=this.value;
    const d=document.getElementById('cd');const c=document.getElementById('cc');
    if(d)d.value=dealMap[i];if(c)c.value=cplMap[i];
    calcROI();
  });
  ['cl','cc','cd'].forEach(id=>document.getElementById(id)?.addEventListener('input',calcROI));
  calcROI();

  // Contact form
  const cf=document.getElementById('contact-form');
  if(cf){
    cf.addEventListener('submit',async e=>{
      e.preventDefault();
      const btn=cf.querySelector('button[type=submit]');
      btn.textContent='Sending...';btn.disabled=true;
      try{
        const r=await fetch(cf.action,{method:'POST',body:new FormData(cf),headers:{Accept:'application/json'}});
        if(r.ok){document.getElementById('form-success').style.display='block';cf.style.display='none';}
        else{btn.textContent='Submit';btn.disabled=false;alert('Something went wrong. Please try again.');}
      }catch{btn.textContent='Submit';btn.disabled=false;}
    });
  }
});
