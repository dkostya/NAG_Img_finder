$(document).ready(function() {
    search.onchange = function space_remove() {
        var search = document.getElementById('search');
        search.value = search.value.trim();
    };
});
