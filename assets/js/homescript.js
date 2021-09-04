var runtimeItemSet = [];
var number;
var clusterNumbers = [1, 2, 3, 4, 5, 6];
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

$(".nameCluster").click
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
            var fired_button = $(this).val();
            number = fired_button;
            launchCluster();
        }
    );
$(".emailJS").click
    (function() 
        {            
            emailjs.send("service_po9swwo","template_34o8pkm",
            {
                from_name: document.getElementById(submittedName).value,
                message: document.getElementById(submittedMessage).value,
                reply_to:document.getElementById(submittedEmail).value,
            });
});
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
        
        return;
    }

function resetCluster()
    {
        /*checks confirmation checkbox*/
        if($('#cluster_'+number+'_reset:checkbox:checked').length > 0==true)
            {
                if(localStorage.getItem("cluster"+number+"Name")!=undefined)
                    {
                        localStorage.removeItem("cluster"+number+"Name");
                    }
                if(localStorage.getItem("cluster"+number+"Data")!=undefined)
                    {
                        localStorage.removeItem("cluster"+number+"Data");
                    }
                    alert("cluster "+number+" reset");
                return;
            } 
            else 
            {
                alert("Checkbox not filled");
            }
            /*alerts user if checkbox not filled*/
    }

function fetchBuild()
    {
         
            {
                buildId = document.getElementById(".build_fetch").value
                localStorage.setItem(JSON.stringify(buildId))
                window.location.href = "edit_build.html";
            }
        /*launches websites*/
    }
/* sets a name on the buttons on the index page */ 
function Fetch()
    {
        newName = document.getElementById("cluster_"+number+"_name").value;
        localStorage.setItem("cluster"+number+"Name", JSON.stringify(newName));
        alert("cluster"+number+"name changed")
    }
