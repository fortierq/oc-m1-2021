// prefix = "/oc-m1-2021"
if (typeof prefix == "undefined") {
    prefix = ""
}

function url(relative) {
    return prefix + "/web/viewer.html?file=" + encodeURI(prefix) + "%2F" + relative;
}
