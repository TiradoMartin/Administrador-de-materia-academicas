$(document).ready(function () {
 
    (function ($) {

        $('#univ_red_buscar').keyup(function () {

            var rex = new RegExp($(this).val(), 'i');
            $('.buscar tr').hide();
            $('.buscar tr').filter(function () {
                return rex.test($(this).text());
            }).show();

        })

    }(jQuery));

});


