/* LES 2 L — comportements d'interface */
(function () {
  'use strict';

  /* ---- En-tête : ombre au défilement ---------------------------------- */
  var header = document.querySelector('.header');
  var toTop = document.querySelector('.to-top');

  function onScroll() {
    var y = window.scrollY || document.documentElement.scrollTop;
    if (header) header.classList.toggle('is-scrolled', y > 12);
    if (toTop) toTop.classList.toggle('is-visible', y > 500);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (toTop) {
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ---- Menu mobile ----------------------------------------------------- */
  var drawer = document.getElementById('drawer');
  var burger = document.querySelector('.burger');
  var drawerClose = document.querySelector('.drawer__close');

  function openDrawer() {
    if (!drawer) return;
    drawer.classList.add('is-open');
    document.body.classList.add('no-scroll');
    burger.setAttribute('aria-expanded', 'true');
    var first = drawer.querySelector('a');
    if (first) first.focus();
  }
  function closeDrawer() {
    if (!drawer) return;
    drawer.classList.remove('is-open');
    document.body.classList.remove('no-scroll');
    burger.setAttribute('aria-expanded', 'false');
    burger.focus();
  }
  if (burger) burger.addEventListener('click', openDrawer);
  if (drawerClose) drawerClose.addEventListener('click', closeDrawer);
  if (drawer) {
    drawer.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') closeDrawer();
    });
  }

  /* ---- Apparition au défilement ---------------------------------------- */
  var revealables = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealables.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---- Visionneuse de galerie ------------------------------------------ */
  var lightbox = document.getElementById('lightbox');
  if (lightbox) {
    var items = Array.prototype.slice.call(document.querySelectorAll('.gallery__item'));
    var lbImg = lightbox.querySelector('img');
    var lbCount = lightbox.querySelector('.lightbox__count');
    var index = 0;
    var lastFocus = null;

    function show(i) {
      index = (i + items.length) % items.length;
      var src = items[index].getAttribute('href') || items[index].querySelector('img').src;
      lbImg.src = src;
      lbImg.alt = items[index].querySelector('img').alt || '';
      if (lbCount) lbCount.textContent = (index + 1) + ' / ' + items.length;
    }
    function openLb(i) {
      lastFocus = document.activeElement;
      show(i);
      lightbox.classList.add('is-open');
      document.body.classList.add('no-scroll');
      lightbox.querySelector('.lightbox__close').focus();
    }
    function closeLb() {
      lightbox.classList.remove('is-open');
      document.body.classList.remove('no-scroll');
      lbImg.src = '';
      if (lastFocus) lastFocus.focus();
    }

    items.forEach(function (item, i) {
      item.addEventListener('click', function (e) { e.preventDefault(); openLb(i); });
    });
    lightbox.querySelector('.lightbox__close').addEventListener('click', closeLb);
    lightbox.querySelector('.lightbox__prev').addEventListener('click', function () { show(index - 1); });
    lightbox.querySelector('.lightbox__next').addEventListener('click', function () { show(index + 1); });
    lightbox.addEventListener('click', function (e) { if (e.target === lightbox) closeLb(); });

    document.addEventListener('keydown', function (e) {
      if (!lightbox.classList.contains('is-open')) return;
      if (e.key === 'Escape') closeLb();
      if (e.key === 'ArrowLeft') show(index - 1);
      if (e.key === 'ArrowRight') show(index + 1);
    });
  }

  /* ---- Échap ferme le menu --------------------------------------------- */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('is-open')) closeDrawer();
  });

  /* ---- Carrousel d'avis -------------------------------------------------- */
  var track = document.getElementById('reviews-track');
  if (track) {
    var dotsBox = document.getElementById('reviews-dots');
    var slides = Array.prototype.slice.call(track.children);
    var timer = null;

    function perView() {
      if (!slides.length) return 1;
      return Math.max(1, Math.round(track.clientWidth / slides[0].offsetWidth));
    }
    function pages() {
      return Math.max(1, Math.ceil(slides.length / perView()));
    }
    function current() {
      var page = track.clientWidth;
      return Math.min(pages() - 1, Math.round(track.scrollLeft / page));
    }
    function goTo(i) {
      var n = pages();
      track.scrollLeft = ((i % n) + n) % n * track.clientWidth;
    }
    function buildDots() {
      dotsBox.innerHTML = '';
      for (var i = 0; i < pages(); i++) {
        var b = document.createElement('button');
        b.type = 'button';
        b.setAttribute('aria-label', 'Page d\u2019avis ' + (i + 1));
        (function (k) { b.addEventListener('click', function () { stop(); goTo(k); }); })(i);
        dotsBox.appendChild(b);
      }
      syncDots();
    }
    function syncDots() {
      var c = current();
      Array.prototype.forEach.call(dotsBox.children, function (b, i) {
        b.setAttribute('aria-current', i === c ? 'true' : 'false');
      });
    }

    document.querySelectorAll('[data-rev]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        stop();
        goTo(current() + (btn.dataset.rev === 'next' ? 1 : -1));
      });
    });

    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function start() { if (!reduce && !timer) timer = setInterval(function () { goTo(current() + 1); }, 6000); }
    function stop() { clearInterval(timer); timer = null; }

    track.addEventListener('scroll', function () {
      window.requestAnimationFrame(syncDots);
    }, { passive: true });
    ['mouseenter', 'focusin', 'touchstart'].forEach(function (e) {
      track.addEventListener(e, stop, { passive: true });
    });
    track.addEventListener('mouseleave', start);
    window.addEventListener('resize', buildDots);

    buildDots();
    start();
  }

  /* ---- Bandeau cookies -------------------------------------------------- */
  var cookie = document.getElementById('cookie');
  if (cookie) {
    var KEY = 'les2l-cookie-ok';
    var accepted = false;
    try { accepted = localStorage.getItem(KEY) === '1'; } catch (err) { accepted = false; }
    if (!accepted) {
      cookie.hidden = false;
      cookie.querySelector('button').addEventListener('click', function () {
        cookie.hidden = true;
        try { localStorage.setItem(KEY, '1'); } catch (err) { /* stockage indisponible */ }
      });
    }
  }

  /* ---- Formulaire de contact (sans back-end pour l'instant) ------------- */
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      if (form.getAttribute('action')) return; // un service d'envoi est configuré
      e.preventDefault();
      var to = form.dataset.mailto;
      var subject = encodeURIComponent('Message depuis le site — ' + (form.elements.nom.value || ''));
      var body = encodeURIComponent(
        'Nom : ' + form.elements.nom.value + '\n' +
        'E-mail : ' + form.elements.email.value + '\n\n' +
        form.elements.message.value
      );
      window.location.href = 'mailto:' + to + '?subject=' + subject + '&body=' + body;
    });
  }
})();
