```{=html}
<script type="text/javascript">
let tabDict = {
  "debian": "Debian/Ubuntu",
  "rhel": "RHEL/Fedora",
  "arch": "Arch",
  "macos": "macOS",
  "windows": "Windows/WSL"
};

let invertedTabDict = invertDictionary(tabDict);

document.addEventListener("DOMContentLoaded", function() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);

    let lang = 'debian';

    if (urlParams.has('lang')){
        lang = urlParams.get('lang');
    }

    changeTabSelections(lang);

    var tabs = document.querySelectorAll('[role="tab"]');
    
    for(var i = 0; i < tabs.length; i++) {
        tab = tabs[i];
        if (tab.textContent in invertedTabDict) {
            tab.addEventListener('click', onTabClicked);
        }
    }

});

function changeTabSelections(language) {
    var tabs = document.querySelectorAll('[role="tab"]');
    var tab_panels = document.querySelectorAll('[role="tabpanel"]');

    // Disable all tab panels
    for(var i = 0; i < tab_panels.length; i++) {
        panel = tab_panels[i];
        panel.classList.remove('active')
    }

    // Iterate over all tabs
    for(var i = 0; i < tabs.length; i++) {
        tab = tabs[i];

        // Disable all tabs
        tab.classList.remove('active');

        // If the tab is the chosen language
        if (tab.textContent == tabDict[language]) {
            // Mark it active
            tab.classList.add('active');
            // Find the linked tab panel and make it active
            var linked_panel = tab.getAttribute('aria-controls')
            var panel = document.getElementById(linked_panel);
            panel.classList.add('active');
        }
    }

}

function onTabClicked(event) {
    changeTabSelections(invertedTabDict[event.srcElement.textContent]);
}

function invertDictionary(dict){
    var ret = {};
    for(var key in dict){
        ret[dict[key]] = key;
    }
    return ret;
}

</script>
```
