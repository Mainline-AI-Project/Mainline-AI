
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
    'index.csr.html': {size: 7808, hash: '952d4dcf8fccbc7cdd569ed8e33c1903e4f9eb331cbaa6dae43f2d897b012952', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 7393, hash: '94d8426ecca5812ce4459d8bbf15d731577250e227db80ad683680c4c561bc53', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'login/index.html': {size: 16332, hash: 'fce8ccc9a26a5e7207bf93265a32669bfba2bfc07966682ec7b1be71ce7ce3c7', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'reset-password/index.html': {size: 225, hash: 'f0d9e0108796e2e7b54a5ebcd679ace5ab8824b2f86a04284da20f61efcdadf1', text: () => import('./assets-chunks/reset-password_index_html.mjs').then(m => m.default)},
    'index.html': {size: 22991, hash: 'dc4e56eead9112d6dc132d7feaf3c5a1e83eb3be23493ef4e8829591a87263e8', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 16332, hash: 'fce8ccc9a26a5e7207bf93265a32669bfba2bfc07966682ec7b1be71ce7ce3c7', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 16332, hash: 'fce8ccc9a26a5e7207bf93265a32669bfba2bfc07966682ec7b1be71ce7ce3c7', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
