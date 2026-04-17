
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
    'index.csr.html': {size: 7808, hash: '629efededb2495be15c6709eaa405960517f84125a12729bccdeda6163103bc5', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 7393, hash: 'bbfa4d65faa5e2a9e7b1e3116b8da83ea2d5fab71cb1f54c9f6a5dd8e0650f01', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 16332, hash: '317e5ba7edf9377cef987610dc3cd4e8f4c7c8559fce641ef5f6ad82ca89bb44', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 16332, hash: '317e5ba7edf9377cef987610dc3cd4e8f4c7c8559fce641ef5f6ad82ca89bb44', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'reset-password/index.html': {size: 225, hash: 'f0d9e0108796e2e7b54a5ebcd679ace5ab8824b2f86a04284da20f61efcdadf1', text: () => import('./assets-chunks/reset-password_index_html.mjs').then(m => m.default)},
    'index.html': {size: 22969, hash: 'c573a8881508a6a49c6ff5e9a13eda4a52599003d81286ed2e75dd1831e4c2d8', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 16332, hash: '317e5ba7edf9377cef987610dc3cd4e8f4c7c8559fce641ef5f6ad82ca89bb44', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
