var runtimeItemSet = [];
/* prevents functions to be launched before dom is ready*/
$( document ).ready(function() 
{
/* onclick events to trigger functions */
$(".submit").click
    (function() 
        {
            var fired_button = $(this).val();
            number = fired_button;
            store_items();
        }
    );

$(".addURL").click
    (function() 
        {
            var fired_button = $(this).val();
            number = fired_button;
            storeUrlCluster();
        }
    );

$(".resetCluster").click
    (function() 
        {
            var fired_button = $(this).val();
            number = fired_button;
            resetCluster();
        }
    );

$(".edit_items").click
    (function() 
        {
            var fired_button = $(this).val();
            number = fired_button;
            nameClusterButton();
        }
    );

$(".fetch").click
    (function() 
        {
            fetchBuild();
        }
    );
});
/*  blelow are main functions for website functionality */
function store_items()
    {
        runtimeItemSet = [];
        /*Reset runtime items to clear old data*/
        var buildID = document.getElementById(".build_name").value
        var helm = document.getElementById(".helm").value
        var amulet = document.getElementById(".amulet").value
        var mainHand = document.getElementById(".main_hand").value
        var body = document.getElementById(".body_armor").value
        var offHand = document.getElementById(".off_hand").value
        var belt = document.getElementById(".belt").value
        var boots = document.getElementById(".boots").value
        var gloves = document.getElementById(".gloves").value
        var ring1 = document.getElementById(".ring_1").value
        var ring2 = document.getElementById(".ring_2").value
        runtimeItemSet = [helm, amulet, mainHand, body, offHand, boots, belt, gloves, ring1, ring2]
        $.ajax({
            type: "POST",
            url: "/store_build",
            data: { runtimeItemSet: buildID },
            success: callbackFunc
        });
        var expiryDate = new Date();
        expiryDate.setMonth(expiryDate.getMonth() + 3);

        setCookie(buildID, $('#wrap_select')[0].outerHTML)
        document.cookie = buildID + '=y; expires=' + expiryDate.toGMTString();
        return;
    }

    function edit_items()
    {
        runtimeItemSet = [];
        /*Reset runtime items to clear old data*/
        var buildID = document.getElementById(".build_name").value
        var helm = document.getElementById(".helm").value
        var amulet = document.getElementById(".amulet").value
        var mainHand = document.getElementById(".main_hand").value
        var body = document.getElementById(".body_armor").value
        var offHand = document.getElementById(".off_hand").value
        var belt = document.getElementById(".belt").value
        var boots = document.getElementById(".boots").value
        var gloves = document.getElementById(".gloves").value
        var ring1 = document.getElementById(".ring_1").value
        var ring2 = document.getElementById(".ring_2").value
        runtimeItemSet = [helm, amulet, mainHand, body, offHand, boots, belt, gloves, ring1, ring2]
        $.ajax({
            type: "POST",
            url: "/edit_build",
            data: { runtimeItemSet: buildID },
            success: callbackFunc
        });
        
        return;
    }

function fetchBuild()
    {
                buildID = document.getElementById(".build_fetch").value
                var template = getCookie(buildID)
                window.location.href = "edit_build.html";
                document.getElementById("insert_wrapper").innerHTML = template
                document.getElementById("wrap_select").id = ".edit_items"
                return
                /*fetches builds*/
    };
