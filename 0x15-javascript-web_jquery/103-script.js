$(document).ready(function() {
    function fetchTranslation() {
        const langCode = $('langauge_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

        $.get(url, function(data) {
            $('#hello').text(data.hello);
        }).fail(function(jqXHR, textStatus, errorThrown) {
            $('#hello').text('Error: ' + textStatus + ' - ' + errorThrown);
        });
    }

    // Trigger translation fetch on button click
    $('#btn_translate').click(fetchTranslation);

    // Trigger translation fetch on pressing Enter
    //  while focused on the input
    $('#langauge_code').keypress(function(event) {
        if (event.which === 13) {
            fetchTranslation();
        }
    });
});
