
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
    'index.csr.html': {size: 7723, hash: 'e2d9b6f6727bccb4688068fce883bcdf227c75943ae5858f557e35165871ed2a', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 7325, hash: '0ee623197d89c5e9b25d9c1ade5d50ee4d27c0be5a07c913083d2ee33becd5f4', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'reset-password/index.html': {size: 225, hash: 'f0d9e0108796e2e7b54a5ebcd679ace5ab8824b2f86a04284da20f61efcdadf1', text: () => import('./assets-chunks/reset-password_index_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 16247, hash: '4ebc5bc491a47a0714da5057e0530b4e3426a6d3e60a13487d126fc6bc35ff98', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 16247, hash: '4ebc5bc491a47a0714da5057e0530b4e3426a6d3e60a13487d126fc6bc35ff98', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'index.html': {size: 22884, hash: '9eeb272c79178a96fe0b683b9e7ce18a4cee19fb8f4f3c3dd52bb762c54d6fa3', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 16247, hash: '4ebc5bc491a47a0714da5057e0530b4e3426a6d3e60a13487d126fc6bc35ff98', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
