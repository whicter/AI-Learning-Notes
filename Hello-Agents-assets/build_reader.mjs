import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const require=createRequire('/Users/congrenhan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/package.json');
const { marked }=require('marked');
const root=path.dirname(path.dirname(new URL(import.meta.url).pathname));
const md=fs.readFileSync(path.join(root,'Hello-Agents 零基础学习笔记.md'),'utf8');
let body=marked.parse(md);
const toc=[];
let count=0;
body=body.replace(/<h([23])>(.*?)<\/h\1>/g,(_,level,title)=>{
  const id=`section-${++count}`;
  if(level==='2')toc.push({id,title});
  return `<h${level} id="${id}">${title}</h${level}>`;
});
body=body.replace(/<img src="([^"]+)"/g,(_,src)=>{
  if(!src.startsWith('/'))throw new Error('Expected absolute image');
  return `<img loading="lazy" width="1400" src="data:image/png;base64,${fs.readFileSync(src).toString('base64')}"`;
});
body=body.replace(/<table>/g,'<div class="table-wrap"><table>').replace(/<\/table>/g,'</table></div>');
const title='Hello-Agents 零基础图文笔记';
const html=`<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<style>
:root{color-scheme:light;--ink:#20324b;--muted:#56677d;--blue:#2563eb;--line:#e2e8f0}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:32px}body{margin:0;color:var(--ink);background:#f5f7fb;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:17px;line-height:1.9}
.shell{max-width:1510px;margin:auto;display:grid;grid-template-columns:260px minmax(0,1fr);gap:38px;padding:40px 36px 80px}
nav{align-self:start;position:sticky;top:30px;max-height:calc(100vh - 60px);overflow:auto;padding:10px 0}nav .brand{font-size:14px;letter-spacing:2px;color:var(--blue);font-weight:700;margin-bottom:20px}nav .label{font-size:13px;color:var(--muted);margin-bottom:12px}nav a{display:block;text-decoration:none;color:var(--muted);font-size:14px;line-height:1.6;margin:4px 0;padding:6px 10px;border-left:2px solid transparent}nav a:hover{color:var(--blue);border-color:var(--blue);background:#eaf0fc}
main{min-width:0;background:#fff;padding:58px 62px 70px;border-radius:20px;box-shadow:0 5px 28px #20324b08}
.eyebrow{font-size:12px;letter-spacing:2.5px;color:var(--blue);font-weight:700;margin-bottom:18px}.cover{border-bottom:1px solid var(--line);padding-bottom:32px;margin-bottom:38px}.cover h1{margin:0 0 16px;font-size:40px;line-height:1.4;letter-spacing:-1px}.cover p{max-width:720px;font-size:18px;color:var(--muted);margin:12px 0}.tags{display:flex;gap:10px;flex-wrap:wrap;margin-top:24px}.tags span{background:#eef4ff;padding:5px 12px;border-radius:6px;font-size:13px;color:#31558f}
article>h1{display:none}h2{margin:70px 0 24px;font-size:28px;line-height:1.5;padding-top:24px;border-top:1px solid var(--line)}h3{margin:34px 0 14px;font-size:21px;line-height:1.5}p{margin:16px 0}a{color:#245dbe;text-underline-offset:4px;overflow-wrap:anywhere}strong{font-weight:650}li{margin:7px 0}img{display:block;width:100%;height:auto;margin:22px 0 8px;border-radius:8px}p:has(>em:only-child){font-size:13px;color:var(--muted);margin:6px 0 25px}em{font-style:normal}pre{background:#f4f6fa;border-left:3px solid #8aa8e7;padding:20px 24px;border-radius:4px;overflow:auto;font-size:14px;line-height:1.8}code{font-family:"SFMono-Regular",Consolas,monospace;font-size:.88em}p code,li code,td code{background:#eef2f7;padding:2px 5px;border-radius:4px}.table-wrap{overflow:auto;margin:22px 0}table{width:100%;border-collapse:collapse;font-size:14px;line-height:1.8;text-align:left}th{background:#eef3fb;color:#314e75;font-weight:600}td,th{padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}tbody tr:nth-child(even){background:#fafbfd}footer{margin-top:60px;border-top:1px solid var(--line);padding-top:20px;font-size:13px;color:var(--muted)}
@media(max-width:1100px){.shell{grid-template-columns:200px minmax(0,1fr);gap:22px;padding:24px}main{padding:40px 34px}.cover h1{font-size:32px}}
@media(max-width:760px){body{font-size:16px}.shell{display:block;padding:12px}nav{position:static;max-height:none;padding:12px 8px 25px}nav a{display:inline-block;font-size:12px;margin:3px;padding:4px 7px;border-left:0;background:#eaf0fc;border-radius:4px}nav .brand{margin-bottom:8px}nav .label{display:none}main{padding:26px 18px;border-radius:12px}.cover h1{font-size:29px}.cover p{font-size:16px}h2{font-size:24px;margin-top:48px}h3{font-size:20px}pre{padding:16px;font-size:12px}th,td{min-width:110px;padding:10px}img{border-radius:0}}
@media print{body{background:white;font-size:11pt}.shell{display:block;padding:0}nav{display:none}main{padding:0;box-shadow:none}.cover{padding-top:10mm}h2{break-before:page;margin-top:0;padding-top:10mm}h3{break-after:avoid}img,tr,pre{break-inside:avoid}a{color:inherit;text-decoration:none}.table-wrap,pre{overflow:visible}footer{display:none}@page{size:A4;margin:17mm}}
</style></head><body><div class="shell"><nav aria-label="章节目录"><div class="brand">HELLO AGENTS</div><div class="label">零基础图文笔记 · 章节目录</div>${toc.map(x=>`<a href="#${x.id}">${x.title}</a>`).join('')}</nav><main><header class="cover"><div class="eyebrow">CONCEPTS · CODE · DIAGRAMS</div><h1>Hello-Agents<br>零基础图文笔记</h1><p>从一次旅行请求出发，看懂模型如何选择工具、执行任务、使用记忆与资料，并通过反馈继续行动。</p><div class="tags"><span>15 个主题</span><span>10 张中文示意图</span><span>代码逐段解释</span><span>原文链接</span></div></header><article>${body}</article><footer>基于 whicter/hello-agents 核心教程整理。示意图为概念解释，图中天气和景点不是实时查询结果。</footer></main></div></body></html>`;
const out=path.join(root,'Hello-Agents 零基础图文笔记.html');
fs.writeFileSync(out,html);
console.log(JSON.stringify({file:out,figures:(body.match(/<img /g)||[]).length,chapters:toc.length,bytes:Buffer.byteLength(html)}));
