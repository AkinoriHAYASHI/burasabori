/**
 * Created by Junya Kaneko on 10/28/14.
 */

function set_footer() {
    var header_height = $('#header').height();
    var nav_height = $('#nav').height();
    var contents_height = $('#contents').height();

    var footer = $('#footer');
    var footer_height = footer.height();

    var document_height = header_height + nav_height + contents_height + footer_height;

    var window_height = $(window).height();


    if(window_height > document_height){
        footer.offset({'top':window_height - footer_height});
    }else {
        footer.offset({'top': window_height - footer.height});
    }
}