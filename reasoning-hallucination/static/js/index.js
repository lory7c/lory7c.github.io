const videoCaptionTrack = document.querySelector('#survey-video-captions');
const videoCaptionData = document.querySelector('#survey-video-caption-data');
if (videoCaptionTrack && videoCaptionData) {
  // A local Blob also loads captions when the static page is opened via file://.
  videoCaptionTrack.src = URL.createObjectURL(new Blob(
    [videoCaptionData.textContent.trim() + '\n'], { type: 'text/vtt' }
  ));
}

const lightbox = document.querySelector('#lightbox');
const expandedImage = document.querySelector('#lightbox-image');
const originalLink = document.querySelector('#figure-original');
document.querySelectorAll('[data-zoom]').forEach((button) => {
  button.addEventListener('click', () => {
    const source = button.querySelector('img');
    expandedImage.src = source.src;
    expandedImage.alt = source.alt;
    originalLink.href = source.src;
    lightbox.showModal();
    document.body.style.overflow = 'hidden';
  });
});
document.querySelector('#close-lightbox').addEventListener('click', () => lightbox.close());
lightbox.addEventListener('click', (event) => {
  if (event.target !== lightbox) return;
  const bounds = lightbox.getBoundingClientRect();
  if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) lightbox.close();
});
lightbox.addEventListener('close', () => { document.body.style.overflow = ''; });
document.querySelector('#copy-citation').addEventListener('click', async () => {
  const text = document.querySelector('#citation-text').textContent;
  const status = document.querySelector('#copy-status');
  try {
    await navigator.clipboard.writeText(text);
    status.textContent = 'Copied';
  } catch {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(document.querySelector('#citation-text'));
    selection.removeAllRanges();
    selection.addRange(range);
    status.textContent = document.execCommand('copy') ? 'Copied' : 'Select and copy citation';
  }
  window.setTimeout(() => { status.textContent = ''; }, 3000);
});
