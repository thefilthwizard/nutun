jQuery(function ($) {
  $("#close-sidebar").click(function () {
    $(".htmlBody").removeClass("toggled");
  });
  $("#show-sidebar").click(function () {
    $(".htmlBody").addClass("toggled");
  });
});
