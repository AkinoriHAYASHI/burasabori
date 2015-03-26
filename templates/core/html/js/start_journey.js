/*
    {% load staticfiles %}
    {% load i18n %}
*/

/**
 * Created by Junya Kaneko on 10/28/14.
 */

function show_railway_settings() {
    var railway_settings = $("#railway_settings");
    show_loading_icon(railway_settings);
    railway_settings.load("{% url 'core:railway_select' %}", function(){
        set_railway_select_onchange();
    });
}

function get_railway_select() {
    return $("select", $("#railway_settings"));
}

function get_selected_railway() {
    var railway_select = get_railway_select();
    var option =  $("option:selected", railway_select);
    return option.attr("value");
}

function show_station_settings() {
    var railway = get_selected_railway();
    var url = "{% url 'core:station_select' %}" + "?railway=" + railway;

    var station_settings = $('#station_settings');
    show_loading_icon(station_settings);

    station_settings.load(url, function(){
        set_station_select_onchange();
    });
}

function get_station_select() {
    return $("select", $("#station_settings"));
}

function get_selected_station() {
    var station_select = get_station_select();
    var option = $("option:selected", station_select);
    return option.attr("value");
}

function set_railway_select_onchange() {
    var railway_select = get_railway_select();
    railway_select.change(function() {
        var railway = get_selected_railway();
        $("#station_settings").empty();
        $("#submit_settings").hide();
        if(railway != ""){
            show_station_settings();
        }
    });
}

function set_station_select_onchange(){
    var station_select = get_station_select();
    station_select.change(function(){
        var station = get_selected_station();
        if(station != ""){
            $("#submit_settings").show();
        }else{
            $("#submit_settings").hide();
        }
        set_footer();
    });
}

function set_initial_settings_form_submit(){
    var initial_settings_form = $('#initial_settings_form');
    initial_settings_form.submit(function(event){
        event.preventDefault();
        $.ajax({
            url: $(this).attr("action"),
            type: $(this).attr("method"),
            data: $(this).serializeArray(),
            success: function(data, textStatus, jqXHR){
                var response = $('<div/>');
                response.html(data);
                var state = $('#state', response).text();
                if(state === "success"){
                    window.location.replace("{% url 'core:journey_report' %}" + "?avatar=" + $('#avatar_id', response).text())
                    show_railway_settings();
                }else{
                    if(state == "user_has_maximum_number_of_avatars"){
                        window.alert("僕の分身は3匹までケロ。新たな旅はまた明日のお楽しみケロ ^ ^。")
                    }else if(state == "invalid_ipaddress"){
                        window.alert("不正なIPアドレスでは旅できないケロ。")
                    }else if(state == "station_does_not_exist"){
                        window.alert("そんな駅ないケロよ？旅できないケロ。")
                    }
                    show_railway_settings();
                }
            }
        });
        show_loading_icon($('#railway_settings'));
        $('#station_settings').empty();
        $('#submit_settings').hide();
    });
}