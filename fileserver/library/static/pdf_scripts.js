document.addEventListener("adobe_dc_view_sdk.ready", function(){ 
    var adobeDCView = new AdobeDC.View({clientId: "c2190c7ef509475e8d332b7ec0097cb0", divId: "adobe-dc-view"});
    adobeDCView.previewFile({
        content:{promise: pdf_content},
        //content:{location: {url: pdf_url}},
        metaData:{fileName: title}
    }, {showDownloadPDF: false, showPrintPDF: false});
});