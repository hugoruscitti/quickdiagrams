/* muestra una imagen de progreso mientras se genera el diagrama. */
function show_running_message()
{
    //$("#placeholder").css("display", "block");
    //$("#placeholder").html("<div class='wait'></div>");

    $("#loading_image").css("display", "block");
    $("#procesing").css("display", "inline");

    $("button[id='draw']").attr("readonly", true);
    $("button[id='draw']").attr("disabled", true);
    
    $("button[id='save']").attr("readonly", true);
    $("button[id='save']").attr("disabled", true);
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

    // TODO: DESCOMENTAR.
    // $("#placeholder").html("<img src='" + data + "'/>");
    $("#image_in_placeholder").attr('src', data);
    $("#loading_image").css("display", "none");
    $("#procesing").css("display", "none");

    $("button[id='draw']").attr("readonly", false);
    $("button[id='draw']").attr("disabled", false);

    $("button[id='save']").attr("readonly", false);
    $("button[id='save']").attr("disabled", false);
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
