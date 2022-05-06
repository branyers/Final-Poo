def __init__(self, name, files):
    self.name = name
    self.files = files


def read_join_csv(self, filenamefunction):
    try:
        def junta_csv(self):
            """
            Crea un archivo .csv a partir de multiples
            archivos .csv con una sola columna

            :param self:
            :param salida: Nombre del archivo de salida.
            :param archivos: Lista de archivos de entrada.
                             Son .csv con header en la primera fila.
            """
            handles = []  # Archivos de entrada
            headers = []  # Headers de cada archivo de entrada
            #
            #   Abrir los archivos de entradas, leer los headers
            #
            for arch in self.files:
                file_handle = open(arch, "r")
                handles.append(file_handle)
                headers.append(file_handle.readline().strip())

            with open(f"{self.name}.csv", "w") as out:
                #   Formar la primera linea con los headers de
                #   las columnas.
                header = ",".join(headers)
                out.write(f"{header}\n")

                eof = False
                while not eof:
                    fila = []
                    #   Leer una fila de cada archivo para
                    #   formar una fila de salida.
                    for handle in handles:
                        dato = handle.readline().lower()
                        if dato:
                            fila.append(dato.strip())
                        else:
                            eof = True
                            break

                    if not eof:
                        #   Grabar la fila de salida.
                        self.name = ','.join(fila)
                        result = filenamefunction(self.name, self.files)
                        out.write(f"{result}\n")
                        return filenamefunction

            #   Cerrar tosdos los archivos
            out.close()
            for handle in handles:
                handle.close()

        return junta_csv
    except FileNotFoundError:
        print("File not found")


def filenamefunction(self, files):
    return self.name