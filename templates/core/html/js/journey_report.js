/*
    {% load staticfiles %}
    {% load i18n %}
 */

/**
 * Created by Junya Kaneko on 11/3/14.
 */

window.twttr = (function (d, s, id) {
  var t, js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src= "https://platform.twitter.com/widgets.js";
  fjs.parentNode.insertBefore(js, fjs);
  return window.twttr || (t = { _e: [], ready: function (f) { t._e.push(f) } });
}(document, "script", "twitter-wjs"));


function get_query_string() {
    url = window.location.href.toString();
    query_string = url.split('?')[1];
    query_string = query_string.split('#')[0];
    return query_string
}

function show_posts(){
    var posts = $('#posts');
    posts.fadeOut();
    //show_loading_icon(posts);
    posts.load("{% url 'core:posts' %}" + "?" + get_query_string(), function(response, status, xhr){
        if(status == 'error'){
            posts.html('<div style="margin-top: 60px;">アバターが見つかりませんでした．</div>');
        }
        $(this).fadeIn();
        last_post_id = $('.post').last().attr('id');
        window.location.href = '#' + last_post_id;
        twttr.widgets.load();
    });
}

function show_latest_post() {
    location.reload();
    last_post_id = $('.post').last().attr('id');
    window.location.href = '#' + last_post_id;
}