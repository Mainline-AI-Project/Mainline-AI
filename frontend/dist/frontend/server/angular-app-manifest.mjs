
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
    'index.csr.html': {size: 7723, hash: 'bfd5fbbe2acf79f9211dab4a2c6d7cd34d122af98ef39950c4d7d60f82ccf457', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 7325, hash: 'bf9939d95047f83ccbe5112166cb2582e3a2905646c9077fdc44ab75488bc8c8', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'reset-password/index.html': {size: 225, hash: 'f0d9e0108796e2e7b54a5ebcd679ace5ab8824b2f86a04284da20f61efcdadf1', text: () => import('./assets-chunks/reset-password_index_html.mjs').then(m => m.default)},
    'signup/index.html': {size: 16247, hash: '3318a62d72f25fad02f879e0708b24aac635a3333e89ccaf07f4c26f9330109b', text: () => import('./assets-chunks/signup_index_html.mjs').then(m => m.default)},
    'index.html': {size: 22884, hash: '9e220ec28be01ee103e418ad9fe14e1e8444a580e95d848e94b1d955ad8ea38f', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 16247, hash: '3318a62d72f25fad02f879e0708b24aac635a3333e89ccaf07f4c26f9330109b', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'select-plan/index.html': {size: 16247, hash: '3318a62d72f25fad02f879e0708b24aac635a3333e89ccaf07f4c26f9330109b', text: () => import('./assets-chunks/select-plan_index_html.mjs').then(m => m.default)},
    'styles-M3S3TEZ4.css': {size: 1298, hash: 'p7lU365+TkY', text: () => import('./assets-chunks/styles-M3S3TEZ4_css.mjs').then(m => m.default)}
  },
};
