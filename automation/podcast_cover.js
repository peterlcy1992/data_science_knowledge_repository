#!/usr/bin/env node
/**
 * Generate a "Data Science in the Wild" episode cover tile (3000x3000 PNG),
 * following the mono-color editorial-print method: a neutral paper substrate,
 * two inks with assigned roles, halftone screening, one focal event, one manual
 * gesture, and a stylized company wordmark + monogram chip (an attribution
 * treatment — NOT a reproduction of any trademarked logo).
 *
 * Run with Playwright + Chromium available (present in the automation env):
 *   NODE_PATH=/opt/node22/lib/node_modules \
 *     node automation/podcast_cover.js \
 *       --company "LinkedIn" \
 *       --title "Feed SR" \
 *       --overline "Sequential Recommenders" \
 *       --subtitle "A transformer that reads 1,000 impressions." \
 *       --episode 3 \
 *       --out podcasts/2026-09-05-<id>.cover.png
 *
 * Optional: --accent-ink/--ink hex overrides, --mono "Li", --motif signal|sequence|loop
 * Defaults are derived from --company when not given, so minimal args still work.
 * Env: CHROMIUM_PATH to point at a specific Chromium if auto-detect fails.
 */
const fs = require('fs');
const path = require('path');

// ---- args ----
function parseArgs(argv){
  const a = {};
  for (let i = 2; i < argv.length; i++){
    const k = argv[i];
    if (k.startsWith('--')) { a[k.slice(2)] = (argv[i+1] && !argv[i+1].startsWith('--')) ? argv[++i] : true; }
  }
  return a;
}
const args = parseArgs(process.argv);
function need(name){ if (!args[name]) { console.error(`Missing required --${name}`); process.exit(2);} return args[name]; }

const company  = need('company');
const title    = need('title');
const out      = need('out');
const overline = args.overline || 'Data Science Deep Dive';
const subtitle = args.subtitle || '';
const episode  = args.episode ? `EP. ${String(args.episode).padStart(2,'0')}` : '';
const motif    = args.motif || 'signal';

// ---- palette: per-company where known, else deterministic from name ----
const PAPER = '#FAFAF7';
const PALETTES = [
  ['#2148B8','#C65F38'], // cobalt + terracotta
  ['#173AE3','#242321'], // electric blue + carbon
  ['#008A4B','#30343A'], // botanical green + charcoal
  ['#C83232','#30343A'], // signal red + charcoal
  ['#63365F','#C65F38'], // aubergine + terracotta
  ['#2058D4','#242321'], // royal blue + carbon
  ['#159DDA','#B64032'], // cyan + brick red
];
const KNOWN = {
  linkedin:['#173AE3','#242321'], shopify:['#008A4B','#30343A'], netflix:['#C83232','#30343A'],
  spotify:['#008A4B','#30343A'], uber:['#30343A','#159DDA'], meta:['#2148B8','#C65F38'],
  pinterest:['#C83232','#30343A'], airbnb:['#C83232','#30343A'], google:['#2148B8','#C65F38'],
  doordash:['#C83232','#30343A'], instacart:['#008A4B','#C65F38'], databricks:['#C83232','#30343A'],
  nvidia:['#008A4B','#30343A'], amazon:['#C65F38','#242321'], cvs:['#C83232','#30343A'],
  deepmind:['#2148B8','#C65F38'], booking:['#173AE3','#242321'],
};
function hashStr(s){ let h=0; for (const c of s) h=(h*31 + c.charCodeAt(0))>>>0; return h; }
const key = String(company).toLowerCase().replace(/[^a-z0-9]/g,'');
let [INK, ACC] = KNOWN[key] || PALETTES[hashStr(key) % PALETTES.length];
if (args.ink) INK = args.ink;
if (args['accent-ink']) ACC = args['accent-ink'];

// monogram: explicit, or first two alnum chars of the company (Title-cased)
let mono = args.mono;
if (!mono) { const m = String(company).replace(/[^A-Za-z0-9]/g,''); mono = (m[0]||'').toUpperCase() + (m[1]||'').toLowerCase(); }

const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const S = 1500;

// ---- deterministic PRNG ----
function makeRnd(seed){ return () => { seed=(seed*1103515245+12345)&0x7fffffff; return seed/0x7fffffff; }; }
const rnd = makeRnd(hashStr(company + '|' + title) || 12345);

function htRect(x0,y0,x1,y1,{step=15,r=2.9,jit=0.7,skip=0.12}={}){
  let s=''; for(let y=y0+step/2;y<y1;y+=step) for(let x=x0+step/2;x<x1;x+=step){
    if(rnd()<skip) continue; const rr=r+(rnd()-0.5)*jit; if(rr<0.5) continue;
    s+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${rr.toFixed(2)}"/>`; } return s;
}
function htBand(cx,cy,rin,rout,{step=17,r=2.8,jit=0.7,skip=0.18}={}){
  let s=''; for(let y=cy-rout;y<cy+rout;y+=step) for(let x=cx-rout;x<cx+rout;x+=step){
    const d=Math.hypot(x-cx,y-cy); if(d<rin||d>rout) continue; if(rnd()<skip) continue;
    const rr=r+(rnd()-0.5)*jit; if(rr<0.5) continue;
    s+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${rr.toFixed(2)}"/>`; } return s;
}

// ---- motifs (each returns an SVG fragment; footer sits in clear paper) ----
function motifSignal(){
  // a screened data-range that reads as both a line chart and a terrain ridge
  const pts=[[0,1090],[120,1035],[240,1075],[360,980],[470,1015],[590,905],[700,955],
    [820,875],[940,930],[1060,860],[1180,915],[1300,845],[1410,895],[1500,865]];
  const ry=x=>{ for(let i=0;i<pts.length-1;i++){const[a,b]=pts[i],[c,d]=pts[i+1];
    if(x>=a&&x<=c){const t=(x-a)/(c-a);return b+(d-b)*t;}} return pts[pts.length-1][1]; };
  let dots=''; const step=16;
  // paper knockout behind the bottom-left footer so it stays legible
  const inFoot=(x,y)=> x>=55 && x<=760 && y>=1352 && y<=1462;
  for(let y=step/2;y<S;y+=step) for(let x=step/2;x<S;x+=step){ const t=ry(x); if(y<t) continue;
    if(inFoot(x,y)) continue;
    const depth=(y-t)/(S-t); let r=0.7+depth*3.3; if(depth<0.24&&rnd()<(0.6-depth*1.7)) continue;
    r+=(rnd()-0.5)*0.7; if(r<0.55) continue; dots+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${r.toFixed(2)}"/>`; }
  let p=`M ${pts[0][0]} ${pts[0][1]}`; for(let i=1;i<pts.length;i++)p+=` L ${pts[i][0]} ${pts[i][1]}`;
  let nodes=''; pts.forEach(([x,y],i)=>{ if(i===0||i===pts.length-1)return; const hi=(i===9);
    nodes+=`<circle cx="${x}" cy="${y}" r="${hi?15:8}" fill="${PAPER}" stroke="${hi?ACC:INK}" stroke-width="${hi?7:5}"/>`; });
  const gx=pts[9][0],gy=pts[9][1];
  const g=`<path d="M ${gx-46} ${gy-8} C ${gx-52} ${gy-46}, ${gx+10} ${gy-58}, ${gx+40} ${gy-38} C ${gx+64} ${gy-22}, ${gx+56} ${gy+34}, ${gx+16} ${gy+44} C ${gx-24} ${gy+54}, ${gx-58} ${gy+28}, ${gx-48} ${gy+2}" fill="none" stroke="${ACC}" stroke-width="4.5" stroke-linecap="round" opacity="0.9"/>`;
  return `<g fill="${INK}">${dots}</g><path d="${p}" fill="none" stroke="${ACC}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>${nodes}${g}`;
}
function motifSequence(){
  const base=1170,x0=60,x1=1440,n=19,bw=24,gap=(x1-x0)/n; let bars='',dots=''; const tops=[];
  for(let i=0;i<n;i++){ const x=x0+i*gap+(gap-bw)/2; const h=70+Math.abs(Math.sin(i*1.3)+rnd()*0.9)*150;
    const ty=base-h; tops.push([x+bw/2,ty]); dots+=htRect(x,ty,x+bw,base,{step:12,r:2.6,jit:0.6,skip:0.1});
    bars+=`<rect x="${x}" y="${ty}" width="${bw}" height="${h}" fill="none" stroke="${INK}" stroke-width="2" opacity="0.35"/>`; }
  const last=tops[n-1]; let arcs='';
  [3,7,11,15].forEach(i=>{ const pp=tops[i]; const mx=(pp[0]+last[0])/2,my=Math.min(pp[1],last[1])-160;
    arcs+=`<path d="M ${pp[0]} ${pp[1]} Q ${mx} ${my} ${last[0]} ${last[1]-26}" fill="none" stroke="${ACC}" stroke-width="3" opacity="0.55"/>`; });
  const node=`<circle cx="${last[0]}" cy="${last[1]-26}" r="17" fill="${PAPER}" stroke="${ACC}" stroke-width="7"/>`;
  const g=`<path d="M ${last[0]-52} ${last[1]-34} C ${last[0]-58} ${last[1]-74}, ${last[0]+6} ${last[1]-86}, ${last[0]+38} ${last[1]-64} C ${last[0]+64} ${last[1]-46}, ${last[0]+54} ${last[1]+10}, ${last[0]+12} ${last[1]+18} C ${last[0]-30} ${last[1]+26}, ${last[0]-64} ${last[1]-2}, ${last[0]-54} ${last[1]-30}" fill="none" stroke="${ACC}" stroke-width="4" stroke-linecap="round" opacity="0.9"/>`;
  const baseline=`<line x1="0" y1="${base}" x2="${S}" y2="${base}" stroke="${INK}" stroke-width="4"/>`;
  return `<g fill="${INK}">${dots}</g>${bars}${baseline}${arcs}${node}${g}`;
}
function motifLoop(){
  const cx=1180,cy=1200,R=340; const dots=htBand(cx,cy,R-130,R+30,{step:18,r:2.7,jit:0.7,skip:0.2});
  const ring=`<circle cx="${cx}" cy="${cy}" r="${R}" fill="none" stroke="${INK}" stroke-width="12" stroke-dasharray="${(2*Math.PI*R*0.44).toFixed(0)} ${(2*Math.PI*R*0.06).toFixed(0)}" stroke-linecap="round"/>`;
  const ah=ang=>{ const a=ang*Math.PI/180,x=cx+R*Math.cos(a),y=cy+R*Math.sin(a),t=a+Math.PI/2,s=26;
    const p=[[x+s*Math.cos(t),y+s*Math.sin(t)],[x+s*Math.cos(t+2.5),y+s*Math.sin(t+2.5)],[x+s*Math.cos(t-2.5),y+s*Math.sin(t-2.5)]];
    return `<polygon points="${p.map(q=>q[0].toFixed(0)+','+q[1].toFixed(0)).join(' ')}" fill="${INK}"/>`; };
  let nodes=''; [-60,30,120,210].forEach((ang,i)=>{ const a=ang*Math.PI/180,x=cx+R*Math.cos(a),y=cy+R*Math.sin(a),hi=(i===0);
    nodes+=`<circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="${hi?20:13}" fill="${hi?ACC:PAPER}" stroke="${hi?ACC:INK}" stroke-width="6"/>`;
    if(hi) nodes+=`<path d="M ${x-58} ${y-10} C ${x-64} ${y-52}, ${x+8} ${y-64}, ${x+42} ${y-42} C ${x+70} ${y-24}, ${x+58} ${y+16}, ${x+14} ${y+22} C ${x-32} ${y+30}, ${x-70} ${y+0}, ${x-58} ${y-32}" fill="none" stroke="${ACC}" stroke-width="4" stroke-linecap="round" opacity="0.9"/>`; });
  return `<g fill="${INK}">${dots}</g>${ring}${ah(-6)}${ah(174)}${nodes}`;
}
const motifSVG = motif==='sequence' ? motifSequence() : motif==='loop' ? motifLoop() : motifSignal();

const html = `<!doctype html><html><head><meta charset="utf-8"><style>
 *{margin:0;padding:0;box-sizing:border-box;}
 html,body{width:${S}px;height:${S}px;}
 #card{position:relative;width:${S}px;height:${S}px;background:${PAPER};overflow:hidden;
       font-family:"Arial Narrow","Helvetica Neue",Arial,sans-serif;}
 svg{position:absolute;inset:0;}
 #hd{position:absolute;left:100px;top:96px;right:100px;display:flex;align-items:center;justify-content:space-between;}
 .brand{display:flex;align-items:center;gap:26px;}
 .chip{width:92px;height:92px;border-radius:22px;background:${INK};color:${PAPER};
       font-family:"Helvetica Neue",Arial,sans-serif;font-weight:800;font-size:46px;
       display:flex;align-items:center;justify-content:center;letter-spacing:-1px;}
 .wm{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:800;font-size:52px;color:${ACC};letter-spacing:-1px;}
 .ep{font-family:"Courier New",monospace;font-weight:700;font-size:34px;color:${ACC};letter-spacing:6px;}
 #type{position:absolute;left:100px;top:300px;right:100px;}
 .ol{font-family:"Courier New",monospace;font-weight:700;font-size:30px;letter-spacing:11px;color:${INK};text-transform:uppercase;margin-bottom:26px;}
 h1{font-weight:800;text-transform:uppercase;font-stretch:condensed;line-height:0.9;letter-spacing:1px;font-size:230px;color:${INK};}
 .sub{margin-top:40px;font-family:"Courier New",monospace;font-weight:700;font-size:38px;letter-spacing:1px;color:${ACC};max-width:1080px;line-height:1.3;}
 #foot{position:absolute;left:100px;bottom:86px;font-family:"Courier New",monospace;font-weight:700;font-size:27px;letter-spacing:9px;color:${INK};text-transform:uppercase;opacity:0.85;}
</style></head><body>
 <div id="card">
  <svg width="${S}" height="${S}" viewBox="0 0 ${S} ${S}">${motifSVG}</svg>
  <div id="hd"><div class="brand"><div class="chip">${esc(mono)}</div><div class="wm">${esc(company)}</div></div><div class="ep">${esc(episode)}</div></div>
  <div id="type"><div class="ol">${esc(overline)}</div><h1>${esc(title)}</h1>${subtitle?`<div class="sub">${esc(subtitle)}</div>`:''}</div>
  <div id="foot">Data&nbsp;Science&nbsp;in&nbsp;the&nbsp;Wild</div>
 </div>
</body></html>`;

(async () => {
  let chromium;
  try { ({ chromium } = require('playwright')); }
  catch (e) { console.error('Playwright not found. Run with NODE_PATH=/opt/node22/lib/node_modules'); process.exit(3); }
  const tmp = path.join(require('os').tmpdir(), `dsitw_cover_${Date.now()}.html`);
  fs.writeFileSync(tmp, html);
  const launchOpts = {};
  if (process.env.CHROMIUM_PATH) launchOpts.executablePath = process.env.CHROMIUM_PATH;
  const browser = await chromium.launch(launchOpts);
  const page = await browser.newPage({ viewport:{width:S,height:S}, deviceScaleFactor:2 });
  await page.goto('file://' + tmp);
  await page.waitForTimeout(120);
  // Shrink-to-fit: the title is a fixed 230px by default, which overflows the
  // card both horizontally (a single long word, e.g. "WEATHERNEXT", wider than
  // the box) and vertically (a long multi-word title wrapping to 4-5 lines runs
  // past the footer and off the bottom of the canvas). Shrink font-size until
  // both dimensions fit; if it still doesn't fit at the floor size, allow
  // mid-word breaking as a last-resort safety net instead of letting
  // overflow:hidden silently clip the text off-canvas.
  await page.evaluate(() => {
    const h1 = document.querySelector('h1');
    const type = document.getElementById('type');
    const foot = document.getElementById('foot');
    const maxHeight = foot.getBoundingClientRect().top - type.getBoundingClientRect().top - 40;
    const floorSize = 40;
    const designMinSize = 90;
    let size = parseFloat(getComputedStyle(h1).fontSize);
    const overflows = () => h1.scrollWidth > h1.clientWidth || type.scrollHeight > maxHeight;
    // Shrink down to the design floor first; if that's not enough (very long
    // titles), keep shrinking past it down to an absolute floor rather than
    // let anything run off-canvas.
    while (overflows() && size > designMinSize) { size -= 4; h1.style.fontSize = size + 'px'; }
    while (overflows() && size > floorSize) { size -= 4; h1.style.fontSize = size + 'px'; }
    if (h1.scrollWidth > h1.clientWidth) {
      h1.style.overflowWrap = 'anywhere';
      h1.style.wordBreak = 'break-word';
    }
  });
  fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
  await page.screenshot({ path: out, clip:{x:0,y:0,width:S,height:S} });
  await browser.close();
  fs.unlinkSync(tmp);
  console.log('wrote', out, `(3000x3000, ink=${INK} accent=${ACC} motif=${motif})`);
})();
