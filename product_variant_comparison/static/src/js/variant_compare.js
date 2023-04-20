odoo.define('product_variants_comparison.variant_compare', function(require) {
'use strict';
var rpc = require('web.rpc');
var ajax = require('web.ajax')

    $('#compare').click(function(){
    console.log("compare")
        var checks = document.querySelectorAll('.variant_check');
        var product_id = $('.product_id_get')[0].id;
        var data_ids = []
        for (var i = 0; i < checks.length; i++){
            if (checks[i].checked === true){
                data_ids.push(parseInt(checks[i].id))
            }
        }

        data_ids.push(parseInt(product_id))
        this.href=`/variant/compare/${data_ids}`
    });

    $('.variant_check').click(function(){
        var checked = $('.variant_check:checkbox:checked');
        if (checked.length > 1){
         $('#compare_list').removeClass('d-none');


        }
        else{
            $('#compare_list').addClass('d-none');
        }
    });

    $('#switch').click(function(){

        console.log('yelloow');
       if ($('#table_ver').hasClass('d-none')){
            $('#table_ver').removeClass('d-none')
            $('#table_hor').addClass('d-none')
       }
       else{
            $('#table_hor').removeClass('d-none')
            $('#table_ver').addClass('d-none')
       }

    });

    $('.delete').click(function(){
        var colIndex = $(this).closest('td').index();
        $('td:nth-child(' + (colIndex + 1) + '), th:nth-child(' + (colIndex + 1) + ')').hide();
    });

    $('#remove').click(function(){
        var checks = $('.variant_check:checkbox:checked');
        for (var i = 0; i < checks.length; i++){
            checks[i].checked=false;
        }
        $('#compare_list').addClass('d-none');
    });

    $('#close').click(function(){
        $('#compare_list').addClass('d-none');
    });
    var isChecked = localStorage.getItem('compareCheckbox') === 'true';
  $('#compare_check').prop('checked', isChecked);
  if (isChecked) {
    $('#product_specs').show();
  } else {
    $('#product_specs').hide();
  }

  // Add a change event listener to the checkbox
  $('#compare_check').change(function() {
    var isChecked = $(this).is(':checked');
    if (isChecked) {
      $('#product_specs').show();
    } else {
      $('#product_specs').hide();
    }
    localStorage.setItem('compareCheckbox', isChecked);
  });
});

