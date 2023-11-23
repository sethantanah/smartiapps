document.addEventListener("adobe_dc_view_sdk.ready", function(){ 
    var adobeDCView = new AdobeDC.View({clientId: "c2190c7ef509475e8d332b7ec0097cb0", divId: "adobe-dc-view"});
    adobeDCView.previewFile({
        content:  {location: {url: pdf_url2}},
        metaData:{fileName: title}
    }, {showDownloadPDF: false, showPrintPDF: false});

    // var reader = new FileReader();
    // reader.onloadend = function(e) {
    //     var filePromise = Promise.resolve(e.target.result);
    //     // Pass the filePromise and name of the file to the previewFile API
    //     adobeDCView.previewFile({
    //          content: {promise: filePromise},
    //          metaData: { fileName: file.name }
    //     })
    // };
    // reader.readAsArrayBuffer(file);
});




       
 