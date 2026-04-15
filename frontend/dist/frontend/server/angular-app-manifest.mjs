
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
    'index.csr.html': {size: 7774, hash: 'adfcf0984f11259e101d165df5d8180b08212e77b0d44d84714957ec386fed16', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 7359, hash: '9a2991d57ea22b37e5ade906b9f75e41c6231d9552075abc1d219b10a979f662', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'reset-password/index.html': {size: 225, hash: 'f0d9e0108796e2e7b54a5ebcd679ace5ab8824b2f86a04284da20f61efcdadf1', text: () => import('./assets-chunks/reset-password_index_html.mjs').then(m => m.default)},
    'index.html': {size: 22935, hash: 'dddbbbe2ac3a9e35be1b87d0a80abe0cfd3274bf9a9b3e708adbe919b706f4b0', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 16298, hash: 'a3262fec1d0a75258b615deef70b6efd79bf428d356275c193c55f4ae313f576', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 16298, hash: 'a3262fec1d0a75258b615deef70b6efd79bf428d356275c193c55f4ae313f576', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 16298, hash: 'a3262fec1d0a75258b615deef70b6efd79bf428d356275c193c55f4ae313f576', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
