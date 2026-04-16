
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
  },
  {
    "renderMode": 2,
    "route": "/reset-password"
  }
],
  entryPointToBrowserMapping: undefined,
  assets: {
    'index.csr.html': {size: 7808, hash: '767e8ca08306dd5242e96ea84dc0b5a67400eba459c5200417c1ee49d3b570eb', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 7393, hash: 'c275888e8cd4eccae98b2a6865688a2e59c2df6a865827f4c0d3099a9fd62953', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'reset-password/index.html': {size: 225, hash: 'f0d9e0108796e2e7b54a5ebcd679ace5ab8824b2f86a04284da20f61efcdadf1', text: () => import('./assets-chunks/reset-password_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 16332, hash: '6bd2ef07e7123cc1cc6f61944f26d238ff8060ce921fed2abb9d69361121eba3', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'index.html': {size: 22969, hash: '57633f0eec16ee4c7cf663ff6ad8964fe9f6d44183734928e1976f8728d91fbb', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 16332, hash: '6bd2ef07e7123cc1cc6f61944f26d238ff8060ce921fed2abb9d69361121eba3', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 16332, hash: '6bd2ef07e7123cc1cc6f61944f26d238ff8060ce921fed2abb9d69361121eba3', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
