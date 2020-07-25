function add_hora_extra(funcionario_id, horas){
    token = $("[name=csrfmiddlewaretoken]").val();
    console.log(token);
      $.ajax({
        type: 'POST',
        url: '/hora-extra/create-js/',
        data: {
            csrfmiddlewaretoken: token,
            funcionario_id: funcionario_id,
            horas: $("#hora_extra_valor").val(),
        },
        dataType: 'application/json',
        success: function (data) {

        },
        complete: function(){
            $("#hora_extra_modal_close").click();
            load_hora_extra(funcionario_id)
        }
      });
}

function load_hora_extra(funcionario_id){
    $.ajax({
        url:'/hora-extra/list-js/'+funcionario_id,
        success: function(data){

            var output='';
            $('#list_hora_extra').empty()
            for(var i in data){
                $('#list_hora_extra').append('<li><a href="/hora-extra/update/'+data[i]['id']+'">'+data[i]['motivo']+'</a></li>')
            }

        },
    });
}

$(document).ready(function(){
    load_hora_extra($('#funcionario_id').val());
});



