
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
    'index.csr.html': {size: 7808, hash: 'b971616b34a081c7f448f4c1f17298b0624f67bae59df908f3d4188090fb3d7f', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 7393, hash: '6908a0953462d26bead1506a1a755b40a1ce345f2a5d3a2ef571805abf6c6d08', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'reset-password/index.html': {size: 225, hash: 'f0d9e0108796e2e7b54a5ebcd679ace5ab8824b2f86a04284da20f61efcdadf1', text: () => import('./assets-chunks/reset-password_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 16332, hash: '96f24c1e189bd0d7a49f7a7f080e2553abc8212d4e440f86030f62d5bff09597', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 16332, hash: '96f24c1e189bd0d7a49f7a7f080e2553abc8212d4e440f86030f62d5bff09597', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'index.html': {size: 22991, hash: '15e57c3b85076ad1132ee94a2960621081d13e9eae874a0c4b6e7b2d9e58c90b', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 16332, hash: '96f24c1e189bd0d7a49f7a7f080e2553abc8212d4e440f86030f62d5bff09597', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
