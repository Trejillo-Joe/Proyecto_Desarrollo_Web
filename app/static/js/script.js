document.addEventListener("DOMContentLoaded", function () {
    // 🔹 BOTÓN "NOSOTROS" (Desplaza hasta la sección)
    const btnNosotros = document.getElementById("btnNosotros");
    const sectionNosotros = document.getElementById("nosotros");

    if (btnNosotros && sectionNosotros) {
        btnNosotros.addEventListener("click", function () {
            sectionNosotros.scrollIntoView({ behavior: "smooth" });
        });
    }

    // Es un evento que esta escuchando si el usuario oprime el boton "Nosotros"
    window.addEventListener("scroll", function () { 
        const btnNosotros = document.getElementById("btnNosotros");
        const sectionNosotros = document.getElementById("nosotros");
    
        if (btnNosotros && sectionNosotros) { // Obtiene la posición de la sección "Nosotros"
            const sectionTop = sectionNosotros.getBoundingClientRect().top; // Obtiene la altura de la ventana
            const windowHeight = window.innerHeight;

            // Oculta el botón cuando la sección está visible
            if (sectionTop < windowHeight / 2) {
                btnNosotros.style.display = "none";
            } else {
                btnNosotros.style.display = "block";
            }
        }
    });

    ///// BOTÓN PARA ABRIR/CERRAR LA CALCULADORA
    const toggleBtn = document.getElementById("toggleCalculator"); // Botón para abrir/cerrar la calculadora
    const calculator = document.getElementById("calculator"); // Contenedor de la calculadora
    const closeBtn = document.getElementById("closeCalculator"); // Botón para cerrar la calculadora 

    if (toggleBtn && calculator) {
        toggleBtn.addEventListener("click", function () {
            calculator.style.display = calculator.style.display === "none" || calculator.style.display === "" ? "block" : "none";
        });

        closeBtn.addEventListener("click", function () {
            calculator.style.display = "none";
        });
    }

    ///// 🔹 FUNCIONALIDAD DE LA CALCULADORA
    const display = document.getElementById("calc-display");
    const buttons = document.querySelectorAll(".calc-btn");
    let expression = "";

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            let value = this.getAttribute("data-value");

            if (value === "=") {
                try {
                    expression = eval(expression);
                } catch {
                    expression = "Error";
                }
            } else if (value === "C") {
                expression = "";
            } else if (value === "%") {
                expression = (parseFloat(expression) / 100).toString();
            } else if (value === "IVA") {
                expression = (parseFloat(expression) * 1.16).toFixed(2).toString();
            } else {
                expression += value;
            }

            display.value = expression;
        });
    });

    ///// HACER LA CALCULADORA ARRASTRABLE
    let isDragging = false, offsetX, offsetY;

    if (calculator) {
        calculator.querySelector(".card-header").addEventListener("mousedown", function (e) {
            isDragging = true;
            offsetX = e.clientX - calculator.offsetLeft;
            offsetY = e.clientY - calculator.offsetTop;
        });

        document.addEventListener("mousemove", function (e) {
            if (isDragging) {
                calculator.style.left = (e.clientX - offsetX) + "px";
                calculator.style.top = (e.clientY - offsetY) + "px";
            }
        });

        document.addEventListener("mouseup", function () {
            isDragging = false;
        });
    }
});
