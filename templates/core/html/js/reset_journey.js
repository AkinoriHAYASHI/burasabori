/**
 * Created by jyuneko on 11/16/14.
 */

function reset_journey() {
    document.cookie = 'avatar_id=; path=/burasabori; ' + new Date(0).toUTCString();
    document.cookie = 'key=; path=/burasabori; ' + new Date(0).toUTCString();
}