$(function(){
    $("#id_fecha_emision").datepicker( {changeMonth:true, changeYear:true, numberOfMonths:2}, $.datepicker.regional["es"], "option", "dateFormat", "dd/mm/yy" );
    $("#id_fecha_emision").datepicker( "option", "showAnim", "clip" );
    $("#id_fecha").datepicker( {changeMonth:true, changeYear:true}, $.datepicker.regional["es"], "option", "dateFormat", "dd/mm/yy" );
    $("#id_fecha").datepicker( "option", "showAnim", "clip" );
});