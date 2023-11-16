

    // Fetch the PDF file
    fetch(pdf_url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.arrayBuffer();
        })
        .then(arrayBuffer => {
            // Handle the ArrayBuffer here
            console.log('ArrayBuffer:', arrayBuffer);
            document.addEventListener("adobe_dc_view_sdk.ready", function(){ 
                var adobeDCView = new AdobeDC.View({clientId: "c2190c7ef509475e8d332b7ec0097cb0", divId: "adobe-dc-view"});
                adobeDCView.previewFile({
                    content:{promise: arrayBuffer},
                    //content:{location: {url: pdf_url}},
                    metaData:{fileName: title}
                }, {showDownloadPDF: false, showPrintPDF: false});
            });

            // You can now send the ArrayBuffer to the server or process it as needed
        })
        .catch(error => console.error('Error fetching PDF:', error));