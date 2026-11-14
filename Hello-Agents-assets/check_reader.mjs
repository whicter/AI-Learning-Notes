import {createRequire} from 'node:module';
import path from 'node:path';
const require=createRequire('/Users/congrenhan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/package.json');
const {chromium}=require('playwright');
const root=path.dirname(path.dirname(new URL(import.meta.url).pathname));
const browser=await chromium.launch({headless:true,executablePath:'/Users/congrenhan/Library/Caches/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-mac-arm64/chrome-headless-shell'});
try{
const page=await browser.newPage({viewport:{width:1440,height:1100},deviceScaleFactor:1});
await page.goto('file://'+path.join(root,'Hello-Agents 零基础图文笔记.html'));
await page.locator('img').evaluateAll(imgs=>imgs.forEach(i=>i.loading='eager'));
await page.waitForFunction(()=>[...document.images].every(i=>i.complete&&i.naturalWidth>0));
await page.screenshot({path:path.join(root,'Hello-Agents-assets/reader-preview.png')});
console.log(await page.evaluate(()=>({imageCount:document.images.length,loaded:[...document.images].every(i=>i.complete&&i.naturalWidth>0),overflow:document.documentElement.scrollWidth>innerWidth,headings:document.querySelectorAll('h2').length})));
await page.setViewportSize({width:390,height:844});
console.log(await page.evaluate(()=>({mobileOverflow:document.documentElement.scrollWidth>innerWidth})));
}finally{await browser.close()}
