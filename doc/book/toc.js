// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded affix "><a href="index.html">Einleitung</a></li><li class="chapter-item expanded "><a href="1.html"><strong aria-hidden="true">1.</strong> Kapitel 1: Was ist Rust?</a></li><li class="chapter-item expanded "><a href="2.html"><strong aria-hidden="true">2.</strong> Kapitel 2: Installation &amp; Systemkonfiguration</a></li><li class="chapter-item expanded "><a href="3.html"><strong aria-hidden="true">3.</strong> Kapitel 3: KI-Assistenten &amp; Tools</a></li><li class="chapter-item expanded "><a href="4.html"><strong aria-hidden="true">4.</strong> Kapitel 4: Erstes Projekt</a></li><li class="chapter-item expanded "><a href="5.html"><strong aria-hidden="true">5.</strong> Kapitel 5: Variablen &amp; Scopes</a></li><li class="chapter-item expanded "><a href="6.html"><strong aria-hidden="true">6.</strong> Kapitel 6: Skalare &amp; zusammengesetzte Typen</a></li><li class="chapter-item expanded "><a href="7.html"><strong aria-hidden="true">7.</strong> Kapitel 7: Übungsprojekt</a></li><li class="chapter-item expanded "><a href="8.html"><strong aria-hidden="true">8.</strong> Kapitel 8: Arrays &amp; Tupel</a></li><li class="chapter-item expanded "><a href="9.html"><strong aria-hidden="true">9.</strong> Kapitel 9: Zusammenfassung Variablen &amp; Typen</a></li><li class="chapter-item expanded "><a href="10.html"><strong aria-hidden="true">10.</strong> Kapitel 10: Funktionen</a></li><li class="chapter-item expanded "><a href="11.html"><strong aria-hidden="true">11.</strong> Kapitel 11: Funktionen Details</a></li><li class="chapter-item expanded "><a href="12.html"><strong aria-hidden="true">12.</strong> Kapitel 12: Operatoren</a></li><li class="chapter-item expanded "><a href="13.html"><strong aria-hidden="true">13.</strong> Kapitel 13: Übungen zu Operatoren</a></li><li class="chapter-item expanded "><a href="14.html"><strong aria-hidden="true">14.</strong> Kapitel 14: Antigravity CLI</a></li><li class="chapter-item expanded "><a href="15.html"><strong aria-hidden="true">15.</strong> Kapitel 15: Kontrollstrukturen</a></li><li class="chapter-item expanded "><a href="16.html"><strong aria-hidden="true">16.</strong> Kapitel 16: Beste Google KI zum Programmieren nutzen</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split("#")[0].split("?")[0];
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);
