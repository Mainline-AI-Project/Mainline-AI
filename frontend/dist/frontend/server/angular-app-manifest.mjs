
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
    'index.csr.html': {size: 7808, hash: '32af67c0dd466a12cb2456b43d3e5dfac01413eafa8be1f45142064e607c99fd', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 7393, hash: '3f1f2cb7f35df4c09e4fb5262e9b909df35ea900635eb67f8fa23ad393514069', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'reset-password/index.html': {size: 225, hash: 'f0d9e0108796e2e7b54a5ebcd679ace5ab8824b2f86a04284da20f61efcdadf1', text: () => import('./assets-chunks/reset-password_index_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 16332, hash: '5fae00c5c49546d39421ba8727f2110ae654f3ec3dc7fc1dfcb29d6ffb96c320', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 16332, hash: '5fae00c5c49546d39421ba8727f2110ae654f3ec3dc7fc1dfcb29d6ffb96c320', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'index.html': {size: 22991, hash: '512a82bb56a24f9f82e9734e6b7090ec41859b590f643a8757941580cab4d46a', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 16332, hash: '5fae00c5c49546d39421ba8727f2110ae654f3ec3dc7fc1dfcb29d6ffb96c320', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
