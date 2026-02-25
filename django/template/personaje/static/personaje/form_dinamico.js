document.addEventListener("DOMContentLoaded", () => {
  const autoCheckbox = document.getElementById("id_auto_generar");
  const autoFields = document.querySelectorAll(".js-auto-fields");
  const manualFields = document.querySelectorAll(".js-manual-fields");
  const modeFields = document.querySelectorAll(".js-mode-fields");

  if (!autoCheckbox) {
    return;
  }

  let touched = false;

  const show = (elements, visible) => {
    elements.forEach((el) => {
      if (visible) {
        el.classList.remove("is-hidden");
      } else {
        el.classList.add("is-hidden");
      }
    });
  };

  const syncVisibility = () => {
    if (!touched) {
      show(autoFields, false);
      show(manualFields, false);
      show(modeFields, false);
      return;
    }

    show(modeFields, true);

    if (autoCheckbox.checked) {
      show(autoFields, true);
      show(manualFields, false);
    } else {
      show(autoFields, false);
      show(manualFields, true);
    }
  };

  autoCheckbox.addEventListener("change", () => {
    touched = true;
    syncVisibility();
  });

  if (document.querySelector(".errorlist")) {
    touched = true;
  }

  syncVisibility();
});
