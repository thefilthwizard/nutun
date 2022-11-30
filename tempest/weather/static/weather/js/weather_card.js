function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function cardInit(historyUrl) {
  $(document).ready(function () {
    $(".save-btn").click(function () {
      const data = $(this).parents(".card").data();
      const csrftoken = getCookie("csrftoken");
      $.ajax({
        url: historyUrl,
        dataType: "json",
        data: JSON.stringify(data),
        method: "POST",
        headers: { "X-CSRFToken": csrftoken },
      }).done(function () {
        const alertEl = $(`<div class="alert alert-success" role="alert">
                            Saved Successfully!
                        </div>`);
        console.log($(".weather-card-list"));
        console.log(alertEl);
        $(".weather-card-list").prepend(alertEl);

        alertEl.get(0).scrollIntoView();
      });
    });
  });
}
