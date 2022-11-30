jQuery(function ($) {
  $(document).ready(function () {
    $("#search-btn").attr("disabled", true);
  });
});

function initMapBox(apiKey) {
  jQuery(function ($) {
    $(document).ready(function () {
      const script = document.getElementById("search-js");

      const autofill = mapboxsearch.autofill({
        accessToken: apiKey,
      });
      autofill.addEventListener("retrieve", (event) => {
        const featureCollection = event.detail;
        const latLong = featureCollection.features[0].geometry.coordinates;
        const latInput = $(
          `<input type="hidden" name="lat" value="${latLong[1]}" />`
        );
        const longInput = $(
          `<input type="hidden" name="long" value="${latLong[0]}" />`
        );
        $("#submit-form").append(latInput, longInput);
        $("#search-btn").attr("disabled", false);
      });
    });
  });
}
