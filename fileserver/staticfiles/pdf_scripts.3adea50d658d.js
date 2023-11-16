document.addEventListener("adobe_dc_view_sdk.ready", function(){ 
    var adobeDCView = new AdobeDC.View({clientId: "c2190c7ef509475e8d332b7ec0097cb0", divId: "adobe-dc-view"});
    adobeDCView.previewFile({
        //content:{url: pdf_url},
        content:{location: {url: "C:/Users/asoro/Downloads/Projects/liz-fileserver-main/liz-fileserver-main/fileserver/songdir/Probability_and_Statistics_for_engineers_update_FnVyBre.pdf"}},
        metaData:{fileName: title}
    }, {showDownloadPDF: false, showPrintPDF: false});
});

