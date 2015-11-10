$(document).ready(refresh);

function refresh() {
    Dajaxice.management.searchUser(searchUserCallBack, {
                                                     "search_user": "",
    });
}

function createUserCallBack(data) {
    if(data == "fail") {
	        alert("用户重名,添加失败!");
    }
    else {
        refresh();
    }
}

function searchUserCallBack(data){
    $("#widget-content").html(data);
}
$("#user-add").click(function() {
    $("#titleLabel").html("新建用户");

});

$("#search_user_button").click(function() {
    var search_user = $("#search_user").val();
    Dajaxice.management.searchUser(searchUserCallBack, {
                                                    "search_user": search_user,
                                                    
                                            });
});


$("#user-save").click(function() {
    var user_name = $("#user_name").val();
    var user_password = $("#user_password").val();
    Dajaxice.management.createUser(createUserCallBack, {
                                                    "user_name": user_name,
                                                    "user_password": user_password,
                                                    
                                            });
});


$(document).on("click", ".btn-set-title", function() {
     user_id = $(this).parent().parent().attr("iid");
     location.href = "/management/titleSetting?user_id=" + user_id;
});
