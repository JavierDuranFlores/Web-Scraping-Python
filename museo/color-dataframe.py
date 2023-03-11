import pandas as pd

# Crear DataFrame de ejemplo
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Crear un diccionario de colores
colors = {'A': 'red', 'B': 'green', 'C': 'blue'}

# Aplicar estilo a las columnas
styled_df = df.style.set_properties(**{'background-color': list(colors.values())}, subset=pd.IndexSlice[:, list(colors.keys())])

# Establecer el título del DataFrame
styled_df.set_caption('Ejemplo de DataFrame con colores de fondo')

# Mostrar el DataFrame con los colores de fondo y el título
styled_df

