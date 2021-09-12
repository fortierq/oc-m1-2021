<script type="text/javascript" src="../utils.js"></script>

<iframe id="pdf-js-viewer" src="" title="webviewer" frameborder="0" width="100%" height="800"></iframe>

<script>
    window.onload = () => document.getElementById("pdf-js-viewer").src = url("{{ pdf }}") + "#zoom={{ zoom }}&pagemode=none";
</script>