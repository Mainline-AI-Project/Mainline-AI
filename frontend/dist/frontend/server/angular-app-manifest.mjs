
export default {
  bootstrap: () => import('./main.server.mjs').then(m => m.default),
  inlineCriticalCss: true,
  baseHref: '/static/',
  locale: undefined,
  routes: [
  {
    "renderMode": 2,
    "route": "/static"
  },
  {
    "renderMode": 2,
    "route": "/static/login"
  },
  {
    "renderMode": 2,
    "route": "/static/signup"
  },
  {
    "renderMode": 2,
    "route": "/static/select-plan"
  },
  {
    "renderMode": 2,
    "route": "/static/chat"
  },
  {
    "renderMode": 2,
    "redirectTo": "/static",
    "route": "/static/**"
  },
  {
    "renderMode": 2,
    "route": "/static/reset-password"
  }
],
  entryPointToBrowserMapping: undefined,
  assets: {
    'index.csr.html': {size: 7730, hash: 'a84eaf7600ef9730fa111fb67724051ea0225d321898f38fb46401dde5777607', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 7332, hash: '536c79ff4a8ab4e2b7ad241544ede65a16b9e58d2fd5ab15786bdc121bac2136', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'index.html': {size: 22891, hash: 'a7abad34adb467de63c60ce4507fa563e59cd218fd82dc95318770942623cf4b', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'reset-password/index.html': {size: 246, hash: '67f4f62f46030e5d98599ee0d3c0acf28d4ee01bc7149bcefcdbf2aa748ff131', text: () => import('./assets-chunks/reset-password_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 16254, hash: '0491dddc1498bd4e213e9cb2ec80ff4c442c7e23a34b7a614c943875f57c6dc7', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 16254, hash: '0491dddc1498bd4e213e9cb2ec80ff4c442c7e23a34b7a614c943875f57c6dc7', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 16254, hash: '0491dddc1498bd4e213e9cb2ec80ff4c442c7e23a34b7a614c943875f57c6dc7', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
