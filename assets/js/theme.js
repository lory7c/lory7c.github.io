(function () {
  'use strict';
  const key = 'zhe-yu-theme';
  const preference = window.matchMedia('(prefers-color-scheme: dark)');
  let choice;
  try { choice = localStorage.getItem(key); } catch (_) {}
  if (choice !== 'light' && choice !== 'dark') choice = null;

  function apply(theme) {
    document.documentElement.dataset.theme = theme;
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = theme === 'dark' ? '#111923' : '#f3f5f8';
    const button = document.getElementById('theme-toggle');
    if (button) {
      const label = theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
      button.setAttribute('aria-label', label);
      button.title = label;
    }
  }

  apply(choice || (preference.matches ? 'dark' : 'light'));
  preference.addEventListener('change', function (event) {
    if (!choice) apply(event.matches ? 'dark' : 'light');
  });
  document.addEventListener('DOMContentLoaded', function () {
    apply(document.documentElement.dataset.theme);
    const button = document.getElementById('theme-toggle');
    if (!button) return;
    button.addEventListener('click', function () {
      choice = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem(key, choice); } catch (_) {}
      apply(choice);
    });
  });
})();
