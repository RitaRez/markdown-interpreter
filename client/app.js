const api_endpoint = 'https://markdown-interpreter.herokuapp.com/convert/';
const request_delay = 1000;
var timeout;

var display_result = (html) => {
    var viewport = document.getElementById('preview-container');
    viewport.innerHTML = html;
}


var api_req = (markdown) => {
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', api_endpoint);

    xhttp.setRequestHeader('Content-type', 'application/json');
    xhttp.onreadystatechange = () => {
        display_result(xhttp.responseText);
    };
    xhttp.send(JSON.stringify({ markdown }));
    console.log(xhttp)
}
var keyup = () => {
    if(timeout){
        clearTimeout(timeout);
    }

    var textarea = document.getElementById('markdown-textarea');
    var markdown_content = textarea.value;

    timeout = setTimeout(() => {
        api_req(markdown_content);
    }, request_delay);
}

var show_markdown = () => {
    preview_container = document.getElementById('preview-container');
    markdown_textarea = document.getElementById('markdown-textarea');
    markdown_button = document.getElementById('markdown-button');
    preview_button = document.getElementById('preview-button');

    preview_container.style.display = 'none';
    markdown_textarea.style.display = 'block';

    markdown_button.style.backgroundColor = 'white';
    markdown_button.style.borderBottom = 'none';
    markdown_button.style.borderRight = '1px solid rgb(208, 215, 222)';

    preview_button.style.backgroundColor = 'rgb(246, 248, 250)';
    preview_button.style.borderBottom = '1px solid rgb(208, 215, 222)';
    preview_button.style.borderLeft = 'none';
    preview_button.style.borderRight = 'none';
}

var show_result = () => {
    preview_container = document.getElementById('preview-container');
    markdown_textarea = document.getElementById('markdown-textarea');
    markdown_button = document.getElementById('markdown-button');
    preview_button = document.getElementById('preview-button');

    preview_container.style.display = 'block';
    markdown_textarea.style.display = 'none';

    markdown_button.style.backgroundColor = 'rgb(246, 248, 250)';
    markdown_button.style.borderBottom = '1px solid rgb(208, 215, 222)';
    markdown_button.style.borderRight = 'none';

    preview_button.style.backgroundColor = 'white';
    preview_button.style.borderBottom = 'none';
    preview_button.style.borderLeft = '1px solid rgb(208, 215, 222)';
    preview_button.style.borderRight = '1px solid rgb(208, 215, 222)';
}