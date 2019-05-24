from pathlib import Path

def arbol(carpeta):
    """
    Muestra el árbol de una carpeta.
    """
    carpeta = Path(carpeta)
    print(f'+ {carpeta}')
    for ruta in sorted(carpeta.rglob('[!.]*')):
        profundidad = len(ruta.relative_to(carpeta).parts)
        espacio = '    ' * profundidad
        print(f'{espacio}+ {ruta.name}')