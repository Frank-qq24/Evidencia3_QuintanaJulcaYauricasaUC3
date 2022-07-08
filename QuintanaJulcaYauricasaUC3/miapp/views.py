from django.shortcuts import render,HttpResponse

# Create your views here.
def inicio(request):
    mensaje="""
        <h1>Universidad Nacional Tecnológica de Lima Sur</h1>
        <h2>EP Ingeniería de Sistemas</h2>
        <h3>Bienvenidos</h3>
    """
    return HttpResponse(mensaje)
def uc3(request):
    mensaje="""
        <h1>Lenguaje de Programación III</h1>
        <h3>Evaluación de la Unidad de Competencia 3</h3>
        <h3>Docente: Mg. Flor Elizabeth Cerdán León</h3>
        <h3>Integrantes:</h3>
        <h3>- Quintana Quispe Frank Raul</h3>
        <h3>- Julca Espillco Humberto Enrique</h3>
        <h3>- Yauricasa Mendoza Miguel Angel</h3>
    """
    return HttpResponse(mensaje)
def noticia(request):
    mensaje="""
    <h>SELECCIÓN PERUANA</h>
    <h1>Ricardo Gareca sobre si volverá a Perú: "Si Dios quiere vamos a regresar por acá"</h1>
    <p>Ricardo Gareca dejó este viernes el Perú con sentimientos encontrados. El entrenador argentino de 64 años, que estuvo acompañado de su esposa, recibió el cariño de decenas de hinchas que le pidieron que acepte la oferta de renovación de la Federación Peruana de Fútbol (FPF) con miras a las Eliminatorias al Mundial 2026.</p>
    <p>El 'Tigre' Gareca habló en exclusiva con RPP Noticias y le aseguró que seguramente volverá a Lima en su momento. "Sí por supuesto, si dios quiere vamos a regresar por acá, tengo un montón de cosas acá en Lima", declaró.</p>
    <p>"Yo tengo un excelente relación con Perú", agregó Gareca que dejó el territorio peruano en compañía de su esposa Gladys Hartintegui.</p>
    <p>A su vez se dio tiempo para felicitar a Melgar por su pase a los cuartos de final de la Copa Sudamericana. "Muy contento por Melgar. Una alegría para el fútbol,están haciendo una campaña muy destacada. Nos pone muy felices a todos", señaló.</p>
    <p>Hay que destacar, que el exDT de Vélez Sarsfield y Universitario de Deportes, negó algún contacto con Boca Juniors sobre la posibilidad de ser el reemplazante de Sebastián Battaglia, quien fue destituido de su cargo tras la eliminaación xeneize de la Copa Libertadores.</p>
    <img src="https://e.rpp-noticias.io/normal/2022/07/07/583158_1282751.jpg">
    <a href="https://rpp.pe/futbol/seleccion-peruana/ricardo-gareca-en-seleccion-peruana-si-dios-quiere-vamos-a-regresar-por-peru-noticia-1416596">Noticia completa Aqui</a>
    """
    return HttpResponse(mensaje)