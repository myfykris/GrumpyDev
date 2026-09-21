(() => {
  "use strict";

  const copyText = async (text) => {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }

    const input = document.createElement("textarea");
    input.value = text;
    input.setAttribute("readonly", "");
    input.style.position = "fixed";
    input.style.opacity = "0";
    document.body.append(input);
    try {
      input.select();
      if (!document.execCommand("copy")) {
        throw new Error("Copy command was rejected");
      }
    } finally {
      input.remove();
    }
  };

  document.querySelectorAll("[data-copy-target]").forEach((button) => {
    let resetTimer;
    const showCopied = (copied) => {
      const copyIcon = button.querySelector("[data-copy-icon]");
      const copiedIcon = button.querySelector("[data-copied-icon]");
      if (!copyIcon || !copiedIcon) return;
      copyIcon.classList.toggle("hidden", copied);
      copiedIcon.classList.toggle("hidden", !copied);
      button.setAttribute("aria-label", copied ? "Copied install prompt" : "Copy install prompt");
      button.setAttribute("title", copied ? "Copied" : "Copy install prompt");
    };
    button.addEventListener("click", async () => {
      const target = document.querySelector(button.dataset.copyTarget);
      const status = document.getElementById(button.dataset.copyStatus);
      if (!target || !status) return;

      window.clearTimeout(resetTimer);
      showCopied(false);
      button.disabled = true;
      try {
        await copyText(target.textContent.trim());
        status.textContent = "Copied setup prompt.";
        showCopied(true);
        resetTimer = window.setTimeout(() => showCopied(false), 1800);
      } catch {
        status.textContent = "Copy failed. Select the prompt and copy it manually.";
      } finally {
        button.disabled = false;
      }
    });
  });
})();
