$(document).ready(function () {
    $("#sticky_notes").click(function () {
      $.ajax({
        url: "/home/sticky_notes/",
        success: function (data) {
          $("#content-container").html(data);
        },
      });
    });
    $("#account-link").click(function () {
      $.ajax({
        url: "/path/to/account/view/",
        success: function (data) {
          $("#content-container").html(data);
        },
      });
    });
  });


