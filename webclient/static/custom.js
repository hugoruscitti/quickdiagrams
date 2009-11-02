/* muestra una imagen de progreso mientras se genera el diagrama. */
function show_running_message()
{
    $("#placeholder").css("display", "block");
    $("#placeholder").html("<div class='wait'></div>");
}

/* callback asociado a la pulsacion del boton id=draw */
function on_draw__clicked()
{
    var textarea_content = $("#diagram_code").val();
    var post = {'diagram_code': textarea_content};

    $.post("draw", post, on_draw_ajax__done);
    show_running_message();
}

/* callback asociado a la pulsacion del boton id=save */
function on_save__clicked()
{
    var textarea_content = $("#diagram_code").val();
    var post = {'diagram_code': textarea_content};

    $.post("save", post, on_save_ajax__done);
}

/* muestra el resultado de haber generado el diagrama. */
function on_draw_ajax__done(data)
{
    $("#save_message").fadeOut(500);
    $("#placeholder").html("<img src='" + data + "'/>");
}

/* muestra la direccion en donde se ha almacenado el modelo */
function on_save_ajax__done(data)
{
    $("#save_message").html(data);
    $("#save_message").fadeIn(1000);
}




$(document).ready(
    function()
    {
        $("#diagram_code").tabby();
        $("#draw").click(on_draw__clicked);
        $("#save").click(on_save__clicked);
        $("#diagram_code").TextAreaResizer();
        on_draw__clicked();
    }
);
