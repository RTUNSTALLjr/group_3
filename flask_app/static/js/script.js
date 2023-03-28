let input = document.getElementById('file-upload');
let previewArea = document.getElementById('file-preview-area')
let filePreview = document.getElementById('file-preview')

input.addEventListener('change', showFile);

function showFile(e) {
    // the change event gives the input it occurred in 
    let input = e.target;

    // input has an array of files in the `files` property
    // DISPLAY FILE PREVIEW
    const imageSrc = URL.createObjectURL(input.files[0]);
    filePreview.src = imageSrc;
    previewArea.classList.remove("d-none");
}
