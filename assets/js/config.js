/* =========================================================
   0Office.com — SITE CONFIG (edit this file only)
   Everything monetization-related is switched on from here.
   ========================================================= */
window.OFFICE0 = {
  siteName: "0Office.com",

  /* Owner inquiry link shown on top of every page */
  ownerContactUrl: "https://web.works/contact",

  /* Contact routing. The address is stored encoded and only assembled
     in the browser at send time — it never appears as text on the site.
     (XOR 0x5A, reversed char codes.) Do not replace with plain text. */
  _ck: [55,53,57,116,54,51,59,55,61,26,107,59,41,49,40,53,45,56,63,45],

  /* OPTIONAL (recommended): after the first form submission, FormSubmit
     emails an activation link. After activating, FormSubmit gives you a
     random alias string. Paste it here so even the encoded address is
     no longer used by the forms. Example: "a1b2c3d4e5f6..." */
  formAlias: "",

  /* Google AdSense — paste your publisher ID, e.g. "ca-pub-1234567890123456".
     Empty = ad slots show "Advertise here" house ads instead. */
  adsenseClient: "",
  adSlots: { top: "", inContent: "", sidebar: "", footer: "" },

  /* Google Analytics 4 measurement ID, e.g. "G-XXXXXXXXXX" (optional) */
  ga4: "",

  /* Donation / support links. Leave empty to route to the pledge form. */
  donate: {
    paypal: "",        // e.g. "https://paypal.me/yourname"
    buymeacoffee: "",  // e.g. "https://buymeacoffee.com/yourname"
    kofi: "",          // e.g. "https://ko-fi.com/yourname"
    stripe: "",        // e.g. Stripe Payment Link "https://buy.stripe.com/..."
    githubSponsors: "" // e.g. "https://github.com/sponsors/yourname"
  },

  /* YouTube. Add your channel URL and video IDs (the part after v=). */
  youtubeChannel: "",
  videos: [
    /* { id: "VIDEO_ID", title: "Title", topic: "Remote setup" } */
  ],

  /* Affiliate IDs / links for the Software Stack directory (optional).
     key = product slug used in software.html, value = your tracked URL */
  affiliates: {}
};
