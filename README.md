<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Redmi</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Redmi</h1>
    </header>
    <main>
        <section id="introduccion">
            <h2>Introducción</h2>
            <p>Este repositorio es un escaparate de mi trabajo como desarrollador Python freelance. Aquí encontrarás una selección de mis proyectos más destacados, así como información sobre mi experiencia y habilidades.</p>
        </section>
        <section id="acerca-de-mi">
            <h2>Acerca de mí</h2>
            <p>Soy un estudiante de 8º semestre de Ingeniería de Sistemas en la Universidad Nacional. Tengo un fuerte interés en análisis de datos y me apasiona utilizar la tecnología para resolver problemas y mejorar la eficiencia.</p>
        </section>
        <section id="portafolio">
            <h2>Portafolio</h2>
            <ul>
                <li>
                    <h3>[PROYECTO 1]</h3>
                    <p>Descripción breve del proyecto, tecnologías utilizadas y enlace al código fuente.</p>
                </li>
                <li>
                    <h3>[PROYECTO 2]</h3>
                    <p>Descripción breve del proyecto, tecnologías utilizadas y enlace al código fuente.</p>
                </li>
                <li>
                    <h3>[PROYECTO 3]</h3>
                    <p>Descripción breve del proyecto, tecnologías utilizadas y enlace al código fuente.</p>
                </li>
            </ul>
        </section>
        <section id="tecnologías">
            <h2>Tecnologías</h2>
            <ul>
                <li>Python: NumPy, Pandas, Matplotlib</li>
                <li>Web: Streamlit</li>
                <li>Bases de datos: MySQL, SQL Server</li>
            </ul>
        </section>
        <section id="contacto">
            <h2>Contacto</h2>
            <ul>
                <li>Correo electrónico: [CORREO ELECTRÓNICO]</li>
                <li>LinkedIn: [LINKEDIN]</li>
                <li>GitHub: [GITHUB]</li>
            </ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 - [Tu nombre]</p>
    </footer>
</body>
</html>

body {
    font-family: Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    margin: 0;
    padding: 20px;
}

header {
    background-color: #333;
    color: #fff;
    padding: 10px;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
}

section {
    border: 1px solid #ddd;
    margin-bottom: 20px;
    padding: 20px;
}

h2 {
    font-size: 18px;
    margin-bottom: 10px;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

a {
    color: #333;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 10px;
    text-align: center;
}

@media (max-width: 768px) {
    main {
        flex-direction: column;
    }
}
