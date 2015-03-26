/**
 * Created by Junya Kaneko on 11/13/14.
 */

function load_own_journey(){
    var avatar_id = null;
    var key = null;
    var csrftoken = null;

    var cookie = document.cookie;
    var cookie_value_strings = cookie.split(';');
    for(var i = 0; i < cookie_value_strings.length; i++){
        variable = cookie_value_strings[i].split('=');
        if(variable[0].trim() == 'avatar_id'){
            avatar_id = variable[1];
        }else if(variable[0].trim() == 'key'){
            key = variable[1];
        }else if(variable[0].trim() == 'csrftoken'){
            csrftoken = variable[1];
        }
    }
    $.ajax({
        url: "{% url 'core:user_verification' %}?",
        type: "get",
        data: {'avatar': avatar_id, 'key': key, 'csrftoken': csrftoken},
        success: function(data, textStatus, jqXHR){
            var response = $('<div/>');
            response.html(data);
            var avatar_id = $('#avatar_id', response).text();
            if(avatar_id != "None"){
                window.location.replace("{% url 'core:journey_report' %}" + "?avatar=" + avatar_id);
            }else{
            }
        }
    });
}