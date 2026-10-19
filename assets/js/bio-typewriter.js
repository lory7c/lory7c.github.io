(function () {
  'use strict';
  const text = document.getElementById('bio-typewriter-text');
  if (!text) return;

  const phrases = ['LLM Researcher 🔬', 'Agent Safety 🛡️', 'Self-Improving Agents 🌱'];
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const segmenter = typeof Intl.Segmenter === 'function'
    ? new Intl.Segmenter('en', { granularity: 'grapheme' }) : null;
  const characters = phrases.map(function (phrase) {
    return segmenter
      ? Array.from(segmenter.segment(phrase), function (part) { return part.segment; })
      : Array.from(phrase);
  });
  let phraseIndex = 0;
  let position = characters[0].length;
  let deleting = true;
  let timer;

  function tick() {
    const current = characters[phraseIndex];
    position += deleting ? -1 : 1;
    text.textContent = current.slice(0, position).join('');
    let delay = deleting ? 40 : 85;
    if (!deleting && position === current.length) {
      deleting = true;
      delay = 2200;
    } else if (deleting && position === 0) {
      deleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      delay = 350;
    }
    timer = window.setTimeout(tick, delay);
  }

  function restart() {
    window.clearTimeout(timer);
    phraseIndex = 0;
    position = characters[0].length;
    deleting = true;
    text.textContent = phrases[0];
    if (!motion.matches && !document.hidden) {
      timer = window.setTimeout(tick, 2200);
    }
  }

  motion.addEventListener('change', restart);
  document.addEventListener('visibilitychange', restart);
  restart();
})();
