
export default {
  bootstrap: () => import('./main.server.mjs').then(m => m.default),
  inlineCriticalCss: true,
  baseHref: '/',
  locale: undefined,
  routes: [
  {
    "renderMode": 2,
    "route": "/"
  },
  {
    "renderMode": 2,
    "route": "/login"
  },
  {
    "renderMode": 2,
    "route": "/signup"
  },
  {
    "renderMode": 2,
    "route": "/select-plan"
  },
  {
    "renderMode": 2,
    "route": "/chat"
  },
  {
    "renderMode": 2,
    "redirectTo": "/",
    "route": "/**"
  }
],
  entryPointToBrowserMapping: undefined,
  assets: {
    'index.csr.html': {size: 2141, hash: '1684b45c83abab7c5f6fa7f62f7fca0beedffbad178c4083366662e519d5009a', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 1743, hash: '632e29bc2b7fa41374beacb2d6b859071e72c604a3d0414327dd671dfeb97fcf', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 11642, hash: '43a6b94dc32e3af53ad8cc20b1495c1e401d69fa629607d6ae9b63da683d9d88', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 11642, hash: '43a6b94dc32e3af53ad8cc20b1495c1e401d69fa629607d6ae9b63da683d9d88', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'index.html': {size: 17157, hash: '717d9d07468833586d37721a4458c28c64ab438441621c6cf8fc03f29148f5c2', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 11642, hash: '43a6b94dc32e3af53ad8cc20b1495c1e401d69fa629607d6ae9b63da683d9d88', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
