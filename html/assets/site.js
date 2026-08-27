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
    input.select();

    const copied = document.execCommand("copy");
    input.remove();
    if (!copied) {
      throw new Error("Copy command was rejected");
    }
  };

  const installSection = document.getElementById("install");
  let installHighlightTimer;
  let installClickPending = false;

  const highlightInstallPrompt = () => {
    if (!installSection) {
      return;
    }

    window.clearTimeout(installHighlightTimer);
    installSection.classList.remove("install-prompt-highlight");

    // Force a style flush so clicking an install link again replays the cue.
    void installSection.offsetWidth;
    installSection.classList.add("install-prompt-highlight");

    installHighlightTimer = window.setTimeout(() => {
      installSection.classList.remove("install-prompt-highlight");
    }, 2200);
  };

  document.addEventListener("click", (event) => {
    if (!(event.target instanceof Element) || !installSection) {
      return;
    }

    const trigger = event.target.closest('a[href$="#install"]');
    if (!trigger) {
      return;
    }

    const destination = new URL(trigger.href, window.location.href);
    if (destination.pathname !== window.location.pathname) {
      return;
    }

    installClickPending = true;
    const delay = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 300;
    window.setTimeout(() => {
      installClickPending = false;
      highlightInstallPrompt();
    }, delay);
  });

  window.addEventListener("hashchange", () => {
    if (window.location.hash === "#install" && !installClickPending) {
      highlightInstallPrompt();
    }
  });

  if (window.location.hash === "#install") {
    window.requestAnimationFrame(highlightInstallPrompt);
  }

  document.querySelectorAll("[data-copy-target]").forEach((button) => {
    let copiedResetTimer;

    button.addEventListener("click", async () => {
      const target = document.querySelector(button.dataset.copyTarget);
      const status = document.getElementById("copy-status");
      if (!target || !status) {
        return;
      }

      try {
        await copyText(target.textContent.trim());
        status.textContent = "Copied setup prompt.";

        const copyIcon = button.querySelector("[data-copy-icon]");
        const copiedIcon = button.querySelector("[data-copied-icon]");
        if (copyIcon && copiedIcon) {
          window.clearTimeout(copiedResetTimer);
          copyIcon.classList.add("hidden");
          copiedIcon.classList.remove("hidden");
          button.setAttribute("aria-label", "Copied install prompt");
          button.setAttribute("title", "Copied");

          copiedResetTimer = window.setTimeout(() => {
            copiedIcon.classList.add("hidden");
            copyIcon.classList.remove("hidden");
            button.setAttribute("aria-label", "Copy install prompt");
            button.setAttribute("title", "Copy install prompt");
          }, 1800);
        }
      } catch {
        status.textContent = "Copy failed. Select the prompt and copy it manually.";
      }
    });
  });
})();
