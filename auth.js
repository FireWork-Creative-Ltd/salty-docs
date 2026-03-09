(function() {
  var PASSWORD = 'salty2026';
  var STORAGE_KEY = 'salty_docs_auth';

  if (sessionStorage.getItem(STORAGE_KEY) === 'true') return;

  document.documentElement.style.overflow = 'hidden';

  document.addEventListener('DOMContentLoaded', function() {
    document.body.style.visibility = 'hidden';

    var overlay = document.createElement('div');
    overlay.id = 'auth-gate';
    overlay.innerHTML =
      '<div style="background:#fff;border-radius:16px;padding:2.5rem;max-width:360px;width:90%;box-shadow:0 12px 40px rgba(14,58,45,0.15);text-align:center">' +
        '<h1 style="font-family:Inter,-apple-system,sans-serif;font-size:1.5rem;font-weight:700;color:#0E3A2D;margin-bottom:0.25rem">SALTY Docs</h1>' +
        '<p style="font-family:Inter,-apple-system,sans-serif;font-size:0.875rem;color:#666;margin-bottom:1.5rem">Enter password to continue</p>' +
        '<input id="auth-pw" type="password" placeholder="Password" autofocus style="width:100%;padding:0.75rem 1rem;border:1.5px solid rgba(14,58,45,0.2);border-radius:10px;font-size:1rem;font-family:Inter,-apple-system,sans-serif;outline:none;transition:border-color 0.2s" />' +
        '<button id="auth-btn" style="width:100%;margin-top:0.75rem;padding:0.75rem;background:#0E3A2D;color:#fff;border:none;border-radius:10px;font-size:1rem;font-weight:600;font-family:Inter,-apple-system,sans-serif;cursor:pointer;transition:opacity 0.2s">Enter</button>' +
        '<p id="auth-err" style="font-family:Inter,-apple-system,sans-serif;font-size:0.8rem;color:#E53935;margin-top:0.75rem;display:none">Wrong password</p>' +
      '</div>';

    Object.assign(overlay.style, {
      position: 'fixed', top: '0', left: '0', width: '100%', height: '100%',
      background: '#F7F4ED', display: 'flex', alignItems: 'center', justifyContent: 'center',
      zIndex: '99999'
    });

    document.body.appendChild(overlay);
    document.body.style.visibility = 'visible';

    var input = document.getElementById('auth-pw');
    var btn = document.getElementById('auth-btn');
    var err = document.getElementById('auth-err');

    function attempt() {
      if (input.value === PASSWORD) {
        sessionStorage.setItem(STORAGE_KEY, 'true');
        overlay.remove();
        document.documentElement.style.overflow = '';
      } else {
        err.style.display = 'block';
        input.style.borderColor = '#E53935';
        input.value = '';
        input.focus();
      }
    }

    btn.addEventListener('click', attempt);
    input.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') attempt();
    });
    input.addEventListener('input', function() {
      err.style.display = 'none';
      input.style.borderColor = 'rgba(14,58,45,0.2)';
    });
  });
})();
