import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import py3Dmol
import matplotlib
matplotlib.use("Agg")

# Configuración del sidebar con un menú
menu = st.sidebar.selectbox(
    "Selecciona una sección del Dashboard:",
    [
        "Inicio",
        "¿Qué es la Metionina?",
        "Estructura 3D Interactiva",
        "Contenido en Alimentos",
        "Calculadora de Consumo Diario",
    ],
)

# Definir los datos de los alimentos fuera de las secciones para que se pueda acceder desde cualquier parte
data = {
    "Alimento": ["Huevo", "Carne de Pollo", "Pescado", "Leche", "Nueces", "Tofu"],
    "Metionina (g/100g)": [0.39, 0.85, 0.75, 0.08, 0.26, 0.12],
}
df = pd.DataFrame(data)

# Título principal
st.title("Dashboard de la Proteína Metionina")

# Sección: Inicio
if menu == "Inicio":
    st.header("Bienvenido al Dashboard de Metionina")
    st.markdown(
        """
        Este dashboard interactivo está diseñado para explorar información clave sobre la proteína metionina: 
        su papel en el cuerpo humano, alimentos ricos en metionina, y calculadoras útiles para su consumo.
        
        Usa el menú lateral para navegar por las diferentes secciones.
        """
    )
    st.image(
        "/Users/camilaocampo/Desktop/bioinformatica/download.jpeg",
        caption="Estructura química de la Metionina",
        use_column_width=True,
    )

# Sección: ¿Qué es la Metionina?
elif menu == "¿Qué es la Metionina?":
    st.header("¿Qué es la Metionina?")
    st.markdown(
        """
        La metionina es un aminoácido esencial que desempeña un papel clave en la síntesis de proteínas y el metabolismo. 
        Es importante para la salud del hígado, el crecimiento del cabello y la piel, y actúa como un antioxidante en el cuerpo.
        """
    )

# Sección: Estructura 3D Interactiva
elif menu == "Estructura 3D Interactiva":
    st.header("Estructura 3D de la Metionina")
    st.markdown(
        """
        A continuación, puedes explorar la estructura 3D de la molécula de metionina. 
        Usa el ratón o el touchpad para rotar, acercar o alejar la molécula.
        """
    )
    
    # Visualizador 3D usando py3Dmol
    structure_pdb = """
    HETATM    1  N   MET A   1      -0.681  -1.181  -0.016  1.00  0.00           N
    HETATM    2  CA  MET A   1       0.682  -0.535  -0.014  1.00  0.00           C
    HETATM    3  C   MET A   1       1.637  -0.777  -1.175  1.00  0.00           C
    HETATM    4  O   MET A   1       1.523  -1.764  -1.880  1.00  0.00           O
    HETATM    5  CB  MET A   1       0.813   0.981  -0.507  1.00  0.00           C
    HETATM    6  CG  MET A   1       1.956   1.678   0.222  1.00  0.00           C
    HETATM    7  SD  MET A   1       1.430   3.420   0.486  1.00  0.00           S
    HETATM    8  CE  MET A   1       2.900   3.998   1.222  1.00  0.00           C
    HETATM    9  H1  MET A   1      -1.399  -0.564   0.332  1.00  0.00           H
    HETATM   10  H2  MET A   1      -1.024  -1.960  -0.546  1.00  0.00           H
    HETATM   11  H3  MET A   1      -0.846  -1.208   0.997  1.00  0.00           H
    HETATM   12  HA  MET A   1       1.237  -0.736   0.890  1.00  0.00           H
    HETATM   13 1HB  MET A   1      -0.052   1.469  -0.822  1.00  0.00           H
    HETATM   14 2HB  MET A   1       0.963   1.079  -1.566  1.00  0.00           H
    HETATM   15 1HG  MET A   1       2.706   1.294  -0.486  1.00  0.00           H
    HETATM   16 2HG  MET A   1       2.131   1.852   1.294  1.00  0.00           H
    HETATM   17 1HE  MET A   1       3.065   3.743   2.307  1.00  0.00           H
    HETATM   18 2HE  MET A   1       2.852   5.065   1.092  1.00  0.00           H
    HETATM   19 3HE  MET A   1       3.788   3.653   0.717  1.00  0.00           H
    """
    
    viewer = py3Dmol.view(width=800, height=400)
    viewer.addModel(structure_pdb, "pdb")  # Carga la estructura en formato PDB
    viewer.setStyle({"stick": {}})  # Estilo: Representación en bastón
    viewer.zoomTo()  # Ajusta la vista
    
    # Mostrar el modelo 3D en Streamlit
    st.components.v1.html(viewer._make_html(), height=400)

# Sección: Contenido en Alimentos
elif menu == "Contenido en Alimentos":
    st.header("Contenido de Metionina en Alimentos")
    st.subheader("Tabla de alimentos ricos en Metionina")
    st.dataframe(df)


# Sección: Calculadora de Consumo Diario
elif menu == "Calculadora de Consumo Diario":
    st.header("Calculadora de Consumo Diario de Metionina")

    # Interactividad: Calculadora de consumo diario

    st.header("Calculadora de Consumo de Metionina")
    st.markdown(
    """
    Se recomienda un consumo diario de **10-13 mg de metionina por kilogramo de peso corporal**.
    """
)

    peso = st.number_input("Ingresa tu peso (kg):", min_value=1, max_value=200, value=70, step=1)
    recomendacion = peso * 12
    st.write(f"Tu consumo diario recomendado de metionina es aproximadamente **{recomendacion:.1f} mg**.")

# Pie de página
st.markdown(
    """
    ---
    Este dashboard es solo para fines informativos. Consulta a un profesional de la salud para recomendaciones específicas.
    """
)