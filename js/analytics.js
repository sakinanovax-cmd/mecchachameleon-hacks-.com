(function () {
  "use strict";
  var cfg = window.SITE_CONFIG || {};

  // Inject GSC verification meta if configured
  if (cfg.gscVerification && typeof cfg.gscVerification === "string" && cfg.gscVerification.length > 8) {
    var meta = document.createElement("meta");
    meta.name = "google-site-verification";
    meta.content = cfg.gscVerification;
    document.head.appendChild(meta);
  }

  // Load GA4 only when a real ID is set
  if (cfg.ga4Id && /^G-[A-Z0-9]+$/i.test(cfg.ga4Id)) {
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(cfg.ga4Id);
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag() {
      window.dataLayer.push(arguments);
    }
    window.gtag = gtag;
    gtag("js", new Date());
    gtag("config", cfg.ga4Id, { anonymize_ip: true, send_page_view: true });
  }
})();
