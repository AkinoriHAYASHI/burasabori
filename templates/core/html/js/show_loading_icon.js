/*
    {% load staticfiles %}
    {% load i18n %}
*/

/**
 * Created by Junya Kaneko on 10/29/14.
 */

function show_loading_icon(parent){
    parent.empty();
    var url = "{% static 'img/ajax-loader.gif' %}";
    var img_tag ="<img src='" + url + "' style='vertical-align: middle; width: 30px; max-width:'/>";
    var icon = "<p>" + img_tag + " Now loading... " + img_tag + "</p>";
    parent.html(icon);
}