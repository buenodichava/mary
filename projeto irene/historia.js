document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector("header");
    const links = [...document.querySelectorAll('.menu a[href^="#"]')];
    const secoes = links
        .map(link => document.querySelector(link.getAttribute("href")))
        .filter(Boolean);

   
    const progresso = document.createElement("div");
    progresso.className = "progresso-leitura";
    progresso.setAttribute("aria-hidden", "true");
    document.body.appendChild(progresso);

    function atualizarPagina() {
        const altura = document.documentElement.scrollHeight - window.innerHeight;
        const percentual = altura > 0 ? (window.scrollY / altura) * 100 : 0;

        progresso.style.width = `${Math.min(100, Math.max(0, percentual))}%`;
        header?.classList.toggle("scrolled", window.scrollY > 30);
    }

    window.addEventListener("scroll", atualizarPagina, { passive: true });
    window.addEventListener("resize", atualizarPagina);
    atualizarPagina();

    const elementos = document.querySelectorAll(
        ".capitulo-imagem, .capitulo-texto, .queda-conteudo, .final-historia > div"
    );

    elementos.forEach(elemento => elemento.classList.add("revelar"));

    if ("IntersectionObserver" in window) {
        const observadorElementos = new IntersectionObserver((entradas, observador) => {
            entradas.forEach(({ target, isIntersecting }) => {
                if (isIntersecting) {
                    target.classList.add("visivel");
                    observador.unobserve(target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: "0px 0px -40px 0px"
        });

        elementos.forEach(elemento => observadorElementos.observe(elemento));

        const observadorSecoes = new IntersectionObserver(entradas => {
            entradas.forEach(({ target, isIntersecting }) => {
                if (!isIntersecting) return;

                links.forEach(link => {
                    const ativo = link.getAttribute("href") === `#${target.id}`;
                    link.classList.toggle("ativo", ativo);

                    if (ativo) {
                        link.setAttribute("aria-current", "location");
                    } else {
                        link.removeAttribute("aria-current");
                    }
                });
            });
        }, {
            rootMargin: "-30% 0px -55% 0px"
        });

        secoes.forEach(secao => observadorSecoes.observe(secao));
    } else {
        elementos.forEach(elemento => elemento.classList.add("visivel"));
    }

    links.forEach(link => {
        link.addEventListener("click", evento => {
            const destino = document.querySelector(link.getAttribute("href"));
            if (!destino) return;

            evento.preventDefault();
            destino.scrollIntoView({
                behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches
                    ? "auto"
                    : "smooth",
                block: "start"
            });
        });
    });
});
