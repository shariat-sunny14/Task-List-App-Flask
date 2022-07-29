// row data select script start
$('#data').on('click', 'tbody tr', function (event) {
    $(this).addClass('highlight').siblings().removeClass('highlight');
});

//row data select script end 

//checkbox check after refresh start
var checkboxValues = JSON.parse(localStorage.getItem('checkboxValues')) || {},
    $checkboxes = $("#checkbox-container :checkbox");

$checkboxes.on("change", function () {
    $checkboxes.each(function () {
        checkboxValues[this.id] = this.checked;
    });

    localStorage.setItem("checkboxValues", JSON.stringify(checkboxValues));
});

// On page load
$.each(checkboxValues, function (key, value) {
    $("#" + key).prop('checked', value);
});
//checkbox check after refresh end


// req type row value color change script
elements = document.getElementsByClassName("reqtype-class")
for (var i = elements.length; i--;) {
    if (elements[i].innerText === "New Req.") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#808B96";
    }
    if (elements[i].innerText === "Bugs") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#F0B27A";
    }
}
// console.log(elements)
// req type row value color change script end


// Status row value color change script
elements = document.getElementsByClassName("status-class")
for (var i = elements.length; i--;) {
    if (elements[i].innerText === "Pending") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#5499C7";
    }
    if (elements[i].innerText === "Done") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#239B56";
    }
    if (elements[i].innerText === "Half Done") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#7DCEA0";
    }
    if (elements[i].innerText === "Not Done") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#D98880";
    }
}
// Status row value color change script end

// priority row value color change script
elements = document.getElementsByClassName("priority-class")
for (var i = elements.length; i--;) {
    if (elements[i].innerText === "Very High") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#7D6608";
    }
    if (elements[i].innerText === "High") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#B7950B";
    }
    if (elements[i].innerText === "Medium") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#F1C40F";
    }
    if (elements[i].innerText === "Low") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#F4D03F";
    }
    if (elements[i].innerText === "Very Low") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#F7DC6F";
    }
}
// priority row value color change script end


// dev Status row value color change script
elements = document.getElementsByClassName("devstatus-class")
for (var i = elements.length; i--;) {
    if (elements[i].innerText === "Pending") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#5499C7";
    }
    if (elements[i].innerText === "Done") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#239B56";
    }
    if (elements[i].innerText === "Half Done") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#7DCEA0";
    }
    if (elements[i].innerText === "Not Done") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#D98880";
    }
}
// dev Status row value color change script end


// qa Status row value color change script
elements = document.getElementsByClassName("qastatus-class")
for (var i = elements.length; i--;) {
    if (elements[i].innerText === "Pending") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#5499C7";
    }
    if (elements[i].innerText === "Done") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#239B56";
    }
    if (elements[i].innerText === "Half Done") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#7DCEA0";
    }
    if (elements[i].innerText === "Not Done") {
        elements[i].style.color = "#fff";
        elements[i].style.background = "#D98880";
    }
}
// qa Status row value color change script end

// search filter page navigation and table row filter page value always stay start
$(document).ready(function () {
    $('#data, #prescription_data, #admission_data, #billing_data').DataTable({
        // table row filter page value always stay start
        deferRender: true,
        paging: true,
        Destroy: true,
        scrollCollapse: true,
        scroller: true,
        scroll: true,
        autoWidth: true,
        stateSave: true,
        stateSaveCallback: function (settings, data) {
            localStorage.setItem('DataTables' + settings.sInstance, JSON.stringify(data))
        },
        stateLoadCallback: function (settings) {
            return JSON.parse(localStorage.getItem('DataTables' + settings.sInstance))
        },
        // table row filter page value always stay end

        // search filter page navigation start
        columns: [
            null,
            { searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            { orderable: true, searchable: true },
            null]
        // search filter page navigation end
    });
});
// search filter page navigation and table row filter page value always stay end
