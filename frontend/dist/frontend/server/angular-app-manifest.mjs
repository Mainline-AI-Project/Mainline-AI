
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
    'index.csr.html': {size: 7808, hash: '31b48f71c4d7d011aae742f21fcf00a220219c4b5df879f27e3bca3659395e8a', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 7393, hash: '468736a1c21d184e1ca04306bd81b6199e46ded3a11cef62666c9f16644be192', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'reset-password/index.html': {size: 225, hash: 'f0d9e0108796e2e7b54a5ebcd679ace5ab8824b2f86a04284da20f61efcdadf1', text: () => import('./assets-chunks/reset-password_index_html.mjs').then(m => m.default)},
    'index.html': {size: 22969, hash: 'f1db5a19995e8498df07e6865628fae80fd7f90d5f3c654f3a7ab55526b3a29a', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 16332, hash: 'c735e880c17e91c717f943f433ccef8e488e742d9167e443a214f025565a2f04', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 16332, hash: 'c735e880c17e91c717f943f433ccef8e488e742d9167e443a214f025565a2f04', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 16332, hash: 'c735e880c17e91c717f943f433ccef8e488e742d9167e443a214f025565a2f04', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
